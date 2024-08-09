#Q1- Write a code to reverse a string.
#Reversing a string in Python can be done in several ways.
def reverse_string(s):
    return s[::-1]

# Usage
original_string = "hello"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "olleh"

def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Usage
original_string = "world"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "dlrow"


def reverse_string(s):
    return ''.join(reversed(s))

# Usage
original_string = "python"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "nohtyp"


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Usage
original_string = "recursive"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "evisrucer"


#Q2- Write a code to count vowels in a string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Usage
string = "My name is Pooja"
vowel_count = count_vowels(string)
print(vowel_count)  # Output: 6

#Q3- Write a code to check if a given string is a palindrome or not.
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase to make the check case-insensitive
    return s == s[::-1]

# Usage
string = "Racecar"
result = is_palindrome(string)
print(result)  # Output: True


#Q4- write a code to check if two given strings are anagrams of each other.
#anagrams of each other i.e., they contain the same characters in the same frequencies but potentially in a different order.
def are_anagrams(s1, s2):
    # Convert both strings to lowercase and sort them
    return sorted(s1.lower()) == sorted(s2.lower())

# Usage
string1 = "Listen"
string2 = "Silent"
result = are_anagrams(string1, string2)
print(result)  # Output: True


#Q5-Write a code to find all the occurances of a given sustring within another string.
def find_occurrences(s, substring):
    start = 0
    occurrences = []
    while True:
        start = s.find(substring, start)
        if start == -1:
            break
        occurrences.append(start)
        start += len(substring)  # Move past the current occurrence
    return occurrences

# Usage
string = "This is a test string. This is another test."
sub = "test"
positions = find_occurrences(string, sub)
print(positions)  # Output: [15, 36]


#Q6- write a code to perform basic string compression using counts of repeated characters.
#To perform basic string compression by counting repeated characters, you can implement an algorithm that 
# iterates through the string, counts consecutive occurrences of each character, and constructs a compressed
#  version of the string. 
'''Approach
Initialize Variables: Set up a variable to store the compressed result and a counter for tracking the occurrences of each character.

Iterate Through the String: Traverse the string while counting consecutive occurrences of each character.

Build the Compressed String: Append each character followed by its count to the result string whenever the character changes.

Handle the Last Group: Ensure that the final group of characters is also added to the result after the loop ends.

Compare Lengths: If the compressed string is longer than the original, return the original string to avoid unnecessary compression.
'''
def compress_string(s):
    if not s:
        return s

    compressed = []
    count = 1
    length = len(s)

    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    # Append the last group
    compressed.append(s[-1] + str(count))

    compressed_string = ''.join(compressed)

    # Return the original string if compression is not effective
    return compressed_string if len(compressed_string) < length else s

# Usage
original_string = "aabcccccaaa"
compressed_string = compress_string(original_string)
print(compressed_string)  # Output: "a2b1c5a3"


#Q7- Write a python code to determine if string has all unique characters.
def has_unique_characters(s):
    return len(s) == len(set(s))

# Usage
string = "abcdefg"
result = has_unique_characters(string)
print(result)  # Output: True

string = "aabbcc"
result = has_unique_characters(string)
print(result)  # Output: False


#Q8- write a code to convert a given string to uppercase or lowercase.
def to_uppercase(s):
    return s.upper()

# Usage
string = "my name is pooja"
uppercase_string = to_uppercase(string)
print(uppercase_string)  # Output: "MY NAME IS POOJA"


def convert_case(s, to_upper=True):
    if to_upper:
        return s.upper()
    else:
        return s.lower()

# Usage
string = "Mixed CASE String"
uppercase_string = convert_case(string, to_upper=True)
print(uppercase_string)  # Output: "MIXED CASE STRING"

lowercase_string = convert_case(string, to_upper=False)
print(lowercase_string)  # Output: "mixed case string"



#Q9- Write a code to count the number of words in string.
def count_words(s):
    # Split the string into words based on whitespace
    words = s.split()
    # Return the number of words
    return len(words)

# Usage
string = "This is an example string with several words."
word_count = count_words(string)
print(word_count)  # Output: 7


#Q10- Write a code to concatenate two string without using + operator.
def concatenate_strings(s1, s2):
    return s1.__add__(s2)

# Usage
string1 = "Good "
string2 = "morning!"
result = concatenate_strings(string1, string2)
print(result)  # Output: "Good morning!"


def concatenate_strings(s1, s2):
    return ''.join([s1, s2])

# Usage
string1 = "Pooja "
string2 = "Verma"
result = concatenate_strings(string1, string2)
print(result)  # Output: "Pooja Verma"

#Q11- Write a code to remove all the occurance of a specific element from a list.
def remove_all_occurrences(lst, element):
    return [x for x in lst if x != element]

