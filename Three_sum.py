def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    triplet = []
    for i in range(0, len(nums)-2):
        for j in range(1, len(nums)-1):
            for k in range(2, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    appended_numbers = [nums[i], nums[j], nums[k]]
                    if [nums[i], nums[j], nums[k]] or [nums[i], nums[k], nums[j]] or [nums[j], nums[k], nums[i]] or \
                        [nums[j], nums[i], nums[k]] or [nums[k], nums[i], nums[j]] or [nums[k], nums[j], nums[i] in triplet:  
                        continue
                    else:
                        triplet.append(appended_numbers)
                                    
    return triplet

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

# i, j, k
# i, k, j
# j, k, i
# j, i, k
# k, i, j
# k, j, i