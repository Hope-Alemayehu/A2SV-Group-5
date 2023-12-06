class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        mini=[]
        maxi=[]
        pivotlist=[]

        for num in nums:
            if num < pivot:
                mini.append(num)
            elif num > pivot:
                maxi.append(num)
            else:
                pivotlist.append(num)
        return mini+pivotlist+maxi

