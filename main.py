# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# In-memory storage for messages
messages = []
message_id_counter = 1

class Message(BaseModel):
    id: int
    message: str
    sender: str
    timestamp: str

@app.get("/api/messages", response_model=List[Message])
def get_messages():
    return messages

@app.post("/api/messages", response_model=List[Message])
def create_message(msg: Message):
    global message_id_counter
    new_message = Message(id=message_id_counter, message=msg.message, sender="user", timestamp="...")
    messages.append(new_message)
    message_id_counter += 1
    # Simulating a bot response
    bot_response = Message(id=message_id_counter, message="Hello!", sender="bot", timestamp="...")
    messages.append(bot_response)
    message_id_counter += 1
    return [new_message, bot_response]

@app.put("/api/messages/{id}", response_model=Message)
def edit_message(id: int, msg: Message):
    for message in messages:
        if message.id == id:
            message.message = msg.message
            return message
    raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/api/messages/{id}")
def delete_message(id: int):
    global messages
    messages = [message for message in messages if message.id != id]
    return {"message": "Message deleted successfully."}