class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        target=[[0]*n for _ in range(m)]
        for i in target:
            for j in range(len(i)):
                i[j]=1
        for i in target:
            i[0]=1
        for i in range(1,m):
            for j in range(1,n):
                target[i][j]=target[i-1][j]+target[i][j-1]

        return target[m-1][n-1]


        