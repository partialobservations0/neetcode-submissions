class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        grid = [[0 for _ in range(n2 + 1) ] for _ in range(n1 + 1)]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if text1[i] == text2[j]: 
                    grid[i][j] = 1 + grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]