class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i in range(0,len(nums)-k+1):
            sliding_window_max = max(nums[i:i+k])
            answer.append(sliding_window_max)
        return answer