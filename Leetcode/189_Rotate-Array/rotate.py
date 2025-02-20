class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            for i in range(k):
                nums.insert(0, nums[-1])
                del(nums[-1])
        else:
            temp = nums[-k:]
            del(nums[-k:])
            nums[0:0] = temp
if __name__ == "__main__":
    task = Solution()
    nums = [1,2,3,4,5,6,7]
    k=3
    task.rotate(nums, k)
    print(nums)
    nums = [-1,-100,3,99]
    k=2
    task.rotate(nums, k)
    print(nums)
    nums = [1, 2]
    k=3
    task.rotate(nums, k)
    print(nums)
