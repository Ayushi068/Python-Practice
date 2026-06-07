#contains the logic for handling the requests related to tasks. 
# It will contain the functions that will be called when a request is made to the endpoints defined in the router.py file.
from src.tasks.dtos import TaskRequest, TaskPatchRequest
from sqlalchemy.orm import Session 
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.user.models import UserModel

def create_task(data: TaskRequest,db:Session,user: UserModel):
    data1= data.model_dump()
    #storing the data in the database
    new_task = TaskModel(**data1) #this will create an instance of the TaskModel class and populate it with the data from the request body. 
    #The **data syntax is used to unpack the dictionary and pass its key-value pairs as keyword arguments to the TaskModel constructor.
    new_task.user_id = user.id #this will set the user_id field of the new task to the id of the authenticated user. This is important because we want to associate the task with the user who created it.  
    db.add(new_task) #this will add the new task to the database session. It is not yet committed to the database, it is just added to the session.
    db.commit() #this will commit the changes to the database and save the new task in the database.
    db.refresh(new_task) #this will refresh the new_task instance with the data from the database. This is useful because when we add a new task to the database, it will automatically generate an id for the task and we want to get that id back in our response.
    return new_task #this will return a response to the client indicating that the task was created successfully. We can also return the details of the created task if we want to.


def get_tasks(db:Session,user: UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all() #this will query the database and get all the tasks from the tasks table. It will return a list of TaskModel instances.
    return tasks #this will return a response to the client indicating that the tasks were fetched successfully. We can also return the list of tasks in the response.


def get_task_by_id(task_id:int,db:Session,user: UserModel):
    #task = db.query(TaskModel).filter(TaskModel.id == task_id).first() #this will query the database and get the task with the given id from the tasks table. It will return a TaskModel instance if a task with the given id exists, otherwise it will return None.
    task = db.query(TaskModel).get(task_id) #this is a more efficient way to get a task by id. It will directly get the task with the given id from the database without having to filter through all the tasks. It will return a TaskModel instance if a task with the given id exists, otherwise it will return None.
    if task.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to update this task") #this will return a response to the client indicating that the user is not authorized to update the task if the user is trying to update a task that does not belong to them.
    
    if not task:
        raise  HTTPException(status_code=404, detail="Task not found") #this will return a response to the client indicating that the task was not found if there is no task with the given id in the database.
    return task #this will return a response to the client indicating that the task was fetched successfully. We can also return the details of the fetched task in the response.


def update_task(body:TaskRequest,task_id:int, db:Session,user: UserModel):
    task = db.query(TaskModel).get(task_id) #this will get the task with the given id from the database.
    
    if task.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to update this task") #this will return a response to the client indicating that the user is not authorized to update the task if the user is trying to update a task that does not belong to them.
    
    if not task:
        raise  HTTPException(status_code=404, detail="Task not found") #this will return a response to the client indicating that the task was not found if there is no task with the given id in the database.
    task_data = body.model_dump()
    # task.title = task_data.get("title")
    # task.description = task_data.get("description")
    # task.is_completed = task_data.get("is_completed")
    
    for field, value in task_data.items():
        setattr(task, field, value) #this will set the value of the field in the task instance to the value provided in the request body. It is a more efficient way to update the fields of the task instance without having to write separate lines of code for each field.
     
    db.commit()
    db.refresh(task)
    return task #this will return a response to the client indicating that the task was updated successfully. We can also return the details of the updated task in the response.


def patch_task(task_id: int, body: TaskPatchRequest, db: Session, user: UserModel):
    """Update only the fields provided in the request body"""
    
    task = db.query(TaskModel).get(task_id)
    
    if task.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to update this task")
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Get only the fields that were actually set by the user
    update_data = body.model_dump(exclude_unset=True)
    
    # Update only the fields that are present in the request
    for field, value in update_data.items():
        setattr(task, field, value)
    
    db.commit()
    db.refresh(task)
    return task



def delete_task(task_id:int, db:Session, user: UserModel):
    task = db.query(TaskModel).get(task_id)
    if task.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to delete this task")
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return None

