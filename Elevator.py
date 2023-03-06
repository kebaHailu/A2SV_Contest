for _ in range(int(input())):
    
    wt,et,ce = map(int,input().split())
    minval = float("inf")
    
    for i in range(1,5):
        cal = wt * i + et * (4-i) + abs(i-ce)*et 
        minval = min(minval,cal)
    
    path1 = wt * 4 
    path2 = ce*et + et*4
    minval = min(minval,path2,path1)

    print(minval)
        

    
    