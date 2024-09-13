class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        #time complexity O(N + M)
        #space complexity O(N) 
        length = len(rolls)
        total = sum(rolls)
        reminderTotal = mean*(length + n) -  total
     
        if reminderTotal <= 0:
            return []
     
        ans = []
        numm = reminderTotal // n
        rem = reminderTotal % n
        # print("num",numm)
        # print("rem",rem)
        if numm > 6 or numm == 0:
            return []
        for i in range(n):
            if rem:
                if numm+1 > 6:
                    return []
                ans.append(numm  + 1)
                rem -= 1
            else:
                ans.append(numm)
        return ans
        