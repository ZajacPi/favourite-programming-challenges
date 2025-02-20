class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        #checking row condition
        for row in board:
            check = []
            for num in row:
                if num == '.':
                    continue
                elif num in check:
                    return False
                else:
                    check.append(num)

        #checking column condition
        for col in range(9):
            check = []
            for row in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                elif num in check:
                    return False
                else:
                    check.append(num)
        #checking box condition
        ranges = [(0, 3), (3, 6), (6, 9)]
        for i, j in ranges:
            for x, y in ranges:
                check = []
                for col in range(i, j):
                    for row in range(x, y):
                        num = board[row][col]
                        if num == '.':
                            continue
                        elif num in check:
                            return False
                        else:
                            check.append(num)
        
        
        return True
if __name__ == "__main__":
    task = Solution()
    board1 =[["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(task.isValidSudoku(board1))

    board2 =[["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(task.isValidSudoku(board2))