print("Chatbot: Hello! Welcome to Simple Chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    input1 = input("You: ").lower()
    if "hello" in input1 or "hi" in input1:
        print("Chatbot: Hello! How are you?")
    elif "name" in input1:
        print("Chatbot: I am a Simple Chatbot.")
    elif "how are you" in input1:
        print("Chatbot: I am fine. Thank you!")
    elif "help" in input1:
        print("Chatbot: How can I help you?")
    elif "thank" in input1:
        print("Chatbot: You are welcome!")
    elif "bye" in input1:
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("Chatbot: Sorry, I don't understand.")
