#Iteration depends on the condition , until the condition is true the code will be executed
#while condition:
    #code to be executed if the condition is true
    #addition 

#for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It is used when you know the number of iterations beforehand.
#for variable in sequence (string, tuple , list):
    #code to be executed for each item in the sequence


for alphabet in "Ayushi":
    print("alphabet is :",alphabet) #Output: A y u s h i

for num in [1,2,3,4,5]:
    print("number is :",num) #Output: 1 2 3 4 5

#with for loop if can be used

for num in [1,2,3,4,5]:
    if num % 2 == 0:
        print("number is divisible by 2:",num) #Output: 2 4   
    else:
        print("number is not divisible by 2:",num) #Output: 1 3 5

#while loop is used to execute a block of code repeatedly until a certain condition is met. It is used when you do not know the number of iterations beforehand.
#definate and indefinate loops
#indefinate loop = infinte loop


salary = 1
while salary<=5:
    print("salary is:",salary) #Output: 1 2 3 4 5
    salary+=1


#Nested loops - one loop inside another loop

#Example 1

rows = 3
columns = 3

#Outer loop for rows
for i in range(rows):
    #Inner loop for columns
    for j in range(columns):
        print(f"{i*j}",end="\t")
    print() #for new line after each row

#Loop Control Statements - break, continue, pass

#Break - It is used to exit the loop when a certain condition is met.
#Continue - It is used to skip the current iteration of the loop and move to the next iteration when a certain condition is met.
#Pass - non-operational statement, it does nothing, it is used as a placeholder for future code or to create an empty block of code.

count = 0
while(count<5):
    if count == 3:
        print("count is 3, exiting the loop")
        break #it will exit the loop when count is 3
    print("count is:",count) #Output: 0 1 2
    count+=1

for Rajat in "Python":
    if Rajat == "h":
        continue #it will skip the iteration when Rajat is h
    print("Rajat is:",Rajat) #Output: P y t o n

for i in range(5):
    if i == 2:
        pass #it will do nothing when i is 2
    print("i is:",i) #Output: 0 1 2 3 4