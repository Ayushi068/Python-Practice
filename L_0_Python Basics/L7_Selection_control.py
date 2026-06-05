#1. if-else
#2. if
#3 multiple way selection - 1. Nested if statements 2. elif statements

#if condition:
    #code to be executed if the condition is true
#else:
    #code to be executed if the condition is false

#Example 1

salary = int(input("Enter your salary: "))
if salary >= 50000:
    print("You are eligible for a loan.")   
else:
    print("You are not eligible for a loan.")   

#if condition:
    #code to be executed if the condition is true

#Example 2

score = int(input("Enter your score: "))

if(score==100):
    print("You rocked in the class student")
print("Thank you student")


#nested if statements
#if condition1:
    #code to be executed if condition1 is true
    #if condition2:
        #code to be executed if condition2 is true
    #else:
        #code to be executed if condition2 is false

#Example 3
name = "Rajat"
company = "Google"
salary = 60000

if company=="Google":
    if name=="Rajat":
        print("Welcome to Google, Rajat", "your saalry is", salary)
    else:
        print("Welcome to Google,",name)


#elif statements

#Example 4

Raj_sal = 100000
om_sal = 50000
anil_sal = 30000

if Raj_sal > om_sal and Raj_sal > anil_sal:
    print("Raj has the highest salary.")
elif om_sal > Raj_sal and om_sal > anil_sal:
    print("Om has the highest salary.")
elif anil_sal > Raj_sal and anil_sal > om_sal:
    print("Anil has the highest salary.")
else:
    print("All three have the same salary.")