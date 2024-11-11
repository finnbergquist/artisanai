# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, constr
from typing import List
from context import ContextType
from bot import get_openai_response
import time
import os
app = FastAPI()

# CORS configuration
origins = [
    os.getenv("FRONTEND_URL"),
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for messages
messages = []
message_id_counter = 1


class Message(BaseModel):
    id: int
    message: str
    sender: str
    timestamp: str
    context: ContextType  # Use the defined Literal for context

class Chat(BaseModel):
    id: int
    messages: List[Message]


@app.get("/api/messages", response_model=List[Message])
def get_messages():
    """Retrieve all messages."""
    return messages

@app.post("/api/messages", response_model=List[Message])
def create_message(msg: Message):
    """Create a new message and simulate a bot response.
    
    Args:
        msg (Message): The message to be created.
    
    Returns:
        List[Message]: The list containing the new message and the bot's response.
    """
    global message_id_counter
    new_message = Message(
        id=message_id_counter,
        message=msg.message,
        sender=msg.sender,
        timestamp=msg.timestamp,
        context=msg.context
    )
    messages.append(new_message)
    message_id_counter += 1

    bot_response = get_openai_response(messages, msg.context)
    

    # Simulating a bot response
    bot_response = Message(
        id=message_id_counter,
        message=bot_response,
        sender="bot",
        timestamp=msg.timestamp,
        context=msg.context 
    )
    messages.append(bot_response)
    message_id_counter += 1
    time.sleep(3)
    return [new_message, bot_response]

@app.put("/api/messages/{id}", response_model=Message)
def edit_message(id: int, msg: Message):
    """Edit an existing message by its ID.
    
    Args:
        id (int): The ID of the message to edit.
        msg (Message): The updated message data.
    
    Returns:
        Message: The updated message.
    
    Raises:
        HTTPException: If the message with the given ID is not found.
    """
    for message in messages:
        if message.id == id:
            message.message = msg.message
            message.context = msg.context  # Update context if needed
            return message
    raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/api/messages/{id}")
def delete_message(id: int):
    """Delete a message by its ID.
    
    Args:
        id (int): The ID of the message to delete.
    
    Returns:
        dict: A confirmation message indicating successful deletion.
    """
    global messages
    messages = [message for message in messages if message.id != id]
    return {"message": "Message deleted successfully."}

@app.post("/api/newchat")
def new_chat():
    """Clear the current chat messages and reset the message ID counter.
    
    Returns:
        dict: A confirmation message indicating the chat has been cleared.
    """
    global messages, message_id_counter
    messages = []  # Clear the current chat messages
    message_id_counter = 1
    return {"message": "Chat cleared successfully."}
