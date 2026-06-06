from pydantic import BaseModel,Field


class ProductRequest(BaseModel):
    id : int
    title :str 
    price : int = 0 #if we don't pass any value for price in the request body, then it will take the default value of 0.
    count : int  = 0
