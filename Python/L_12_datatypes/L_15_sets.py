#sets - collection of unique items, unordered, mutable
#Keys:
#1. Unordered - elements are not stored in a specific order and cannot be accessed using an index
#2. Mutable - can be modified after creation
#3. Unique - cannot have duplicate elements
#4. Variable length - can store any number of elements
#5. Hybrid elements - can store different types of elements
#Syntax - {element1, element2, element3}
# Unindexed - we cannot access the elements of the set using an index because it is unordered, but we can access the elements of the set using a loop or by converting the set to a list.
# set si useful to eliminate duplicate elements from a list or a tuple and to perform set operations like union, intersection, difference, etc.

# Example:

my_set = {1,2,3,4,5}
print(my_set)

#set() - it is a built-in function that creates a new set. It can take an iterable (like a list or a tuple) as an argument and returns a set containing the unique elements of the iterable. If no arguments are provided, it returns an empty set.
my_set2 = set([1,2,3,4,4,5,1,5])
print(my_set2)

 # Creating a set - 2 ways
fruits = {"apple", "banana", "orange"}
print(fruits)

numbers = set([1,2,3,3,4,1,2,4,5,6])
print(numbers) #Output: {1, 2, 3, 4, 5, 6} - duplicate elements are removed

#how to make a empty set , as if we use {}, this makes an empty dictionary

empty_set = set()
print(empty_set)


#Accessing set by iteration

for fruit in fruits:
    print(fruit)

#Accessing using membership operator
print("apple" in fruits) #Output: True
print("grape" in fruits) #Output: False 

#pop()

fruit_pop = fruits.pop() #Output: it will remove and return an arbitrary element from the set. The order of the elements is not guaranteed, so the element that is removed can be any element from the set.
print(fruit_pop)

#methods in set
# 1. add() - it adds an element to the set. If the element already exists, it does not add it again and does not raise an error.
# 2. update() - it updates the set with the elements from another iterable (like a list, a tuple, or another set). It adds the unique elements from the iterable to the set. If the iterable contains duplicate elements, only one instance of each element will be added to the set. 
# 3. remove() - it removes a specified element from the set. If the element is not found, it raises a KeyError.
# 4. discard() - it removes a specified element from the set. If the element is not found, it does not raise an error and does nothing.
# 5. clear() - it removes all the elements from the set and returns an empty set.
# 6. union() - it returns a new set that contains all the unique elements from both sets. It can also take multiple sets as arguments and return a new set that contains all the unique elements from all the sets.
# 7. intersection() - it returns a new set that contains only the elements that are present in both sets. It can also take multiple sets as arguments and return a new set that contains only the elements that are present in all the sets.
# 8. difference() - it returns a new set that contains the elements that are present in the first set but not in the second set. It can also take multiple sets as arguments and return a new set that contains the elements that are present in the first set but not in any of the other sets.
# 9. symmetric_difference() - it returns a new set that contains the elements that are  present in either of the sets but not in both sets. It can also take multiple sets as arguments and return a new set that contains the elements that are present in any of the sets but not in all the sets.        
# 10. issubset() - it returns True if all the elements of the first set are present in the second set, otherwise it returns False.  
# 11. issuperset() - it returns True if all the elements of the second set are present in the first set, otherwise it returns False.
# 12. isdisjoint() - it returns True if the two sets have no elements in common, otherwise it returns False.        
