import heapq

class Prim:
  def __init__(self, graph_dict: dict):
    self.graph_dict = graph_dict

  def generate_mst_graph(self) -> dict:
    nodes = list(self.graph_dict.keys())
    start = nodes[0]

    visited = {start}
    mst = {n: {} for n in self.graph_dict}

    priority_queue = [
      (weight, start, neighbor)
      for neighbor, weight in self.graph_dict[start].items()
    ]
    heapq.heapify(priority_queue)

    while priority_queue:
      weight, u, v = heapq.heappop(priority_queue)

      if v in visited:
        continue

      visited.add(v)
      mst[u][v] = weight
      mst[v][u] = weight

      for neighbor, edge_weight in self.graph_dict[v].items():
        if neighbor not in visited:
          heapq.heappush(priority_queue, (edge_weight, v, neighbor))

    return mst
