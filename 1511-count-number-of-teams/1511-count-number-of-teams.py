class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(1, n - 1):
            left_smaller = left_larger = right_smaller = right_larger = 0
            
            # Count soldiers on the left
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1
            
            # Count soldiers on the right
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_larger += 1
            
            # Calculate valid teams
            count += left_smaller * right_larger + left_larger * right_smaller
        
        return count