import networkx as nx


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Представлення графа за допомогою ребер
G = nx.Graph()
G.add_edge("Babych_S", "Babych_R")
G.add_edge("Babych_S", "Mescheryakova")
G.add_edge("Babych_R", "Ryabtsev")
G.add_edge("Babych_R", "Ryabtsev")
G.add_edge("Babych_R", "Fenoga")
G.add_edge("Didkovsky", "Krasnovska")
G.add_edge("Didkovsky", "Ryabtsev")
G.add_edge("Didkovsky", "Schedrovitsky")
G.add_edge("Fenoga", "Ryabtsev")
G.add_edge("Ilina", "Mescheryakova")
G.add_edge("Mescheryakova", "Moskalenko")
G.add_edge("Mescheryakova", "Ryabtsev")
G.add_edge("Moskalenko", "Ryabtsev")
graph = G


if __name__ == '__main__':

    # Виклик функції DFS
    dfs_recursive(graph, 'Mescheryakova')
