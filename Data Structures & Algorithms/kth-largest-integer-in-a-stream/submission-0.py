class KthLargest:

    # find k largest integer
    # initialize get the kth largest integer

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = sorted(nums, reverse=True)[0:k]
        self.k = k

    def add(self, val: int) -> int:
        self.minHeap.append(val)
        self.minHeap = sorted(self.minHeap, reverse=True)[0:self.k]
        return self.minHeap[-1]