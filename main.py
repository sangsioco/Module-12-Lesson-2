'''FIRST OBJECTIVE'''
# Task 1: •	Implement a function to create a new list using list comprehension that contains squares of 
# numbers from 1 to n, where n is a parameter. 
'''Time and space complexity = O(n)'''

def squares_list(n):
    return [i ** 2 for i in range(1, n + 1)]

# Function example
print(squares_list(10))  

# Task 2: Implement a function to reverse a sublist within a list from index i to j (inclusive). 
'''Time and space complexity = O(j-i+1)'''
def reverse_sublist(lst, i, j):
    # Ensure i and j are within the bounds of the list
    if i < 0 or j >= len(lst) or i > j:
        raise ValueError("Invalid indices")

    # Reverse the sublist in place
    lst[i:j + 1] = lst[i:j + 1][::-1]
    return lst

# Function example
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_sublist(lst, 2, 4)) 

# Task 3: Implement a function to merge two sorted lists into a single sorted list. 
'''Time complexity = O(j - i +1) processes the length sublist j-i+1'''
'''Space complexity = O(j - i +1) due to temporary sublist storage used for reversing'''

def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0

    # Traverse both lists and append the smaller element to the merged_list
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    # Append remaining elements of lst1 (if any)
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1

    # Append remaining elements of lst2 (if any)
    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1

    return merged_list

# Function example

lst1 = [5, 10, 15, 20, 25]
lst2 = [4, 8, 12, 16, 20]
print(merge_sorted_lists(lst1, lst2))

'''SECOND OBJECTIVE'''

# Task 1: Merge Two Dictionaries
'''Time complexity = O(n + m)-- n= number of items in dict1, m=number of items in dict2'''
'''Space complexity = O(n + m) -- due to storage of the merged dicstionary'''
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    merged_dict.update(dict2)   # Update with the second dictionary's items
    return merged_dict

# Function example
dict1 = {'apple': 1, 'banana': 2, 'carrot': 3}
dict2 = {'bird': 4, 'dog': 5}

print("Merged Dictionary:", merge_dicts(dict1, dict2))  # Should output {'apple': 1, 'banana': 2, 'carrot': 3, 'bird': 4, 'dog': 5}

# Task 2: Intersection of Two Dictionaries
'''Time complexity = O(n + m)-- n= number of items in dict1, m=number of items in dict2'''
'''Space complexity = O(min(n, m)) -- intersection dicstionary contains at most min(n,m) items'''
def intersect_dicts(dict1, dict2):
    intersection = {key: dict1[key] for key in dict1 if key in dict2}
    return intersection

print("Intersection of Dictionaries:", intersect_dicts(dict1, dict2))  # Should output {} as there are no common keys

# Task 3: Count the Frequencies
'''Time complexity - O(n) -- n=number of words in the list'''
'''Spcae complexity - O(u) -- u=number of unique words in the list'''
def count_word_frequencies(words):
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

# Example list of words for counting frequencies
words = ['apple', 'banana', 'apple', 'carrot', 'banana', 'banana']

print("Word Frequencies:", count_word_frequencies(words))  # Should output {'apple': 2, 'banana': 3, 'carrot': 1}
