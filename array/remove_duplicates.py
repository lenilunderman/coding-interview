# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]

def removeDuplicates(nums):
    i = 0
    j = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
     # plus one because it starts from zero.   
    return i + 1
        
       


nums = [0,1,2,3,4]
removeDuplicates(nums)    