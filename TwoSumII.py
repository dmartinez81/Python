# class Solution(object):
def twoSum( numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    for i in range(0,len(numbers)-1):       
        for j in range(i+1, len(numbers)):
            if i == j: continue
            if numbers[i] + numbers[j] == target:
                return i+1, j+1


input = [2,7,11,15]
target = 9
print(twoSum(input,target))

input = [2,3,4]
target = 6
print(twoSum(input,target))

input = [-1,0]
target = -1
print(twoSum(input,target))

input = [-1,0]
target = -1
print(twoSum(input,target))

