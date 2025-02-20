class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}
        for letter, i in s:
            letters[letter].append()
            



if __name__ == "__main__":
    test = Solution()
    s = "egg"
    t = "add"
    print(test.isIsomorphic(s, t))
    s = "foo"
    t = "bar"
    print(test.isIsomorphic(s, t))