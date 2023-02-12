## Problem definition ##
# There are two lists: you need to return the elements that are 
# in the first list but are missing in the second. 
# Describe the complexity of your solution using Big O Notation.

# Importing the List module from the typing library
# The typing library allows us to have a clearer documentation 
# and provides hints when we are writing the code
from typing import List

# Function getMissingElements
# @list1 a List of intergers
# @list2 a List of intergers 
# returns a set of elements that are in list1 but not in list2
def getMissingElements(list1: List[int], list2: List[int]) -> set:
    
    # We can easily find the difference between two sets using the
    # difference() method. We only need to convert the list
    # to set first. 
    set1 = set(list1)
    set2 = set(list2)

    missingElements = set1.difference(set2)

    # Return the missing elements
    return missingElements;

# Testing our solution
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 4, 0]

print(getMissingElements(list1, list2))
