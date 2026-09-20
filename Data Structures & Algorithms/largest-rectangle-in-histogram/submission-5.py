class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # common rectangles are height of bar and length of array times minimum height
        # brute force solution:
            # for each i and j compute the size of rectangle

        # easier solution only go back to previous good point

        def get_max_area_between_two_index(i, j, heights):
            return max(heights[i:j+1] + [min(heights[i:j+1])*(j-i+1)])

        if len(heights) == 1:
            return heights[0]
    
        solution = []
        prev_sol = []
        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                max_area_at_ij = get_max_area_between_two_index(i,j,heights)
                solution.append(max_area_at_ij)

        return max(solution)