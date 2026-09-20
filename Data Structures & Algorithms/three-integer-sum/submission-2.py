class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findTarget(snums, target):
            sol = []
            p1 = 0
            p2 = len(snums)-1
            while(p1 < p2):
                total = snums[p1] + snums[p2]
                if total > target:
                    p2 = p2 - 1
                elif total < target:
                    p1 = p1 + 1
                else:
                    sol.append([snums[p1], snums[p2]])
                    p1 = p1 + 1
            return sol
        nums = sorted(nums)
        solutions = []
        alreadyAdded = {}
        for i,n in enumerate(nums):
            partialsol = findTarget(nums[i+1:], -1*n)
            if partialsol:
                for sol in partialsol:
                    soln = [n] + sol
                    key = tuple(soln)
                    if key not in alreadyAdded:
                        solutions.append(soln)
                        alreadyAdded[key] = 1
        return solutions
