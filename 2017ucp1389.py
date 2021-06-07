#Siddharth Jain 2017UCP1389
import queue

#helper function to find node(city) farthest from a node(city) u
def bfsHelper(graph, visit, u, dist):
    lastVisited = 0
    q = queue.Queue()
    
    #push u to the front of queue and initialize the distance as 0
    q.put(u)
    dist[u] = 0
    
    #loop until each node is visited once
    while(not q.empty()):
        u = q.get()
        #update the value of the last visited node
        if(visit[u]):
            lastVisited = u
            
        #go through the neighbours of u from the adjacency matrix
        for i in range(len(graph[u])):
            v = graph[u][i]
            #update the distance between u and its neighbours
            if(dist[v] == -1):
                dist[v] = dist[u] + 1
                q.put(v)
                
    return lastVisited
    
#function to return number of possible epicentres
def findNumOfEpicentres(edges, n, hotspots, h, x):
    #initialize and populate adjacency matrix from the list of edges
    graph = [[] for i in range(n)]
    u, v = 0, 0
    for i in range(n-1):
        u = edges[i][0]
        v = edges[i][1]
        graph[u].append(v)
        graph[v].append(u)
        
    #initialize list to mark hotspots as visited
    visited = [False] * n
    for i in range(h):
        visited[hotspots[i]] = True
        
    #initialize lists to store distances
    temp = [-1] * n
    ftemp = [-1] * n
    stemp = [-1] * n
    
    #bfs to get city farthest from a starting city
    u = bfsHelper(graph, visited, 0, temp)
    
    #bfs to get second farthest city and find distance b/w cities and first farthest city
    u = bfsHelper(graph, visited, u, ftemp)
    
    #bfs to get distance b/w cities and second farthest cities
    bfsHelper(graph, visited, u, stemp)
    
    result = 0
    
    for i in range(n):
        #compare if distance both current and first farthest city and current and second farthest city
        #is less than or equal to x and update result
        if(ftemp[i] <= x and stemp[i] <= x):
            result += 1
    
    #compare if any epicenter is possible
    if(result != 0):
        return result
    else:
        return -1
        
print("Enter the following separated by a space:")
print("  number of cities, number of hotspots and maximum distance travelled by virus")
n, h, x = list(map(int, input().split()))
print("  integers denoting hotspots")
hotspots = list(map(lambda x: int(x)-1, input().split()))
edges = []
print("  "+str(n-1)+" lines of integers u and v denoting existence of road between city u and city v")
for i in range(n-1):
    edges.append(list(map(lambda x: int(x)-1, input().split())))
    
answer = findNumOfEpicentres(edges, n, hotspots, h, x)
print(answer)
