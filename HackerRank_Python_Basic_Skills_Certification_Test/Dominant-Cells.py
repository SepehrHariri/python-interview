def numCells(grid):
    n,m=len(grid), len(grid[0])
    count=0
    for i in range(n):
        for j in range(m):
            is_dominant = True
            for x in range(max(0,i-1), min(n,i+2)):
                for y in range(max(0,j-1), min(m,j+2)):
                    if grid[x][y]>=grid[i][j] and (x,y)!=(i,j):
                        is_dominant = False
            if is_dominant:
                count+=1
    return count
