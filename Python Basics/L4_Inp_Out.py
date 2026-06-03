#Input and Output in Python

name = input("Enter your name :") #user input is always taken as a string
print("Hello, "+name +"!")
print("Hello,", name)


"""
"+" & "," in print(): delimiters for output
    
The comma and + work differently in print():

Using + (concatenation):

Joins strings into one single string before printing
No automatic spaces — you control everything
Only works with strings — will error if you mix types


Using , (multiple arguments):

Passes separate arguments to print()
print() automatically adds a space between each argument
Works with any type — no conversion needed


print() with , automatically converts each argument to its string representation for display, which is why it's beginner-friendly!
Behind the scenes, print() calls str() on each argument:

"Hello" → already a string
5 → converted to "5" for printing
"""



age = input("Enter your age :")
print(f"Your age is : {age}")
#f-string is a way to format strings in Python. 
#It is a more readable and concise way to format strings than the traditional string formatting methods.
#It allows you to embed expressions inside string literals, using curly braces {}. 
#The expressions are evaluated at runtime and then formatted using the __format__ protocol.


num1 = input("Enter first number :")
num2 = input("Enter second number :")
#Using + operator to concatenate the numbers will result in string concatenation, not addition.
print("The sum of the numbers is : " + num1 + num2) #This will concatenate the numbers as strings, not add them as integers.
#To add the numbers, we need to convert them to integers first.
num1 = int(num1) #Casting the input to an integer
num2 = int(num2) #Casting the input to an integer
print("The sum of the numbers is : " + str(num1 + num2)) #This will add the numbers and then convert the result to a string for printing.
print("The sum of the numbers is :", num1 + num2) #This will add the numbers and print the result without needing to convert it to a string.

