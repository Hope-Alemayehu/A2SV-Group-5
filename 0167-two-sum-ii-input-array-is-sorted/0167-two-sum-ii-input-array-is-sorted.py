class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #time complexity O(N)
        #space complexity O(1)

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif  numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return []