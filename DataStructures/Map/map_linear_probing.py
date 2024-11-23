import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))



from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random
from DataStructures.List import array_list as al

""" 
Implementacion de Linear Probing
"""


def new_map(num_elements, load_factor, prime=109345121):
    """
    Crea una tabla de símbolos (map) sin elementos, implementada con Linear Probing.

    :param num_elements: Número de parejas <key, value> que inicialmente puede almacenar la tabla
    :type num_elements: int
    :param load_factor: Factor de carga máximo de la tabla
    :type load_factor: float
    :param prime: Número primo utilizado en la función hash (opcional, por defecto 109345121)
    :type prime: int

    :return: Un nuevo map implementado con Linear Probing
    :rtype: map_linear_probing
    """
    
    
    if num_elements == 0:
        
        num_elements = num_elements + 5
    
    
    
    
    
    # Calcula la capacidad basada en el número de elementos y el factor de carga
    capacity = mf.next_prime(int(num_elements / load_factor))
    
    # Genera valores aleatorios para scale y shift
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)

    # Crea la tabla vacía con la capacidad definida usando al.new_list
    table = al.new_list()
    for _ in range(capacity):
        al.add_last(table, None)  # Llena la tabla con valores iniciales None
    
    # Construye el mapa con los atributos iniciales
    new_map = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,  # Factor de carga actual
        'limit_factor': load_factor,  # Factor de carga máximo
        'size': 0,  # Número de elementos actuales
        'type': 'PROBING'  # Tipo de tabla
    }
    
    return new_map




def is_available(table,pos):
    entry = al.get_element(table["table"],pos)
    if me.get_key(entry) == None or me.get_key(entry) == "_EMPTY_": 
        return True
    else: 
        return False

def find_slot(my_map, key, hash_value):
    ocupado = False
    entry = al.get_element(my_map["table"],hash_value)
    if me.get_key(entry) == key: 
        ocupado = True
        return ocupado, hash_value
    

"""
def put(my_map, key, value):
    ""
    Ingresa una pareja llave-valor a la tabla de hash. Si la llave ya existe en la tabla, se reemplaza el valor.

    Parameters:
    my_map (map_linear_probing) – El mapa donde se guarda la pareja llave-valor.
    key (any) – La llave asociada a la pareja.
    value (any) – El valor asociado a la pareja.

    Returns:
    map_linear_probing – El mapa actualizado.
    ""
    
    # Obtener el índice hash para la llave
    index = mf.hash_value(my_map, key)  # Usamos la función hash_value para obtener el índice
    initial_index = index  # Guardamos el índice inicial para detectar ciclos en caso de colisiones
    found = False
    
    # Proceso de linear probing para encontrar una posición válida
    while my_map['table'][index] is not None:  # Mientras haya una entrada en la posición
        entry = my_map['table'][index]
        
        if entry['key'] == key:  # Si la clave ya existe, reemplazar el valor
            entry['value'] = value
            found = True
            break
        
        # Si no encontramos la clave, seguimos con el siguiente índice (probando de forma lineal)
        index = (index + 1) % my_map['capacity']
        
        # Si volvemos al punto de inicio, significa que la tabla está llena o no hay espacio
        if index == initial_index:
            break
    
    # Si no encontramos la clave y no se reemplazó, insertamos el nuevo par llave-valor
    if not found:
        my_map['table'][index] = {'key': key, 'value': value}  # Insertamos la nueva entrada
        my_map['size'] += 1  # Incrementamos el tamaño del mapa
    
    # Si el factor de carga se excede, podemos proceder con la expansión, aunque eso se dejaría para otra función
    
    return my_map



##############################################################################


def put(my_map, key, value):
    ""
    Ingresa una pareja llave-valor a la tabla de hash. Si la llave ya existe en la tabla, se reemplaza el valor.

    :param my_map: El map a donde se guarda la pareja llave-valor
    :type my_map: map_linear_probing
    :param key: La llave asociada a la pareja
    :type key: any
    :param value: El valor asociado a la pareja
    :type value: any

    :return: El map actualizado
    :rtype: map_linear_probing
    ""
    # Calcular la posición hash inicial
    hash_position = mf.hash_value(my_map, key) % my_map['capacity']
    
    # Explorar la tabla usando Linear Probing
    original_position = hash_position
    while my_map['table']['elements'][hash_position] is not None:
        current_entry = my_map['table']['elements'][hash_position]
        
        # Si la llave ya existe, reemplazamos el valor
        if me.get_key(current_entry) == key:
            me.set_value(current_entry, value)
            return my_map
        
        # Si la posición está ocupada por una entrada distinta, seguimos buscando
        hash_position = (hash_position + 1) % my_map['capacity']
        
        # Si hemos recorrido toda la tabla, termina el ciclo
        if hash_position == original_position:
            raise Exception("La tabla de hash está llena, no se puede insertar más elementos.")
    
    # Si encontramos una posición vacía, insertamos la nueva pareja (key, value)
    new_entry = me.new_map_entry(key, value)
    my_map['table']['elements'][hash_position] = new_entry  # Insertar la nueva entrada en la posición calculada
    
    # Incrementar el tamaño de la tabla y actualizar el factor de carga
    my_map['size'] += 1
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    
    # Verificar si es necesario redimensionar la tabla (si el factor de carga supera el límite)
    if my_map['current_factor'] > my_map['limit_factor']:
        # Aquí podrías agregar código para redimensionar la tabla (por ejemplo, rehashing)
        pass
    
    return my_map


"""


