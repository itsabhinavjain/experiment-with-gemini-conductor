import pytest
from agent.manager import agent_manager
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

def test_agent_manager_creates_client():
    """
    Verifies that the AgentManager can successfully create a ClaudeSDKClient.
    """
    client = agent_manager.create_client()
    assert isinstance(client, ClaudeSDKClient)
    # We no longer check for a hardcoded model as it uses local default
    assert client.options.max_thinking_tokens == 4000

def test_agent_manager_custom_options():
    """
    Verifies that the AgentManager respects custom options when creating a client.
    """
    custom_options = ClaudeAgentOptions(model="claude-3-opus-20240229", max_thinking_tokens=1000)
    client = agent_manager.create_client(options=custom_options)
    assert client.options.model == "claude-3-opus-20240229"
    assert client.options.max_thinking_tokens == 1000
