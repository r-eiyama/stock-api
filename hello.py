import uvicorn
from fastapi import FastAPI

app = FastAPI()


# uvicorn hello:app --reload で実行可能
@app.get('/')  # URI / にGETリクエストが来たときの処理
def get_hello():
    return {'message': 'Hello from FastAPI Server!'}


if __name__ == '__main__':  # コンストラクタ
    uvicorn.run(app)
