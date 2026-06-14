import heapq

class Kruskal:
  def __init__(self, graph_dict: dict):
    self.graph_dict = graph_dict
    
  def _union_find_setter(self, nodes):
    parent = {n: n for n in nodes}
    rank = {n: 0 for n in nodes}
    
    return {parent, rank}
    
  def _find(self, item, parent):
    if parent[item] != item:
      parent[item] = self._find(parent[item])
      
    return parent[item]
  
  def _union(self, x, y, parent, rank):
    isUnion = False
    xroot = self._find(x, parent)
    yroot = self._find(y, parent)
    
    if(xroot == yroot):
      isUnion = False
      return {isUnion, parent, rank}
    
    if rank[xroot] < rank[yroot]:
      parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
      parent[yroot] = xroot
    else:
      parent[yroot] = xroot
      rank[xroot] += 1
    
    isUnion = True
    
    return {isUnion, parent, rank}
    
  def generate_mst_graph(self) -> dict:
    
    mst = {n: {} for n in self.graph_dict}
    
    edges = []
    seen = set()
    
    for u in self.graph_dict:
      for v, weight in self.graph_dict[u].items():
        if(v, u) not in seen:
          edges.append((weight, u, v))
          seen.add((u, v))
    
    heapq.heapify(edges)
    
    parent, rank = self._union_find_setter(self.graph_dict.keys())
    
    while edges:
      weight, u, v = heapq.heappop(edges)
      
      if self._union(u, v, parent, rank):
        mst[u][v] = weight
        mst[v][u] = weight
        
    return mst