# Usage
my_list = [1, 2, 3, 4, 2, 5, 2, 6]
element_to_remove = 2
result = remove_all_occurrences(my_list, element_to_remove)
print(result)  # Output: [1, 3, 4, 5, 6]


def remove_all_occurrences(lst, element):
    return list(filter(lambda x: x != element, lst))

# Usage
my_list = [1, 3, 4, 3, 5, 3, 6]
element_to_remove = 3
result = remove_all_occurrences(my_list, element_to_remove)
print(result)  # Output: [1, 4, 5, 6]


#Q12- Implement a code to find Second largest no. in a given list of integer.
def find_second_largest(lst):
    if len(lst) < 2:
        return None  # Not enough elements to find the second largest
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[1]

# Usage
my_list = [10, 20, 4, 45, 99]
second_largest = find_second_largest(my_list)
print(second_largest)  # Output: 45


def find_second_largest(lst):
    if len(lst) < 2:
        return None  # Not enough elements to find the second largest
    
    largest = second_largest = float('-inf')
    
    for number in lst:
        if number > largest:
            second_largest = largest
            largest = number
        elif largest > number > second_largest:
            second_largest = number
    
    return second_largest if second_largest != float('-inf') else None

# Usage
my_list = [10, 20, 4, 45, 99, 99]
second_largest = find_second_largest(my_list)
print(second_largest)  # Output: 45


#Q13- Create a code to count the occurrence of each element in a lisst and return adictionary with elements as key and their counts as values.
def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Usage
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 5]
result = count_occurrences(my_list)
print(result)  # Output: {1: 1, 2: 2, 3: 1, 4: 3, 5: 2}


def count_occurrences(lst):
    return {item: lst.count(item) for item in set(lst)}

# Usage
my_list = [1, 1, 2, 3, 4, 2, 4, 4, 5]
result = count_occurrences(my_list)
print(result)  # Output: {1: 2, 2: 2, 3: 1, 4: 3, 5: 1}


#Q14- Write a code to reverse a list in a place without using any built in reverse function.
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # Swap the elements at left and right indices
        lst[left], lst[right] = lst[right], lst[left]
        # Move towards the center
        left += 1
        right -= 1

# Usage
my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print(my_list)  # Output: [5, 4, 3, 2, 1]


#Q15- implement a code to find and remove duplicates from a list while preseving the original order of elements.
def remove_duplicates(lst):
    seen = set()
    unique_list = []
    
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    
    return unique_list

# Usage
my_list = [1, 2, 2, 3, 4, 4, 5, 3, 6]
result = remove_duplicates(my_list)
print(result)  # Output: [1, 2, 3, 4, 5, 6]


#Q16- Create a code to check if given list is sorted (either in a ascending or descending order) or not.
def is_sorted(lst):
    if lst == sorted(lst):
        return "Ascending"
    elif lst == sorted(lst, reverse=True):
        return "Descending"
    else:
        return "Not sorted"

# Usage
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
list3 = [3, 1, 4, 2]

print(is_sorted(list1))  # Output: "Ascending"
print(is_sorted(list2))  # Output: "Descending"
print(is_sorted(list3))  # Output: "Not sorted"


#Q17- Write a code to merge two sorted lists into a  single sorted list.
def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    # Merge the lists by comparing elements from both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # If there are remaining elements in list1, add them to merged_list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If there are remaining elements in list2, add them to merged_list
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


#Q18- Implement a code to find the intersection of two given lists.
def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1 & set2)
    return intersection

# Usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_intersection(list1, list2)
print(result)  # Output: [4, 5]

#List comprehension
def find_intersection(list1, list2):
    intersection = [item for item in list1 if item in list2]
    return intersection

# Usage
list1 = ['apple', 'pineapple', 'cherry', 'date']
list2 = ['cherry', 'date', 'fig', 'grape']
result = find_intersection(list1, list2)
print(result)  # Output: ['cherry', 'date']

#Q19- Create a code to find the union of two lists without duplicates.
def find_union(list1, list2):
    return list(set(list1) | set(list2))

# Usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_union(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


def find_union(list1, list2):
    return list(set(list1).union(set(list2)))

# Usage
list1 = ['apple', 'pineapple', 'cherry']
list2 = ['cherry', 'date', 'fig', 'apple']
result = find_union(list1, list2)
print(result)  # Output: ['apple', 'pineapple', 'date', 'cherry', 'fig']


#Q20- Write a code to shuffle a  given list randomly without using an built-in shuffle functions.
import random

def shuffle_list(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        # Generate a random index from 0 to i
        j = random.randint(0, i)
        # Swap the elements at indices i and j
        lst[i], lst[j] = lst[j], lst[i]

# Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle_list(my_list)
print(my_list)  # Output: A shuffled version of my_list, e.g., [3, 1, 7, 9, 5, 8, 4, 6, 2]


#Q21- Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples.








