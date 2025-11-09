
'''
In Python, a list is a collection of items enclosed within square brackets [ ]. Lists are ordered and mutable, meaning you can change, add, and remove elements after the list is created. Lists can contain elements of different data types, including integers, floats, strings, and even other lists. 

'''

# create list 
fruits_list = ['apple','banana','grapes']

# adding value in the list 
fruits_list.append('orange')
fruits_list.extend(['football','cricket','hokey'])

# diplaying value from list 
print('before:===============>')
for i in fruits_list:
    print(i)

# update 
fruits_list[0] = 'baseball'
print('after:====================>')
for i in fruits_list:
    print(i)


# remove from list 
fruits_list.remove('banana')
fruits_list[0] = 'baseball'
print('after removing :====================>')
for i in fruits_list:
    print(i,end=" ")



list_of_books = ['mindsets', 'Money talks', 'self improvement', 'Clean Code']
print(list_of_books)

list_of_books.insert(2,"Atomic Habit")
print(list_of_books)

list_of_books.reverse()
print(list_of_books)

list_of_books.sort()
print(list_of_books)


# pop() - will remove element from last index
electronics = ['laptop', 'mobile', 'pc']
print(electronics)
electronics.pop()
print(electronics)


# printing with index
# The enumerate() function in Python is a built-in function that adds a counter to an iterable and returns it as an enumerate object. This object can then be used in loops to access both the index (or count) and the value of each item in the iterable simultaneously. 

ingridents = ['water', 'coffee power', 'suger']
for i, fruit in enumerate(ingridents):
    print(i, fruit)

list_of_nums = [10,20,30,40]
total_sum = sum(list_of_nums)
print(total_sum)
print("total length of the list:", len(list_of_nums))
print("Minimum value in the list:",min(list_of_nums))
print("Max vale in the list:", max(list_of_nums))