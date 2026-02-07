import pytest
from agent.session import SessionManager
from claude_agent_sdk import ClaudeSDKClient

def test_session_creation():
    """
    Tests that a new session is created when no ID is provided.
    """
    sm = SessionManager()
    session_id, client = sm.get_or_create_session()
    assert session_id is not None
    assert isinstance(client, ClaudeSDKClient)
    assert session_id in sm._sessions

def test_session_retrieval():
    """
    Tests that an existing session can be retrieved using its ID.
    """
    sm = SessionManager()
    session_id, client1 = sm.get_or_create_session()
    id2, client2 = sm.get_or_create_session(session_id)
    
    assert session_id == id2
    assert client1 is client2

def test_session_deletion():
    """
    Tests that a session can be successfully deleted.
    """
    sm = SessionManager()
    session_id, _ = sm.get_or_create_session()
    assert sm.delete_session(session_id) is True
    assert session_id not in sm._sessions
    assert sm.delete_session("non-existent-id") is False
