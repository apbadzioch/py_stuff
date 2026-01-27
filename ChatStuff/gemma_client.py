# gemma_client (reusable helper module)
from ollama import chat, ChatResponse

def ask_gemma(message: str, history: list | None = None) -> str:
    messages = [
        {
            'role': 'system',
            'content': 'you are a very helpful bot that keeps responses between four and five sentences.',
        },
    ]

    if history:
        messages.extend(history)

    messages.append({'role': 'user', 'content': message})

    response: ChatResponse = chat(
        model = 'gemma3:1b',
        messages = messages
    )

    return response.message.content

