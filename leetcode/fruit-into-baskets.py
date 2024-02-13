class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        checker = defaultdict(int)
        n = len(fruits)
        res = float("-inf")
        left = 0
        for i in range(n):
            checker[fruits[i]] += 1

            while left < n and len(checker) > 2:
                checker[fruits[left]] -= 1
                if checker[fruits[left]] == 0:
                    del(checker[fruits[left]])
                left += 1
            
            res = max(res,i- left + 1)
        return res
              