#Q1- Discuss String Slicing and provide examles.
#String Slicing is String slicing in Python is a technique used to extract a portion of a string by specifying a range of indices. Slicing allows you to access a substring by using the syntax string[start:stop:step]
text = "My name is pooja"
sliced_text = text[0:5]  # "My nam"

text = "Hello, World!"
sliced_text1 = text[:5]    # "Hello"
sliced_text2 = text[7:]    # "World!"


text = "Welcome"
sliced_text = text[-6:-1]  # "elcome"

text = "Welcome!"
reversed_text = text[::-1]  # "!emocleW"

#Q2- Explain key features of list in python.
#List in python is a data structure that is ordered,
# mutable (modifiable), and can store elements of different data types.
my_list = [3, 1, 4, 1, 5, 9]
print(my_list)  # Output: [3, 1, 4, 1, 5, 9]

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list[4] = 10  # Changing the third element
print(my_list)   # Output: [1, 2, 3, 4, 10, 6, 7, 8]

my_list = [1, "Pooja", 3.14, [1, 2, 3]]
print(my_list)  # Output: [1, 'Pooja', 3.14, [1, 2, 3]]

my_list = [1, 2, 3, 5]
my_list.append(4)    # Adding an element to the end
print(my_list)       # Output: [1, 2, 3, 5, 4]

my_list.remove(2)    # Removing the element with value 2
print(my_list)       # Output: [1, 3, 5, 4]

my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list[2])     # Output: 'c'
print(my_list[1:4])   # Output: ['b', 'c', 'd']


my_list = [[1, 2, 3], ['a', 'b'], [True, False]]
print(my_list[0])      # Output: [1, 2, 3]
print(my_list[1][1])   # Output: 'b'


my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()        # Sorting the list
print(my_list)        # Output: [1, 1, 3, 4, 5, 9]

popped_element = my_list.pop()  # Removing the last element
print(popped_element)  # Output: 9
print(my_list)         # Output: [1, 1, 3, 4, 5]


#Q3- Describe how to access, modify and delete elements in a list in python.
# You can access elements in a list using their index. Indexing in Python starts at 0 for the first element
my_list = ['apple', 'banana', 'cherry', 'date', 'Pineapple']

# Access the first element
first_element = my_list[0]  # 'apple'

# Access the third element
third_element = my_list[2]  # 'cherry'

# Access the last element using negative indexing
last_element = my_list[-1]  # 'Pineapple'

#Modifying Elements-You can modify elements in a list by assigning a new value to a specific index.
my_list = ['apple', 'banana', 'cherry', 'date','Pineapple']

# Modify the second element
my_list[1] = 'blueberry'
print(my_list)  # ['apple', 'blueberry', 'cherry', 'date', 'Pineapple']

# Modify the last element using negative indexing
my_list[-1] = 'dragonfruit'
print(my_list)  # ['apple', 'blueberry', 'cherry', 'date', 'dragonfruit']


#Deleting Elements- Using del Statement: You can remove an element from a list by its index.
#Using remove() Method: You can remove an element by its value.
#Using pop() Method: You can remove and return an element by its index.
my_list = ['apple', 'banana', 'cherry', 'date','Pineapple']

# Delete the second element
del my_list[1]
print(my_list)  # ['apple', 'cherry', 'date', 'Pineapple']

# Delete the last element using negative indexing
del my_list[-1]
print(my_list)  # ['apple', 'cherry', 'date']

my_list = ['apple', 'banana', 'cherry', 'date','Pineapple']

# Remove the element 'banana' by value
my_list.remove('banana')
print(my_list)  # ['apple', 'cherry', 'date', 'Pineapple']

my_list = ['apple', 'banana', 'cherry', 'date', 'pineapple']

# Pop (remove and return) the second element
popped_element = my_list.pop(2)
print(popped_element)  # 'cherry'
print(my_list)         # ['apple', 'banana', 'date', 'Pineapple']

