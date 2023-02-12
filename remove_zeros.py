## Problem definition ##
# There is an array of integers. You need to remove the zeros from it. 
# Only O(1) of additional memory can be used.

# Importing the List module from the typing library
# The typing library allows us to have a clearer documentation 
# and provides hints when we are writing the code
from typing import List

# Function removeZeros
# @nums a List of intergers 
# returns the list of intergers without 0s 
def removeZeros(nums: List[int]) -> List[int]:
    # Loop through a range equal to the amount of 0s in our array
    for _ in range(nums.count(0)):
        # Remove the 0 you find and repeat
        nums.remove(0)
    # Return the list when we have removed all the 0s that we counted
    return nums

# Testing our solution 
array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
print(removeZeros(array))
