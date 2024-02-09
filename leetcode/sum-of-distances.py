class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexMap = defaultdict(list)
        n = len(nums)
        res = [0] * n

        for i in range (n):
            indexMap[nums[i]].append(i)
      

        for key,vals in indexMap.items():
            if len(vals) > 1:
                prefix = []
                m = len(vals)
                suffix = [0] * m
                cur = 0

                for i in range(m):
                    cur += vals[i]
                    prefix.append(cur)
               
                cur = 0
                for i in range (m-1,-1,-1):
                    cur  += vals[i]
                    suffix[i] = cur
                
                for i in range(m):
                    res[vals[i]] = vals[i]*i - prefix[i] + suffix[i] - vals[i]*(m-1-i)
                    
        return res