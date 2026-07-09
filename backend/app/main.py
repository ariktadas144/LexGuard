from fastapi import FastAPI

app = FastAPI(
    title="AI Legal Document Analyzer API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Backend is running!"
    }