class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        rec = set(recipes)
        sup = set(supplies)

        graph = defaultdict(list)
        indegree = Counter()
  

        for idx,elem in enumerate(ingredients):
            indegree[recipes[idx]] += len(elem)+1
            for a in elem:
                if a not in rec:

                    indegree[a] += 1

                graph[a].append(recipes[idx])
        print(indegree)
        print(graph)
        
        ans = []
        queue = deque()
        for key,val in indegree.items():
            if  key in sup:
                queue.append(key)
                if key in rec:
                    ans.append(key)
            
       
        while queue:
            node = queue.pop()
            for elm in graph[node]:
                indegree[elm] -= 1 

                if indegree[elm] == 1:
                    queue.append(elm)
                    ans.append(elm)
 
        return ans