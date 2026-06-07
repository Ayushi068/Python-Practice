from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_router
from src.user.router import user_router


Base.metadata.create_all(engine)
#this will create connection with db and then create all the tables in the database based on the models we have defined.


app = FastAPI(title = "Task Management API", description = "API for managing tasks", version = "1.0.0")
app.include_router(task_router)
#this will include all the routes defined in the task_router in our main application.
#So whenever we define a route in the task_router, it will be available in our main application as well. 
#This is a common pattern for organizing routes in a FastAPI application. We can have multiple routers for different parts of our application and then include them in the main application to create a modular and organized codebase.
app.include_router(user_router)