def contains(my_map, key):
    """
    Valida si la llave key se encuentra en el map.

    :param my_map: El map donde se guarda la pareja llave-valor.
    :type my_map: map_linear_probing
    :param key: La llave asociada a la pareja.
    :type key: any

    :return: True si la llave se encuentra en el map, False en caso contrario.
    :rtype: bool
    """
    # Calcular la posición hash inicial
    hash_position = mf.hash_value(my_map, key) % my_map['capacity']
    
    # Explorar la tabla usando Linear Probing
    original_position = hash_position
    while my_map['table']['elements'][hash_position] is not None:
        current_entry = my_map['table']['elements'][hash_position]
        
        # Si la llave ya existe, retornamos True
        if me.get_key(current_entry) == key:
            return True
        
        # Si la posición está ocupada por una entrada distinta, seguimos buscando
        hash_position = (hash_position + 1) % my_map['capacity']
        
        # Si hemos recorrido toda la tabla, termina el ciclo
        if hash_position == original_position:
            break
    
    # Si no encontramos la llave, retornamos False
    return False

"""
def rehash(my_map):
    ""
    Hace rehash de todos los elementos de la tabla de hash.

    :param my_map: El map a hacer rehash.
    :type my_map: map_linear_probing

    :return: El map con la nueva capacidad.
    :rtype: map_linear_probing
    ""
    # Incrementar la capacidad de la tabla al doble
    new_capacity = my_map['capacity'] * 2
    
    # Crear una nueva tabla con la nueva capacidad
    nuevo_mapa = new_map(new_capacity, 0.5, my_map["prime"])  # Reutilizamos la función new_map para crear la nueva tabla
    nuevo_mapa['capacity'] = new_capacity  # Establecer nueva capacidad
    
    
    
    table = al.new_list()
    for _ in range(new_capacity):
        al.add_last(table, None)  # Llena la tabla con valores iniciales None

    
    nuevo_mapa['table'] = table
    nuevo_mapa['size'] = my_map["size"]
    nuevo_mapa['current factor'] =  my_map["size"] / new_capacity
    
    
    
    # Llenar la nueva tabla con elementos existentes
    for i in range(my_map['capacity']):
        entry = my_map['table']['elements'][i]
        
        # Si encontramos un elemento no vacío, lo insertamos en el nuevo mapa
        if entry is not None:
            key = me.get_key(entry)
            value = me.get_value(entry)
            put(nuevo_mapa, key, value)
           
    
    # Devolver el mapa con la nueva capacidad
    return nuevo_mapa

"""

