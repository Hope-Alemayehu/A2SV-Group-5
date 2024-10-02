class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        sortedA = sorted(list(set(arr)))
        ans = []
        for i in range(len(sortedA)):
            if sortedA[i] in rank:
                rank[sortedA[i]] = min(rank[sortedA[i]], i)
            else:
                rank[sortedA[i]] = i
        
        for n in arr:
            ans.append(rank[n]+1)
        return ans