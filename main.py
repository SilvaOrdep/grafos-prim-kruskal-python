import streamlit as st
from algorithms import kruskal, prim
from  graphs import graphs, graph_drawer

def main():
  graph_list = {'Grafo 1': graphs.grafo1, 'Grafo 2': graphs.grafo2, 
                'Grafo 3': graphs.grafo3, 'Grafo 4': graphs.grafo4}
  
  st.set_page_config(page_title="MST Visualizer", layout='centered')
  
  st.title('MST Visualizer')
  st.write('Selecione um dos grafos disponíveis e gere a MST dele. Você pode escolher o algoritmo de Kruskal e o de Prim')
  
  st.markdown('---')
  
  col_input1, col_input2 = st.columns(2)
  
  with col_input1:
    selected_graph = st.selectbox(
      'Selecione o Grafo:',
      options=list(graph_list.keys()),
      index=None,
      placeholder='Escolha uma opção...'
    )
  
  with col_input2:
    selected_algorithm = st.selectbox(
      'Selecione o algoritmo de MST:',
      options=['Kruskal', 'Prim'],
      index=None,
      placeholder='Escolha uma opção...'
    )
  
  st.write('')
  generate_mst_btn = st.button('Gerar MST', type='primary', use_container_width=True)
  
  st.markdown('---')
  
  if generate_mst_btn:
    if not selected_graph or not selected_algorithm:
      st.warning(
          "⚠️ Por favor, selecione um grafo e um algoritmo antes de gerar a MST.")
      return 
  
    graph_dict = graph_list[selected_graph]
    algorithm = None
    if selected_algorithm == 'Kruskal':
      algorithm = kruskal.Kruskal(graph_dict)
    elif selected_algorithm == 'Prim':
      #TODO
      # algorithm = prim.Prim(graph_dict)
      algorithm = None
      
    original_graph = graph_drawer.GraphDrawer(
      graph_dict=graph_dict,
      title=f'Grafo Original',
      edge_color='gray'
    )
    
    mst_graph = graph_drawer.GraphDrawer(
        graph_dict=algorithm.generate_mst_graph(),
        pos=original_graph.pos,
        title=f'Árvore Geradora Mínima (MST)',
        edge_color='green'
    )
    
    plot_col1, plot_col2 = st.columns(2)
    
    with plot_col1:
      st.pyplot(original_graph.get_figure())
    with plot_col2: 
      st.pyplot(mst_graph.get_figure())

if __name__ == "__main__":
  main()