def size(my_map):
    """
    Retorna el número de parejas llave-valor en el map.

    :param my_map: El map a examinar.
    :type my_map: map_linear_probing

    :return: Número de parejas llave-valor en el map.
    :rtype: int
    """
    return my_map['size']






def rehash(my_map):
    """
    Hace rehash de todos los elementos de la tabla de hash.

    :param my_map: El map a hacer rehash.
    :type my_map: map_linear_probing

    :return: El map con la nueva capacidad.
    :rtype: map_linear_probing
    """
    # Incrementar la capacidad de la tabla al doble
    new_capacity_tool = my_map['capacity'] 
    
    # Crear una nueva tabla con la nueva capacidad
    nuevo_mapa = new_map(new_capacity_tool, 0.5, my_map["prime"])
    #nuevo_mapa['capacity'] = new_capacity  # Establecer nueva capacidad
    
    
    
    table = al.new_list()
    for _ in range(nuevo_mapa["capacity"]):
        al.add_last(table, None)  # Llena la tabla con valores iniciales None

    nuevo_mapa['table'] = table
    
    
    # Llenar la nueva tabla con elementos existentes
    for i in range(my_map['capacity']):
        entry = my_map['table']['elements'][i]
        
        # Si encontramos un elemento no vacío, lo insertamos en el nuevo mapa
        if entry is not None:
            key = me.get_key(entry)
            value = me.get_value(entry)
            put(nuevo_mapa, key, value)
    
    # Devolver el mapa con la nueva capacidad
    nuevo_mapa['current factor'] =  my_map["size"] / nuevo_mapa["capacity"] 
    
    return nuevo_mapa



def put(my_map, key, value):
    """
    Ingresa una pareja llave-valor a la tabla de hash. Si la llave ya existe en la tabla, se reemplaza el valor.

    :param my_map: El map a donde se guarda la pareja llave-valor
    :type my_map: map_linear_probing
    :param key: La llave asociada a la pareja
    :type key: any
    :param value: El valor asociado a la pareja
    :type value: any

    :return: El map actualizado
    :rtype: map_linear_probing
    """
    # Calcular la posición hash inicial
    hash_position = mf.hash_value(my_map, key) % my_map['capacity']
    
    # Explorar la tabla usando Linear Probing
    original_position = hash_position
    while my_map['table']['elements'][hash_position] is not None:
        current_entry = my_map['table']['elements'][hash_position]
        
        # Si la llave ya existe, reemplazamos el valor
        if me.get_key(current_entry) == key:
            me.set_value(current_entry, value)
            return my_map
        
        # Si la posición está ocupada por una entrada distinta, seguimos buscando
        hash_position = (hash_position + 1) % my_map['capacity']
        
        # Si hemos recorrido toda la tabla, termina el ciclo
        if hash_position == original_position:
            raise Exception("La tabla de hash está llena, no se puede insertar más elementos.")
    
    # Si encontramos una posición vacía, insertamos la nueva pareja (key, value)
    new_entry = me.new_map_entry(key, value)
    my_map['table']['elements'][hash_position] = new_entry  # Insertar la nueva entrada en la posición calculada
    
    # Incrementar el tamaño de la tabla y actualizar el factor de carga
    my_map['size'] += 1
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    
    # Verificar si es necesario redimensionar la tabla (rehashing)
    if my_map['current_factor'] > my_map['limit_factor']:
        nuevo_mapa = rehash(my_map)
        my_map['prime'] =  nuevo_mapa['prime']
        my_map['capacity']      =     nuevo_mapa['capacity'] 
        my_map['scale']         =   nuevo_mapa['scale']
        my_map['shift']         =     nuevo_mapa['shift'] 
        my_map['table']         =       nuevo_mapa['table'] 
        my_map['current_factor']=     nuevo_mapa['current_factor']
        my_map['limit_factor']  =      nuevo_mapa['limit_factor']
        my_map['size']          =      nuevo_mapa['size']
        my_map['type']          =     nuevo_mapa['type']  
        
        
        #print(my_map['current_factor'],my_map['size'],my_map['capacity'])
        return my_map
        
    return my_map


