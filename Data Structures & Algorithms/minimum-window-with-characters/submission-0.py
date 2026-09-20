from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = defaultdict(int)
        for c in t:
            tmap[c] += 1
        sols = []
        sols_len = []
        minsol = 100000
        currsol = ""
        for i in range(0,len(s)):
            tmap_copy = dict(tmap)
            for j in range(i, len(s)):
                if s[j] in tmap_copy:
                    tmap_copy[s[j]] = max(0, tmap_copy[s[j]] - 1)
                    if sum(tmap_copy.values()) == 0:
                        #sols.append(s[i:j])
                        #sols_len.append(j-i)
                        if (j - i) < minsol:
                            minsol = j-i
                            currsol = s[i:j+1]
        return currsol    