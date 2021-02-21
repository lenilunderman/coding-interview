# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Input: nums = [2,2,1]
# Output: 1
# Input: nums = [4,1,2,1,2]
# Output: 4
def singleNumber(nums):
    no_duplicates = []
    for idx, value in enumerate(nums):
        if nums[idx] not in no_duplicates:
            no_duplicates.append(nums[idx])
        else:
            no_duplicates.remove(nums[idx])
    
    # return the result
    return no_duplicates
        

nums = [4,1,2,1,2]
singleNumber(nums)
