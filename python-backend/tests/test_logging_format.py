import logging
import re
import pytest

def test_logging_format(caplog):
    """
    Verifies that the logging format follows [YYYY-MM-DD HH-MM-SS] - LEVEL - MESSAGE.
    """
    logger = logging.getLogger("test_logger")
    
    # We need to ensure the logger is configured with the format we expect
    # In the actual app, this is done in main.py via logging.basicConfig
    # For this test, we want to verify that the configuration in main.py works.
    # However, basicConfig only works if the root logger has no handlers.
    # So we'll trigger a log and check the caplog records.
    
    with caplog.at_level(logging.INFO):
        logger.info("Test message")
    
    # Check if any record matches the expected format
    # Note: caplog doesn't capture the formatted string by default, 
    # it captures the log record objects. 
    # To test the actual formatting, we need to check how the formatter is configured.
    
    # Instead, let's test by importing the app or triggering something that logs.
    from main import logger as app_logger
    
    with caplog.at_level(logging.INFO):
        app_logger.info("Application test message")
    
    # The caplog fixture doesn't show the formatted output (with asctime etc)
    # unless we check the handler's formatter.
    
    root_logger = logging.getLogger()
    assert len(root_logger.handlers) > 0
    formatter = root_logger.handlers[0].formatter
    
    # We expect the format string to be set correctly in main.py
    # Since we haven't implemented it yet, this test should fail if we check the format string.
    
    expected_format = '[%(asctime)s] - %(levelname)s - %(message)s'
    expected_datefmt = '%Y-%m-%d %H-%M-%S'
    
    assert formatter._fmt == expected_format
    assert formatter.datefmt == expected_datefmt
