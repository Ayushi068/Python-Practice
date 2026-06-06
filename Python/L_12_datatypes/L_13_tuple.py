#Tuple - Immutable, ordered collection of elements
#Keys:
#1. Immutable - cannot be modified after creation
#2. Ordered - elements are stored in a specific order and can be accessed using an index
#3. Hybrid elements - can store different types of elements
#4. Variable length - can store any number of elements
#5. Indexing starts from 0

#we cannot reverse the tuple or sort the tuple because it is immutable, but we can access the elements of the tuple using indexing and slicing.

#blank tuple
number = ()
print(number)

#nested tuple : tuple insisde a tuple

jungle = (("Lion","Cat"),("peacock","Bird"),("crocodile","Reptile"))
print(jungle)

#accessing the elements of the tuple
print(jungle[0]) #Output: ('Lion', 'Cat')

forest = ("tiger","elephant","deer","monkey")
print(forest)

#what is not allowed in tuple compared to list
#1. replace - we cannot replace the elements of the tuple because it is immutable
#2. delete - we cannot delete the elements of the tuple because it is immutable
#3. append - we cannot append the elements to the tuple because it is immutable
#4. reverse - we cannot reverse the tuple because it is immutable
#5. sort - we cannot sort the tuple because it is immutable
#6. insert - we cannot insert the elements to the tuple because it is immutable
#7. slicing - we can slice the tuple but it will return a new tuple and the original tuple will remain unchanged
#8. extend - we cannot extend the tuple because it is immutable
#what is allowed in tuple compared to list
#1. indexing - we can access the elements of the tuple using indexing
#2. slicing - we can slice the tuple but it will return a new tuple and the original tuple will remain unchanged
#3. count - we can count the number of occurrences of an element in the tuple using the count() method
#4. index - we can find the index of the first occurrence of an element in the tuple using the index() method
#5. concatenation - we can concatenate two tuples using the + operator
#6. repetition - we can repeat the elements of the tuple using the * operator
#7. membership - we can check if an element is present in the tuple using the in operator
#8. unpacking - we can unpack the elements of the tuple into variables using the unpacking operator (*)
#9. nested tuple - we can have a tuple inside a tuple, which is called a nested tuple. We can access the elements of the nested tuple using indexing and slicing.


my_tuple = (1,2,3,4,5)
empty_tuple = ()

single_element_tuple = (1,) #we need to add a comma after the single element to create a single element tuple otherwise it will be considered as a normal value and not a tuple

print(my_tuple[0])
print(my_tuple[-1])

#slicing 
sub_tuple = my_tuple[1:4] #parameters - start index, end index (exclusive)
print(sub_tuple) #Output: (2, 3, 4)

sub_tuple2 = my_tuple[:3] #parameters - start index, end index (exclusive)
print(sub_tuple2) #Output: (1, 2, 3)


#Packing and Unpacking
#Packing - we can pack the values into a tuple
packed_tuple = 1,2,3,4,5 #we can also create a tuple without using parentheses, but it is recommended to use parentheses for better readability
print(packed_tuple) #Output: (1, 2, 3, 4, 5)    
#Unpacking - we can unpack the values from a tuple into variables
a,b,c,d,e = packed_tuple
print(a) #Output: 1


#immutable
#my_tuple[0] = 10 #Output: TypeError: 'tuple' object does not support item assignment

#count - return the no. of times the value occurs
print(my_tuple.count(2)) #Output: 1

#index - returns the first value of index occurence.
print(my_tuple.index(3)) #Output: 2

