class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        if len(edges) == 0 and n == 1:
            return True

        for start, finish in edges:
            graph[start].append(finish)
            graph[finish].append(start)
        
        stack = [source]
        visited = set()
        visited.add(source)

        while stack:
            node = stack.pop()

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if neighbour == destination:
                        return True
                    visited.add(neighbour)
                    stack.append(neighbour)

        return False
