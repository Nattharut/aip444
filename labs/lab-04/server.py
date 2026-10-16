"""API server for the flashcard app.

This server does not make the flashcards itself. It takes the user's notes,
checks them, and passes them to generate_flashcards() in flashcard_generator.py.

Endpoint:
    POST /api/generate
    Body: {"notes": "your notes here", "cards": 3}
    - 200: returns the flashcards from generate_flashcards()
    - 422: the body is wrong (bad JSON, missing notes, cards not a number)
    - 500: something failed while making the flashcards

Run it with `python server.py`. It listens on port 3000.
FastAPI also makes a test page at http://localhost:3000/docs.
"""
import uvicorn
import time
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# The part that actually calls the AI model lives in its own file.
from flashcard_generator import generate_flashcards

app = FastAPI()

# The frontend runs on a different port, so the browser treats it as a
# different origin and blocks the call unless we allow it here.
# "*" allows any website, which is fine for a lab but too open for a real app.
# CORS only applies to browsers. curl or a script can call the API anyway.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add an X-Process-Time header showing how long the request took."""
    start_time = time.time()
    # Everything after this line runs after the route has finished.
    response = await call_next(request)
    process_time = time.time() - start_time
    # Time is in seconds. Useful for seeing how slow the AI call is.
    response.headers["X-Process-Time"] = str(process_time)
    return response

# The JSON body that /api/generate expects.
# notes is required. cards is optional and defaults to 3.
# This only checks types, so empty notes or a negative cards value still pass.
class GenerateRequest(BaseModel):
    notes: str
    cards: int = 3

@app.post("/api/generate")
async def generate_cards(request: GenerateRequest):
    """Make flashcards from the notes sent in the request body."""
    # Because of the GenerateRequest type hint, FastAPI checks the body
    # before this function runs and sends back a 422 if it is invalid.
    # So "request" here is the checked body, not the raw HTTP request.
    try:
        result = await generate_flashcards(request.notes, request.cards)
        return result
    except Exception as e:
        print(f"Server Error: {e}")
        # This sends the real error message to the client. OK for a lab,
        # but a real app should log it and send a generic message instead.
        raise HTTPException(status_code=500, detail=str(e))

# Only runs with `python server.py`, not when uvicorn imports this file.
if __name__ == "__main__":
    print("🚀 Server running on http://localhost:3000")
    # 0.0.0.0 means other devices on the same network can reach it too,
    # not just this computer.
    uvicorn.run(app, host="0.0.0.0", port=3000)
