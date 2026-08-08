class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        left=0
        maxstring=0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            maxstring=max(maxstring,right-left+1)
        return maxstring