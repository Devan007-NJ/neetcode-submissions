class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        L=list()
        for i in set(nums):
            hashmap.setdefault(i,0)
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
        value=list(hashmap.values())
        value.sort(reverse=True)
        value=value[0:k]
        for i in hashmap:
            if hashmap[i] in value:
                L.append(i)
        return L

        