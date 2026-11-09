from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # two possible solutions dp and recursion
        # first step go over s[i:j] and check if it is in wordDict
        # once found store in a array 
        # at index j it is possible to break if 0:i and i:j are in wordDict

        # for each possible i,j store if s[i:j] is in dict
        memo = [False] * (len(s) + 1)
        memo[0] = True

        # lets try dp
        for i in range(len(s)):
            for word in wordDict:
                w = len(word)
                j = i + w
                if memo[i] and j <= len(s) and s[i:j] == word:
                    memo[j] = True
                if memo[len(s)] == True:
                    return True
            
        return False






        grid_dict = {i:[] for i in range(len(s))}
        n = len(s)
        for i in range(n):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    grid_dict[i].append(j)
        
        @cache
        def dfs(i):
            if i == len(s):
                return True
            for j in grid_dict[i]:
                if dfs(j): return True
            return False

        return dfs(0)
            


