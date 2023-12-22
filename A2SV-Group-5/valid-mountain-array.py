class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        flag=True

        for i in range(len(arr)-1):
            if i==0 and arr[i]>=arr[i+1]:
                return False
            elif arr[i]==arr[i+1]:
                return False
            elif arr[i]>arr[i+1] and flag:
                flag=False
            elif not flag and arr[i]<=arr[i+1]:
                return False
        return True if not flag else False
