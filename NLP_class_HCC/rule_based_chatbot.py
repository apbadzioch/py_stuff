import random

bot_responses = {
    "greeting": ['hello', 'hi', 'hey', 'good morning', 'good evening', 'greet', 'greeting'],
    "signoff": ['bye', 'goodbye', 'see ya', 'see you later', 'adios', 'signoff'],
    "times": ['what time is it?', 'can you tell me what time it is?', 'can you tell me the time?', 'time'],
    "baseball": ['do you know anything about baseball?', 'let me know about the baseball scores today.', 'baseball news today', 'baseball'],
    "anything": ['do you know anything?', 'what do you know?', 'anything'],
    "artificial_intel": ['can you tell me about AI?', 'what is AI?', 'ai', 'AI', 'artificial intel', 'machine learning'],
    "star_wars": ['what is star wars?', 'do you know about star wars?', 'who are the skywalkers?', 'was darth vader the real father of luke?', 'star wars']
}

responses = {
    "greeting": ['Hello, how may I help you?', 'What can I do for you today?', 'What is up?', 'Hey, what can I do for you?'],
    "signoff": ['See you later!', 'Goodbye', 'Have a great day.', 'Ciao'],
    "times": ['I do not know the time.', 'I am not connected to the time.'],
    "baseball": ['I do not know about baseball, sorry.', 'What is baseball?'],
    "anything": ['I am a limited chatbot, I only know what I am programmed with.'],
    "artificial_intel": ['I am not aware of what AI is.', 'That is beyond the scope of what I know.'],
    "star_wars": ['I do not know about Star Wars?', 'What is Star Wars?', 'Was there another war?'] 
}

def get_bot_response(user_input):
    for intent, phrases in bot_responses.items():
        for phrase in phrases:
            if phrase in user_input:
                return random.choice(responses[intent])
    return "Sorry, I do not understand, do you have another question?"

def main():
    print("Bot: Hi! How may I help you today? When done type 'quit'.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ['quit', 'exit']:
            print("Bot: Goodbye.")
            break
        print(f"Bot: {get_bot_response(user_input)}")

if __name__ == "__main__":
    main()