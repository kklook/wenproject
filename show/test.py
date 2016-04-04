# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class Solution(object):
    def numIslands(self, grid):
        if grid==[]:
            return 0
        temp=[]
        for i in grid:
            temp.append(list(i))
        grid=temp
        dp=[[0]*len(grid[0]) for i in range(len(grid))]
        print dp
        for i in range(len(grid)):
            dp[i][0]=int(grid[i][0])
        for j in range(len(grid[0])):
            dp[0][j]=int(grid[0][j])
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if int(grid[i][j])==1 and i<len(grid)-1 and j<len(grid[0])-1:
                    t=int(grid[i][j-1])+int(grid[i][j+1])+int(grid[i-1][j])+int(grid[i+1][j])==0
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])+1
                    continue
                elif int(grid[i][j])==1:
                    t=int(grid[i][j-1])+int(grid[i-1][j])
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])+1
                    continue
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(grid)-1][len(grid[0])-1]
        """
        :type grid: List[List[str]]
        :rtype: int
        """