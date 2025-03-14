class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # transpose: flip along diag, rows becomes cols, cols become rows
        # reverse each row (CW) - rev each col (CCW)
        # i = rows, j = cols
        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Print the rotated matrix
        self.print_matrix(matrix)

        # rev each rows
        for i in range(n):
            matrix[i].reverse()

        # Print the rotated matrix
        self.print_matrix(matrix)



    def print_matrix(self, matrix):
        for row in matrix:
            print(row)

# Example 1:
matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
solution.rotate(matrix_1)
print("Output for Example 1:", matrix_1)

# Example 2:
matrix_2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solution = Solution()
solution.rotate(matrix_2)
print("Output for Example 2:", matrix_2)
