from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskRequest, TaskPatchRequest, TaskResponse
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import UserModel

task_router = APIRouter(prefix="/tasks")

@task_router.post("/",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(data: TaskRequest, db: Session = Depends(get_db),user: UserModel = Depends(is_authenticated)):
    return controller.create_task(data, db,user)

@task_router.get("/",response_model=List[TaskResponse],status_code=status.HTTP_200_OK)
def get_all_tasks(db: Session = Depends(get_db),user: UserModel = Depends(is_authenticated) ):
    return controller.get_tasks(db,user)

@task_router.get("/{task_id}",response_model=TaskResponse,status_code = status.HTTP_200_OK)
def get_task_by_id(task_id:int, db: Session = Depends(get_db),user: UserModel = Depends(is_authenticated) ):
    return controller.get_task_by_id(task_id, db,user)

@task_router.put("/{task_id}",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def update_task(body:TaskRequest, task_id:int, db:Session=Depends(get_db),user: UserModel = Depends(is_authenticated) ):
    return controller.update_task(body, task_id, db,user)

@task_router.patch("/{task_id}",response_model=TaskResponse  ,status_code=status.HTTP_200_OK)
def patch_task(body: TaskPatchRequest, task_id: int, db:Session=Depends(get_db),user: UserModel = Depends(is_authenticated) ):
    return controller.patch_task(task_id, body, db,user)

@task_router.delete("/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db:Session=Depends(get_db),user: UserModel = Depends(is_authenticated) ):
    return controller.delete_task(task_id, db,user)
