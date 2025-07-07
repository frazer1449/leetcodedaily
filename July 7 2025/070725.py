# Topological Sort 
# Advanced Algorithms
# Works like Postorder DFS

# Q: What if there is a cycle?

def topologicalSort(edges, n):
    adj = {}
    for i in range(1, n+1):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)
    
    topSort = []
    visit = set()
    # path : used for cycle detection
    path = set()
    for i in range(1, n+1):
        dfs(i, adj, visit, topSort)
    topSort.reverse()
    return topSort
def dfs(src, adj, path, visit, topSort):
    if src in path:
        return False
    if src in visit:
        return True
    path.add(src)
    visit.add(src)

    for neighbor in adj[src]:
        dfs(neighbor, adj, visit, topSort)
    topSort.append(src)
    path.remove(src)

edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]]
n = 6

print(topologicalSort(edges, n))
