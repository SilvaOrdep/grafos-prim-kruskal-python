import matplotlib.pyplot as plt
import networkx as nx

class GraphDrawer:
  def __init__(self, graph_dict: dict):
    self.graph_dict = graph_dict
    self.graph = self._build_graph()
    
  def _build_graph(self) -> nx.Graph:
    G = nx.Graph()
    for node, edges in self.graph_dict.items():
      G.add_node(node)
      for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)
    return G
  
  def get_figure(self) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10,7))
    
    pos = nx.spring_layout(self.graph, seed=42)
    
    nx.draw_networkx_nodes(
      self.graph, pos, ax=ax,
      node_color='lightblue',
      node_size=800,
      edgecolors='black'
    )
    
    nx.draw_networkx_labels(
      self.graph, pos, ax=ax,
      font_size=12, font_family='arial',
      font_weight='bold'
    )
    
    nx.draw_networkx_edges(
      self.graph, pos, ax=ax,
      width=2,
      alpha=0.6,
      edge_color='gray'
    )
    
    edge_labels = nx.get_edge_attributes(self.graph, 'weight')
    nx.draw_networkx_edge_labels(
      self.graph, pos, ax=ax,
      edge_labels=edge_labels,
      font_color='red',
      font_size=10
    )
    
    ax.axis('off')
    
    fig.tight_layout()
    
    return fig
  
  