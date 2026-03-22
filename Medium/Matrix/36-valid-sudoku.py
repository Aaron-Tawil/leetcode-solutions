from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #rows
        for i in range(9):
            s = set()
            for j in range(9):
                d = board[i][j]
                if d =='.':
                    continue 
                if d in s:
                    return False
                s.add(d)
        #cols
        for i in range(9):
            s = set()
            for j in range(9):
                d = board[j][i]
                if d =='.':
                    continue 
                if d in s:
                    return False
                s.add(d)

        #box
        for i in range(9):
            s = set()
            for j in range(3):
                for k in range(3):
                    d = board[j+3*(i//3)][k+3*(i%3)]
                    if d =='.':
                        continue 
                    if d in s:
                        return False
                    s.add(d)
            


        return True
        
