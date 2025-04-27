import uuid
import time
from typing import Dict, Optional
from fastapi import Request, Response
from app.config import SESSION_COOKIE_NAME, SESSION_EXPIRY_MINUTES

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, Dict] = {}
        self.last_access: Dict[str, float] = {}
    
    def create_session(self, response: Response) -> str:
        """Create a new session and set cookie"""
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {}
        self.last_access[session_id] = time.time()
        
        # Set cookie
        response.set_cookie(
            key=SESSION_COOKIE_NAME,
            value=session_id,
            httponly=True,
            max_age=SESSION_EXPIRY_MINUTES * 60,
            samesite="lax"
        )
        
        return session_id
    
    def get_session_id(self, request: Request) -> Optional[str]:
        """Get session ID from request cookie"""
        return request.cookies.get(SESSION_COOKIE_NAME)
    
    def update_session_access(self, session_id: str) -> None:
        """Update last access time for a session"""
        if session_id in self.sessions:
            self.last_access[session_id] = time.time()
    
    def get_session_data(self, session_id: str) -> Optional[Dict]:
        """Get session data for a session ID"""
        if session_id in self.sessions:
            self.update_session_access(session_id)
            return self.sessions[session_id]
        return None
    
    def set_session_data(self, session_id: str, key: str, value) -> None:
        """Set data in a session"""
        if session_id in self.sessions:
            self.sessions[session_id][key] = value
            self.update_session_access(session_id)
    
    def delete_session(self, session_id: str, response: Response) -> None:
        """Delete a session and clear cookie"""
        if session_id in self.sessions:
            del self.sessions[session_id]
        
        if session_id in self.last_access:
            del self.last_access[session_id]
        
        response.delete_cookie(SESSION_COOKIE_NAME)
    
    def clean_expired_sessions(self) -> None:
        """Remove expired sessions"""
        current_time = time.time()
        expired_sessions = [
            session_id for session_id, last_access in self.last_access.items()
            if current_time - last_access > SESSION_EXPIRY_MINUTES * 60
        ]
        
        for session_id in expired_sessions:
            if session_id in self.sessions:
                del self.sessions[session_id]
            if session_id in self.last_access:
                del self.last_access[session_id]