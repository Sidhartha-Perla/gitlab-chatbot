import asyncio
from pathlib import Path
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import  List
import logging
from app.session import SessionManager
from app.agent_factory import AgentFactory
from app.config import API_HOST, API_PORT

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

# Initialize app
app = FastAPI(title="RAG Agent API", docs_url="/documentation", redoc_url="/redoc")

# Initialize session manager and agent factory
session_manager = SessionManager()
agent_factory = AgentFactory()

# Session cleanup task
async def cleanup_expired_sessions():
    while True:
        # Run every 5 minutes
        await asyncio.sleep(300)
        session_manager.clean_expired_sessions()
        logger.info("Cleaned expired sessions")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup create a recurring cleanup task
    cleanup_task = asyncio.create_task(cleanup_expired_sessions())
    logger.info("Started session cleanup task")
    yield
    cleanup_task.cancel()
    

# Request/Response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    session_id: str

class MessagesResponse(BaseModel):
    messages: List[dict]  # Changed from List[Dict] to List[dict] to match State
    session_id: str

# Dependency to ensure session exists
async def get_session_id(request: Request, response: Response) -> str:
    session_id = session_manager.get_session_id(request)
    if not session_id:
        session_id = session_manager.create_session(response)
    return session_id

# Routes
@app.post("/api/query", response_model=QueryResponse)
async def process_query(
    query_request: QueryRequest,
    response: Response,
    session_id: str = Depends(get_session_id)
):
    try:
        # Get agent for this session
        agent = agent_factory.get_agent(session_id)
        
        # Process query
        answer = agent.process_user_query(query_request.query)
        
        return QueryResponse(answer=answer, session_id=session_id)
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing query")

@app.post("/api/reset")
async def reset_session(
    response: Response,
    session_id: str = Depends(get_session_id)
):
    try:
        # Remove agent
        agent_factory.remove_agent(session_id)
        
        # Create new session
        new_session_id = session_manager.create_session(response)
        
        return {"message": "Session reset successfully", "session_id": new_session_id}
    except Exception as e:
        logger.error(f"Error resetting session: {str(e)}")
        raise HTTPException(status_code=500, detail="Error resetting session")

@app.get("/api/messages", response_model=MessagesResponse)
async def get_messages(
    session_id: str = Depends(get_session_id)
):
    try:
        # Get agent for this session
        agent = agent_factory.get_agent(session_id)
        # Get message history
        messages = agent.get_messages()
        return MessagesResponse(messages=messages, session_id=session_id)
    except Exception as e:
        logger.error(f"Error retrieving messages: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving messages")


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def serve_index():
    dist_path = Path(__file__).parent / "dist" / "index.html"
    return FileResponse(dist_path)

# Mount static files (assets)
app.mount("/assets", StaticFiles(directory=Path(__file__).parent / "dist" / "assets"), name="assets")


# Run server if executed directly
if __name__ == "__main__":
    uvicorn.run("app.main:app", host=API_HOST, port=API_PORT, reload=True)