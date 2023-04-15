# 3981 -eolymp -From adjacency matrix to adjacency list
# A simple directed graph is given with an adjacency matrix. 
# Print its representation in the form of adjacency list.

arr = []
for _ in range(int(input())):
    arr.append(list(map(int,input().split())))


ans = []
for a in arr:
    temp = [0]
    for idx,val in enumerate(a):
        if val == 1:
            temp[0]+= 1 
            temp.append(idx+1)
    ans.append(temp)
    
for a in ans:
    print(*a)

        
    