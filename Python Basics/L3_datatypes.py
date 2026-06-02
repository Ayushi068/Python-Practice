#DataType - A data type is a classification of data that tells the compiler or interpreter how the programmer intends to use the data. Python has several built-in data types, including:
#1. Numeric Types - int, float, complex
#2. Sequence Types - list, tuple, range
#3. Text Type - str
#4. Mapping Type - dict
#5. Set Types - set, frozenset
#6. Boolean Type - bool
#7. Binary Types - bytes, bytearray, memoryview
#8. None Type - NoneType
#Numeric Types - int, float, complex
x = 5 #int
y = 3.14 #float
z = 1 + 2j #complex

print(type(x)) #Output: <class 'int'>
print(type(y)) #Output: <class 'float'>
print(type(z)) #Output: <class 'complex'>

 
x = "Hello World!" #str
print(type(x)) #Output: <class 'str'>

x = [1,2,3,4,5]  #list
print(type(x)) #Output: <class 'list'>

x =(1,2,3,4,5) #tuple , immutable
print(type(x))

x = range(1,10) #range
print(type(x)) #Output: <class 'range'>
for i in x:
    print(i) #Output: 1 2 3 4 5 6 7 8 9

x = {"name":"Ayushi", "age":25} #dict
print(type(x))

x = {"apple","banana", "cherry"} #set
print(type(x))

x = ({"apple","banana", "cherry"}) #frozenset , immutable
print(type(x))

x = True #bool
print(type(x)) #Output: <class 'bool'>


