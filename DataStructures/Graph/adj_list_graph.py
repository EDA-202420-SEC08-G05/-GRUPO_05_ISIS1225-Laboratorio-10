import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))





from DataStructures.Utils.utils import handle_not_implemented
from DataStructures.Graph import adj_list_graph as gl
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
from DataStructures.Graph import edge







def new_graph(size=19, directed=False):
    """
    Crea un grafo vacio

    Se crea un grafo con los siguientes atributos:

        vertices: Mapa de vertices del grafo donde su llave es el vertice y su valor es una lista de arcos adyacentes.

        information: Mapa de informacion asociada a los vertices donde su llave es el vertice y su valor es la informacion asociada (diccionario).

        in_degree: Mapa de grados de entrada de los vertices del grafo, inicializado en None en caso de no ser dirigido. Donde su llave es el vertice y su valor es el grado de entrada (int).

        edges: Numero de arcos del grafo.

        directed: Indica si el grafo es dirigido o no.

        type: Tipo de grafo. Inicializado en “ADJ_LIST”

    Parameters:

            size (int) – Numero de vertices del grafo, por defecto 19 en caso de no ser especificado.

            directed (bool) – Indica si el grafo es dirigido o no. Por defecto es False.

    Returns:

        Grafo creado
    Return type:

        adj_list_graph
    """
   
    
    # Crear el mapa de sondeo lineal usando la función new_map de mp
    my_map_vertices = mp.new_map(size, 0.5)
    my_map_information = mp.new_map(size, 0.5)
    
    
    # Mapa de vértices con listas vacías para cada vértice
    for i in range(size):
        mp.put(my_map_vertices, i, al.new_list())  # Insertar el vértice con una lista vacía
    
    # Mapa de información con diccionarios vacíos para cada vértice
    for i in range(size):
        mp.put(my_map_information, f"info_{i}", {})  # Insertar información vacía para cada vértice
    
    # Mapa de grados de entrada (sólo si el grafo es dirigido)
    in_degree = None
    if directed:
        in_degree = {i: 0 for i in range(size)}
    
    # Inicializar los atributos del grafo
    graph = {
        'vertices': my_map_vertices,  # Usando el mapa para almacenar los vértices
        'information': my_map_information,  # Usando el mapa para almacenar la información
        'in_degree': in_degree,  # Solo para grafos dirigidos
        'edges': 0,  # Número de arcos
        'directed': directed,  # Si el grafo es dirigido o no
        'type': 'ADJ_LIST'  # Tipo de grafo
    }
    
    return graph 

def insert_vertex(my_graph, key_vertex, info_vertex):
    """
    Inserta un vértice al grafo my_graph.

    Si la llave key_vertex no existe en el grafo se agrega al grafo, de lo contrario se actualiza la información asociada al vértice.

    Parameters:
    my_graph (adj_list_graph) – El grafo sobre el que se ejecuta la operación.
    key_vertex (any) – El vértice que se desea insertar.
    info_vertex (any) – Información asociada al vértice.

    Returns:
    adj_list_graph – El grafo con el nuevo vértice o la información actualizada.
    """
    
    # Verificamos si el vértice ya existe en el grafo
    if key_vertex in my_graph['vertices']:
        # Si el vértice ya existe, actualizamos la información asociada
        my_graph['information'][key_vertex] = info_vertex
    else:
        # Si el vértice no existe, lo agregamos al grafo
        my_graph['vertices'][key_vertex] = []  # Inicializamos la lista de arcos adyacentes
        my_graph['information'][key_vertex] = info_vertex  # Insertamos la información del vértice
        if my_graph['in_degree'] is not None:
            my_graph['in_degree'][key_vertex] = 0  # Si el grafo no es dirigido, el grado de entrada es 0
        
    
    return my_graph   


# l lL

def add_edge(graph, vertex_a, vertex_b, weight=0):
    """ 
    Agrega un arco al grafo. Al momento de agregar un arco se deben tener en cuenta los siguientes casos:

    Si alguno de los vertices NO existe, NO se agrega el arco. Si los vertices existen y el arco YA existe, Se reemplaza el peso del arco (NO se acepta arcos paralelos).

    Si los vertices existen y si el arco NO existe:

        Agrega el arco vertex_a -> vertex_b, con peso weight, a la lista de adyacencia del vertice vertex_a

        Si el grafo es No dirigido: se agrega el arco vertex_b -> vertex_a, con peso weight, a la lista de adyacencia del vertice vertex_b

        Si el grado es Dirigido: Se incrementa el grado de entrada (in_degree) del vertice vertex_b en 1

    Parameters:

            my_graph (adj_list_graph) – El grafo sobre el que se ejecuta la operacion

            vertex_a (any) – Vertice de inicio

            vertex_b (any) – Vertice destino

            weight (double) – Peso del arco, por defecto 0

    Returns:

        El grafo con el nuevo arco
    Return type:

        adj_list_graph
    """

def get_edge(graph, vertex_a, vertex_b):
    """ 
    Retorna el arco asociado a los vertices vertex_a —- vertex_b El arco debe existir en la misma direccion vertex_a -> vertex_b en caso de grafo sea dirigido o grafo No dirigido

    Parameters:

            my_graph (adj_list_graph) – El grafo sobre el que se ejecuta la operacion

            vertex_a (any) – Vertice de inicio

            vertex_b (any) – Vertice destino

    Returns:

        El arco que une los verices vertex_a y vertex_b
    Return type:

        edge


    """
    

def contains_vertex(graph, vertex):
    """ 
        Retorna si el vertice con llave`key_vertex` esta presente en el grafo.

    Parameters:

            my_graph (adj_list_graph) – El grafo sobre el cual consultar la existencia del vertice

            key_vertex (any) – Vertice a buscar

    Returns:

        True si el vertice esta presente, False en caso contrario
    Return type:

        bool
    """
    
    # Hasta aqui son las funciones del lab. Desde aqui son las demas de DICS
    
    def remove_vertex(my_graph, key_vertex):
        """
        Remueve el vertice del grafo

        Parameters:

                graph (adj_list_graph) – El grafo sobre el que se ejecuta la operacion

                key_vertex (any) – El vertice que se desea remover

        Returns:

            El grafo sin el vertice
        Return type:

            adj_list_graph
        """