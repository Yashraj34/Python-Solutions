import re

responses={
    "hello": "Hi there! How can i assist you today?",
    "hi": "Hello! How can i help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you.",
    "help": "Sure! I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're Welcome! I'm happy to help.",
    "default": "I'm not sure I understand. Could you please rephrase?" 
}

def chatbot_response(user_input):
    user_input=user_input.lower()
    
    for keyword in responses:
        if re.search(keyword,user_input):
            return responses[keyword]
    
    return responses["default"]

def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (type 'bye to exit)")

    while True:
        user_input=input("You: ")

        if user_input.lower() == 'bye':
            print("Chatbot: Bye! have a great day!")
            break

        responses=chatbot_response(user_input)
        print(f"Cahtbot: {responses}")

chatbot()