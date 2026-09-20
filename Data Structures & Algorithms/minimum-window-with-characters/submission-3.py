from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hist = defaultdict(int)
        startpoints = [i for i,c in enumerate(s) if c in t]
        sol = 1000000
        curr_sol = ""
        for i,c in enumerate(t):
            hist[c] += 1

        for i,ind in enumerate(startpoints):
            hist_copy = dict(hist)
            for j,indj in enumerate(startpoints[i:]):
                hist_copy[s[indj]] = max(hist_copy[s[indj]] - 1, 0)
                if sum(hist_copy.values()) == 0:
                    if (indj + 1 - ind) < sol:
                        curr_sol = s[ind:indj+1]
                        sol = indj - ind + 1
        return curr_sol
        