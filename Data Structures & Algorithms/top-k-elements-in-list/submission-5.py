class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            hashmap[i]=1+hashmap.get(i,0)
        buckets=[[]for i in range(len(nums)+1)]
        for key,value in hashmap.items():
            buckets[value].append(key)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res)==k:
                    return res


