import os
from context import context_corpus
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_openai_response(messages, context):
    prompt = build_prompt(messages)
    system_prompt = build_system_prompt(context)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def build_prompt(messages):
    # Take the 10 most recent messages
    recent_messages = messages[-10:]
    # Extract the message attribute from the messages
    message_history = [message.message for message in recent_messages]
    # Organize the context and message history in a way that the LLM will understand
    prompt = f"Message History: {' '.join(message_history)}"

    return prompt  # Return the prompt as plain text

def build_system_prompt(context):
    return "You are a helpful assistant. Here is the context: " + "\n".join(context_corpus[context])