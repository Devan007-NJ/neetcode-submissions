class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost=[0]*(len(cost)+1)
        mincost[1]=cost[0]
        mincost[2]=cost[1]
        for i in range(3,len(cost)+1):
            mincost[i]=min(mincost[i-1],mincost[i-2])+cost[i-1]
        return min(mincost[-1],mincost[-2])     