import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chatbot_loop import chatbot_loop  # import your function

def test_chatbot_response(monkeypatch):
    inputs = iter(["hello", "exit"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    expected_outputs = []

    def fake_print(*args, **kwargs):
        expected_outputs.append(" ".join(str(arg) for arg in args))

    monkeypatch.setattr('builtins.print', fake_print)

    chatbot_loop()

    assert "Chatbot: You said 'hello'" in expected_outputs
    assert "Chatbot: Goodbye!" in expected_outputs

