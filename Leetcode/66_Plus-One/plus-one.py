class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i, digit in enumerate(reversed(digits)):
            num += digit*(10**i)
        num +=1
        res = []
        while num != 0:
            current = num%10
            res.insert(0, int(current))
            num -= current
            num /= 10
        return res



if __name__ == "__main__":
    task = Solution()
    digits = [1,2,3]
    print(task.plusOne(digits))
    digits = [4,3,2,1]
    print(task.plusOne(digits))
    digits = [9]
    print(task.plusOne(digits))