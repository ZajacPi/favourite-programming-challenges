class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointer problem!!!
        last = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[last]:
                last +=1
                nums[last] = nums[i]
        nums[last+1:] = [None] * (len(nums) - (last + 1))

            
        return last+1
    
if __name__ == "__main__":
    task = Solution()

    nums = [1,1,2]
    print(task.removeDuplicates(nums))
    print(nums)
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(task.removeDuplicates(nums))
    print(nums)
