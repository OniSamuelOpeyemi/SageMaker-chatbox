import builtins
from chatbot_loop import chatbot_loop  # Make sure this import path is correct

def test_chatbot_response(monkeypatch):
    # Simulated user inputs
    inputs = iter(["hello", "end"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Capture printed outputs
    printed_lines = []

    def fake_print(*args, **kwargs):
        line = " ".join(str(arg) for arg in args)
        printed_lines.append(line)

    monkeypatch.setattr(builtins, "print", fake_print)

    # Run the chatbot loop
    chatbot_loop()

    # Debug: print all lines (optional)
    # for line in printed_lines:
    #     print(f"> {line}")

    # Assertion checks
    assert any("Chatbot: Hello!" in line for line in printed_lines), "Greeting not found"
    assert any("Chatbot: You said 'hello'" in line for line in printed_lines), "Expected response for 'hello' not found"
    assert any("Chatbot: Goodbye!" in line for line in printed_lines), "Goodbye message not found"
