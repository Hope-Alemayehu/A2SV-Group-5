class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def jumble(num):
            return int("".join(str(mapping[int(s)]) for s in str(num)))

        return sorted(nums, key = jumble)