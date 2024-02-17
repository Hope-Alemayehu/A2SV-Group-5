class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        check = defaultdict(int)
        n = len(nums)
        #number of unique numbers in the array
        m = len(set(nums))

        res = 0
        left = 0
        count = 0 # to count the unique elements
        for i in range(n):
            
            check[nums[i]] += 1

            while len(check) == m:
                check[nums[left]] -= 1
                if  check[nums[left]] == 0:
                    del(check[nums[left]])
                left += 1
                count += n - i
            

        return count