class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        if len(nums)==3:
            return max(nums)
        rob1,rob2=0,0
        for n in range(len(nums)-1):
            temp=max(rob1+nums[n],rob2)
            rob1=rob2
            rob2=temp
        t1,t2=0,0
        for n in range(1,len(nums)):
            temp=max(t1+nums[n],t2)
            t1=t2
            t2=temp
        return max(rob2,t2)
        
            

        