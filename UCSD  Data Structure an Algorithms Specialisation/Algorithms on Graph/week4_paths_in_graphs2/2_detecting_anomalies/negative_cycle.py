#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    dist = [10**18] * len(adj)
    dist[0] = 0
    prev = [None] * len(adj)
    prev[0] = 0 
    

    for v in range(len(adj)):

        for edgeV in range(len(adj)):

            for index, neibours in enumerate(adj[edgeV]):
                weight = cost[edgeV][index]

                relax(dist,prev,edgeV,neibours,weight)

    for edgeV in range(len(adj)):

            for index, neibours in enumerate(adj[edgeV]):
                weight = cost[edgeV][index]

                if relax(dist,prev,edgeV,neibours,weight):
                     return 1
    
    return 0

def relax(dist : list ,prev,n, neibours ,weight ):

     if dist[neibours] > dist[n] + weight:
                dist[neibours] = dist[n] + weight
                prev[neibours] = n

                return 1


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
    print(negative_cycle(adj, cost))
