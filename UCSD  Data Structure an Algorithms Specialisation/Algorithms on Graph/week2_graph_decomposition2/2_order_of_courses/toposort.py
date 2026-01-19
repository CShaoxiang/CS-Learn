#Uses python3

import sys


def dfs(adj, used, order : list , x : int):
    '''
    perfrom dfs on vertex x and travel along the path , 
    '''
    used[x] = 1
    for v in adj[x]:
        if not used[v]:
            dfs(adj,used,order,v)
        
    order.append(x)

def toposort(adj):
    # run dfs on gragh , sort vertices by reverse post-order
    used = [0] * len(adj)
    order = []

    for i in range(len(adj)):
        if not used[i]:
            dfs(adj,used,order,i)

    #write your code here

    return reversed(order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

