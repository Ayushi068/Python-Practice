#Dictionary - unordered, mutable, and indexed collection of key-value pairs
#Keys:
#1. Unordered - elements are not stored in a specific order and cannot be accessed using an index
#2. Mutable - can be modified after creation
#3. Indexed - elements are stored in key-value pairs and can be accessed using the key
#4. Hybrid elements - can store different types of elements
#5. Variable length - can store any number of elements
#6. Keys must be unique and immutable (string, number, tuple)

#Syntax - {key1:value1, key2:value2, key3:value3}

#blank dictionary
temperature = {}
print(temperature)

#Example 2:
zoo={}

zoo["cat"] = 45
zoo["lion"] = 55
zoo["monkey"] = 69

print(zoo)

#creating and accessing a dict

student = {
    "name": "Ayushi",
    "age" : 29,
    "subjects": ["Python","Data Science","Machine Learning"],
}

print(student["name"]) #Output: Ayushi
print(student["age"]) #Output: 29
print(student["subjects"]) #Output: ['Python', 'Data Science', 'Machine Learning']  


#ADD, MODIFY AND DELETE ELEMENTS IN DICTIONARY

student["marks"] = "A+"
student["age"] = 23
del student["subjects"]

print(student) #Output: {'name': 'Ayushi', 'age': 23, 'marks': 'A+'}


#5 methods 
# 1. keys() - it returns a view object that displays a list of all the keys in the dictionary.
# 2. values() - it returns a view object that displays a list of all the values in the dictionary.
# 3. items() - it returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.
# 4. get() - it returns the value of the specified key. If the key
# 5. pop() - it removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
# 6. update() - it updates the dictionary with the specified key-value pairs. If the key already exists, it will update the value of the key. If the key does not exist, it will add the key-value pair to the dictionary.
# 7. clear() - it removes all the key-value pairs from the dictionary and returns an empty dictionary.
# 8. copy() - it returns a shallow copy of the dictionary. A shallow copy means that it creates a new dictionary with the same key-value pairs, but the values are not copied. If the value is a mutable object, then both the original and the copied dictionary will refer to the same object in memory. If the value is an immutable object, then both the original and the copied dictionary will refer to different objects in memory.
# 9. fromkeys() - it creates a new dictionary with the specified keys and values. The keys are provided as an iterable (like a list or a tuple), and the values can be set to a specific value or left as None by default.
# 10. setdefault() - it returns the value of the specified key. If the key does not exist, it inserts the key with the specified value and returns that value. If the key already exists, it returns the existing value without modifying the dictionary.
# 11. popitem() - it removes and returns an arbitrary key-value pair from the dictionary. If the dictionary is empty, it raises a KeyError. The order of the key-value pairs is not guaranteed, so the pair that is removed can be any pair from the dictionary.
# 12. dict() - it is a built-in function that creates a new dictionary. It can take an iterable of key-value pairs (like a list of tuples) or keyword arguments to create the dictionary. If no arguments are provided, it returns an empty dictionary.
# 13. len() - it returns the number of key-value pairs in the dictionary.

#get method
print(student.get("name")) #Output: Ayushi

#get method with default value
print(student.get("subjects","Not found")) #Output: Not found

#keys method
print(student.keys()) #Output: dict_keys(['name', 'age', 'marks'])

#values method
print(student.values()) #Output: dict_values(['Ayushi', 23, 'A+'])

#items method
print(student.items()) #Output: dict_items([('name', 'Ayushi'), ('age', 23), ('marks', 'A+')])

#pop method
age = student.pop("age")
print(age) #Output: 23

print(student) #Output: {'name': 'Ayushi', 'marks': 'A+'}

#update method
student.update({"age": 25, "city": "Delhi"})
print(student) #Output: {'name': 'Ayushi', 'marks': 'A+',

student.update(age=26, country="India")
print(student) #Output: {'name': 'Ayushi', 'marks': 'A+', 'age': 26, 'city': 'Delhi', 'country': 'India'}   

#clear method
student.clear()
print(student) #Output: {}

#copy method
student = {
    "name": "Ayushi",
    "age" : 29,
    "subjects": ["Python","Data Science","Machine Learning"],
    }


studen_copy = student.copy()
print(studen_copy) #Output: {'name': 'Ayushi', 'age': 29, 'subjects': ['Python', 'Data Science', 'Machine Learning']}

#fromkeys method
keys = ["name", "age", "city"]
values = ["Ayushi", 29, "Delhi"]
new_dict = dict.fromkeys(keys, values)
print(new_dict) #Output: {'name': ['Ayushi', 29, 'Delhi'], 'age': ['Ayushi', 29, 'Delhi'], 'city': ['Ayushi', 29, 'Delhi']}

# setdefault method
print(student.setdefault("name", "Unknown")) #Output: Ayushi
print(student.setdefault("country", "Unknown")) #Output: Unknown
print(student) #Output: {'name': 'Ayushi', 'age': 29, 'subjects': ['Python', 'Data Science', 'Machine Learning'], 'country': 'Unknown'}

#popitem method
print(student.popitem()) #Output: ('country', 'Unknown')
print(student) #Output: {'name': 'Ayushi', 'age': 29, 'subjects': ['Python', 'Data Science', 'Machine Learning']}

#dict method
new_dict = dict(name="Ayushi", age=29, city="Delhi")
print(new_dict) #Output: {'name': 'Ayushi', 'age': 29, 'city': 'Delhi'}


#dictionary comprehension - it is a concise way to create dictionaries. 
#It consists of an expression pair (key: value) followed by a for statement inside curly braces {}.
#it uses iterable and then apply condition to create dictionary with a dynamic way
#Syntax - {key: value for item in iterable if condition}
#readable and concise
#conditional logic : if(filter)
#transforming data: if we have any other list or dictionary we can transform it and create a new dictionary out of it with new add on features and filters
#Performace - it is faster than traditional for loop to create a dictionary

#Example 1:

square = {x:x**2 for x in range(1,6)}
print(square) #Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Example 2, even square:

even_square = {x:x**2 for x in range(1,6) if x%2==0}
print(even_square) #Output: {2: 4, 4: 16}
