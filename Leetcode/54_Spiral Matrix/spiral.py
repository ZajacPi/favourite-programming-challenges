class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # col = len(matrix[0])
        # row = len(matrix)
        # spiral = []
        # n = 0
        # num_of_loops = min(col, row)//2 + min(col, row)%2
        # while n < num_of_loops:
        #     for c in range(n, col-n):
        #         spiral.append(matrix[n][c])
        #     current_col = c
        #     for r in range(n+1 , row-n):
        #         spiral.append(matrix[r][c])
        #     current_row = r
        #     #left and up
        #     for c in reversed(range(n,current_col)):
        #         spiral.append(matrix[current_row][c])
        #     for r in reversed(range(n+1, current_row)):
        #         spiral.append(matrix[r][c])

        #     n+=1
        # return spiral

        top_max, bottom_max = 0, len(matrix) - 1
        left_max, right_max = 0, len(matrix[0]) - 1
        spiral = []
        
        while top_max <= bottom_max and left_max <= right_max:
            for c in range(left_max, right_max + 1):
                spiral.append(matrix[top_max][c])
            top_max += 1
            
            for r in range(top_max, bottom_max + 1):
                spiral.append(matrix[r][right_max])
            right_max -= 1
            
            if top_max <= bottom_max:
                for c in range(right_max, left_max - 1, -1):
                    spiral.append(matrix[bottom_max][c])
                bottom_max -= 1
            
            if left_max <= right_max:
                for r in range(bottom_max, top_max - 1, -1):
                    spiral.append(matrix[r][left_max])
                left_max += 1
        
            return spiral
        
if __name__ == "__main__":
    task = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(task.spiralOrder(matrix))

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print([1,2,3,4,8,12,11,10,9,5,6,7])
    print(task.spiralOrder(matrix))