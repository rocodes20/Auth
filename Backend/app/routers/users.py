from fastapi import APIRouter, HTTPException, Depends

from app.schemas.user import UserCreate
from app.services.user_service import register_user
from app.db.connection import get_db

router = APIRouter()
@router.post("/register")
def create_user_route(user:UserCreate,db = Depends(get_db)):
    return register_user(user,db)