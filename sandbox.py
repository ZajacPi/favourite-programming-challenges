# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from matplotlib import pyplot as plt
import matplotlib.patches as patches

class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        result = (None, None)
        volume = 0
        i=0
        j=len(heights)-1
        while i!=j:
            volume = max(volume, min(heights[i], heights[j])*(j-i))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return volume
if __name__ == "__main__":
    task = Solution()
    height1 = [1,8,6,2,5,4,8,3,7]
    print(task.maxArea(height1))
    height2 = [1,1]
    print(task.maxArea(height2))
