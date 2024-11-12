class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        #sort the array
        arr.sort()
        #min_distance variable
        min_distance = arr[1] - arr[0]
        #create a result list
        result = [[arr[0],arr[1]]]
        #start iterating till len(arr) - 1
        for i in range(1,len(arr)-1):
            a, b = arr[i], arr[i+1]
            distance = b - a 
            
            if distance == min_distance:
                result.append([a,b])
            elif distance < min_distance:
                min_distance = distance
                result.clear()
                result.append([a,b])
            else:
                continue
        return result