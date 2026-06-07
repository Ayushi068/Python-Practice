from pydantic import BaseModel
from typing import Optional

class TaskRequest(BaseModel):
    title : str
    description : str = "" #if we don't pass any value for description in the request body, then it will take the default value of an empty string.
    is_completed:bool = False

class TaskPatchRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id: int|None =0