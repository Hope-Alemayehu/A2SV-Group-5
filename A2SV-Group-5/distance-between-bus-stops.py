class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total=sum(distance)
        if start<=destination:
            clockwise=sum(distance[start:destination])
        else:
            clockwise=total-sum(distance[destination:start])
        counterclock=total-clockwise
        return min(clockwise,counterclock)