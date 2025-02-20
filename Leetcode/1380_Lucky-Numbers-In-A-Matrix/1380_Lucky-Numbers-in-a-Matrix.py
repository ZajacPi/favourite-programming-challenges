class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        col_max = []
        row_min = []
        for col in range(len(matrix[0])):
            current_col = []
            for row in range(len(matrix)):
                current_col.append(matrix[row][col])
            col_max.append(max(current_col))
        for row in matrix:
            row_min.append(min(row))

        lucky = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                element = matrix[row][col]
                if element == col_max[col] and element == row_min[row]:
                    lucky.append(element)
        return lucky
    
if __name__ == "__main__":
    task = Solution()
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(task.luckyNumbers(matrix))
    matrix2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(task.luckyNumbers(matrix2))