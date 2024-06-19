class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])
        row1 = 0 in matrix[0]
        col1 = 0 in [i[0] for i in matrix]

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:                        
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        
        for j in range(1,cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        if row1:
            matrix[0] = [0]*cols

        if col1:
            for i in range(rows):
                matrix[i][0] = 0

        


