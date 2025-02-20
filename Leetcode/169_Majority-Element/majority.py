class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        visited = []
        stats = {}
        for element in nums:
            if element not in visited:
                visited.append(element)
                stats[element] = 1
            else:
                stats[element] += 1

        return max(stats, key=stats.get)

        

if __name__ == "__main__":
    task = Solution()
    nums = [3,2,3]
    print(task.majorityElement(nums))
    nums = [2,2,1,1,1,2,2]
    print(task.majorityElement(nums))