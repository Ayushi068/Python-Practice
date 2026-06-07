from fastapi import Depends, Request, HTTPException
from sqlalchemy.orm import Session
from src.user.models import UserModel
import jwt
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from src.utils.db import get_db


#Token Send - headers
def is_authenticated(request:Request,db:Session = Depends(get_db)):
    try:
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization header missing")
        token = token.split(" ")[-1]

        #validate token
        data = jwt.decode(token,settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        user_id = data.get("user_id")

        user = db.query(UserModel).get(user_id)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")    
        return user

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


