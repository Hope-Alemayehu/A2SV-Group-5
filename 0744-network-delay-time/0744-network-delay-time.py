class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #usig bellman ford algoritsm (pull DP)
        #with the space optimized
        graph = defaultdict(list)
        for u, v, w in times:
            #we are storing which node are pointing to V
            graph[v-1].append((u-1, w))
        
        prev = [float("inf") for _ in range(n)] 
        #our start node isn't found at index 0 instead k-1
        prev[k-1] = 0

        for i in range (n-1):
            curr = prev[:]
            for j in range(n):
                for nei, weight in graph[j]:
                    #relaxation happens here
                    if weight + curr[nei] < curr[j]:
                        curr[j] = weight + curr[nei]
                    
                prev = curr
        # print(prev)
        res = max(prev)
        return res if res != float('inf') else -1

