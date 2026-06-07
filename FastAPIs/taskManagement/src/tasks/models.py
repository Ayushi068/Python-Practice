from sqlalchemy import Column, Integer, String, Boolean ,ForeignKey
from src.utils.db import Base

#Until and unless this class is not used , the table will not be created in the database. We need to create an instance of this class and then use it to create the table in the database.
class TaskModel(Base):
    __tablename__ = "tasks" #this will be the name of the table in the database.

    id = Column(Integer,primary_key=True) #this will be the primary key for the table and it will be indexed for faster queries.
    title = Column(String,nullable=False) #this will be the title of the task and it cannot be null.
    description = Column(String,nullable=True) #this will be the description of the task and
    is_completed = Column(Boolean, default=False) #this will be a boolean field that will indicate whether the task is completed or not. It will default to False when a new task is created.
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE")) #this will be the id of the user who created the task. It will be a foreign key that will reference the id field in the users table. It cannot be null because every task must be associated with a user.