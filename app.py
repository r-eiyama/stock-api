import uvicorn
from fastapi import FastAPI
from routers import user
app = FastAPI()
app.include_router(user.router)

if __name__ == '__main__':
    uvicorn.run(app)