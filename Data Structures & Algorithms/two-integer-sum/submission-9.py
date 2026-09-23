class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for key,value in enumerate (nums):
            hashmap[value]=key
        for key,value in enumerate (nums):
            diff=target-value
            if diff in hashmap and hashmap[diff]!= key:
                return [key,hashmap[diff]]
