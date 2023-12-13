class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #time complexity O(N)
        #space complexity O(N)
        output=[]
        evensum=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                evensum+=nums[i]

        for val,index in queries:
            if nums[index]%2==0:
                evensum-=nums[index]

            nums[index]=nums[index]+val

            if nums[index]%2==0:
                evensum+=nums[index]
            output.append(evensum)
        return output