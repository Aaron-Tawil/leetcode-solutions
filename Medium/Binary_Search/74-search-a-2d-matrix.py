# Problem: 74 – search a 2d matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix/description/
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix) , len(matrix[0])
        col0 = [matrix[i][0] for i in range(m)]
        row = bisect_left(col0,target)
        
        if row< m and col0[row]== target:
            return True
        if row == 0 : return False
        row-=1
        col = bisect_left(matrix[row],target)
        if col <n and matrix[row][col]==target:
            return True
        return False

        
        