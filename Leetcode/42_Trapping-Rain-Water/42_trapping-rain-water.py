# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         capacity=0
#         for current in range(max(height)):
#             line=[]
#             for i, h in enumerate(height):
#                 if h>current:
#                     line.append(i)
#             for i in range(len(line)-1):
#                 capacity += line[i+1]-line[i]-1
#         return capacity
       
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        capacity=0
        max_left=height[0]
        for i in range(1, len(height)-1):
            if height[i]<max_left and height[i+1]<????????
        return capacity
       
if __name__ == "__main__":
    task = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(task.trap(height))
    height2 = [4,2,0,3,2,5]
    print(task.trap(height2))