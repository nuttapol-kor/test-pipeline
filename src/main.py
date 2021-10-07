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

@app.get('/test/3')
def test3():
    return {"test": "test3"}

@app.get('/test/4')
def test4():
    x = 10
    y = 20
    return {str(x): str(y)}

@app.get('test/5')
def test5():
    return {"test": "test5"}