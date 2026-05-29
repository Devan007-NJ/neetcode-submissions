class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=[ch for ch in s]
        s_list.sort()
        t_list=[ch for ch in t]
        t_list.sort()
        if s_list==t_list:
            return True
        else:
            return False
        