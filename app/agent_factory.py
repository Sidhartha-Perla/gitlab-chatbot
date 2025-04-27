from typing import Dict
from chromadb import HttpClient
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from app.agent import Agent, State
from app.config import (
    CHROMA_HOST, 
    CHROMA_PORT, 
    COLLECTION_NAME, 
    EMBEDDING_MODEL, 
    GOOGLE_API_KEY
)


class AgentFactory:
    def __init__(self):
        """Initialize shared resources"""
        # Initialize embedding model
        self.embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        
        # Initialize Chroma client
        self.chroma_client = HttpClient(
            host=CHROMA_HOST,
            port=CHROMA_PORT
        )
        
        # Initialize vector store
        self.vector_store = Chroma(
            client=self.chroma_client,
            collection_name=COLLECTION_NAME,
            embedding_function=self.embedding_model
        )

        # Initialize llm client
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-001",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            google_api_key=GOOGLE_API_KEY
        )
        
        # Agent cache
        self.agent_cache: Dict[str, Agent] = {}
    
    def get_agent(self, session_id: str) -> Agent:
        """Get or create an agent for the given session ID"""
        if session_id not in self.agent_cache:
            # Create new agent with empty initial state
            initial_state: State = {
                "question": "",
                "context": [],
                "answer": "",
                "chat_history": [],
                "chat_summary": "No conversation yet.",
                "enhanced_question": "",
                "is_followup": False
            }
            
            self.agent_cache[session_id] = Agent(
                vector_store=self.vector_store,
                llm=self.llm,
                initial_state=initial_state
            )
        
        return self.agent_cache[session_id]
    
    def remove_agent(self, session_id: str) -> None:
        """Remove an agent from the cache"""
        if session_id in self.agent_cache:
            del self.agent_cache[session_id]