import matplotlib.pyplot as plt
import networkx as nx


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

print("Список вершин графа: ", G.nodes())
print("Список ребер графа: ", G.edges())
print("Кількість вершин графа: ", G.number_of_nodes())
print("Кількість ребер графа: ", G.number_of_edges())
print("Ступені центральності вершин графа: ", nx.degree_centrality(G))
print("Частина від загальної кількості шляхів, що проходять через вузол: ",
      nx.betweenness_centrality(G))
print("Близкість вузла до центру: ", nx.closeness_centrality(G))


if __name__ == '__main__':

    plt.figure(figsize=(9, 9))
    pos = nx.spring_layout(G, seed=46)
    nx.draw_networkx(G, pos, with_labels=True, node_size=800,
                     node_color="lightblue", width=1.2,  font_size=16,
                     font_weight="light")
    plt.show()
