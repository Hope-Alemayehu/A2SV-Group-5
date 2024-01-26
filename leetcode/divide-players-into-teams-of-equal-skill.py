class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left = 0
        right = len(skill) - 1
        compare = skill[left] + skill[right]
        res = 0
        while left < right:
           
            if skill[left] + skill[right] != compare:
                return -1
            
            cur = skill[left] * skill[right]
            res += cur
            left += 1
            right -= 1
            
        return res
            

        