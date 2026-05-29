class Solution:
    def isValid(self, s: str) -> bool:
        pair={")":"(","]":"[","}":"{"}
        stack=[]
        top=-1
        for i in s:
            if i in pair:
                if stack and stack[top] == pair[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
                


            

        