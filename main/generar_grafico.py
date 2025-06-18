import json
import matplotlib.pyplot as plt
import numpy as np


def _plot_algoritmos(ax, algoritmos, tiempos, title, ylabel, xlabel, colors, note=None):
    """
    Función auxiliar para generar un gráfico de barras.

    Args:
        ax (matplotlib.axes.Axes): El objeto Axes donde se dibujará el gráfico.
        algoritmos (list): Nombres de los algoritmos.
        tiempos (list): Tiempos de ejecución correspondientes.
        title (str): Título del gráfico.
        ylabel (str): Etiqueta del eje Y.
        xlabel (str): Etiqueta del eje X.
        colors (list): Colores para las barras.
        note (str, optional): Una nota adicional para mostrar en el gráfico.
    """
    bars = ax.bar(algoritmos, tiempos, color=colors)

    ax.set_title(title, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.tick_params(axis='x', rotation=20)

    for bar in bars:
        yval = bar.get_height()
        text_y_pos = yval if yval > 0.000001 else 0.000001
        ax.text(bar.get_x() + bar.get_width() / 2, text_y_pos + (ax.get_ylim()[1] * 0.02),
                f'{yval:.6f}s', ha='center', va='bottom', fontsize=9)

    ax.grid(axis='y', linestyle='--', alpha=0.7)

    if note:
        plt.figtext(0.5, 0.01, note, wrap=True, horizontalalignment='center', fontsize=9, color='gray')


def generar_grafico_rendimiento(file_path="resultados_de_performance.json"):
    """
    Genera dos gráficos de barras separados, uno para algoritmos de ordenamiento
    y otro para algoritmos de búsqueda, y los guarda como imágenes PNG.

    Args:
        file_path (str): Ruta al archivo JSON con los resultados de rendimiento.
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'. Asegúrate de ejecutar main.py primero.")
        return
    except json.JSONDecodeError:
        print(f"Error: El archivo '{file_path}' no es un JSON válido.")
        return
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return

    # Separar los datos en ordenamiento y búsqueda
    sorting_data = {k: v for k, v in data.items() if "Sort" in k}
    search_data = {k: v for k, v in data.items() if "Busqueda" in k}

    # Gráfico de Ordenamiento
    fig_sort, ax_sort = plt.subplots(figsize=(10, 6))
    algoritmos_sort = list(sorting_data.keys())
    tiempos_sort = list(sorting_data.values())
    _plot_algoritmos(ax_sort, algoritmos_sort, tiempos_sort,
                     'Comparación de Rendimiento de Algoritmos de Ordenamiento',
                     'Tiempo (segundos)', 'Algoritmo',
                     ['skyblue', 'lightcoral'])
    plt.tight_layout()
    sorting_output_image_name = "ordenamiento_performance_grafico.png"
    try:
        fig_sort.savefig(sorting_output_image_name)
        print(f"\nGráfico de ordenamiento guardado exitosamente como '{sorting_output_image_name}'")
    except Exception as e:
        print(f"Error al guardar el gráfico de ordenamiento: {e}")
    plt.close(fig_sort)

    # Gráfico de Búsqueda
    fig_search, ax_search = plt.subplots(figsize=(10, 6))
    algoritmos_search = list(search_data.keys())
    tiempos_search = list(search_data.values())

    max_search_time = max(tiempos_search) if tiempos_search else 0.0001
    ax_search.set_ylim(bottom=0, top=max_search_time * 1.5)

    note_search = ("Nota: Para un rango pequeño de valores (1-10) y gran cantidad de datos, "
                   "la búsqueda lineal puede ser marginalmente más rápida que la binaria "
                   "debido a la sobrecarga de la binaria y la optimización de caché, "
                   "así como al acceso más predecible en memoria para la búsqueda lineal.")

    _plot_algoritmos(ax_search, algoritmos_search, tiempos_search,
                     'Comparación de Rendimiento de Algoritmos de Búsqueda',
                     'Tiempo (segundos)', 'Algoritmo',
                     ['lightgreen', 'gold'], note=note_search)
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # Ajustar diseño para que la nota no se superponga

    search_output_image_name = "busqueda_performance_grafico.png"
    try:
        fig_search.savefig(search_output_image_name)
        print(f"\nGráfico de búsqueda guardado exitosamente como '{search_output_image_name}'")
    except Exception as e:
        print(f"Error al guardar el gráfico de búsqueda: {e}")
    plt.close(fig_search)

    print("\nProceso de generación de gráficos completado. Se han creado dos archivos PNG.")


if __name__ == "__main__":
    generar_grafico_rendimiento()
