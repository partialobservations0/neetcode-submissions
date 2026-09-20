class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        for i,num in enumerate(temperatures):
            for j,nextnum in enumerate(temperatures[i:]):
                if nextnum > num:
                    result[i] = j
                    break

        return result