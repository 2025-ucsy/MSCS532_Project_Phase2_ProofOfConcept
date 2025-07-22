from graph import Graph
from influential_user import find_most_influential

# Build the graph
g = Graph()
edges = [("Alice", "Bob"), ("Alice", "Carol"), ("Bob", "Dave"), ("Carol", "Eve"), ("Eve", "Frank")]
for n1, n2 in edges:
    g.add_edge(n1, n2)

# Run BFS and DFS
print("BFS from Alice:", g.bfs("Alice"))
print("DFS from Alice:", g.dfs("Alice"))

# Identify most influential user
user, degree = find_most_influential(g)
print(f"Most Influential User: {user} (Degree: {degree})")
