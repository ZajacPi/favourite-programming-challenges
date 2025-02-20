class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev = None
        for i, letter in enumerate(s):
            
            if letter == 'D' or letter == 'M':
                if prev == 'C':
                    result -= 2*100
                if letter == 'D':
                    result += 500
                    prev = 'D'
                if letter == 'M':
                    result += 1000
                    prev = 'M'

            if letter == 'L' or letter == 'C':
                if prev == 'X':
                    result -= 2*10
                if letter == 'L': 
                    result += 50
                    prev = 'L'
                elif letter == 'C': 
                    result += 100
                    prev = 'C'

            if letter == 'V' or letter == 'X':
                if prev == 'I':
                    result -= 2*1
                if letter == 'V':
                    result += 5
                    prev = 'V'
                elif letter == 'X':
                    result += 10
                    prev = 'X'

            if letter == 'I':
                result += 1
                prev = 'I'

        return result

if __name__ == "__main__":
    task = Solution()
    num1 = 'LVIII'
    num2 = 'MCMXCIV'
    print(task.romanToInt(num1))
    print(task.romanToInt(num2))