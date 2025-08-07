import pytest
from unittest.mock import MagicMock, patch

# Import your chatbot module here
# from your_script import chatbot_session

@pytest.fixture
def mock_predictor():
    predictor = MagicMock()
    # Simulate model response as JSON string
    predictor.predict.return_value = '{"generated_text": "Hello, how can I help you?"}'
    return predictor

def test_chatbot_interaction(monkeypatch, mock_predictor):
    # Simulate user inputs: one message then exit
    inputs = iter(["Hello", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    outputs = []
    monkeypatch.setattr('builtins.print', lambda x: outputs.append(x))
    
    # Run the chatbot session (replace with your actual function!)
    # chatbot_session(mock_predictor)
    
    # Check model was called with user input formatted as JSON
    mock_predictor.predict.assert_any_call('{"input_text": "Hello"}')
    
    # Check output parsing and display
    assert any("Hello, how can I help you?" in o for o in outputs)
    
    # Check quit command ends loop
    assert any("Exiting chatbot" in o or "Goodbye" in o for o in outputs)
