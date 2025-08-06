import random

# Categorized responses
responses = {
    "hello": [
        "Hi there!", "Hello!", "Hey!", "Good to see you!",
        "Greetings!", "Howdy!", "Yo!", "Hi friend!", "Welcome!", "Hello human!"
    ],
    "how are you": [
        "I'm doing well, thanks!", "Running smoothly!", "Feeling fantastic!",
        "I'm just code, but I feel electric today!", "100% uptime vibes."
    ],
    "help": [
        "Sure! How can I assist you?", "Let me know what you need.",
        "I'm here to help. Fire away!", "Assistance is my middle name!",
        "Ask me anything you're curious about."
    ],
    "your name": [
        "I'm SageBot — running on SageMaker!", "They call me SageBot.",
        "Name's SageBot. I'm here to serve.", "SageBot, at your service."
    ],
    "bye": [
        "Goodbye!", "Take care!", "See you next time!", "Later!",
        "Logging off... but always here when you need me."
    ],
    "joke": [
        "Why did the computer go to therapy? It had too many bytes of trauma!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "I'm reading a book on anti-gravity... it's impossible to put down!",
        "Parallel lines have so much in common... it's a shame they'll never meet.",
        "Debugging: Being the detective in a crime movie where you are also the murderer."
    ],
    "thanks": [
        "You're welcome!", "No problem!", "Anytime!", "Happy to help!", "Glad I could assist!"
    ],
    "what can you do": [
        "I can chat with you, answer questions, and soon… rule the world (just kidding!).",
        "I’m here to chat, assist, and maybe make you smile.",
        "Let’s just say I’m the MVP of friendly bots.",
        "I'm still learning, but I'm good at conversation!"
    ],
    "who made you": [
        "I was built with love and Python on Amazon SageMaker.",
        "My creator is a wise developer using AWS tools.",
        "Born in the cloud, raised on SageMaker!"
    ],
    "weather": [
        "I don't have a weather sensor yet, but I can guess: Cloudy with a chance of code?",
        "Weather API not integrated yet, sorry!",
        "If you're hot, it’s probably sunny!"
    ]
}

# Example fallback responses
fallback_responses = [
    "That's interesting!", "Could you elaborate?", "I'm learning more every day!",
    "Sorry, I didn’t catch that.", "Tell me more.", "Hmm, go on…", "Okay!", "Nice!", "Cool!", "Wow!"
    # ... (you can keep the rest if you want, just shortened here for space)
]

def get_bot_response(user_input: str) -> str:
    """Returns an appropriate chatbot response based on user input."""
    user_input = user_input.lower()

    if user_input in ["quit", "end"]:
        return "👋 Bye! Have a great day!"

    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])

    return random.choice(fallback_responses)

def chatbot_loop():
    print("🤖 Hello! I'm SageBot. Type 'quit' or 'end' to exit.")
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("SageBot:", response)
        if user_input.lower() in ["quit", "end"]:
            break

# Run the chatbot only if script is executed directly
if __name__ == "__main__":
    chatbot_loop()
