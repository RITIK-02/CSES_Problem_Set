import sys
from collections import defaultdict, deque

# sys.setrecursionlimit(2000000)

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

map = []
for i in range(n):
    map.append(input().split())

# print(map)


# DFS approach
# nodes = []
# for i in range(n):
#     for j in range(m):
#         if (map[i][0][j] == '.'):
#             nodes.append(i*m + j)

# # print(nodes)
# adj = defaultdict(list)
# for node in nodes:
#     i,j = node//m, node % m
#     if 0 < i and map[i-1][0][j] == '.':
#         node2 = (i-1)*m + j
#         if node2 not in adj[node]:
#             adj[node].append(node2)
#             adj[node2].append(node)
#     if i < n-1 and map[i+1][0][j] == '.':
#         node2 = (i+1)*m + j
#         if node2 not in adj[node]:
#             adj[node].append(node2)
#             adj[node2].append(node)
#     if 0 < j and map[i][0][j-1] == '.':
#         node2 = (i)*m + j - 1
#         if node2 not in adj[node]:
#             adj[node].append(node2)
#             adj[node2].append(node)
#     if j < m-1 and map[i][0][j+1] == '.':
#         node2 = (i)*m + j + 1
#         if node2 not in adj[node]:
#             adj[node].append(node2)
#             adj[node2].append(node)
# # print(adj)

# def dfs(node, visited, adj):
#     visited.add(node)
#     for neighbor in adj[node]:
#         if neighbor not in visited:
#             dfs(neighbor, visited, adj)


# ans = 0
# visited = set()
# for node in nodes:
#     if node not in visited:
#         ans += 1
#         dfs(node, visited, adj)

# print(ans)


# BFS
visited = [[False]*m for _ in range(n)]
ans = 0
q = deque()
for i in range(n):
    for j in range(m):
        if map[i][0][j] == '.' and not visited[i][j]:
            ans += 1
            q.append((i, j))
            visited[i][j] = True
            while q:
                r, c = q.popleft()
                if (r > 0 and map[r - 1][0][c] == '.' and not visited[r - 1][c]):
                    q.append((r - 1, c))
                    visited[r - 1][c] = True
                if (r < n - 1 and map[r + 1][0][c] == '.' and not visited[r + 1][c]):
                    q.append((r + 1, c))
                    visited[r + 1][c] = True
                if (c > 0 and map[r][0][c - 1] == '.' and not visited[r][c - 1]):
                    q.append((r, c - 1))
                    visited[r][c - 1] = True
                if (c < m - 1 and map[r][0][c + 1] == '.' and not visited[r][c + 1]):
                    q.append((r, c + 1))
                    visited[r][c + 1] = True
print(ans)