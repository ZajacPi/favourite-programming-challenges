class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #to check if alphanumeric I can use isalnum()
        scrunched = ''.join(c.lower() for c in s if c.isalnum())
        # print([scrunched[::-1]])
        return scrunched==scrunched[::-1]
    
if __name__ == "__main__":
    task = Solution()
    s1 = 'A man, a plan, a canal: Panama'
    s2 = 'race a car'
    print(task.isPalindrome(s1))
    print(task.isPalindrome(s2))