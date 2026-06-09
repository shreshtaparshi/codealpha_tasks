print("👋 Welcome!")
print("🤖 I'm your personal assistant.")
print("Type 'bye' anytime to exit.\n")

responses = {
    "hello": ["hello", "hi", "hey"],
    "Doing well! And you?": ["how are you", "how are you doing"],
    "Great! 👍": ["doing well", "good"],
    "I'm Sheley, your personal assistant 😊": ["what is your name", "who are you"],
    "I can tell jokes, motivate you, and chat with you!": ["help", "what can you do"],
    "Every expert was once a beginner. Keep learning and never give up! 💪":
        ["motivate me", "give me motivation"],
    "😂 Why do programmers prefer dark mode? Because light attracts bugs! 🐞":
        ["tell me a joke", "joke"]
}

while True:
    chat = input("\nYou: ").strip().lower()

    if chat == "bye":
        print("Assistant: Bye! 👋")
        break

    found = False

    for response, keywords in responses.items():
        if chat in keywords:
            print("Assistant:", response)
            found = True
            break

    if not found:
        print("Assistant: Sorry, I didn't understand that.")