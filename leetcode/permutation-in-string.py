class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #time complexity O(N)
        #space complexity O(1)
        if len(s1) > len(s2):
            return False
      
        target = Counter(s1)
        current = defaultdict(int)
        left = 0
        
        for i in range(len(s1)):
            current[s2[i]] += 1
        if current == target:
            return True
        for i in range(len(s1),len(s2)):
            
            
            current[s2[left]] -= 1
            if current[s2[left]] == 0:
                del(current[s2[left]])
            current[s2[i]] += 1
            left += 1
            if current == target:
                return True
    
        return False
        
        