import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))





from DataStructures.Utils.utils import handle_not_implemented
from DataStructures.Graph import adj_list_graph as gl
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
from DataStructures.Graph import edge as ed






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
    #for i in range(size):
       # mp.put(my_map_vertices, i, al.new_list())  # Insertar el vértice con una lista vacía
    
    # Mapa de información con diccionarios vacíos para cada vértice
   # for i in range(size):
       # mp.put(my_map_information, f"info_{i}", {})  # Insertar información vacía para cada vértice
    
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
    #if mp.get(my_graph['vertices'],key_vertex):
        # Si el vértice ya existe, actualizamos la información asociada
        
    #    mp.put(my_graph['vertices'],key_vertex,al.new_list())
        
    #else:
        # Si el vértice no existe, lo agregamos al grafo
       # my_graph['vertices'][key_vertex] = []  # Inicializamos la lista de arcos adyacentes
    mp.put(my_graph['vertices'],key_vertex,al.new_list())
       # my_graph['information'][key_vertex] = info_vertex  # Insertamos la información del vértice
    mp.put(my_graph['information'],key_vertex,info_vertex)
    if my_graph['in_degree'] is not None:
        my_graph['in_degree'][key_vertex] = 0  # Si el grafo no es dirigido, el grado de entrada es 0
        
    
    return my_graph   


# l lL

#def add_edge(graph, vertex_a, vertex_b, weight=0):
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

def add_edge(my_graph, vertex_a, vertex_b, weight=0):
    """
    Agrega un arco al grafo. Considera los casos de vértices no existentes, arcos existentes y el tipo de grafo.

    :param my_graph: El grafo sobre el que se ejecuta la operación
    :type my_graph: adj_list_graph
    :param vertex_a: Vértice de inicio
    :type vertex_a: any
    :param vertex_b: Vértice destino
    :type vertex_b: any
    :param weight: Peso del arco, por defecto 0
    :type weight: double

    :return: El grafo actualizado con el nuevo arco
    :rtype: adj_list_graph
    """
    
    
    # Verificar si ambos vértices existen en el grafo
    if not mp.contains(my_graph['vertices'], vertex_a) or not mp.contains(my_graph['vertices'], vertex_b):
        return my_graph  # No se agrega el arco si alguno de los vértices no existe
    
    # Obtener la lista de adyacencia del vértice 'vertex_a'
    adj_list_a = mp.get(my_graph['vertices'], vertex_a)
    
    
    # Revisar si el arco ya existe
    for edge in adj_list_a["elements"]:
        
        if ed.either(edge) == vertex_a and ed.other(edge,vertex_a) == vertex_b:
            # Si el arco ya existe, reemplazar su peso
            ed.set_weight(edge, weight)
            return my_graph
    
    # Crear un nuevo arco y agregarlo a la lista de adyacencia de 'vertex_a'
    new_edge = ed.new_edge(vertex_a, vertex_b, weight)
    al.add_last(adj_list_a, new_edge)
    
    
    
    # Incrementar el número de arcos en el grafo
    my_graph['edges'] += 1
    
    # Si el grafo es no dirigido, agregar el arco en ambas direcciones
    if not my_graph['directed']:
        adj_list_b = mp.get(my_graph['vertices'], vertex_b)
        reverse_edge = ed.new_edge(vertex_b, vertex_a, weight)
        al.add_last(adj_list_b, reverse_edge)
    else:
        # Si es dirigido, incrementar el grado de entrada de 'vertex_b'
        in_degree_b = mp.get(my_graph['in_degree'], vertex_b)
        mp.put(my_graph['in_degree'], vertex_b, in_degree_b + 1)
    
    return my_graph



def num_vertices(my_graph):
    """
    Retorna el número de vértices del grafo.

    :param my_graph: El grafo sobre el que se ejecuta la operación
    :type my_graph: adj_list_graph

    :return: El número de vértices en el grafo
    :rtype: int
    """
    return mp.size(my_graph['vertices'])


def num_edges(my_graph):
    """
    Retorna el número de arcos del grafo.

    :param my_graph: El grafo sobre el que se ejecuta la operación
    :type my_graph: adj_list_graph

    :return: El número de arcos en el grafo
    :rtype: int
    """
    return my_graph['edges']


def vertices(my_graph):
    """
    Retorna una lista con todos los vértices del grafo.

    :param my_graph: El grafo sobre el que se ejecuta la operación
    :type my_graph: adj_list_graph

    :return: Una lista con los vértices del grafo
    :rtype: array_list
    """
    
    mapa_vertices = my_graph["vertices"]
     
    return mp.key_set(mapa_vertices)

