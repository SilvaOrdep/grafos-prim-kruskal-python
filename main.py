import streamlit as st
from algorithms import kruskal, prim
from  graphs import graphs, graph_drawer

def main():
  kruskal_algorithm = kruskal.Kruskal
  #prim_algorithm = prim.Prim
  graph_plotter = graph_drawer.GraphDrawer
  graph_list = graphs
  

  st.set_page_config(page_title="MST Visualizer", layout='centered')
  
  st.title('MST Visualizer')
  st.write('Seleciona um dos grafos e gere a MST dele. Você pode escolher o algoritmo de Kruskal e o de Prim')
  
  st.markdown('---')
  
  col_input1, col_input2 = st.columns(2)
  
  with col_input1:
    selected_graph = st.selectbox
  
  with col_input2:
    selected_algorithm = st.selectbox
  
  



if __name__ == "__main__":
  main()