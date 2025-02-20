class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_rules = {
            '{':'}',
            '(':')',
            '[':']' 
        }
        
        stack = []
        if len(s)%2 !=0:
            return False
        
        for bracket in s:
            #check if we are beginning the stack
            if bracket in ['{', '[', '(']:
                stack.append(bracket)
            #if not, we clear the stack one by one and check if the rules are not broken
            else:
                if stack == []:
                    return False
                elif bracket_rules[stack.pop()] != bracket:
                    return False
        if stack == []:
            return True
        else:
            return False
                
    
        

if __name__ == "__main__":
    task = Solution()
    s1 = "()[]{}"
    s2 = "(]"
    s3 = "([])"
    s4 = "([)]"
    s5 = "(()"
    print(task.isValid(s1))
    print(task.isValid(s2))
    print(task.isValid(s3))
    print(task.isValid(s4))
    print(task.isValid(s5))