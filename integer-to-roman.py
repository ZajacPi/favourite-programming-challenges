class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        analysing = []
        subtr = 0
        pow_10 = 10
        while subtr != num:
            current = num%pow_10 - subtr
            analysing.append(current)
            subtr += current
            pow_10*=10
        
        print(analysing)
if __name__ == "__main__":
    task = Solution()
    num1 = 3749
    print(task.intToRoman(num1))