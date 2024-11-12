
### Run the app
```
uvicorn main:app --reload
```

### Run the tests
```
pytest test_main.py
```

### Endpoints
- GET /api/messages: Retrieves all messages.
- PUT /api/messages/{id}: Updates a specific message by its ID.
- DELETE /api/messages/{id}: Deletes a specific message by its ID.
- POST /api/messages: Creates a new message. Sends bot response to client.
- POST /api/newchat: Initiates a new chat session.

### Assumptions Made
- Multiple users and concurrent chats are not relevant for this project.
- The data persistence layer is in memory, and the data is lost when the server is restarted.
- Context options are limited to the ones in the `context_corpus` dictionary.
- Bot responses use the gpt-4o model, and the message history is limited to 10 messages.
- To add a new client to the cors policy, add it to the `origins` list in `main.py` or set the `FRONTEND_URL` environment variable.
