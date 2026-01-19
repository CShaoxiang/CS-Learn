#Uses python3
import sys
import math
import heapq

def minimum_distance(x, y):
    result = 0
    #write your code here

    n = len(x)
    dist = [10**18] * n
    dist[0] = 0 

    visited  = [False] * n 

    # start with  node 0 with distance 0
    prioQ = [(0,0)]



    while prioQ:
        d , node = heapq.heappop(prioQ)
        
        if not visited[node] :
            visited[node] = True 

            # Add the min edge weight to total length
            result += d

            # Examine every other node
            for i in range(n):
                if not visited[i]:
                    #calculate distance to other nodes 
                    
                    new_dist = calculate_distance(x[node],y[node],x[i],y[i])
                    
                    
                    if new_dist < dist[i]:
                        dist[i] = new_dist
                        heapq.heappush(prioQ,(new_dist,i))

    return result


def calculate_distance(x1,y1,x2,y2):

    distance = math.sqrt((x1-x2) **2 +(y1 - y2) ** 2)
    return distance

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