"""

def edges(my_graph):
    ""
    Retorna una lista con todos los arcos del grafo.

    Para un grafo No Dirigido, un arco que conecte dos vértices solo aparece una vez en la lista.

    :param my_graph: El grafo sobre el que se ejecuta la operación
    :type my_graph: adj_list_graph

    :return: Una lista con los arcos del grafo
    :rtype: array_list
    #""
    
    edges = al.new_list()
    
    all_vertices = mp.value_set(my_graph["vertices"])
    
    #if my_graph["directed"] == True:
        
        #return all_vertices
        
    #else:
    for lista_vertices_por_nodo in all_vertices["elements"]:
            
            for arista_comparada in lista_vertices_por_nodo["elements"]:

                supervisor = True
        
                for arista in all_vertices["elements"]:
            
                    if ed.compare_edges(arista_comparada,arista) == 0:
                        
                        supervisor = False
            
                if supervisor == True:
                    
                    al.add_last(edges, arista_comparada)    
            
    edges_no_directed = al.new_list()
    
    if my_graph["directed"] == False:
        
        for arista_comparada_2 in edges["elements"]:

                supervisor_2 = True
        
                for arista_2 in all_vertices["elements"]:
            
                    if ed.mismo_edge(arista_comparada_2,arista_2) == 0:
                        
                        supervisor_2 = False
            
                if supervisor_2 == True:
                    
                    al.add_last(edges_no_directed, arista_comparada_2)  
        
        
        return  edges_no_directed
    
    
           
    return edges
###############################

def edges(my_graph):
    ""
    Retorna una lista con todos los arcos del grafo.

    Para un grafo No Dirigido, un arco que conecte dos vértices solo aparece una vez en la lista.

    :param my_graph: El grafo sobre el que se ejecuta la operación
    :type my_graph: adj_list_graph

    :return: Una lista con los arcos del grafo
    :rtype: array_list
    ""
    
    edge_list = al.new_list()
    
    # Obtener los vértices del grafo
    all_vertices = mp.value_set(my_graph["vertices"])
    
    # Lista para arcos ya visitados (para evitar duplicados en grafos no dirigidos)
    visited_edges = al.new_list()

    # Recorrer todos los vértices
    for lista_vertex_por_nodo in all_vertices["elements"]:
        
        for vertex in lista_vertex_por_nodo:
            # Obtener los arcos adyacentes a este vértice
            adj_edges = my_graph["adj_list"][vertex]  # Asumiendo que es una lista de arcos

            for edge in adj_edges:
                # Si el grafo es dirigido, agregamos directamente el arco
                if my_graph["directed"]:
                    al.add_last(edge_list, edge)
                else:
                    # Para grafos no dirigidos, asegurarnos de no agregar duplicados
                    is_duplicate = False
                    for visited_edge in visited_edges:
                        if ed.compare_edges(edge, visited_edge) == 0:
                            is_duplicate = True
                            break
                    
                    if not is_duplicate:
                        al.add_last(edge_list, edge)
                        al.add_last(visited_edges, edge)  # Marca este arco como visitado

    return edge_list

"""


#####################
""""
def edges(my_graph):
    ""
    Retorna una lista con todos los arcos del grafo.

    Para un grafo No Dirigido, un arco que conecte dos vértices solo aparece una vez en la lista.

    :param my_graph: El grafo sobre el que se ejecuta la operación
    :type my_graph: adj_list_graph

    :return: Una lista con los arcos del grafo
    :rtype: array_list
    ""
    
    edge_list = al.new_list()  # Lista que guardará los arcos
    visited_edges = al.new_list()  # Lista para evitar duplicados en grafos no dirigidos
    
    all_vertices = mp.value_set(my_graph["vertices"])  # Obtener todos los vértices del grafo
    
    # Recorrer todos los vértices del grafo
    for vertex in all_vertices:
        adj_edges = my_graph["adj_list"][vertex]  # Obtener los arcos adyacentes al vértice
        
        for edge in adj_edges:
            # Para grafos dirigidos, agregamos directamente el arco
            if my_graph["directed"]:
                al.add_last(edge_list, edge)
            else:
                # Para grafos no dirigidos, evitamos duplicados
                is_duplicate = False
                for visited_edge in visited_edges:
                    if e.compare_edges(edge, visited_edge) == 0:  # Si el arco ya fue visitado
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    al.add_last(edge_list, edge)
                    al.add_last(visited_edges, edge)  # Marcar el arco como visitado

    return edge_list

"""

######################

def edges(my_graph):
    """
    Retorna una lista con todos los arcos del grafo.

    Para un grafo No Dirigido, un arco que conecte dos vértices solo aparece una vez en la lista.

    :param my_graph: El grafo sobre el que se ejecuta la operación.
    :type my_graph: adj_list_graph

    :return: Una lista con los arcos del grafo.
    :rtype: array_list
    """
    
    edge_list = al.new_list()  # Lista para almacenar los arcos
    visited_edges = al.new_list()  # Lista para almacenar arcos visitados (para evitar duplicados)
    
    # Recorremos los vértices
    for vertex in my_graph["vertices"]:
        edges_from_vertex = my_graph["vertices"][vertex]  # Obtenemos los arcos desde el vértice

        for edge in edges_from_vertex:
            # Si el grafo es dirigido, agregamos el arco
            if my_graph["directed"]:
                al.add_last(edge_list, edge)
            else:
                # Si el grafo es no dirigido, verificamos si el arco ya ha sido agregado
                is_duplicate = False
                for visited_edge in visited_edges:
                    if ed.compare_edges(edge, visited_edge) == 0:  # Comparamos el arco con los visitados
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    al.add_last(edge_list, edge)
                    al.add_last(visited_edges, edge)  # Marcamos el arco como visitado

    return edge_list







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