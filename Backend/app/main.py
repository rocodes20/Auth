from fastapi import FastAPI
from app.routers.users import router 
from app.db.connection import get_db
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)