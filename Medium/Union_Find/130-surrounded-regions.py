# Problem: 130 – surrounded regions
# Difficulty: Medium
# Link: https://leetcode.com/problems/surrounded-regions/description/


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # border check
        m,n = len(board) , len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def explore(r,c):
            st = [(r,c)]
            board[r][c]='#'
            while st:
                rc,cc = st.pop()
                for dr,dc in dirs:
                    rn,cn = rc+dr,cc+dc
                    if 0<=rn<m and 0<=cn<n and board[rn][cn]=='O':
                        board[rn][cn]='#'
                        st.append((rn,cn))      
            return
        #first row and last
        for col in range(n):
            if board[0][col]=='O':
                explore(0,col)
            if board[m-1][col]=='O':
                explore(m-1,col)
        #first and last col
        for row in range(m):
            if board[row][0]=='O':
                explore(row,0)
            if board[row][n-1]=='O':
                explore(row,n-1)
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]= 'X'
                if board[r][c]=='#':
                    board[r][c]= 'O'
        return 
                







        # option 2 - BFS to search regions

        # viseted = set()
        # m,n = len(board) , len(board[0])
        # dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # def explore(r,c):
        #     viseted.add((r,c))
        #     region = {(r,c)}
        #     st = [(r,c)]
        #     surr = True
        #     while st:
        #         rc,cc = st.pop()
        #         for dr,dc in dirs:
        #             rn,cn = rc+dr,cc+dc
        #             if rn<0 or rn>=m or cn<0 or cn>=n:
        #                 surr=False
        #             elif  board[rn][cn]=='O' and (rn,cn) not in region:
        #                 viseted.add((rn,cn))
        #                 region.add((rn,cn))
        #                 st.append((rn,cn))
        #     if surr:
        #         for r,c in region:
        #             board[r][c]='X'        
                    
        #     return
        
        # for r in range(m):
        #     for c in range(n):
        #         if board[r][c]=='O' and (r,c) not in viseted:
        #             explore(r,c)
        # return


        