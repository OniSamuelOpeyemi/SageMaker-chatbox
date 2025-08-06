# tests/test_chatbot_loop.py

import os
import sys
import pytest

# Add root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chatbot_loop import chatbot_loop

def test_chatbot_response(monkeypatch):
    # Simulate user input
    inputs = iter(["hello", "end"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Capture printed outputs
    printed_lines = []

    def fake_print(*args, **kwargs):
        printed_lines.append(" ".join(str(arg) for arg in args))

    monkeypatch.setattr("builtins.print", fake_print)

    # Run the chatbot
    chatbot_loop()

    # Assertions
    assert any("Chatbot: You said 'hello'" in line for line in printed_lines)
    assert any("Chatbot: Goodbye!" in line for line in printed_lines)
