class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n+ 1)

        for _first, _last , seats in bookings:
            prefix[_first - 1] += seats
            prefix[_last  ] -= seats
        print(prefix)

        for i in range(1,n):
            prefix[i] += prefix[i-1]
        return prefix[:n]
        


        