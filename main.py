from application import app
import uvicorn
import asyncio

from application.app import create_app

if __name__ == '__main__':
    uvicorn.run(create_app(), host='194.87.74.201', port=443)