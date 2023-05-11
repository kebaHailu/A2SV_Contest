class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        ans = [i for i in range(n)]
        indeg = [0]*n
        for a,b in richer:
            graph[a].append(b)
            indeg[b] += 1 
        
        
        
        queue = deque()
        for i in range(n):
            if indeg[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.pop()
            for nb in graph[node]:
                indeg[nb] -= 1
                


                if quiet[ans[nb]] > quiet[ans[node]]:
                    ans[nb] = ans[node]


                if indeg[nb] == 0:
                    queue.append(nb)

        return ans