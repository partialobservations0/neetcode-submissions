class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(index, cur, total):
            if total == target:
                if cur not in res:
                    res.append(cur.copy())
                return 
            
            if index >= len(candidates) or total > target:
                return

            cur.append(candidates[index])
            backtrack(index+1, cur, total+candidates[index])
            cur.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index+1, cur, total )

        backtrack(0,[], 0)
        return res