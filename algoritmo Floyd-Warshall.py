def floyd_warshall(graph):
    """
    Encuentra las distancias mínimas entre todos los pares de nodos en un grafo.
    
    Args:
        graph: Matriz de adyacencia (lista de listas). 
               graph[i][j] = peso de la arista (i, j).
               Use float('inf') para representar "no conexión".
               
    Returns:
        Matriz de distancias mínimas y detección de ciclos negativos.
    """
    n = len(graph)
    
    # Inicializar matriz de distancias
    dist = [row[:] for row in graph]
    
    # Actualizar distancias usando todos los nodos intermedios
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Detectar ciclos negativos
    has_negative_cycle = any(dist[i][i] < 0 for i in range(n))
    
    return dist, has_negative_cycle

def print_matrix(matrix):
    """Imprime una matriz de forma legible, reemplazando inf por 'INF'"""
    for row in matrix:
        print(' '.join(['INF' if x == float('inf') else f"{x:3}" for x in row]))

# Ejemplo 1: Grafo sin ciclos negativos
graph1 = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

print("Grafo original:")
print_matrix(graph1)

result1, negative_cycle1 = floyd_warshall(graph1)

print("\nDistancias mínimas:")
print_matrix(result1)
print(f"¿Tiene ciclos negativos? {'Sí' if negative_cycle1 else 'No'}")

# Ejemplo 2: Grafo con pesos negativos (sin ciclos negativos)
graph2 = [
    [0, 4, float('inf'), float('inf')],
    [float('inf'), 0, -2, float('inf')],
    [float('inf'), float('inf'), 0, 3],
    [1, float('inf'), float('inf'), 0]
]

print("\n\nGrafo con pesos negativos:")
print_matrix(graph2)

result2, negative_cycle2 = floyd_warshall(graph2)

print("\nDistancias mínimas:")
print_matrix(result2)
print(f"¿Tiene ciclos negativos? {'Sí' if negative_cycle2 else 'No'}")

# Ejemplo 3: Grafo con ciclo negativo
graph3 = [
    [0, 1, float('inf')],
    [float('inf'), 0, -5],
    [2, float('inf'), 0]
]

print("\n\nGrafo con ciclo negativo:")
print_matrix(graph3)

result3, negative_cycle3 = floyd_warshall(graph3)

print("\nDistancias mínimas:")
print_matrix(result3)
print(f"¿Tiene ciclos negativos? {'Sí' if negative_cycle3 else 'No'}")