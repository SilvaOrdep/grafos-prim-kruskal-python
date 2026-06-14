import networkx as nx
import matplotlib.pyplot as plt

class GraphDrawer:
    def __init__(self, graph_dict: dict, pos: dict = None, title: str = "", edge_color: str = 'gray'):
        self.graph_dict = graph_dict
        self.graph = self._build_graph()
        self.title = title
        self.edge_color = edge_color

        self.pos = pos if pos is not None else nx.spring_layout(
            self.graph, seed=42)

    def _build_graph(self) -> nx.Graph:
        G = nx.Graph()
        for node, edges in self.graph_dict.items():
            G.add_node(node)
            for neighbor, weight in edges.items():
                G.add_edge(node, neighbor, weight=weight)
        return G

    def get_figure(self) -> plt.Figure:
        fig, ax = plt.subplots(figsize=(6, 5))

        nx.draw_networkx_nodes(
            self.graph, self.pos, ax=ax,
            node_color='lightblue',
            node_size=800,
            edgecolors='black'
        )

        nx.draw_networkx_labels(
            self.graph, self.pos, ax=ax,
            # Fonte genérica à prova de falhas em servidores
            font_size=12, font_family='sans-serif',
            font_weight='bold'
        )

        nx.draw_networkx_edges(
            self.graph, self.pos, ax=ax,
            width=2,
            alpha=0.6,
            edge_color=self.edge_color
        )

        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(
            self.graph, self.pos, ax=ax,
            edge_labels=edge_labels,
            font_color='red',
            font_size=10
        )

        if self.title:
            ax.set_title(self.title, fontsize=14, fontweight='bold')

        ax.axis('off')
        fig.tight_layout()

        return fig
