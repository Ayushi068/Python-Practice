#List- Different types of elements are stored in list
#Mutable
#Linear - [1,2,3,4,5]
#Hybrid elements (diff datatypes)
#Variable length
#Indexing starts from 0

#blank list
wedding = []
print(wedding)

birds = ["crow","peacock","eagle"]
print(birds[0])

for bird in birds:
    print(bird)

list_test = [10,10.5,"Ayushi",[1,2,3],{"name":"Ayushi", "age":25}]
print(list_test)

for thursday in [10,20,30,40]:
    print(thursday)

#List Operations
my_list = [100,200,300,400,500]
print(my_list)

#1. replace 
my_list[2] = "Ayushi"
print(my_list) #Output: [100, 200, 'Ayushi', 400, 500]

#2. delete 
del my_list[2]
print(my_list) #Output: [100, 200, 400, 500]

#3. append
my_list.append("hehee")
print(my_list) #Output: [100, 200, 400, 500, 'hehee']

#4. reverse
my_list.reverse()
print(my_list) #Output: ['hehee', 500, 400, 200, 100]

#5. sort
#my_list.sort() #Output: TypeError: '<' not supported between instances of 'int' and 'str'
del my_list[0]
my_list.sort()
print(my_list) #Output: [100, 200, 400, 500]
#datatype needs to be same for sorting

#6. insert
my_list.insert(2,300) #parameters - index, value
print(my_list) #Output: [100, 200, 300, 400, 500]

#7 .slicing
sublist = my_list[1:4] #parameters - start index, end index (exclusive)
print(sublist) #Output: [200, 300, 400]


#8. extend
my_list.extend([600,700,800])
print(my_list) #Output: [100, 200, 300, 400, 500, 600, 700, 800]


my_list2 = [900,1000]
my_list.extend(my_list2)
print(my_list) #Output: [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


#9. remove
my_list.remove(300)
print(my_list) #Output: [100, 200, 400, 500, 600, 700, 800, 900, 1000]

#10. pop
my_list.pop() #removes last element
print(my_list) #Output: [100, 200, 400, 500, 600, 700, 800, 900]
my_list.pop(2) #removes element at index 2
print(my_list) #Output: [100, 200, 500, 600, 700, 800, 900]


#11. clear
my_list.clear() #removes all elements from the list
print(my_list) #Output: []

my_list = [100,200,300,400,500,600,500,400]
#12. index 
i = my_list.index(500) #returns the index of the first occurrence of the value
print(i) #Output: 4

#13. count
c = my_list.count(500) #returns the number of occurrences of the value
print(c) #Output: 2

#14. copy
my_list_copy = my_list.copy() #returns a shallow copy of the list
print(my_list_copy) #Output: [100, 200, 300, 400, 500, 600, 500, 400]

#15. len
length = len(my_list) #returns the number of elements in the list
print(length) #Output: 8
