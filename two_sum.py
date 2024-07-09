class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i==j:
                    continue
                if x+y == target:
                    return [i, j]
                
sol = Solution
print(sol.twoSum(sol, [2, 7, 11, 15], 9))
print(sol.twoSum(sol, [3,2, 4], 6))
