from sys import stdin,stdout
from collections import Counter,defaultdict,deque
import sys, threading

def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))



def solve():
    
    # write your code here 
    n,m = II()
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    def inbound(row,col):
        return 0<=row<n and 0<=col<m 

    visited = set()
    def dfs(parent,node):
        x,y = node 
        color = arr[x][y]
        valid = False
        for i,j in direction:
            xi = x + i 
            yj = y + j 
            
            if inbound(xi,yj) and parent != (xi,yj) and arr[xi][yj] == color:
                if (xi,yj) in visited:
                    return True
                visited.add((xi,yj))
                if dfs(node,(xi,yj)):
                    return True
        
    x = False
    for i in range(n):
        for j in range(m):
            if (i,j) not in visited:
                x |= bool(dfs(None,(i,j)))
                  
    if x:
        print("Yes")
    else:
        print("No")
                
                
                
        
    
    
    
    
    
    
    
    
sys.setrecursionlimit(1<<30)
threading.stack_size(1<<27)
main_thread = threading.Thread(target=solve)
main_thread.start()
main_thread.join()

