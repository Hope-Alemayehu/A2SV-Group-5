class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #time complexity O(N) + O(x)
        #space complexity O(1000)

        
        prefix = [0] * 1001

        for passenger , _start, _end in trips:
            if passenger > capacity:
                return False
            prefix[_start] += passenger
            prefix[_end] -= passenger
        max_passenger = 0
        for i in range (1,1001):
            prefix[i] += prefix[i-1]
            max_passenger = max(max_passenger,prefix[i])
        if max_passenger > capacity:
            return False
        return True