# Pop the last element
popped_element = my_list.pop()
print(popped_element)  # 'Pineapple'
print(my_list)         # ['apple', 'banana', 'date']

#Q4- compare and contrast tuples and lists with example.
#List: Lists are mutable, meaning you can change, add, or remove elements after the list is created.
#Tuple: Tuples are immutable, meaning once a tuple is created, its elements cannot be changed, added, or removed.
# List (Mutable)
my_list = [1, 2, 3]
my_list[2] = 20  # Modifying the second element
print(my_list)   # Output: [1, 2, 20]

# Tuple (Immutable)
my_tuple = (1, 2, 3)
# my_tuple[1] = 20  # Uncommenting this will raise a TypeError

# List for dynamic collection
shopping_list = ['apples', 'bananas', 'carrots']
shopping_list.append('dates')  # Adding an item to the list
print(shopping_list)  # Output: ['apples', 'bananas', 'carrots', 'dates']

# Tuple for fixed collection
point = (10, 20)  # A coordinate point that shouldn't change


#Q5- Describe the key features of sets and provide example of their use.
#Sets in Python are an unordered collection of unique elements. They are highly useful when you need to store data without duplicates and perform operations like unions, intersections, and differences efficiently. 
my_set = {3, 1, 4, 2}
print(my_set)  # Output: {1, 2, 3, 4} or similar order

my_set = {1, 2, 2, 3, 4, 4}
print(my_set)  # Output: {1, 2, 3, 4}


my_set = {1, 2, 3}
my_set.add(4)       # Adding an element
my_set.remove(2)    # Removing an element
print(my_set)       # Output: {1, 3, 4}

my_set = {1, 2, 3}
# my_set[0]  # Uncommenting this will raise a TypeError


my_set = {1, 2, 3, 4}
print(3 in my_set)  # Output: True
print(5 in my_set)  # Output: False


set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)         # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a.intersection(set_b)  # Output: {3}

# Difference
difference_set = set_a.difference(set_b)  # Output: {1, 2}

# Symmetric Difference
sym_diff_set = set_a.symmetric_difference(set_b)  # Output: {1, 2, 4, 5}


# Set comprehension to create a set of squares
squares_set = {x**2 for x in range(5)}
print(squares_set)  # Output: {0, 1, 4, 9, 16}


my_frozenset = frozenset([1, 2, 3, 4])
# my_frozenset.add(5)  # Uncommenting this will raise an AttributeError

#Q6- Discuss the use cases of Tuples and Sets in python programming.
#Tuples and sets in Python each serve distinct purposes and are used in different scenarios based on their characteristics.
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returning a tuple

result = divide(10, 3)
print(result)  # Output: (3, 1)


#Packing and Unpacking
#Use Case: Tuples are often used for packing and unpacking multiple values, making it easy to assign or pass multiple values in a single line.
#Example: Assigning multiple values at once or passing a variable number of arguments to a function.
# Packing
person = ('John', 30, 'Engineer')

# Unpacking
name, age, profession = person
print(name)  # Output: John
print(age)   # Output: 30
print(profession)  # Output: Engineer


#Use Cases for Sets
#Unique Collection of Elements
#Use Case: When you need to maintain a collection of unique elements without duplicates.
#Example: Removing duplicates from a list.
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print(unique_items)  # Output: {1, 2, 3, 4, 5}

#Mathematical Set Operations
#Use Case: Performing operations like union, intersection, difference, and symmetric difference on collections of data.
#Example: Finding common elements between two sets or elements that are in one set but not another.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Intersection
common_elements = set_a & set_b
print(common_elements)  # Output: {3, 4}

# Union
all_elements = set_a | set_b
print(all_elements)  # Output: {1, 2, 3, 4, 5, 6}


