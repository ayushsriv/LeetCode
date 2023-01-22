class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        def dfs(res, i, j):
            if (i,j) in res: return
            res.add((i,j))
            neighbours = [[i,j+1], [i+1,j], [i-1,j], [i,j-1]]
            for k,l in neighbours:
                if k>=0 and k<len(heights) and l>=0 and l<len(heights[0]) and heights[i][j]<=heights[k][l]:
                    dfs(res,k,l)
                    
        for i in range(len(heights)):
            dfs(pac,i,0)
            dfs(atl,i,len(heights[0])-1)

        for j in range(len(heights[0])):
            dfs(pac,0,j)
            dfs(atl,len(heights)-1,j)
        
        return pac.intersection(atl)

