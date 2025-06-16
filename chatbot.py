import string
responses = {
("hello", "hi", "hey", "greetings","namaste"): "Hello! How can I help you today?",
    ("how are you", "how r u", "how are you doing"): "I'm just a program, but I'm doing great!",
    ("what is your name", "what's your name"): "I'm a simple chatbot created to assist you.",
    ("bye", "goodbye", "see you"): "Goodbye! Have a great day!",
    ("what can you do", "help", "features"): "I can respond to greetings and answer basic questions. Try saying hello or asking my name."
}
def preprocess_input(user_input):
    
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation)).strip()
    return user_input
def get_response(user_input):
    for key_phrases, reply in responses.items():
        if user_input in key_phrases:
            return reply
    return "I'm sorry, I don't understand that."
def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        processed = preprocess_input(user_input)       
        response = get_response(processed)
        print("Chatbot:", response)      
        if processed in ("bye", "goodbye", "see you"):
            break
chatbot()
