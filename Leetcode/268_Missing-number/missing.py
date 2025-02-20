class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected  = 0
        actual = 0
        for i in range(len(nums)+1):
            expected += i
        for element in nums:
            actual += element
        missing_num = expected-actual
        return missing_num
    
if __name__ == "__main__":
    task = Solution()
    nums = [3,0,1]
    print(task.missingNumber(nums))
    nums = [0,1]
    print(task.missingNumber(nums))
    nums = [9,6,4,2,3,5,7,0,1]
    print(task.missingNumber(nums))
