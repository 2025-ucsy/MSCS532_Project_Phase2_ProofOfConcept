def find_most_influential(graph):
    # Based on degree centrality
    max_node = None
    max_degree = -1

    for node, neighbors in graph.adj_list.items():
        if len(neighbors) > max_degree:
            max_node = node
            max_degree = len(neighbors)

    return max_node, max_degree
