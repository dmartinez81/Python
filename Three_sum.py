# # import numpy as np
# class ThreesumClass:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         self.nums = nums
#         triplet = []
#         for i in range(0, len(nums)-2):
#             for j in range(1, len(nums)-1):
#                 if i == j: continue
#                 for k in range(2, len(nums)):
#                     if j == k or i==k: continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         appended_numbers = [nums[i], nums[j], nums[k]]
#                         # if [nums[i], nums[j], nums[k]] or [nums[i], nums[k], nums[j]] or [nums[j], nums[k], nums[i]] or [nums[j], nums[i], nums[k]] or [nums[k], nums[i], nums[j]] or [nums[k], nums[j], nums[i]] in triplet:  
#                         sorted_appended_numbers = sorted(appended_numbers)
#                         if sorted_appended_numbers in sorted(triplet):
#                             continue
#                         else:
#                             triplet.append(sorted_appended_numbers)
                                        
#         return triplet

# clase = ThreesumClass()
# nums = [-1,0,1,2,-1,-4]
# print(clase.threeSum(nums))

# nums = [3,-2,1,0]
# print(clase.threeSum(nums))

# nums = [-2,0,0,2,2]
# print(clase.threeSum(nums))

# nums = [-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6,12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5,-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12,1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9]
# print(clase.threeSum(nums))

# i, j, k
# i, k, j
# j, k, i
# j, i, k
# k, i, j
# k, j, i

# import numpy as np

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    triplet = []
    for i in range(0, len(nums)-2):
        for j in range(1+i, len(nums)-1):
            if i == j: continue
            for k in range(1+j, len(nums)):
                if j == k or i==k: continue
                if nums[i] + nums[j] + nums[k] == 0:
                    appended_numbers = [nums[i], nums[j], nums[k]]
                    # if [nums[i], nums[j], nums[k]] or [nums[i], nums[k], nums[j]] or [nums[j], nums[k], nums[i]] or [nums[j], nums[i], nums[k]] or [nums[k], nums[i], nums[j]] or [nums[k], nums[j], nums[i]] in triplet:  
                    sorted_appended_numbers = sorted(appended_numbers)
                    if sorted_appended_numbers in sorted(triplet):
                        continue
                    else:
                        triplet.append(sorted_appended_numbers)
                                    
    return triplet

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums = [3,-2,1,0]
print(threeSum(nums))

nums = [-2,0,0,2,2]
print(threeSum(nums))

nums = [-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6,12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5,-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12,1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9]
print(threeSum(nums))

