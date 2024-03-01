class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        # def backtrack(left,right):
        #     if left > right:
        #         return 0,0
        #     best1 , nextbest1 = backtrack(left+1,right)
        #     best2 ,nextbest2 = backtrack(left,right-1)

        #     if nums[left] + nextbest1 >= nums[right] +nextbest2:
        #         return nums[left]+nextbest1, best1
            
        #     return nums[right] + nextbest2, best2

        # player1, player2 = backtrack(0,len(nums)-1)
        # return player1 >= player2

        n = len(nums)

        def score(left,right):
            if left > right:
                return 0
            leftScore = nums[left] - score(left+1,right)
            rightScore = nums[right] - score(left, right-1)

            return max(leftScore,rightScore)
        
        if score(0,n-1) >= 0:
            return True
        return False





