for _ in range(int(input())):
    
    n , m = map(int,input().split())
    arr = input()
    arr = list(map(int,arr))
    arr = [0] + arr + [0]
    arr = list(map(int,arr))
    

    iterate = min(n,m)
    nums = arr[:]
    for _ in range(m):
        for i in range(1,n+1):
            if arr[i] == 0 and (arr[i+1] + arr[i-1] == 1):
                nums[i] = 1
                
        
        if arr == nums:
            break
         
        
        arr = nums[:]
    
    ans = ""
    for i in arr[1:-1]:
        ans += str(i)
    print(ans)
            
        
        
    
    
    
    
    
    
    