class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0] * len(temperatures)
        for i ,t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                standT,standind = stack.pop()
                result[standind] = (i-standind)
            stack.append([t,i])
  
        return result
            

        