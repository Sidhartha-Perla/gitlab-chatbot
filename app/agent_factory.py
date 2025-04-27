from typing import Dict
from chromadb import HttpClient
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain.prompts import PromptTemplate
from app.agent import Agent, State
from app.config import (
    CHROMA_HOST, 
    CHROMA_PORT, 
    COLLECTION_NAME, 
    EMBEDDING_MODEL, 
    GOOGLE_API_KEY,
    PROMPTS_DIR
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

        """# Initialize in-memory rate limiter
        rate_limiter = InMemoryRateLimiter(
            requests_per_second=0.25,  # One request 4 seconds
            check_every_n_seconds=0.25,  # Wake up every 250 ms to check whether allowed to make a request,
            max_bucket_size=15,  # Maximum burst size.
        )"""

        # Initialize llm client
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-001",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            google_api_key=GOOGLE_API_KEY,
            #rate_limiter=rate_limiter
        )

        prompt_text = (PROMPTS_DIR/ "system_prompt.txt").read_text(encoding="utf-8")
        self.prompt = PromptTemplate.from_template(prompt_text)
        
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
                prompt=self.prompt,
                initial_state=initial_state
            )
        
        return self.agent_cache[session_id]
    
    def remove_agent(self, session_id: str) -> None:
        """Remove an agent from the cache"""
        if session_id in self.agent_cache:
            del self.agent_cache[session_id]