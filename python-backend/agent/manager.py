import os
import logging
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
from config import get_settings
from typing import Optional

logger = logging.getLogger(__name__)

class AgentManager:
    """
    Manages the lifecycle and configuration of the Claude Agent SDK client.
    """
    def __init__(self):
        self.settings = get_settings()

    def create_client(self, options: Optional[ClaudeAgentOptions] = None) -> ClaudeSDKClient:
        """
        Creates a new instance of ClaudeSDKClient with the provided options.
        If no options are provided, it uses default settings.
        
        Prioritizes ANTHROPIC_API_KEY from settings. If not available,
        it relies on the local 'claude' CLI authentication by default.
        """
        logger.info("Creating new Claude SDK client")
        if options is None:
            # Default options for the agent. 
            # We omit 'model' to use the local claude config default.
            options = ClaudeAgentOptions(
                max_thinking_tokens=4000,
                system_prompt="You are a helpful and concise AI assistant built with the Claude Agent SDK."
            )
        
        # If ANTHROPIC_API_KEY is provided, set it in the environment for the SDK.
        # The SDK (or its underlying client) will pick this up.
        # This gives precedence to the explicit API key.
        if self.settings.anthropic_api_key and self.settings.anthropic_api_key != "your_anthropic_api_key_here":
            os.environ["ANTHROPIC_API_KEY"] = self.settings.anthropic_api_key
        elif "ANTHROPIC_API_KEY" in os.environ: # If it was previously set and now is not in settings, remove it.
            del os.environ["ANTHROPIC_API_KEY"]


        # The SDK will use the local 'claude' CLI for authentication if ANTHROPIC_API_KEY
        # is not set in the environment.
        return ClaudeSDKClient(options=options)

# Singleton instance for easy access across the app
agent_manager = AgentManager()
