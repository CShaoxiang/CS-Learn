#python3
from collections import deque


class Edge:
    def __init__(self,u,v,capacity):
        self.u = u
        self.v = v
        self.capacity = capacity 
        self.flow = 0


class FlowGraph:
    def __init__(self,n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    
    def add_edge(self,from_,to,capacity):
        forward_edge = Edge(from_,to,capacity)
        backward_edge = Edge(to,from_ , 0)

        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)

        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)
    
    def get_ids(self,from_):
        return self.graph[from_]
    
    def get_edge(self,id):
        return self.edges[id]
    
    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for _ in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0]) if n > 0 else 0

        # Construct the flow network:
        # Nodes: 0 (source), 1..n (flights), n+1..n+m (crews), n+m+1 (sink)
        total_nodes = 1 + n + m + 1
        graph = FlowGraph(total_nodes)
        source = 0
        sink = total_nodes - 1

        # Connect source to flights
        for i in range(n):
            graph.add_edge(source, i + 1, 1)

        # Connect flights to crews based on adj_matrix
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] == 1:
                    graph.add_edge(i + 1, n + 1 + j, 1)

        # Connect crews to sink
        for j in range(m):
            graph.add_edge(n + 1 + j, sink, 1)

        # Compute max flow using Ford-Fulkerson
        max_flow = 0
        while True:
            # BFS to find augmenting path
            parent = [-1] * graph.size()
            visited = [False] * graph.size()
            queue = deque([source])
            visited[source] = True

            while queue:
                u = queue.popleft()
                for edge_id in graph.get_ids(u):
                    edge = graph.get_edge(edge_id)
                    if not visited[edge.v] and edge.capacity > edge.flow:
                        visited[edge.v] = True
                        parent[edge.v] = edge_id
                        queue.append(edge.v)
                        if edge.v == sink:
                            break

            if not visited[sink]:
                break

            # Find bottleneck capacity
            min_residual = float('inf')
            v = sink
            while v != source:
                edge_id = parent[v]
                edge = graph.get_edge(edge_id)
                residual = edge.capacity - edge.flow
                if residual < min_residual:
                    min_residual = residual
                v = edge.u

            # Update flows
            v = sink
            while v != source:
                edge_id = parent[v]
                graph.add_flow(edge_id, min_residual)
                v = graph.get_edge(edge_id).u

            max_flow += min_residual

        # Extract matching from flow assignments
        matching = [-1] * n
        for i in range(n):
            for edge_id in graph.get_ids(i + 1):
                edge = graph.get_edge(edge_id)
                if edge.flow == 1 and edge.v >= n + 1 and edge.v <= n + m:
                    matching[i] = edge.v - (n + 1)
                    break

        return matching


    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))
        
    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
