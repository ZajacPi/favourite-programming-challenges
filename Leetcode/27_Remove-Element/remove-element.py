class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        last = len(nums)-1

        for i in range(len(nums)):

            while nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                nums[last] = None
                last -= 1

        return last+1



if __name__ == "__main__":
    task = Solution()
    nums1 = [3,2,2,3]
    val1 = 3
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    
    k1= task.removeElement(nums1, val1)   
    k2= task.removeElement(nums2, val2)   
    print(nums1)
    print(k1)
    print(nums2)
    print(k2)