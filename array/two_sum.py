# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

def twoSum(nums, target):
    # return the indices of two number that adds to target...
    # how to calc target?  x = target - y
    # create an dict to storage the indices
    temp_dict = dict()
    # loop the nums and check for target 'items to be igual to target.
    for i, element in enumerate(nums):
        # possible match?
        possible_match = target - element
        if possible_match in temp_dict:
            return [temp_dict[possible_match], i]
            # add the value to the dict
        
        temp_dict[element] = i
            
            

nums = [2,7,11,15] 
target = 9
twoSum(nums,target)