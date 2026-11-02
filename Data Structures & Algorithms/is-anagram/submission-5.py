class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=[a for a in s]
        t_list=[a for a in t]
        s_list.sort()
        t_list.sort()
        if s_list==t_list:
            return True
        return False
            
        