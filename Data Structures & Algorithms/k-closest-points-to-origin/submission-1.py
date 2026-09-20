class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #mses = [((point[0]**2 + point[1]**2), point) for point in points]
        #heapq.heapify(mses)
        #print(mses)
        return heapq.nsmallest(k, points, key=lambda x: (x[1]**2 + x[0]**2))