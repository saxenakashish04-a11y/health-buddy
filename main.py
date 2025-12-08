from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Health AI is running!"}

@app.get("/ask")
def ask(question: str):
    return {
        "answer": f"You asked: {question}. If this is serious, please visit a doctor."
    }
