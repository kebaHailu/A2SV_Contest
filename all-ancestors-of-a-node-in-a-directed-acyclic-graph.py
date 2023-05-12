class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list) 
        indeg = [0 for n in range(n)]
        for a ,b in edges:
            graph[a].append(b)
            indeg[b] += 1
        
        ans = [set() for _ in range(n)]
        
        queue = deque()

        for i in range(n):
            if indeg[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            
            for nb in graph[node]:
                indeg[nb] -= 1 
                ans[nb].add(node)
                for child in ans[node]:
                    ans[nb].add(child)
                
                
                if indeg[nb] == 0:
                    queue.append(nb)
  
        for i in range(len(ans)):
            ans[i] = sorted(ans[i])
        
        
        return ans