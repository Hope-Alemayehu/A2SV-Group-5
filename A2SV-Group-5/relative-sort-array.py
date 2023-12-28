class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arrange={}
        #to map the arr2 based on their indices
        for i , x in enumerate(arr2):
            arrange[x]=i
        
        arr1.sort(key = lambda x: arrange.get(x,10000+x))
        return arr1
        

