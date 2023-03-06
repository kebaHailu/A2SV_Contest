class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        r = x

        while l <= r:

            m = l + (r-l)//2


            if (m ** 2) < x:
                l = m + 1 
            elif m ** 2 == x:
                return m

            else :
                r = m - 1

        return r