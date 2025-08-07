import builtins
from unittest.mock import patch
import pytest

# Import from your chatbot file (ensure the name matches your file)
from chatbot_loop import chatbot_loop

def test_chatbot_response():
    user_inputs = ["hello", "quit"]
    # These are the possible greetings and exit messages your bot produces
    expected_greetings = [
        "Hi there!", "Hello!", "Hey!", "Good to see you!",
        "Greetings!", "Howdy!", "Yo!", "Hi friend!", "Welcome!", "Hello human!"
    ]
    expected_exit = "👋 Bye! Have a great day!"

    with patch.object(builtins, 'input', side_effect=user_inputs):
        with patch.object(builtins, 'print') as mock_print:
            chatbot_loop()
    
    # Gather printed output
    printed_texts = [call.args[0] for call in mock_print.call_args_list]

    # Check that a greeting (with SageBot prefix) was printed
    assert any(f"SageBot: {greeting}" in printed_texts for greeting in expected_greetings)
    # Check that the exit message was printed
    assert any(f"SageBot: {expected_exit}" in printed_texts for _ in printed_texts)
