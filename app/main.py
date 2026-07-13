from fastapi import FastAPI

app = FastAPI(title="MES FastAPI")

@app.get("/")
def root():
    return {"message": "Hello MES Agent"}