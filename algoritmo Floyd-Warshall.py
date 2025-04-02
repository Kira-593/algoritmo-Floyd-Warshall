try:
    import networkx as nx
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: Necesitas instalar las dependencias:")
    print("pip install networkx matplotlib")
    exit()

# ----------------------------------------------------------
# Algoritmo de Floyd-Warshall
# ----------------------------------------------------------
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist, any(dist[i][i] < 0 for i in range(n))

# ----------------------------------------------------------
# Funciones de visualización
# ----------------------------------------------------------
def print_graph(matrix, title):
    n = len(matrix)
    nodos = [chr(65 + i) for i in range(n)]
    
    print(f"\n{title}:")
    print(f"    {'   '.join(nodos)}")
    for i in range(n):
        fila = [f"{nodos[i]}"] + ['INF' if x == float('inf') else f"{x:3}" for x in matrix[i]]
        print(' '.join(fila))

def draw_graph(graph):
    G = nx.DiGraph()
    n = len(graph)
    nodos = [chr(65 + i) for i in range(n)]
    
    # Añadir aristas
    for i in range(n):
        for j in range(n):
            peso = graph[i][j]
            if i != j and peso != float('inf'):
                G.add_edge(nodos[i], nodos[j], weight=peso)
    
    # Configurar diseño
    pos = nx.spring_layout(G, seed=42)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='red',
            font_size=14, arrows=True, arrowsize=25, connectionstyle='arc3,rad=0.1')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred')
    plt.title("Grafo Ingresado por el Usuario", fontsize=16)
    plt.show()

# ----------------------------------------------------------
# Entrada de usuario
# ----------------------------------------------------------
def input_matrix():
    while True:
        try:
            n = int(input("\n► Ingrese el número de nodos: "))
            if n < 1:
                print("¡Debe haber al menos 1 nodo!")
                continue
            break
        except ValueError:
            print("¡Entrada inválida! Ingrese un número entero.")

    print("\n► Instrucciones:")
    print(" - Diagonal principal: ingrese 0")
    print(" - Sin conexión: ingrese 9999")
    print(" - Pesos negativos permitidos")
    print(" - Ejemplo para 3 nodos: 0 5 9999\n")

    graph = []
    for i in range(n):
        nodo_actual = chr(65 + i)
        while True:
            try:
                entrada = input(f"Ingrese fila para nodo {nodo_actual} ({n} valores separados por espacios): ")
                fila = []
                for x in entrada.split():
                    if x == '9999':
                        fila.append(float('inf'))
                    else:
                        valor = float(x)
                        fila.append(valor)
                
                if len(fila) != n:
                    print(f"¡Error! Necesita {n} valores")
                    continue
                
                if fila[i] != 0:
                    print(f"¡El valor {nodo_actual}→{nodo_actual} debe ser 0!")
                    continue
                
                graph.append(fila)
                break
                
            except ValueError:
                print("¡Entrada inválida! Use números o 9999 para infinito")
    
    return graph

# ----------------------------------------------------------
# Ejecución principal
# ----------------------------------------------------------
if __name__ == "__main__":
    print("\n" + "="*60)
    print(" "*10 + "ALGORITMO DE FLOYD-WARSHALL - VERSIÓN COMPLETA")
    print("="*60)
    
    # Obtener y mostrar grafo
    matriz = input_matrix()
    print_graph(matriz, "Matriz Original")
    draw_graph(matriz)
    
    # Calcular resultados
    distancias, ciclos_neg = floyd_warshall(matriz)
    print_graph(distancias, "Matriz de Distancias Mínimas")
    print(f"\n► Ciclos negativos detectados: {'SÍ' if ciclos_neg else 'NO'}")
    
    # Mostrar rutas
    print("\n" + "-"*60)
    print("Rutas más cortas entre todos los pares:")
    nodos = [chr(65 + i) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != j:
                distancia = distancias[i][j]
                valor = 'INF' if distancia == float('inf') else f"{distancia:.2f}"
                print(f" ▷ {nodos[i]} → {nodos[j]}: {valor}")