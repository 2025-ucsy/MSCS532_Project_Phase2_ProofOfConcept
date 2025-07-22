from graph import Graph
from influential_user import find_most_influential  # ✅ Corrected import

def run_tests():
    g = Graph()

    # Add edges to form a simple connected graph
    g.add_edge("Alice", "Bob")
    g.add_edge("Bob", "Charlie")
    g.add_edge("Charlie", "Diana")
    g.add_edge("Eve", "Bob")  # Eve connects in, tests incoming
    g.add_edge("Frank", "Diana")

    # Optionally test edge cases
    g.add_node("Isolated")  # A disconnected node

    # Print graph structure
    print("Graph structure:")
    for node, neighbors in g.adj_list.items():
        print(f"{node}: {neighbors}")

    # Run influence detection
    top_user, degree = find_most_influential(g)
    print(f"Most influential user: {top_user} (Degree: {degree})")

if __name__ == "__main__":
    run_tests()