def get(my_map, key):
    """
    Retorna el valor asociado a la llave key en el map.

    :param my_map: El map a examinar.
    :type my_map: map_linear_probing
    :param key: La llave a buscar.
    :type key: any

    :return: El valor asociado a la llave key, o None si la llave no se encuentra.
    :rtype: any
    """
    # Calcular la posición hash inicial
    hash_position = mf.hash_value(my_map, key) % my_map['capacity']
    
    # Explorar la tabla usando Linear Probing
    original_position = hash_position
    while my_map['table']['elements'][hash_position] is not None:
        current_entry = my_map['table']['elements'][hash_position]
        
        # Si la llave coincide, retornamos el valor asociado
        if me.get_key(current_entry) == key:
            return me.get_value(current_entry)
        
        # Continuar buscando en la siguiente posición
        hash_position = (hash_position + 1) % my_map['capacity']
        
        # Si hemos recorrido toda la tabla, salimos del ciclo
        if hash_position == original_position:
            break
    
    # Si no encontramos la llave, retornamos None
    return None

def key_set(my_map):
    """
    Retorna una lista con todas las llaves de la tabla de hash.

    :param my_map: El map a examinar.
    :type my_map: map_linear_probing

    :return: Lista de todas las llaves presentes en la tabla de hash.
    :rtype: array_list
    """
    # Crear una lista vacía para almacenar las llaves
    keys = al.new_list()

    # Recorrer todas las posiciones en la tabla
    for entry in my_map['table']['elements']:
        # Si la posición no está vacía, obtener la llave y agregarla a la lista
        if entry is not None:
            al.add_last(keys, me.get_key(entry))
    
    return keys

def remove(my_map, key):
    """
    Elimina la pareja llave-valor del map.

    :param my_map: El map a examinar.
    :type my_map: map_linear_probing
    :param key: La llave a eliminar.
    :type key: any

    :return: El map sin la llave key.
    :rtype: map_linear_probing
    """
    # Calcular la posición hash inicial
    hash_position = mf.hash_value(my_map, key) % my_map['capacity']
    
    # Explorar la tabla usando Linear Probing
    original_position = hash_position
    while my_map['table']['elements'][hash_position] is not None:
        current_entry = my_map['table']['elements'][hash_position]
        
        # Si encontramos la llave, la eliminamos
        if me.get_key(current_entry) == key:
            my_map['table']['elements'][hash_position] = None
            my_map['size'] -= 1
            
            # Rehash de los elementos restantes para mantener la consistencia
            next_position = (hash_position + 1) % my_map['capacity']
            while my_map['table']['elements'][next_position] is not None:
                entry_to_rehash = my_map['table']['elements'][next_position]
                my_map['table']['elements'][next_position] = None
                my_map['size'] -= 1  # Temporalmente reducimos el tamaño
                put(my_map, me.get_key(entry_to_rehash), me.get_value(entry_to_rehash))
                next_position = (next_position + 1) % my_map['capacity']
            
            return my_map
        
        # Continuar buscando en caso de colisión
        hash_position = (hash_position + 1) % my_map['capacity']
        if hash_position == original_position:
            break
    
    # Si no encontramos la llave, no hacemos nada
    return my_map


def value_set(my_map):
    """
    Retorna una lista con todos los valores de la tabla de hash.

    :param my_map: El map a examinar.
    :type my_map: map_linear_probing

    :return: Lista de valores.
    :rtype: array_list
    """
    # Crear una lista vacía para almacenar los valores
    values_list = al.new_list()

    # Recorrer la tabla de hash
    for entry in my_map['table']['elements']:
        if entry is not None:  # Ignorar posiciones vacías
            value = me.get_value(entry)
            al.add_last(values_list,value)

    return values_list

