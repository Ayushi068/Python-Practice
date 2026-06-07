from fastapi import APIRouter,status,Depends,Request
from sqlalchemy.orm import Session
from src.user import controller
from src.user.dtos import UserRequest,UserResponse,LoginSchema
from src.utils.db import get_db


user_router = APIRouter(prefix="/users")


@user_router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_request:UserRequest, db:Session=Depends(get_db)):
    return controller.register_user(user_request, db)


@user_router.post("/login", status_code=status.HTTP_200_OK)
def login_user(body: LoginSchema, db:Session=Depends(get_db)):
    return controller.login_user(body, db)


@user_router.get("/is_auth",response_model=UserResponse, status_code=status.HTTP_200_OK)
def is_auth(request:Request,db:Session=Depends(get_db)):
    return controller.is_authenticated(request,db)


 