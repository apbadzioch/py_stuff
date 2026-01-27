from ollama import chat
from ollama import ChatResponse

# as of 11-18-25, this model was trained up till November 2, 2023.
# found out when asked the model to tell me the 2025 world series results.

while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        break

    response: ChatResponse = chat(
        model='gemma3:1b',
        messages=[
            {
                # initial instructions for the model
                'role': 'system',
                'content': 'you are very helpful and keep your responses between three and four sentences.'
            },
            {
                # using the users input until they 'quit' the loop
                'role': 'user',
                'content': user_input,
            }
        ]
    )

#    print(response['message']['content'])
    print(response.message.content)