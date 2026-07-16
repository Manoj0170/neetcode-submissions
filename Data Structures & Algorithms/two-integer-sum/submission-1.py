class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums),0,-1):

            if target - nums[i-1] in nums[:i-1]:

                return [nums.index(target - nums[i-1]),i-1]
        