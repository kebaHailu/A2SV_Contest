from sys import stdin,stdout
from collections import Counter,defaultdict 

def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))



def solve():
    
    # write your code here 
    val = input()
    return val[:2] + "... "+val+"?"
    
    
    
    
    
    
    
    
    


for _ in range(I()):
    print(solve())
