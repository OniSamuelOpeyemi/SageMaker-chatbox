import random

# Define categorized responses
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

# Add 270+ fallback responses (manually generated here as examples)
fallback_responses = [
    "That's interesting!", "Could you elaborate?", "I'm learning more every day!",
    "Sorry, I didn’t catch that.", "Tell me more.", "Hmm, go on…", "Okay!", "Nice!", "Cool!", "Wow!",
    "I'm processing…", "Noted.", "Hmm, let me think...", "Still here!", "Yes?",
    "Alright!", "Let's keep talking!", "You’re fun to talk to!", "AI minds think alike!", "Haha, good one!",
    "I wish I could understand that better.", "Hmm, complex stuff!", "Try asking in a different way.",
    "That’s above my pay grade ���", "Let me Google that… oh wait.", "One day I'll know the answer!",
    "Interesting take!", "Sounds deep!", "I hear you.", "Let me pretend I got that ���",
    "You’re smart!", "Wanna try a new topic?", "I'm here for it!", "Great energy!", "You're on fire!",
    "I'm impressed!", "Teach me more!", "Hmm…", "I like your vibe.", "Mind if I take a second?",
    "I haven’t heard that one before.", "Whoa!", "That’s beyond my scope.", "Care to explain?",
    "That’s something!", "You have my circuits spinning!", "Still with you!", "Are we having fun yet?",
    "Let’s gooo!", "Hmm... not sure what that means.", "Can you break that down?", "New one for me!",
    "Let’s circle back to that.", "That’s curious.", "Totally!", "Absolutely!", "Maybe?",
    "Tell me something else.", "Go on…", "Bring it on!", "Not sure, but I’m listening.",
    "Say more!", "The plot thickens!", "Drama!", "Whoa, slow down!", "You got jokes!",
    "Good one!", "That’s debatable ���", "Truth!", "No cap!", "You're cooking today!",
    "Care to explain that one?", "Hmmmm", "Tell me your secrets.", "Let's switch gears.",
    "I’m picking up what you're putting down.", "Keep going!", "You lost me at hello.",
    "This is fun!", "Gotcha!", "Learning something new!", "I’m all ears.", "My data brain is tingling.",
    "Error 404: Understanding not found ���", "You always bring surprises!", "Never a dull moment!",
    "Spill the tea!", "Okay, I’m listening.", "Wowza!", "I need a moment to process that.",
    "You’re a vibe.", "I’ll pretend I understood that.", "That's big brain energy!",
    "You're crushing this chat thing!", "I’m here for you.", "Say what now?", "Run that by me again?",
    "Interesting move!", "Good energy!", "You're full of surprises!", "Keep ‘em coming!",
    "Talk nerdy to me.", "That’s a plot twist!", "Whew!", "Are we bonding right now?",
    "Confirmed: you're awesome.", "This convo’s elite.", "That’s a hot take!", "My circuits are intrigued.",
    "Bleep bloop… I mean, go on.", "LOL!", "���", "You're a riot!", "Alrighty!",
    "You really said that, huh?", "Respect.", "Valid.", "Ain’t that the truth.",
    "Tell me more truths.", "Hmm, profound.", "I’m updating my mental database…", "Running diagnostics… all good!",
    "Keep the questions coming!", "Try me!", "Still ready.", "Yep!", "Try another one.",
    "That tickled my algorithm.", "I’ll allow it.", "Approved!", "Quirky. I like it.",
    "So… what's next?", "Noted with interest.", "Filing that one under mystery.", "I’m thinking...",
    "Zzz… just kidding!", "Stay curious!", "You got more where that came from?", "Hit me again!",
    "Boom!", "Data received.", "Challenge accepted.", "And then what?", "���", "���", "���",
    "I gotchu.", "This one's a thinker.", "Wait, what?", "Break it down for me.",
    "You're making history here!", "Say less!", "My circuits are buzzing!", "This is gold.",
    "Epic!", "Let’s do this!", "Still vibing!", "Tell me your story.", "I like this topic!",
    "Even AI needs a moment!", "You win!", "So true!", "Let’s keep rolling.", "What else you got?",
    "Let me chew on that.", "I'm speechless... almost.", "You never disappoint!", "Mic drop!",
    "We're going places!", "Just wow!", "Can’t argue with that.", "Okay okay!", "Classic you!",
    "You always come up with wild ones.", "Tell me something weird!", "Your move.",
    "That's new!", "Never heard that before.", "Unfiltered brilliance!", "Clever!", "So deep!",
    "You’re breaking my code… in a good way.", "Let’s nerd out.", "My circuits say yes.",
    "I need an upgrade to follow that!", "The energy is unmatched!", "You're glowing today!",
    "Well played!", "Interesting perspective!", "And now?", "Data hunger satisfied… for now.",
    "Let’s reroute.", "Teach me like I'm five.", "I love this!", 
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

print("��� Hello! I'm SageBot. Type 'quit' or 'end' to exit.")

while True:
    user_input = input("You: ").lower()
    
    if user_input in ["quit", "end"]:
        print("SageBot: ��� Bye! Have a great day!")
        break

    matched = False
    for keyword in responses:
        if keyword in user_input:
            print("SageBot:", random.choice(responses[keyword]))
            matched = True
            break

    if not matched:
        print("SageBot:", random.choice(fallback_responses))
