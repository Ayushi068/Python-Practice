x = 5
y = 10 
print(x,y)


#Case sensitive
x = "Rajat"
X = "Ayushi"
print(x)   
print(X)

#Variable names can contain letters, numbers, and underscores. They cannot start with a number. They are case sensitive.
my_variable = "Hello"
my_variable2 = "World"
print(my_variable)
print(my_variable2)

#Variable names cannot contain spaces. They can use underscores to separate words.
my_variable_name = "Hello World"
print(my_variable_name) 

#Variable names cannot be the same as reserved keywords in Python. Reserved keywords are words that have a special meaning in Python and cannot be used as variable names.
#For example, "if", "else", "while", "for", "def", "class", etc. are reserved keywords in Python and cannot be used as variable names.

#Variable names should be descriptive and meaningful. They should give an idea of what the variable is used for. This makes the code more readable and easier to understand.
my_age = 25
my_name = "Ayushi"
print(my_age)
print(my_name)

#You can also assign multiple variables in one line. This is called unpacking.
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


Fruit = ("Apple", "Banana", "Cherry","Mango")
x,y,z= Fruit
print(x)
print(y)
print(z)

#If the number of variables is less than the number of values, you can use the * operator to assign the remaining values to a variable as a list else you will get a ValueError: too many values to unpack (expected 3) error.
# Example:   
a, b, *c = 1, 2, 3, 4, 5
print(a) #Output: 1
print(b) #Output: 2
print(c) #Output: [3, 4, 5]



#You can also assign the same value to multiple variables in one line.
x = y = z = 0
print(x)
print(y)
print(z)

#You can also use the input() function to get user input and assign it to a variable.
name = input("Enter your name: ")
print("Hello, " + name + "!")


#You can also use the type() function to check the type of a variable.
print(type(x))
print(type(name))


#Casting -You can also use the str(), int(), and float() functions to convert variables from one type to another.
age = input("Enter your age: ")
age = int(age) #Casting the input to an integer
print("Your age is:", age)
print(type(age))


#Long Variable Name:
#3 solutions - Camel Case, Pascal Case, Snake Case
#Camel Case - The first letter of each word is capitalized except for the first word. Example: myVariableName
#Pascal Case - The first letter of each word is capitalized. Example: MyVariableName
#Snake Case - All letters are lowercase and words are separated by underscores. Example: my_variable_name

#How to output variables

x = "Biden is president of USA"
print(x) #Using print() function to output the variable

x = "Biden"
y = "is"
z = "president"

print(x,y,z)
print(x+" "+y+" "+z)


#Global Variables - A variable that is defined outside of a function and can be accessed inside the function as well as outside the function.
#Local Variables - A variable that is defined inside a function and can only be accessed inside that function.

x = "Global Variable"
print("Outside the function:", x) #Accessing the global variable outside the function

def my_function():
    global x #Using the global keyword to access the global variable inside the function if we want to modify it. If we don't use the global keyword, it will create a new local variable with the same name and will not modify the global variable.
    print("Inside the function:", x) #Accessing the global variable inside the function
    x = "Local Variable"
    print("Inside the function:", x)

my_function()
print("Outside the function:", x)


#Why we need to define the 'x' variable as global though we have accessed it before modyfing it
#and though we can access it both inside and outside the function without defining it as global?

"""
The key: Python makes this decision before the function runs — at compile time, not runtime.

How Python reads your function:

First pass (compile time): Python scans the entire function to find all assignments

Sees: x = "Local Variable" on line 5
Decision: "x is a local variable for this entire function"
Second pass (runtime): Python executes line by line

Line 4: print(x) — looks for local x (because it decided earlier that x is local)
Problem: Local x doesn't exist yet!
Error: UnboundLocalError
It doesn't matter that the assignment comes after the read — Python already decided x is local before executing any line.

Visual breakdown:

Why Python works this way:

Python needs to know variable scope before running code to optimize performance. It can't change its mind halfway through the function.

The rule: If a variable is assigned anywhere in a function (without global), Python treats it as local for the entire function, even before the assignment line.

"""

#At compile time, Python determines that 'x' is a local variable because it sees an assignment to 'x' later in the function. Therefore, when it tries to execute 'print(x)' before the assignment, it looks for a local variable 'x' that hasn't been defined yet, resulting in an UnboundLocalError.
#To fix this, you can either define 'x' as a global variable using the 'global' keyword or avoid assigning to 'x' inside the function if you want to access the global variable.

#The Order of execution of variables in Python is as follows at runtime:
#1. Local variables
#2. Enclosing variables (if the function is nested)
#3. Global variables
#4. Built-in variables

#This is called LEGB rule: Local → Enclosing → Global → Built-in

