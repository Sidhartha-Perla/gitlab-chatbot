import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"

# API settings
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8001"))

# Database settings
CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "gitlab_data")

# Session settings
SESSION_COOKIE_NAME = "rag_session_id"
SESSION_EXPIRY_MINUTES = int(os.getenv("SESSION_EXPIRY_MINUTES", "60"))

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Model settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gemini-2.0-flash-001"