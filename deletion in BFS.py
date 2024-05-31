n, m = map(int, input().split())  # n = 5, m = 4
adj = [[] for _ in range(n)]      # adj = [[], [], [], [], []]

edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
def initiateBFSTraversal(node, visited, adj, result):
    Q = [node]
    visited[node] = True 
 
    while len(Q) > 0:
        curr = Q.pop(0)
        result.append(curr)
        for neighbour in adj[curr]:
            if visited[neighbour] == False:
                visited[neighbour] = True 
                Q.append(neighbour)
 
 
def printBFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateBFSTraversal(node, visited, adj, result)
 
    print("BFS traversal is: ", result)
 
 
 
# Adjacency List Construction 
n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
printBFSTraversal(adj, n)
 
 
 

