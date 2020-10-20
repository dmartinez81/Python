class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(0,len(nums)):
            for p in range(i+1, len(nums)):
                if (nums[i] + nums[p] == target):
                    return i, p

                # added comment 6
                # else:
                #     return False      