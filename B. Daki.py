mylist = []

for _ in range(int(input())):
    
    mylist =list((input().split()))
    
    hashlist = []    

    for i in mylist:
        for c in i:
            if c.isdigit():
                hashlist.append([i,c])
            
            
    hashlist.sort(key = lambda i:i[1])   
    out =[i[0].replace(i[1],"") for i in hashlist]


    print(" ".join(out))

    
    
    