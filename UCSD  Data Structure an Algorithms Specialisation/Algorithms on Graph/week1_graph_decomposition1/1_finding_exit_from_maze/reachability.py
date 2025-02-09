#Uses python3
import sys
from collections import deque

def reach(adj, x, y):
    #BFS

    visited = [False] * len(adj)
    visited[x] = True
    
    queue = deque([x])

    while queue:
        v = queue.pop()

        if v == y:
            return 1
        
        for n in adj[v]:
            if not visited[n]:
                visited[n] = True 
                queue.append(n)

    return 0 


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
