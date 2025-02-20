class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            i=1
            r=0
            t=x
            c = []
            while t >0:
                r = t%(10**i)
                c.append(r/10**(i-1))
                t-=r
                i+=1
            f = len(c)//2
            for i in range(len(c)//2):
                if c[i] != c[-(i+1)]:
                    return False
            return True
        return False

if __name__ == "__main__":
    task = Solution()
    num1=121
    num2=123321
    num3=10
    print(task.isPalindrome(num1))
    print(task.isPalindrome(num2))
    print(task.isPalindrome(num3))