from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}


# Route for items
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


# Route for users
@app.post("/users/")
def create_user(name: str, age: int):
    return {"name": name, "age": age}


# Route for status check
@app.get("/status")
def health_check():
    return {"status": "Healthy", "uptime": "Everything is running smoothly!"}
