grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

count = 0
rows = len(grid)
cols = len(grid[0])
visit = set()

def bfs(r, c):
    searchQ = deque()
    visit.add((r,c))
    searchQ.append((r,c))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while searchQ:
        row, col = searchQ.popleft()

        for dr, dc in directions:
            r, c = row+dr, col+dc

            if ((r in range(rows)) and (c in range(cols)) and grid[r][c] == "1" and (r,c) not in visit):
                searchQ.append((r,c))
                visit.add((r,c))
    

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "1" and (r, c) not in visit:
            bfs(r, c)
            count += 1

print(count)




count = 0
row = len(grid)
col = len(grid[0])

def dfs(r, c):
    if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
        return 
    grid[r][c] = '0'

    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)        


for r in range(row):
    for c in range(col):
        if grid[r][c] == '1':
            dfs(r,c)
            count+=1
print(count)