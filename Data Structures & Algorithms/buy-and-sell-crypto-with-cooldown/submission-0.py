class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        states = {'bought': 0,
                  'canbuy': 1,
                  'cooldown': 2
                    }
        
        actions = { 'buy': 0,
                    'hold': 1,
                    'sell': 2
        }

        valid_actions = {'bought': ['sell', 'hold'],
                        'canbuy': ['buy'],
                        'cooldown': []}
        

        state_space = states.keys()
        action_space = actions.keys()
        time_steps = len(prices)
        values = [[0 for _ in range(time_steps+1)] for _ in range(len(state_space))]

        for t in range(time_steps - 1, -1, -1):
            values[states['canbuy']][t] = max(values[states['bought']][t+1] - prices[t], values[states['canbuy']][t+1])
            values[states['bought']][t] = max(values[states['bought']][t+1], values[states['cooldown']][t+1] + prices[t])
            values[states['cooldown']][t] = values[states['canbuy']][t+1]
        return values[states['canbuy']][0]
