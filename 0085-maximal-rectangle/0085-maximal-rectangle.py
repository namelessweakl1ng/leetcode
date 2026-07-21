class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=="1":
                    heights[c]+=1
                else:
                    heights[c]=0
            ans = max(ans, self.largesetrectangle(heights))
        return ans
    def largesetrectangle(self, heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    width = i - stack[-1]-1
                else:
                    width = i
                max_area= max(max_area, h*width)
            stack.append(i)
        heights.pop()
        return max_area
