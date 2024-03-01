class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        curmin = nums[0]

        for n in nums[1:]:

            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n,curmin])
            curmin = min(n,curmin)
        return False