class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        counts,countt={},{}
        for i in range(len(s)):
            counts[s[i]]=1 + counts.get(s[i],0)
        for i in range(len(t)):
            countt[t[i]]=1+ countt.get(t[i],0)
        for j in counts:
            if counts[j]!= countt.get(j,0):
                return False
        return True

        