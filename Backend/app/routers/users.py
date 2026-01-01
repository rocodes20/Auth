from fastapi import APIRouter, HTTPException, Depends

from app.schemas.user import UserCreate,LoginResponse,LoginRequest
from app.services.user_service import register_user,login_user
from app.db.connection import get_db

router = APIRouter()
@router.post("/register")
def create_user_route(user:UserCreate,db = Depends(get_db)):
    return register_user(user,db)

@router.post("/login",response_model = LoginResponse )
def login_user_route(user:LoginRequest,db = Depends(get_db)):
    try:
        return login_user(user, db)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))