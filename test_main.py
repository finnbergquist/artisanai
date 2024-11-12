import pytest
from fastapi.testclient import TestClient
from main import app, Message

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_messages():
    """Clear messages before each test."""
    client.post("/api/newchat")

def test_create_message():
    response = client.post("/api/messages", json={
        "id": 1,
        "message": "Hello, world!",
        "sender": "user",
        "timestamp": "2023-10-01T12:00:00Z",
        "context": "Onboarding"
    })
    # Log response content for debugging
    print(response.json())  # Add this line to see the response
    assert response.status_code == 200

def test_get_messages():
    client.get("/api/messages")
    response = client.get("/api/messages")
    assert response.status_code == 200

def test_edit_message():
    client.post("/api/messages", json={
        "id": 1,
        "message": "Hello, world!",
        "sender": "user",
        "timestamp": "2023-10-01T12:00:00Z",
        "context": "Onboarding"
    })
    response = client.put("/api/messages/1", json={
        "id": 1,
        "message": "Hello, updated world!",
        "sender": "user",
        "timestamp": "2023-10-01T12:00:00Z",
        "context": "Onboarding"
    })
    # Log response content for debugging
    print(response.json())  # Add this line to see the response
    assert response.status_code == 200

def test_delete_message():
    client.post("/api/messages", json={
        "id": 1,
        "message": "Hello, world!",
        "sender": "user",
        "timestamp": "2023-10-01T12:00:00Z",
        "context": "Onboarding"
    })
    response = client.delete("/api/messages/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Message deleted successfully."}


def test_new_chat():
    client.post("/api/messages", json={
        "id": 1,
        "message": "Hello, world!",
        "sender": "user",
        "timestamp": "2023-10-01T12:00:00Z",
        "context": "Onboarding"
    })
    response = client.post("/api/newchat")
    assert response.status_code == 200
    assert response.json() == {"message": "Chat cleared successfully."}
