class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sq = int(sqrt(area))

        for i in range(sq,1,-1):
            if area % i == 0:
                return [area//i, i]
        return[area,1]
