class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        bigweight = -1
        sumweight = 0

        for weight in weights:
            bigweight = max(bigweight,weight)
            sumweight += weight 

        
        left = bigweight 
        right = sumweight 

        while left < right :

            mid = left + (right-left)//2 
            myday = 1
            curw = 0
            for weight in weights:
                if curw + weight > mid:
                    myday += 1
                    curw = 0
                curw += weight
            if myday > days:
                left = mid + 1
            else :
                right = mid 
        return left