#Recursion - function calls itself to solve a problem.
#3 main points -
#Base case - condition under which the function will stop calling itself.
#Breaking down the problem - Big piece of problem - solve it in small chunks.
# Memory usage - it takes so much memory and it is intensive over memeory 
          # because it add the memory stack iterations.

#Example      

def factorial(n):
    if n ==0:
        return 1
    return n*factorial(n-1)

print(factorial(5)) #Output: 120


def fibonacci(n,memo={}):
   if n in memo:
       return memo[n]
   if n<=1:             #Base Case
       return n
   
   memo[n] = fibonacci(n-1,memo)+fibonacci(n-2,memo)
   return memo[n]

print(fibonacci(10))