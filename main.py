from application import app
import uvicorn
import asyncio

from application.app import create_app

if __name__ == '__main__':
    uvicorn.run(create_app(), host='0.0.0.0', port=8000)