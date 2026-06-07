from sqlalchemy.orm import Session
from src.user.dtos import UserRequest,LoginSchema
from src.user.models import UserModel
from fastapi import HTTPException,Request
from pwdlib import PasswordHash 
from pwdlib.hashers.argon2 import Argon2Hasher
import jwt
from datetime import datetime, timedelta
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError



password_hasher = PasswordHash((Argon2Hasher(),))


def get_password_hash(password):
    return password_hasher.hash(password)


def register_user(user_request: UserRequest, db: Session):
    user_data = user_request.model_dump()
    #Validations-
    #1. username duplicacy
    #2. email duplicacy
    
    existing_user = db.query(UserModel).filter(UserModel.username == user_data["username"]).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = db.query(UserModel).filter(UserModel.email == user_data["email"]).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")


    # Remove password and map to hash_password BEFORE creating UserModel
    hash_password =  get_password_hash(user_data.pop("password")) # Remove password from dict
    user_data["hash_password"] = hash_password  # Add hash_password to dict
    
    user = UserModel(**user_data)  # Now all keys match UserModel columns
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login_user(body: LoginSchema, db:Session):
    user= body.model_dump()
    user_= db.query(UserModel).filter(UserModel.username == user["username"]).first()
    if not user_:
        raise HTTPException(status_code=401, detail="Username or password is incorrect")
    if not password_hasher.verify(user["password"], user_.hash_password):
        raise HTTPException(status_code=401, detail="Username or password is incorrect")
    

#we pass 3 agruments to the jwt.encode() method:
# 1. The payload: This is the data that we want to include in the token, it contains the unique values. In this case, we are including the user's id and username.
# 2. The secret key: This is a string that is used to sign the token. It should be kept secret and not shared with anyone. In a real application, you would want to store this in an environment variable or a secure vault.
# 3. The algorithm: This is the algorithm that is used to sign the token. In this case, we are using the HS256 algorithm, which is a symmetric algorithm that uses the same secret key for both signing and verifying the token.
# So basically , the secret key is used to create a signature for the token, which can be used to verify that the token has not been tampered with.
#  The algorithm specifies how the signature is created and verified. 
# When a client sends a request with a token, the server can use the secret key and the algorithm to verify the token's signature and ensure that it is valid before processing the request.
#The algorithm decides how the secret key (or a private key) is used to sign the token and how the server will verify it.

    exp_time = datetime.now()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({"user_id": user_.id, "username": user_.username,"exp": exp_time.timestamp()}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return {"access_token": token}


#Token Send - headers
def is_authenticated(request:Request,db:Session):
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



