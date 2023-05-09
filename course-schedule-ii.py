class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inrequest = defaultdict(int)
        arr = []
        for a,b in prerequisites:
            graph[b].append(a)
            inrequest[a] += 1 
        
        queue = deque()
        for k in range(numCourses):
            if inrequest[k] == 0:
                queue.append(k)
                
        
        while queue:
            node = queue.pop()
            arr.append(node)

            for elem in graph[node]:
                inrequest[elem] -= 1

                if inrequest[elem] == 0:
                    queue.append(elem)
                    

               

        if len(arr) == numCourses:
            return arr
        return []