class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force is to look at each character and then check 
        # if this is the index at which the solution is available
        # to do it in one pass 
        # a possible way is to start again from index of char that
        # broke pattern of not-repeat

        seen = {}
        currsol = 0
        maxsol = 0
        i = 0
        while (i <= len(s)-1):
            c = s[i]
            if c in seen:
                i = seen[c] + 1
                maxsol = max(maxsol, currsol)
                currsol = 0
                seen = {}
            else:
                seen[c] = i
                currsol += 1
                i += 1
        return max(maxsol,currsol)


