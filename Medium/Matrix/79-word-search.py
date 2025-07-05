# Problem: 79 – word search
# Difficulty: Medium
# Link: https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:  
        m , n = len(board) , len(board[0])
        used = [[False]*n for row in range(m)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def backtrack(row,col,k): # k is index in word
            if board[row][col]!=word[k]:
                return False
            k+=1
            if len(word)==k:
                return True
            for drow,dcol in dirs:
                rowt , colt = row+drow, col+dcol
                if 0<= rowt < m and 0 <=colt <n and not used[rowt][colt]:
                    used[rowt][colt] = True
                    if backtrack(rowt,colt,k):
                        return True
                    used[rowt][colt] = False
            return False

        for row in range(m):
            for col in range(n):
                used[row][col] = True
                if backtrack(row,col,0):
                    return True
                used[row][col] = False
        return False
        