#Removing Duplicates
#Use Case: Sets automatically eliminate duplicates, so they are useful when you need to create a collection with no repeated elements.
#Example: Cleaning up a list of email addresses.
emails = ['a@gmail.com', 'b@gmail.com', 'a@gmail.com']
unique_emails = set(emails)
print(unique_emails)  # Output: {'a@gmail.com', 'b@gmail.com'}


#Q7- Describe how to add, modify and delete items in a dictionary in python.
#dictionaries are mutable collections of key-value pairs, where each key is unique.
my_dict = {'name': 'Pooja', 'age': 23}

# Adding a new key-value pair
my_dict['city'] = 'Hamirpur'
print(my_dict)  # Output: {'name': 'Pooja', 'age': 23, 'city': 'Hamirpur'}

my_dict = {'name': 'Pooja', 'age': 23}

# Adding multiple key-value pairs
my_dict.update({'city': 'Hamirpur', 'occupation': 'Engineer'})
print(my_dict)  # Output: {'name': 'Pooja', 'age': 23, 'city': 'Hamirpur', 'occupation': 'Engineer'}

my_dict = {'name': 'Pooja', 'age': 23, 'city': 'Hamirpur'}

# Modifying the value of an existing key
my_dict['age'] = 24
print(my_dict)  # Output: {'name': 'Pooja', 'age': 24, 'city': 'Hamirpur'}

my_dict = {'name': 'pooja', 'age': 23, 'city': 'Hamirpur'}

# Modifying multiple key-value pairs
my_dict.update({'age': 24, 'city': 'Delhi'})
print(my_dict)  # Output: {'name': 'Pooja', 'age': 24, 'city': 'Delhi'}

my_dict = {'name': 'Pooja', 'age': 24, 'city': 'Hamirpur'}

# Deleting a key-value pair
del my_dict['age']
print(my_dict)  # Output: {'name': 'Pooja', 'city': 'Hamirpur'}


my_dict = {'name': 'Pooja', 'age': 23, 'city': 'Hamirpur'}

# Removing a key-value pair and returning its value
age = my_dict.pop('age')
print(age)      # Output: 23
print(my_dict)  # Output: {'name': 'Pooja', 'city': 'Hamirpur'}

my_dict = {'name': 'Pooja', 'age': 23, 'city': 'Hamirpur'}

# Removing and returning the last inserted key-value pair
last_item = my_dict.popitem()
print(last_item)  # Output: ('city', 'Hamirpur')
print(my_dict)    # Output: {'name': 'Pooja', 'age': 23}

my_dict = {'name': 'Pooja', 'age': 23, 'city': 'Hamirpur'}

# Clearing the dictionary
my_dict.clear()
print(my_dict)  # Output: {}


#Q8-Discuss the importance of Dictionary keys being immutable and provide example.
#dictionary keys must be immutable. This means that once a key is created, it cannot be changed. The immutability 
# of dictionary keys is crucial because dictionaries use a hashing mechanism to store and retrieve data efficiently.
#Immutable Keys (Valid):
#Strings: Strings are immutable, making them a popular choice for dictionary keys.
#Tuples: Tuples are also immutable, but they must only contain immutable elements to be used as dictionary keys.
# Using strings as keys
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])  # Output: Alice

# Using a tuple as a key
point = (10, 20)
coordinates = {point: 'Home'}
print(coordinates[(10, 20)])  # Output: Home


#Mutable Keys (Invalid):
#Lists: Lists are mutable and cannot be used as dictionary keys because their contents can change, affecting their hash value.
#Dictionaries: Dictionaries are mutable and also cannot be used as keys.
# Attempting to use a list as a key (will raise a TypeError)
try:
    my_dict = {[1, 2, 3]: 'This will not work'}
except TypeError as e:
    print(e)  # Output: unhashable type: 'list'

# Attempting to use a dictionary as a key (will raise a TypeError)
try:
    my_dict = {{'key': 'value'}: 'Invalid'}
except TypeError as e:
    print(e)  # Output: unhashable type: 'dict'









