from sys import stdin,stdout
from collections import Counter,defaultdict 
from heapq import *

def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))



def solve():
    
    # write your code here 
    n = I()
    nums = IL() 
    
    nums = [(-i,idx+1) for idx,i in enumerate(nums)]
    heapify(nums)
    arr = []
    while len(nums) > 1:
        
        val1,idx1 = heappop(nums)
        val2,idx2 = heappop(nums)
        if val1 and val2:
            
            arr.append((idx1,idx2))
        
            val1 += 1
            val2 += 1
            if val1:
                heappush(nums,(val1,idx1))
            if val2:
                heappush(nums,(val2,idx2))
    k = len(arr)
    print(k)
    for val in arr:
        print(*val)
        
            

for _ in range(I()):
    solve()
