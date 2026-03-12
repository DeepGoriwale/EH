import numpy as np


def page_rank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    num_nodes = len(graph)
    page_ranks = np.ones(num_nodes) / num_nodes

    # Precompute incoming links (important)
    incoming = [[] for _ in range(num_nodes)]
    for src, out in enumerate(graph):
        for dest in out:
            incoming[dest].append(src)

    for _ in range(max_iterations):
        prev = page_ranks.copy()

        for node in range(num_nodes):
            if incoming[node]:
                page_ranks[node] = (1 - damping_factor) / num_nodes + \
                    damping_factor * sum(prev[i] / len(graph[i])
                                         for i in incoming[node])
            else:
                # No incoming links → base rank
                page_ranks[node] = (1 - damping_factor) / num_nodes

        if np.linalg.norm(page_ranks - prev, 2) < tolerance:
            break

    return page_ranks


# Example usage
if __name__ == "__main__":
    web_graph = [
        [1, 2],
        [0, 2],
        [0, 1],
        [1, 2],
    ]

    result = page_rank(web_graph)

    for i, pr in enumerate(result):
        print(f"Page {i}: {pr:.6f}")
