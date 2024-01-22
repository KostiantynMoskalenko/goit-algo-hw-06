def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<25} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 50)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<25} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances


# Приклад графа у вигляді словника
graph = {
    'Ilina': {'Mescheryakova': 10},
    'Mescheryakova': {'Ilina': 10, 'Babych_S': 10, 'Moskalenko': 5,
                      'Ryabtsev': 20},
    'Babych_S': {'Mescheryakova': 10, 'Babych_R': 5},
    'Babych_R': {'Babych_S': 5, 'Fenoga': 10, 'Ryabtsev': 25},
    'Moskalenko': {'Mescheryakova': 5, 'Ryabtsev': 10},
    'Fenoga': {'Babych_R': 10, 'Ryabtsev': 5},
    'Ryabtsev': {'Mescheryakova': 20, 'Moskalenko': 10, 'Babych_R': 25,
                 'Fenoga': 5, 'Didkovsky': 10},
    'Didkovsky': {'Ryabtsev': 10, 'Krasnovska': 5, 'Schedrovitsky': 10},
    'Krasnovska': {'Didkovsky': 5},
    'Schedrovitsky': {'Didkovsky': 10}
}

# Виклик функції для вершини 'Mescheryakova'
dijkstra(graph, 'Mescheryakova')
