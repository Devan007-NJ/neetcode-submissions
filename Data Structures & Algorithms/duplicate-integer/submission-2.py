class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res=set(nums)
        #we convert to hashset to detect if any duplicates are present
        if len(res)==len(nums):
            return False
        return True