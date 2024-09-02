class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        heap = []
        heapq.heapify(heap)
        for key, val in counter.items():
            heapq.heappush(heap, [-val, key])
        
        res = []

        while k:
            x, y = heapq.heappop(heap)
            res.append(y)
            k -= 1
        return res
            
