#Uses python3

import sys


def acyclic(adj):
    
    visited = [False] * len(adj)

    rec_visited = visited


    # O(V)
    for u in range(len(adj)):
      if not visited[u]  and  explore(adj,visited,rec_visited,u):
          return 1
      
    return 0 



def explore(adj,visited, rec_visited ,n) :
    if not visited[n]:

        visited[n] = True
        rec_visited[n] = True 
        

        for v in adj[n]:


            # Recurse  for all the vertices adjacent to this vertex , O(E)
            if not visited[v] and explore(adj,visited,rec_visited,v):
                return True 
            

            elif rec_visited[v]:
                return True 

    
    rec_visited[n] = False

    return False 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
