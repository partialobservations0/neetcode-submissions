class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # lets start again 
        # AAAABBBB
        # ABABABABABB
        # AABBAABBAABB
        # AAAABBAAABB
        # which character to reply with

        # main idea is to find the most frequent character within a substring
        # and then replace the rest with that char
        res = 0
        for i in range(0,len(s)):
            count, maxf = {}, 0
            for j in range(i,len(s)):
                count[s[j]] = 1 + count.get(s[j],0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j-i+1)
        return res

        
 

        

