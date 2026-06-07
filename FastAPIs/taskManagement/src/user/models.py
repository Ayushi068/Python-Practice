from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    username = Column(String, nullable = False)
    hash_password = Column(String, nullable = False)
    email = Column(String, nullable = False)
    phone_number = Column(String, nullable = True)
    

