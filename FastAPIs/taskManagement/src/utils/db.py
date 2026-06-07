

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings

Base = declarative_base() #this will be the base class for all our models.
#We will inherit from this class to create our models.
engine = create_engine(url = settings.DB_CONNECTION) 
#this will create a connection to the database using the connection string we have defined in our settings. 
# We will use this engine to perform all our database operations.

local_session = sessionmaker(bind=engine)

#now we need to create a db provider so that whenever we need to access the database, we can use this provider to get a session and perform our operations.

def get_db():
    session = local_session()
    try:
        yield session
    finally:
        session.close()

#yield is used here to create a generator that will yield a session to the caller and then close the session once the caller is done with it. This is a common pattern for managing database sessions in FastAPI.
#Basically, when we call get_db(), it will create a new session and yield it to the caller. Once the caller is done with the session, it will automatically close the session to free up resources.
#so yeild in simple words is used to create a generator that can be used to manage resources like database sessions in a clean and efficient way.
# defination of yeild - The yield statement is used to produce a value from a generator function and pause the function’s execution, allowing it to be resumed later.