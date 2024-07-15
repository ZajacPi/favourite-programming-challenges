class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) != m+n:
            raise ValueError("nums1 should be longer")
        print(nums1)
        print(nums2)
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()
if __name__ == "__main__":
    task = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3 
    nums2 = [2,5,6]
    n = 3
    task.merge(nums1, m, nums2, n)   
    print(nums1)