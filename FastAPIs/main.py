from fastapi import FastAPI, Request #FastAPI  is just a class which is used to create an instance of the FastAPI application.
from mock_data import products #This line imports the products variable from the mock_data module. This variable likely contains some sample data that we can use in our API.

app = FastAPI() #Here we are creating an instance of the FastAPI application and assigning it to the variable app.

@app.get("/") #This is a decorator that tells FastAPI that the function below is associated with the root endpoint ("/") and will handle GET requests.
def home() :
    return {"message" : "Hello World"} #This is a simple function that returns a dictionary with a key "message" and a value "Hello World". This will be the response when we access the root endpoint of our API.

# @app.get("/contact")
# def contact():
#     return {"message": "you can connect us anytime"}

@app.get("/products") #This is another decorator that tells FastAPI that the function below is associated with the "/products" endpoint and will handle GET requests.
def get_products():
    return products #This function simply returns the products variable that we imported from the mock_data module. This will allow us to access the list of products when we call this function.

#what if we want to get a specific product
#we have to pass the id of the product in the url and then we can use that id to get the specific product from the products list.
#We can use path parameters to achieve this.
    # We can define a path parameter in the url by using curly braces {}. 
    # For example, we can define a path parameter called id like this: /products/{id}. 
    # Then we can use that id in the function to get the specific product from the products list.

#We can use query parameters to filter the products based on certain criteria.
    # We can define a query parameter in the url by using the question mark ? followed by the parameter name and value.
    # Here we pass the value as key-value pair in the url.
    # It is used when we don't know the number of parameters we want to pass in the url. We can pass any number of parameters in the url and we can access them in the function by defining arguments with the same name as the parameter name in the url.
    # For example, we can define a query parameter called price like this: /products?price=1000. 
    # We can give multiple parameters as well ,which are separated by '&', For example, /products?id=1&title=Mobile&count=10
    # Then we can use that price in the function to filter the products based on their price.

 #Path Params

@app.get("/products/{id}")
def get_product_by_id(id:int): #have to define the argument as the same name as the path parameter defined in the url.
    #if product available with the given id , then return product else return error message.
    for p in products:
        if p.get("id") == id:
            return p
        
    return {
        "error": "Product not found"
    }


@app.get("/greet/{name}/{date}") #Here we are defining a path parameter called name in the url. We can access this parameter in the function by defining an argument with the same name.
def greet_user(name:str, date:str) :
    return {
        "greeting": f"Hello {name}, today's date is {date}"
    }


#Query Params

# @app.get("/greet") #unlike path parameters, query parameters are optional. So we can call this endpoint without passing any query parameter and it will still work.
# def greet_user(name:str) :
#     return {
#         "greeting": f"Hello {name}"
#     }
 

# @app.get("/greet") #unlike path parameters, query parameters are optional. So we can call this endpoint without passing any query parameter and it will still work.
# def greet_user(name:str,age:int) :
#     return {
#         "greeting": f"Hello {name}, your age is {age} "
#     }
 


#since we can have any number of parameters in the url ,so we won't define it like above
#we can use **kwargs to get all the query parameters in the url and then we can use those parameters to filter the products based on certain criteria.

@app.get("/products/filter")
def filter_products(**kwargs) :
    filtered_products = products
    for key, value in kwargs.items():
        filtered_products = [p for p in filtered_products if str(p.get(key)) == value]
    return filtered_products


#we use request body when we want to send some data to the server in the form of json. 
# We can use the @app.post decorator to define a post endpoint 
# and then we can use the request body to get the data sent by the client.
# request contains all the things - body parameters, query parameters, path parameters, headers, cookies, etc.

@app.get("/greet")
def filter_products(request: Request):
    #print(request) #This will print all the query parameters sent by the client in the url.
    #print(request.query_params) #This will print the query parameters sent by the client in the url. It will be of type QueryParams which is a subclass of dict.
#It is an object of Pydantic's BaseModel class which contains all the information about the request sent by the client.
#  We can access the query parameters using request.query_params, path parameters using request.path_params, headers using request.headers, cookies using request.cookies, etc.
    query_params = dict(request.query_params) #This will convert the query parameters into a dictionary.
    return f"greeting:Hello {query_params.get("name")},your age is {query_params.get("age")}"


#Different HTTPs methods
#CRUD operations are performed using different HTTP methods.
# GET - used to get data from the server
# POST - used to send data to the server
# PUT - used to update data on the server
# DELETE - used to delete data from the server

#Why we have these Https method
# We have 2 things client and server.
#Now if the client wants to get some data from the server, client will send a request to the server.
#the request will be the get request
#based on the request the server will response with some data.
#Now if the client wants to send some data to the server, client will send a post request to the server.
#based on the request the server will response with some message that data is received successfully.
#the server connects to the database and stores the data sent by the client in the database.
#Now if the client wants to update some data on the server, client will send a put request to the server.
#based on the request the server will response with some message that data is updated successfully.
#in this case in the request body we will send the id of the data that we want to update and the new data that we want to update.
#Now if the client wants to delete some data from the server, client will send a delete request to the server.
#based on the request the server will response with some message that data is deleted successfully.
#in this case in the request body we will send the id of the data that we want to delete.

