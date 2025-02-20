import math
class Solution(object):
    def newton(self, n, k):
        return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        max_jumps = n//2
        combinations = 0
        for k in range(max_jumps+1):
            combinations += self.newton(n-k, k)
        return int(combinations)

if __name__ == "__main__":
    task = Solution()
    n=5
    print(task.climbStairs(n))