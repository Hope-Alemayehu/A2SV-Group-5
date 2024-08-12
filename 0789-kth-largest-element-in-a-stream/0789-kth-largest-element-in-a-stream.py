class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lis, self.k = nums, k
        heapq.heapify(self.lis)

        

        

    def add(self, val: int) -> int:
        heapq.heappush(self.lis, val)

        while len(self.lis) > self.k:
            heapq.heappop(self.lis)

        return self.lis[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)