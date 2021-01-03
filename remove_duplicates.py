# class Solution(object):
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        
    nums.sort()
    # for i in range(0, len(nums)-1):
    #     if nums[i] == nums[i+1]:
    #         nums.remove(nums[i+1])
    #         # i -= 1
    i=0
    # while i < len(nums)-1:
    # if nums[i] == nums[i+1]:
    for j in range(0,len(nums)-1):
        if j < len(nums)-1:
            while j < len(nums)-1 and nums[j+1] == nums[j]:
                nums.remove(nums[j+1])
            # j +=1
        
    return len(nums)
    

nums = [0,0,1,1,1,2,2,3,3,4]

# nums = [1,1]

print(removeDuplicates(nums))