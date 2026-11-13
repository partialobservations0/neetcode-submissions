from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        #actions = {'add': 1, "subtract":-1}
        #state = current_sum
        #next_sum = operate(current_sum, action)

        #2 -> 2 and -2 -> 4, 0, 0, -4
        ##2 -> 2 and -2
        #2 -> 2 and -2 -> 6, 2, 2, 2, -2, -2, -6
        # for each number i can keep a data strucutre that says the count ended up on and also the number of ways

        # dp ?
        # dp[n-1] should give number of ways to solve target, nums[n]
        # dp[n] = (dp[target - nums[n]] + 1) + dp[target + nums[n]] + 1

        sums = defaultdict(int)
        sums[nums[0]] += 1
        sums[-1*nums[0]] += 1
        for i,n in enumerate(nums[1:]):
            this_round = defaultdict(int)
            for tsum,ways in sums.items():
                this_round[tsum + n] += ways
                this_round[tsum - n] += ways
            sums = this_round
        
        return sums.get(target, 0)
