from collections import deque
import networkx as nx


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні,
    # то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)


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

    # Виклик функції BFS
    bfs_recursive(graph, deque(["Mescheryakova"]))
