from sys import stdin

N, M = map(int, stdin.readline().split())

maze = [list(map(int, stdin.readline().strip())) for i in range(N)]


# m = []
# k = [[999999] * M for i in range(N)]


# def dfs(i, j, c):
#     maze[i][j] = 0
#     c += 1
#     if k[i][j] > c:
#         k[i][j] = c

#     if k[i][j] < c:
#         return

#     if i < N-1 and 1 == maze[i+1][j]:
#         dfs(i+1, j, c)
#         maze[i+1][j] = 1
#     if j < M-1 and 1 == maze[i][j+1]:
#         dfs(i, j+1, c)
#         maze[i][j+1] = 1
#     if i > 0 and 1 == maze[i-1][j]:
#         dfs(i-1, j, c)
#         maze[i-1][j] = 1
#     if j > 0 and 1 == maze[i][j-1]:
#         dfs(i, j-1, c)
#         maze[i][j-1] = 1

#     if i == N-1 and j == M-1:
#         m.append(c)


# dfs(0, 0, 0)
# print(min(m))


queue = [[0, 0]]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    y, x = queue.pop(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
            continue

        if maze[ny][nx] != 1:
            continue

        maze[ny][nx] = maze[y][x] + 1
        queue.append([ny, nx])

print(maze[N - 1][M - 1])
