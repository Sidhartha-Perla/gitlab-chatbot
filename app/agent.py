import os
from dotenv import load_dotenv
from pathlib import Path
from typing import List, TypedDict
from chromadb import HttpClient
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, StateGraph
from langchain_core.documents import Document
from langchain.prompts import PromptTemplate

class State(TypedDict):
        question: str
        context: List[Document]
        answer: str
        chat_history: List[dict]
        chat_summary: str
        enhanced_question: str
        is_followup: bool

class Agent:
    
    def __init__(self, vector_store: Chroma, llm: ChatGoogleGenerativeAI, prompt: PromptTemplate, initial_state: State = None):
        self.vector_store = vector_store
        
        self.graph = self.build_graph()
        self.llm = llm
        
        self.prompt = prompt

        if initial_state is None:
            self.current_state = {
            "question": "",
            "context": [],
            "answer": "",
            "chat_history": [],
            "chat_summary": "No conversation yet.",
            "enhanced_question": "",
            "is_followup": False
            }
        else:
            self.current_state = initial_state
    
    def store_interaction(self, state: State):
        state["chat_history"].append({
            "question": state["question"],
            "answer": state["answer"]
        })
        return state
    
    def update_summary(self, state: State):
        last_question = state["question"]
        last_answer = state["answer"]
        
        if len(state["chat_history"]) > 0:
            summary_messages = [
                {
                    "role": "system",
                    "content": """You are a conversation summarizer. Your task is to create or update a summary of the ongoing conversation.
                    Include key topics discussed and important keywords that might be useful for information retrieval.
                    Be concise but comprehensive. Focus on the main points and themes.
                    Please provide an updated summary that incorporates the latest interaction.
                    Make sure to include key topics and important keywords in your summary.
                    Format: [Concise summary of conversation topics] | Keywords: [comma-separated list of keywords]"""
                },
                {
                    "role": "user",
                    "content": f"""Here is the current conversation summary:
                    {state["chat_summary"]}
                    
                    The latest interaction was:
                    User: {last_question}
                    Assistant: {last_answer}
                    """
                }
            ]
            summary_response = self.llm.invoke(summary_messages)
            state["chat_summary"] = summary_response.content
        
        return state
    
    def detect_followup(self, state: State):
        # If there's no chat history, it can't be a follow-up
        if not state["chat_history"]:
            state["is_followup"] = False
            return state
            
        # If there is chat history, analyze the recent conversations
        recent_history = ""
        if len(state["chat_history"]) > 0:
            for entry in state["chat_history"][-2:]:
                recent_history += f"User: {entry['question']}\nAssistant: {entry['answer']}\n\n"
        
        followup_check_messages = [
            {"role": "system", "content": "You are a conversation analyzer. Your task is to determine if the new question is a follow-up to the previous conversation."},
            {"role": "user", "content": f"""Based on this recent conversation history:
            
            {recent_history}
            
            Is this new question a follow-up or continuation of the previous topic?
            
            New question: "{state['question']}"
            
            Please respond with only "FOLLOWUP" if it's a follow-up question that relies on previous context, or "NEW_TOPIC" if it's a fresh, independent question."""}
        ]
        
        followup_response = self.llm.invoke(followup_check_messages)
        state["is_followup"] = "FOLLOWUP" in followup_response.content.upper()
        return state
    
    def enhance_query(self, state: State):
        if state["is_followup"]:
            recent_history = ""
            if len(state["chat_history"]) > 0:
                for entry in state["chat_history"][-5:]:
                    recent_history += f"User: {entry['question']}\nAssistant: {entry['answer']}\n\n"
        
            messages = [
                {
                    "role": "system",
                    "content": """You are a helpful query enhancement assistant. Your task is to:
                    1. Analyze the conversation summary and the new follow-up question
                    2. Since this is a follow-up question, augment the query with relevant keywords from previous interactions, based on the conversation summary.
                    3. Add any other search terms that would help in retrieving relevant documents
                    4. Generate an enhanced query that incorporates relevant context from previous interactions.
                    5. If there are multiple possible versions of the enhanced query, combine them into a single query.
                    6. If the question is vague or meta (e.g. "what did we talk about so far"), do not reject it. Instead, produce a lightly rephrased or echoed version of the question that can still be used in a search, even if it is imprecise.
                        
                    Important: Never refuse to enhance a query. Always return some enhanced version, even if minimal.
                    Give only the enhanced query for search. DO NOT repeat the user query"""
                },
                {
                    "role": "user", 
                    "content": f"""Given this conversation summary:
                    {state['chat_summary']}

                    And the recent conversation history:
                    {recent_history}
                    
                    And this follow-up question:
                    {state['question']}

                    Enhance the search query to improve document retrieval.
                    """
                }
            ]
        else:
            messages = [
                {
                    "role": "system", 
                    "content": """You are a helpful query enhancement assistant. Your task is to:
                    1. Analyze the user's query
                    2. Identify important keywords that would help in retrieving relevant documents
                    3. Create an enhanced version of the query that will improve document retrieval
                    4. If there are multiple possible versions of the enhanced query, combine them into a single query.
                    5. If the question is vague or meta (e.g. "Hi", "what did we talk about so far"), do not reject it. Instead, produce a lightly rephrased or echoed version of the question that can still be used in a search, even if it is imprecise.

                    Give only the enhanced query for search. DO NOT repeat the user query"""
                },
                {
                    "role": "user", 
                    "content": f"Enhance this user query to improve document retrieval while maintaining the original intent of the question: {state['question']}"
                }
            ]
        
        enhanced_query_response = self.llm.invoke(messages)
        state["enhanced_question"] = enhanced_query_response.content
        return state
 
    def retrieve(self, state: State):
        retrieved_docs = self.vector_store.similarity_search(
            state["enhanced_question"],
            k=20,
        )
        return {"context": retrieved_docs}
    
    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        history_text = ""
        if state["chat_history"]:
            for i, entry in enumerate(state["chat_history"][-5:]):
                history_text += f"User: {entry['question']}\nAssistant: {entry['answer']}\n\n"
        
        if state["is_followup"]:
            messages = self.prompt.invoke({
                "question": state["question"],
                "context": docs_content,
                "chat_history_summary": state["chat_summary"],
                "chat_history": history_text,
                "follow_up": "This appears to be a follow-up question. Make sure to consider the chat history."
            })
        else:
            messages = self.prompt.invoke({
                "question": state["question"],
                "context": docs_content,
                "chat_history_summary": state["chat_summary"],
                "chat_history": "NA",
                "follow_up": ""
            })
        
        response = self.llm.invoke(messages)
        return {"answer": response.content}
    
    def build_graph(self):
        graph_builder = StateGraph(State)
        graph_builder.add_node("detect_followup", self.detect_followup)
        graph_builder.add_node("enhance_query", self.enhance_query)
        graph_builder.add_node("retrieve", self.retrieve)
        graph_builder.add_node("generate", self.generate)
        graph_builder.add_node("store_interaction", self.store_interaction)
        graph_builder.add_node("update_summary", self.update_summary)
        
        graph_builder.add_edge(START, "detect_followup")
        graph_builder.add_edge("detect_followup", "enhance_query")
        graph_builder.add_edge("enhance_query", "retrieve")
        graph_builder.add_edge("retrieve", "generate")
        graph_builder.add_edge("generate", "store_interaction")
        graph_builder.add_edge("store_interaction", "update_summary")
        
        return graph_builder.compile()
    
    def process_user_query(self, query: str):
        self.current_state["question"] = query
        self.current_state = self.graph.invoke(self.current_state)
        return self.current_state["answer"]
    
    def get_messages(self):
        return self.current_state["chat_history"]
