class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for a ,b in prerequisites:
            graph[a].append(b)
        

        def dfs(node,target,visited):
            visited.add(node)
            ans = False 
            for nb in graph[node]:
                if nb not in visited:
                    if nb == target:
                        return True 
                    else:
                        ans |= dfs(nb,target,visited)
            return ans 

        arr = []
        for x,y in queries:
            arr.append(dfs(x,y,set()))

        return arr