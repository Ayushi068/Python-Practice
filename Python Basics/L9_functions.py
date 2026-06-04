#functions - A block of code that performs a specific task, it executes when we call it.
#Arguments - these are given inside paranthesis along with function name.
#calling : name()
#Function return the data on the bsis of thr operations inside it, which you will define
#Syntax : def function_name(parameters):
                #operations
                #return value

def ayushi_func():
    print("This is a function") #Output: This is a function

ayushi_func() #Calling the function


#coffe machine - scenario
#Input - coffee type , sugar level ,milk 
#Output - my choice of coffee

def coffee(type, sugarlevel,milk):
    if milk:
        milk_status = "with milk"
    else:
        milk_status = "without milk"
    return f"{type} with {sugarlevel} sugar and {milk_status}"

#using this function

order = coffee("Latte", "2 tsp", True)
print(order) #Output: Latte with 2 tsp sugar and with milk


#Functional Arguments(args) - these are the values that you pass to the function when you call it.
                            #add as many args but there should be comma between them.
                            #Arguments vs Parameters 
                            #Parameters are the variables that are defined in the function definition, while arguments are the values that are passed to the function when it is called.


#4 type of functional arguments - 1. Positional Arguments 2. Keyword Arguments 3. Default Arguments 4. Variable Length Arguments  (*args and **kwargs)  
#1.Positional Arguments - these are the arguments that are passed to the function in the correct order. The number of arguments should be equal to the number of parameters in the function definition.
def func1(a,b,c):
    return f"a is {a}, b is {b} and c is {c}"

print(func1(1,2,3)) #Output: a is 1, b is 2 and c is 3

#Keyword Arguments - these are the arguments that are passed to the function with the name of the parameter. The order of the arguments does not matter in this case.
print(func1(c=3,b=2,a=1)) #Output: a is 1, b is 2 and c is 3

#Default Arguments - these are the arguments that are given a default value in the function definition. If the argument is not passed when the function is called, then the default value will be used.
def func2(a,b=2,c=3): #if we assign the default value to b then we should assign the default value to c as well, otherwise we will get a SyntaxError: non-default argument follows default argument error.
    return f"a is {a}, b is {b} and c is {c}"   


print(func2(1,2)) #Output: a is 1, b is 2 and c is 3
print(func2(1,2,4)) #Output: a is 1, b is 2 and c is 4
#Mutable - which is why tuple shows a strange behaviour
def func3(a,b=2,c=3):
    a.append(4) #if we append 4 to a then it will change the value of a in the next function call as well, because a is mutable.
    return f"a is {a}, b is {b} and c is {c}"

print(func3([1,2,3])) #Output: a is [1, 2, 3, 4], b is 2 and c is 3
#To avoid this we can use the default value as None and then check if the value is None or not, if it is None then we can assign the default value to the parameter.
def func4(a=None,b=2,c=3):
    if a is None:
        a = [1,2,3]
    a.append(4) #if we append 4 to a then it will change the value of a in the next function call as well, because a is mutable.
    return f"a is {a}, b is {b} and c is {c}"

print(func4()) #Output: a is [1, 2, 3, 4], b is 2 and c is 3


#Variable Length Arguments - these are the arguments that can take any number of values. There are two types of variable length arguments - *args and **kwargs.
#*args - these are the variable length arguments that can take any number of positional arguments. The arguments are passed as a tuple to the function.
def func5(*args):
    return f"The arguments are {args}"
print(func5(1,2,3,4,5)) #Output: The arguments are (1, 2, 3, 4, 5)

def sum_num(*args):
    return sum(args)

print(sum_num(1,2,3,4,5)) #Output: 15

#joining strings

def join_str(*args):
    return " ".join(args)
print(join_str("Hello","World!","python")) #Output: Hello World!


#**kwargs - these are the variable length arguments that can take any number of keyword arguments. The arguments are passed as a dictionary to the function.
def func6(**kwargs):    
    return f"The arguments are {kwargs}"

print(func6(a=1,b=2,c=3)) #Output: The arguments are {'a': 1, 'b': 2, 'c': 3}

#You can also use both *args and **kwargs in the same function definition, but *args should be before **kwargs.
def func7(*args, **kwargs):
    return f"The positional arguments are {args} and the keyword arguments are {kwargs}"
print(func7(1,2,3,a=4,b=5,c=6)) #Output: The positional arguments are (1, 2, 3) and the keyword arguments are {'a': 4, 'b': 5, 'c': 6}

# '*' - wildcard character - it is used to unpack the arguments from a list or a tuple. It can also be used to unpack the keyword arguments from a dictionary.


