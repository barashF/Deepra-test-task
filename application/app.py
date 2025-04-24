from fastapi import FastAPI
from application.routers import test_task

def _init_routers(app: FastAPI):
    app.include_router(test_task.router)

def create_app():
    app = FastAPI(
        title='Test task deepra',
        docs_url='/api/swwager'
    )
    _init_routers(app)
    return app