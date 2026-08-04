class NumMatrix(object):

    def __init__(self, matrix):
        ROWS , COLS = len(matrix) , len(matrix[0])

        self.mat_sum = [[0]*(COLS+1) for r in range(ROWS+1)] # make a matrix with extra row and col
        for r in range(ROWS):
            prefix= 0
            for c in range(COLS):
                prefix += matrix[r][c] # increase the prefix 
                above = self.mat_sum[r][c+1] # the above must also be added when its the case of row2
                self.mat_sum[r+1][c+1] = prefix + above # above is added
        

    def sumRegion(self, row1, col1, row2, col2):
        row1, row2,col1,col2 = row1+1,row2+1,col1+1,col2+1
        # all rows and cols are incremented so that it matches with the mat_sum
        bottom_right = self.mat_sum[row2][col2]
        left = self.mat_sum[row2][col1-1]
        above = self.mat_sum[row1-1][col2]
        top_left = self.mat_sum[row1-1][col1-1]
        return bottom_right - left - above + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)