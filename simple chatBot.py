def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if "hello" in user_input.lower():
            print("Chatbot: Hi there!")
        elif "how are you" in user_input.lower():
            print("Chatbot: I am good and hope you are also good.")
        elif "what is the name of this training" in user_input.lower():
            print("Chatbot: Python programming for School of Future")
        elif "what is the name of your district" in user_input.lower():
            print("Chatbot: Bandarban")
        elif "bye" in user_input.lower() or "exit" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")
            
chatbot()