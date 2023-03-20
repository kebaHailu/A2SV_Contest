def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))



def solve():
        
    n , d = II()
    arr = SIL()
    nums = arr[:]
    
    count = 0
    x = 0
    
    for i in range(n-1,-1,-1):
        curmax = 0
        while x < n:
            curmax += arr[i]
            x += 1
            
            if curmax > d:
                count += 1
                break 
        
            
        
      
    
    return count
            
            
    
    
        
        
        






print(solve())
    
    
   
    
    
    
    
    




