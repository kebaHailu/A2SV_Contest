from sys import stdin,stdout
from collections import Counter,defaultdict,deque 

import threading

def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))



def solve():
    
    # write your code here 
    n,m = II()
    nums = IL()
    visited = set()
    graph = defaultdict(list)
    for _ in range(m): 
        a,b = II()
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node):
        stack = [node]
        min_val = nums[node-1]
        
        while stack:
            cur = stack.pop()
            min_val = min(min_val,nums[cur-1])
            visited.add(cur)
            
            for child in graph[cur]:
                if child not in visited:
                    stack.append(child)
        
        return min_val
    gold = 0
    for i in range(1,n+1):
        if i not in visited:
            gold += dfs(i)
    print(gold)
          
solve()    
    
    
    
    



