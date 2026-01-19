# python3
from collections import deque
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)

        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)

        print("edge id :" + str(len(self.edges)))

        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

        print("edge id :" + str(len(self.edges)))

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id + 1 ].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def find_augmented_path(graph,s,t):
    parent = [-1] * graph.size()
    visited = [0] * graph.size()

    queue = deque([s])
    visited[s] = 1

    while queue:
        u = queue.popleft()

        for edge_id in graph.get_ids(u):
            edge =graph.get_edge(edge_id)

            if not visited[edge.v] and edge.capacity > edge.flow:

                visited[edge.v] =True
                parent[edge.v] = edge_id
                queue.append(edge.v)

                if edge.v == t:
                    path = []

                    v = t
                    while v != s:
                        edge_id = parent[v]
                        edge = graph.get_edge(edge_id)
                        path.append(edge_id)

                        v = edge.u
                    path.reverse()
                    return path 
    
    return None

def fork_fulkerson(graph, from_, to):
    max_flow = 0
    
    while True:
        path = find_augmented_path(graph,from_,to)

        if not path:
            break

        # Find bottleneck capacity
        min_residual = float("inf")

        for edge_id in path:
            edge = graph.get_edge(edge_id)
            residual = edge.capacity - edge.flow

            if residual < min_residual:
                min_residual = residual
        
        # Update flow along path
        for edge_id in path:
            graph.add_flow(edge_id,min_residual)

        max_flow += min_residual

    return max_flow


if __name__ == '__main__':
    graph = read_data()
    print(fork_fulkerson(graph, 0, graph.size() - 1))
