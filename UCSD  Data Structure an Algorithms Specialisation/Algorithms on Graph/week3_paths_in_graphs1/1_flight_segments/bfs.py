#Uses python3

import sys
from collections import deque



def distance(adj, s, t):

    dist = [float('inf')] * len(adj)
    dist[s] = 0 

    pred = [None] * len(adj)

    q = deque([s])

    while q:
        v = q.popleft()
        for n in adj[v]:

            if dist[n] == float('inf'):  # Only process unvisited nodes
                q.append(n)
                dist[n] = dist[v] + 1
                pred[n] = v
            


    return dist[t] if dist[t] != float('inf') else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
