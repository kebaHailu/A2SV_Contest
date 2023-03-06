n = int(input())
nums = list(map(int,input().split()))

pre_sum = nums[:]
suf_sum = nums[::-1]

for i in range(1,n):
    pre_sum[i] += pre_sum[i-1]
    suf_sum[i] += suf_sum[i-1]
suf_sum = suf_sum[::-1]
edward = 0 
alphonse = 0  
    
left = 0 
right = n -1 

while left <= right :
    if pre_sum[left] <= suf_sum[right]:
        edward += 1 
        left += 1
    else :
        alphonse += 1 
        right -= 1

print(edward,alphonse)