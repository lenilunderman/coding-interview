# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Input: [1,2,3,1]
# Output: true

# Input: [1,2,3,4]
# Output: false
def containDuplicates(nums):
    # create a lsit with unique values
    unique = list(set(nums))
    # check if the new list is unique comparing with the old list
    if unique == nums:
        # if so, return true
        return True
    else:
        # return false
        return False





nums = [1,2,3,2]
containDuplicates(nums)