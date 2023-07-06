from sys import stdin,stdout
from collections import Counter,defaultdict 

def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))


def solve():
    
    
    

    # write your code here 
    n= I()
    
    arr = []
    for _ in range(n):
        val = list(input())
        arr.append(val)
    
    narr = list(zip(*arr))
    temp = ""
    for el in narr:
        sel = set(el)
        if len(sel) == 1 and '?' in sel:
            temp += 'k'
        elif len(sel) == 1:
            for i in sel:
                temp += i 
                
        elif len(sel) == 2 and '?' in sel:
            for i in sel:
                if i != '?':
                    temp += i 
        else:
            temp += '?'
    
    print(temp)
 
    
    
    
    
    
    
    
    
    
    
solve()
