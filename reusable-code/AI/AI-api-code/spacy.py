import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a function to generate polite responses
def generate_response(user_input):
    # Process the user's input
    doc = nlp(user_input)

    # Analyze the input and generate a polite response
    polite_responses = {
        "hello": "Hello! How can I assist you today?",
        "thank you": "You're welcome! If you have more questions, feel free to ask.",
        "goodbye": "Goodbye! Have a great day!",
    }

    # Check for specific keywords or patterns in the user's input
    for keyword, response in polite_responses.items():
        if keyword in user_input.lower():
            return response

    # If no specific polite response is matched, provide a default response
    response = "I appreciate your question. Unfortunately, I don't have enough information to answer it fully. Is there anything else you'd like to know?"

    return response

# Main interaction loop
print("Bot: Hello! How can I assist you today? Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye! Have a great day!")
        break

    response = generate_response(user_input)
    print("Bot:", response)
