import uuid
import logging
from typing import Dict, Optional
from claude_agent_sdk import ClaudeSDKClient
from agent.manager import agent_manager

logger = logging.getLogger(__name__)

class SessionManager:
    """
    Manages in-memory user sessions, mapping session IDs to ClaudeSDKClient instances.
    This allows for conversation continuity.
    """
    def __init__(self):
        # Maps session_id (str) to ClaudeSDKClient instance
        self._sessions: Dict[str, ClaudeSDKClient] = {}

    def get_or_create_session(self, session_id: Optional[str] = None) -> tuple[str, ClaudeSDKClient]:
        """
        Retrieves an existing session or creates a new one.
        Returns a tuple of (session_id, client).
        """
        if session_id and session_id in self._sessions:
            logger.info(f"Retrieving existing session: {session_id}")
            return session_id, self._sessions[session_id]
        
        # Create a new session if ID not provided or not found
        new_id = session_id or str(uuid.uuid4())
        logger.info(f"Creating new session: {new_id}")
        client = agent_manager.create_client()
        self._sessions[new_id] = client
        return new_id, client

    def delete_session(self, session_id: str) -> bool:
        """
        Removes a session from the store.
        """
        if session_id in self._sessions:
            logger.info(f"Deleting session: {session_id}")
            del self._sessions[session_id]
            return True
        return False

# Singleton instance
session_manager = SessionManager()
