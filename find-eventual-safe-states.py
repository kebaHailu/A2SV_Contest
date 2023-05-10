class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nums = [0]*len(graph)
        
        def dfs(idx):
            if not graph[idx]:
                nums[idx] = 2
                return True
            elif nums[idx] == 1:
                return False 
            elif nums[idx] == 2:
                return True
            
            boolval = True 
           
            nums[idx] = 1
            for i in graph[idx]:
                boolval &= dfs(i)
            if boolval:
                nums[idx] = 2
            return boolval
        ans = []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans