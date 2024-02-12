class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        #time complexity O(N)
        #space complexity O(N)
        
        n = len(nums)
        checked = set()

        for i in range(n):
            if i not in checked:
                cycle_set = set()
                while True:
                    if i in cycle_set:
                        return True 
                    checked.add(i)
                    cycle_set.add(i)

                    prev,i = i ,(i+nums[i])%n

                    #checking unicycle
                    if prev == i:
                        break
                    
                    #checking sign differnces
                    if nums[prev] > 0 != nums[i] < 0:
                        break
        return False