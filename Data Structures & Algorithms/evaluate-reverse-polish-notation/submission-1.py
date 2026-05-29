class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        opr=["+","-","/","*"]
        for i in tokens:
            if i not in opr:
                stack.append(int(i))
            else:
                a=stack[-1]
                stack.pop()
                stack[-1]=int(eval(f"{stack[-1]} {i} {a}"))
        return stack[-1]



        