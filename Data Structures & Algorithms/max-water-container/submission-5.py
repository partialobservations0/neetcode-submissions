class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area is ( j - i ) * ( min(h[i], h[j]))
        # we can choose to increase i or decrease j if min(h[j],h[i]) increases
        # if doing both helps do both
        if not heights:
            return 0

        i = 0
        j = len(heights) - 1
        curr_max = (j - i) * min(heights[i], heights[j])
        while (i < j):
            if heights[i] >= heights[j]:
                j = j - 1
                curr_max = max(curr_max, (j - i ) * min(heights[i], heights[j]))
            elif heights[j] > heights[i]:
                i = i + 1
                curr_max = max(curr_max, (j - i ) * min(heights[i], heights[j]))



        return curr_max