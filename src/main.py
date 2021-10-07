from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": "sea"}

@app.get('/test')
def test1():
    return {"test": "tests"}

@app.get('/test/2')
def test2():
    return {"test": "test2"}