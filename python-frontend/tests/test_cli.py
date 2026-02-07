import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from io import StringIO
from rich.console import Console
from main import main # Import the main async function

# Helper async generator mocks
async def mock_stream_chat_success_generator(prompt, session_id):
    yield {"type": "session_id", "content": "test-session-123"}
    yield {"type": "thinking", "content": "Thinking about your request..."}
    yield {"type": "text", "content": "Hello! This is a test response."}

async def mock_stream_chat_error_generator(prompt, session_id):
    yield {"type": "error", "content": "Backend connection failed."}

async def never_ending_stream_generator(prompt, session_id):
    while True:
        await asyncio.sleep(100) # Sleep indefinitely
        yield {"type": "text", "content": "..."}

@pytest.fixture
def mock_backend_client(mocker):
    """Mocks the BackendClient for testing CLI interactions."""
    # Use a regular MagicMock for stream_chat because it returns a generator, not a coroutine
    mock = mocker.MagicMock()
    return mock

@pytest.fixture
def cli_test_environment(mock_backend_client, mocker):
    """Sets up a controlled environment for CLI testing."""
    # Patch backend_client in main.py to use our mock
    mocker.patch('main.backend_client', new=mock_backend_client)
    
    # Capture console output
    from rich.console import Console
    mock_stdout = StringIO()
    test_console = Console(file=mock_stdout, force_terminal=False, width=100, color_system=None)
    
    # Mock Live
    mock_live = mocker.MagicMock()
    def mock_live_update(renderable):
        test_console.print(renderable)
    mock_live.update.side_effect = mock_live_update
    
    # Make Live context manager return the mock_live object
    mock_live_class = mocker.patch('main.Live')
    mock_live_class.return_value.__enter__.return_value = mock_live
        
    return {
        "mock_backend_client": mock_backend_client,
        "mock_stdout": mock_stdout,
        "mocker": mocker,
        "test_console": test_console
    }

@pytest.mark.asyncio
async def test_cli_basic_interaction(cli_test_environment):
    """
    Tests a basic CLI interaction: user input, agent response, and exit.
    """
    mock_stdout = cli_test_environment["mock_stdout"]
    mock_backend_client = cli_test_environment["mock_backend_client"]
    mocker = cli_test_environment["mocker"]
    test_console = cli_test_environment["test_console"]

    # Simulate user input
    mocker.patch('rich.prompt.Prompt.ask', side_effect=["hello", "quit"])

    # Configure mock_backend_client.stream_chat for this test
    mock_backend_client.stream_chat.side_effect = mock_stream_chat_success_generator

    # Run the main CLI function
    await main(console_override=test_console)

    output = mock_stdout.getvalue()
    
    # Assertions
    assert "Claude Agent SDK CLI" in output
    assert "Type 'exit' or 'quit' to end the conversation." in output
    assert "Thinking..." in output
    assert "Claude's Thinking" in output
    assert "Thinking about your request..." in output
    assert "Claude: Hello! This is a test response." in output or "Claude:[/bold green] Hello! This is a test response." in output
    
    # Check if stream_chat was called correctly
    mock_backend_client.stream_chat.assert_called_with("hello", None)

@pytest.mark.asyncio
async def test_cli_error_handling(cli_test_environment):
    """
    Tests CLI error handling when the backend client encounters an error.
    """
    mock_stdout = cli_test_environment["mock_stdout"]
    mock_backend_client = cli_test_environment["mock_backend_client"]
    mocker = cli_test_environment["mocker"]
    test_console = cli_test_environment["test_console"]

    # Configure mock_backend_client.stream_chat for this test to yield an error
    mock_backend_client.stream_chat.side_effect = mock_stream_chat_error_generator

    mocker.patch('rich.prompt.Prompt.ask', side_effect=["test error", "quit"])

    await main(console_override=test_console)

    output = mock_stdout.getvalue()
    assert "Error: Backend connection failed." in output
    mock_backend_client.stream_chat.assert_called_with("test error", None)

@pytest.mark.asyncio
async def test_cli_keyboard_interrupt(cli_test_environment):
    """
    Tests CLI behavior on KeyboardInterrupt.
    """
    mock_stdout = cli_test_environment["mock_stdout"]
    mock_backend_client = cli_test_environment["mock_backend_client"]
    mocker = cli_test_environment["mocker"]
    test_console = cli_test_environment["test_console"]

    # Simulate KeyboardInterrupt during Prompt.ask
    mocker.patch('rich.prompt.Prompt.ask', side_effect=KeyboardInterrupt)
    
    await main(console_override=test_console)

    output = mock_stdout.getvalue()
    assert "Conversation interrupted." in output