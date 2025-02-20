class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.traverse(nums, 0)
    
    def traverse(self, nums, current, jump = 0):
        if current == len(nums)-1:
            return 0
        for i in range(1, nums[current]+1):
            jump += self.traverse(nums, current+i) + i
        if jump >= len(nums) -1:
            return True
if __name__ == "__main__":
    task = Solution()

    nums = [2,3,1,1,4]
    print(task.canJump(nums))