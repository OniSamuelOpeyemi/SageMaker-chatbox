import pytest
from chatbot_loop import get_bot_response

def test_get_bot_response_known_keywords():
    assert get_bot_response("hello") in [
        "Hi there!", "Hello!", "Hey!", "Good to see you!",
        "Greetings!", "Howdy!", "Yo!", "Hi friend!", "Welcome!", "Hello human!"
    ]
    assert get_bot_response("how are you") in [
        "I'm doing well, thanks!", "Running smoothly!", "Feeling fantastic!",
        "I'm just code, but I feel electric today!", "100% uptime vibes."
    ]
    assert get_bot_response("quit") == "👋 Bye! Have a great day!"
    assert get_bot_response("end") == "👋 Bye! Have a great day!"

def test_get_bot_response_unknown_keyword():
    # Should return one of the fallback_responses
    unknown = "unrecognized input"
    assert get_bot_response(unknown) in [
        "That's interesting!", "Could you elaborate?", "I'm learning more every day!",
        "Sorry, I didn’t catch that.", "Tell me more.", "Hmm, go on…", "Okay!", "Nice!", "Cool!", "Wow!"
    ]
