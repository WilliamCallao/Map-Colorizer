
# Map Colorizer con Algoritmo Voraz

Este proyecto es una herramienta para colorear mapas de 16 a 30 regiones, asegurando que regiones adyacentes no compartan el mismo color. Utiliza un algoritmo voraz para asignar colores de manera eficiente.

## Descripción del Proyecto

El objetivo es asignar un color a cada región del mapa de manera que regiones adyacentes no compartan el mismo color. El número de regiones y colores son parámetros ingresados por el usuario.

## Tecnologías Utilizadas

- **Python:** Lenguaje de programación principal.
- **Tkinter y Ttk:** Para la interfaz gráfica de usuario (GUI).
- **NetworkX:** Para la visualización y manipulación de grafos.
- **Matplotlib:** Para la representación gráfica de los grafos y su coloreo.

## Capturas de Pantalla

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
  <img src="https://github.com/tu-usuario/map-colorizer/assets/image1.png" alt="Interfaz del Proyecto" width="45%" />
  <img src="https://github.com/tu-usuario/map-colorizer/assets/image2.png" alt="Grafo Generado" width="45%" />
</div>

## Cómo Ejecutar el Proyecto

### Requisitos

- Python 3.10 o superior.

### Instrucciones

1. Clona este repositorio:
    ```
    git clone https://github.com/WilliamCallao/Map-Colorizer.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd Map-Colorizer
    ```

3. (Opcional) Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Ejecuta el proyecto:
    ```bash
    python main.py
    ```
