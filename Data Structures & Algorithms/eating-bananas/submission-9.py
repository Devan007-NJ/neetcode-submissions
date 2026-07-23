class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res=max(piles)
        import math
        l,r=1,max(piles)
        while l<=r:
            k=(l+r)//2
            totaltime=0
            for i in piles:
                totaltime+=math.ceil(float(i)/k)
            if totaltime <= h:
                r=k-1
                res=k
                
            else:
                l=k+1
        return res
