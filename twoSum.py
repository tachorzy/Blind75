class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
  
        for index, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                indexOfDiff = prevMap[diff]
                return [indexOfDiff, index]
            prevMap[val] = index