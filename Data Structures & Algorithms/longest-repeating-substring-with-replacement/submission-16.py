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
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(0,len(s)):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r-l+1)
        return res
        
 

        

