import time
print("🤖 Chat Bot")
print("Type bye to stop chatting")
while True:
    user = input("You: ")
    if user == "hi":
        time.sleep(1)
        print("Bot: Hello!")
    elif user == "how are you":
        time.sleep(1)
        print("Bot: I am fine 😊")
    elif user == "bye":
        time.sleep(1)
        print("Bot: Goodbye!")
        break
    else:
        time.sleep(1)
        print("Bot: I don't understand")