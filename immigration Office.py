n = int(input())
arr = list(map(str,input().split()))


for _ in range(int(input())):
    
    s = input()
    
    left = 0
    right = len(arr)-1
    
    while left <= right :
        mid = left + ( right - left)//2 
        
        if arr[mid] > s:
            right = mid - 1 
        else :
            left = mid + 1
            
    print(left)
        
    
    