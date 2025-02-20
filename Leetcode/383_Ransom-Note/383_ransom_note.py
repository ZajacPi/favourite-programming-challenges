class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in ransomNote:
            if letter in magazine:
                magazine -= letter
            else:
                return False
        return True

if __name__ == "__main__":
    task = Solution()
    ransomNote = "a"
    magazine = "b"
    ransomNote = "barbara"
    magazine = "rabarbar"
    print(task.canConstruct(ransomNote, magazine))