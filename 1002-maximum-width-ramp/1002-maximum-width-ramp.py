class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for i,n in enumerate(nums):
            if not stack:
                stack.append([n,i])
            elif stack and stack[-1][0] > n:
                stack.append([n,i])
            else:
                stack_len = len(stack) - 1

                while stack_len >= 0 :
                    if stack[stack_len][0] > n:
                        break 
                    ans = max((i - stack[stack_len][1]), ans)
                    stack_len -= 1
        return ans
