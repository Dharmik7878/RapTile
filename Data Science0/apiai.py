from openai import OpenAI

key = "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"

messages = []

client = OpenAI(
    api_key=key,  # This is the default and can be omitted
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(messages=messages, model="gpt-4o")
    
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message["content"]}")

if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)