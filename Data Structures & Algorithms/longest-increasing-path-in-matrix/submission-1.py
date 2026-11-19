class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # we are going to check for every i,j entry
        # starting from i,j if this is the biggest increasig path
        # i,j -> i+1,j; i-1,j; i,j+1; i,j-1
        # we can hopefully memoize the visited states to know we are ok

        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(i,j, prev_val):

            if (i < 0 or i >= rows or j < 0 or j >= cols
                or matrix[i][j] <= prev_val):
                return 0
            else:
                if memo[i][j] > -1:
                    return memo[i][j]
                answer = 1 + max( dfs(i+1, j, matrix[i][j]), 
                                dfs(i-1, j, matrix[i][j]),
                                dfs(i, j-1, matrix[i][j]),
                                dfs(i, j+1, matrix[i][j])
                                )
                memo[i][j] = answer
                return answer                
        solutions = []
        for i in range(rows):
            for j in range(cols):
                solutions.append(dfs(i,j,-1))
        return max(solutions)
