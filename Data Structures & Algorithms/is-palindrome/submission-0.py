class Solution:
    def isPalindrome(self, s: str) -> bool:
        rec=''
        for c in s:
            if c.isalnum():
                rec+=c.lower()
        return rec == rec[::-1]

        