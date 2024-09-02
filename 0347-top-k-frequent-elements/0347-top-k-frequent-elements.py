class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #time complexity O(N)
        #space complexity O()

        counter = {}
        N = len(nums) + 1
        #don't Do freq [[]] * N because it will create a shallow copy
        freq = [[] for i in range(N)] 

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
      
        for key, val in counter.items():
            freq[val].append(key)
    
        res = []

        for i in range(N - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
       


