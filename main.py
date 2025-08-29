import networkx as nx
import matplotlib.pyplot as plt

# --- Grafo não planar: K3,3 ---
G_np = nx.complete_bipartite_graph(3, 3)
is_planar_np, embedding_np = nx.check_planarity(G_np)
print("K3,3 planar?", is_planar_np)

# --- Grafo planar: ex. grafo em grade 3x3 ---
G_p = nx.grid_2d_graph(3, 3)  # grafo planar em grade 3x3
is_planar_p, embedding_p = nx.check_planarity(G_p)
print("Grafo 3x3 planar?", is_planar_p)

# --- Plotar os dois grafos ---
plt.figure(figsize=(12, 6))

# Grafo não planar
plt.subplot(1, 2, 1)
pos_np = nx.spring_layout(G_np)
nx.draw(G_np, pos_np, with_labels=True, node_color='lightcoral', node_size=800, font_size=12)
plt.title("Grafo não planar: K3,3")

# Grafo planar
plt.subplot(1, 2, 2)
pos_p = {(i,j):(j,-i) for i,j in G_p.nodes()}  # layout em grade
nx.draw(G_p, pos_p, with_labels=True, node_color='lightgreen', node_size=800, font_size=12)
plt.title("Grafo planar: grade 3x3")

plt.show()
