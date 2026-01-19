#Uses python3

import sys
import heapq


def distance(adj, cost, s, t):
    #write your code here
    dist = [float('inf')] * len(adj)
    dist[s] =  0
    prev = [None] * len(adj)
    
    
    priority_queue : heapq = [(dist[s],s)]

    while priority_queue:

        # dist[v] , v 
        d , v = heapq.heappop(priority_queue)

        # If this distance is outdated, skip processing
        if d > dist[v]:
            continue
        
        for index, neibour  in enumerate(adj[v]):
            weight = cost[v][index]

            if weight + dist[v] < dist[neibour] :
                     dist[neibour] = weight + dist[v]
                     prev[neibour] = v 

                     heapq.heappush(priority_queue,(dist[neibour], neibour))

    return dist[t] if dist[t] != float('inf') else -1 


        
    



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
