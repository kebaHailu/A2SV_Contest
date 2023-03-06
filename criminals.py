for _ in range(int(input())):
    
    n = int(input())
    nums = list(map(int,input().split()))
    
    left_index = 0 
    
    while left_index < n-1 and nums[left_index] == 0:
        left_index += 1 
        
    
    zero_count = nums[left_index:-1].count(0)
    non_zero_sum = sum(nums[:-1])
    print(zero_count + non_zero_sum)
    
    
    