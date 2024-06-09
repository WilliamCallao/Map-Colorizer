import tkinter as tk
from tkinter import ttk, PhotoImage, Button, messagebox
import random
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pathlib import Path

# Colores disponibles
colores_disponibles = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']

# Rangos para menús desplegables
rango_regiones = list(range(16, 31))
rango_colores = list(range(1, len(colores_disponibles) + 1))

# Obtener ruta relativa
def relative_to_assets(path: str) -> Path:
    current_folder = Path(__file__).parent
    assets_folder = current_folder / "assets"
    return assets_folder / path

# Visualizar grafo
def visualizar_grafo(grafo, coloreo=None, frame_grafo=None):
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    G = nx.Graph()
    
    # Crear nodos y aristas
    for nodo, vecinos in grafo.items():
        G.add_node(nodo)
        for vecino in vecinos:
            G.add_edge(nodo, vecino)
    pos = nx.spring_layout(G)
    
    # Colorear nodos
    if coloreo:
        colores = [coloreo.get(nodo) for nodo in G.nodes()]
    else:
        colores = 'lightblue'
        
    nx.draw(G, pos, with_labels=True, node_color=colores, edge_color='gray', ax=ax)
    
    # Limpiar y mostrar gráfico
    if frame_grafo:
        for widget in frame_grafo.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=frame_grafo)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Colorear grafo
def colorear_grafo(grafo, num_colores):
    coloreo = {}
    if num_colores > len(colores_disponibles):
        print("Advertencia: Demasiados colores solicitados.")
        num_colores = len(colores_disponibles)
    
    for nodo in grafo:
        colores_nodo = colores_disponibles[:num_colores]
        for vecino in grafo[nodo]:
            if vecino in coloreo:
                if coloreo[vecino] in colores_nodo:
                    colores_nodo.remove(coloreo[vecino])
        coloreo[nodo] = colores_nodo[0] if colores_nodo else 'black'
    
    return coloreo

# Generar grafo aleatorio
def generar_grafo_aleatorio(num_regiones):
    G = nx.Graph()
    G.add_nodes_from(range(num_regiones))
    
    # Crear aristas
    for i in range(1, num_regiones):
        G.add_edge(i - 1, i)
    
    nodos = list(G.nodes)
    intentos = 0
    max_intentos = num_regiones * 10

    # Añadir aristas adicionales
    while G.number_of_edges() < num_regiones * 2 and intentos < max_intentos:
        nodo_a, nodo_b = random.sample(nodos, 2)
        if not G.has_edge(nodo_a, nodo_b):
            G.add_edge(nodo_a, nodo_b)
            if not nx.check_planarity(G)[0]:
                G.remove_edge(nodo_a, nodo_b)
        intentos += 1
        
    grafo = {str(nodo): set(str(neighbor) for neighbor in G.neighbors(nodo)) for nodo in G.nodes()}
    return grafo

# Generar y mostrar grafo
def generar_grafo():
    try:
        num_regiones = int(entrada_regiones.get())
        num_colores = int(entrada_colores.get())
        
        # Validar entradas
        if not entrada_regiones.get() or not entrada_colores.get():
            messagebox.showerror("Error", "Campos vacíos.")
            return
        if not (16 <= num_regiones <= 30):
            messagebox.showerror("Error", "Regiones entre 16 y 30.")
            return
        if num_colores < 1:
            messagebox.showerror("Error", "Al menos 1 color.")
            return
        
        # Generar y colorear grafo
        grafo_generado = generar_grafo_aleatorio(num_regiones)
        print("Grafo generado:", grafo_generado)
        coloreo = colorear_grafo(grafo_generado, num_colores)
        visualizar_grafo(grafo_generado, coloreo, frame_grafo)
    except ValueError as e:
        messagebox.showerror("Error", f"Números válidos. Error: {e}")

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Colorear Regiones - Generación Automática")
ventana.geometry("800x650")

# Frame de entrada
frame_entrada = ttk.Frame(ventana, padding="10")
frame_entrada.pack(fill=tk.X)

# Etiqueta y entrada de regiones
etiqueta_regiones = ttk.Label(frame_entrada, text="Número de Regiones (16-30):")
etiqueta_regiones.pack(side=tk.LEFT)
entrada_regiones = ttk.Combobox(frame_entrada, values=rango_regiones)
entrada_regiones.pack(side=tk.LEFT, padx=(0, 20))
entrada_regiones.set(rango_regiones[0])

# Etiqueta y entrada de colores
etiqueta_colores = ttk.Label(frame_entrada, text="Número de Colores:")
etiqueta_colores.pack(side=tk.LEFT)
entrada_colores = ttk.Combobox(frame_entrada, values=rango_colores)
entrada_colores.pack(side=tk.LEFT)
entrada_colores.set(rango_colores[0])

# Frame para grafo
frame_grafo = ttk.Frame(ventana, padding="10")
frame_grafo.pack(fill=tk.BOTH, expand=True)

# Frame de acciones
frame_acciones = ttk.Frame(ventana, padding="10")
frame_acciones.pack(fill=tk.X)

# Canvas para textos
canvas_textos = tk.Canvas(ventana, height=100)
canvas_textos.place(relx=0.5, rely=0.95, anchor="center", width=800)

# Textos en canvas
textos = [
    ("IA - UMSS", 37, 20),
    ("Callao Lopez William Humberto", 36, 35),
    ("Fernandez Sandoval Camila Wara", 36, 50),
    ("Vilela Montoya Maria Fernanda", 36, 65),
]

# Añadir textos
for texto, x, y in textos:
    canvas_textos.create_text(x, y, anchor="nw", text=texto, fill="#A4A4A4", font=("Inter ExtraLight", 10))

# Botón de generación
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(canvas_textos, image=button_image_1, borderwidth=0, highlightthickness=0, command=generar_grafo, relief="flat")
canvas_textos.create_window(400, 50, window=button_1, width=193, height=38)

# Iniciar ventana
ventana.mainloop()
