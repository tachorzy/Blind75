# two-sum solution using a dictionary/hashmap O(n) time complexity
# explanation: cache each value that you iterate over in a hashmap, and then check if the difference between the target and the current value is in the hashmap. If it is, return the index of the difference and the current index.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
  
        for index, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                indexOfDiff = prevMap[diff]
                return [indexOfDiff, index]
            prevMap[val] = index