from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": "sky"}

@app.get('/test')
def test1():
    return {"test": "test"}