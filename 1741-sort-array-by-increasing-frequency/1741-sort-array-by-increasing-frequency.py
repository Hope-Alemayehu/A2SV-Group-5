class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        ans = []
        check = set()
        for num in nums:
            if num not in check:
                ans.append([count[num],num])
                check.add(num)
        
        ans.sort(key=lambda x:(x[0], -x[1]))
        res = []
        
        for freq, val in ans:
            while freq > 0:
                res.append(val)
                freq -= 1
        return res

        