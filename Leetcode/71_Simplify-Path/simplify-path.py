class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        directory = ['/']
        word=''
        for i, symbol in enumerate(path):
            if symbol == '/':
                if directory[-1] != '/':
                    directory.append(symbol)
                else:
                    continue
            else:
                word += symbol
                if i != len(path)-1:
                    if path[i+1] == '/' and word != '':
                        directory.append(word) 
                        word = '' 
                else:
                    directory.append(word)
                
        stack = ['/']
        #the dot mechanic 
        for element in directory:
            if element == '.':
                if len(stack) < 3:
                    stack=['/']
                else:
                    stack.pop()
                
            elif element == '..':
                if len(stack) < 5:
                    stack=['/']
                else:
                    stack.pop()
                    stack.pop()
                    stack.pop()
            else:
                if element == '/' and stack[-1] == '/':
                    continue
                else: 
                    stack.append(element)
        
        #checking if the last element is /
        if len(stack)> 1 and stack[-1] == '/':
            stack.pop()
        
        #and turning into string  
        result_path=''
        for element in stack:
            result_path += element
        return result_path
        


if __name__=="__main__":
    task = Solution()
    path1="/home/"
    path2 = "/home//foo/"
    path3 = "/home/user/Documents/../Pictures"
    path4 = "/../"
    path5 = "/.../a/../b/c/../d/./"
    path6="/a/../../b/../c//.//"
    print(task.simplifyPath(path1))
    print(task.simplifyPath(path2))
    print(task.simplifyPath(path3))
    print(task.simplifyPath(path4))
    print(task.simplifyPath(path5))
    print(task.simplifyPath(path6))