import random
import timeit
import sys

from services.ordenamiento import ordenamiento_quick_sort, ordenamiento_insertion_sort
from services.busqueda import busqueda_lineal, busqueda_binaria

# Se establece un límite de recursión más alto para quick_sort.
sys.setrecursionlimit(20000)


def generar_scores_nps(calificaciones_numericas):
    """
    Genera una lista de puntuaciones NPS aleatorias (del 1 al 10).

    Args:
        calificaciones_numericas (int): El número de puntuaciones a generar.

    Returns:
        list: Una lista de puntuaciones NPS.
    """
    return [random.randint(1, 10) for _ in range(calificaciones_numericas)]


def calcular_nps(calificaciones):
    """
    Calcula el número de Detractores, Pasivos, Promotores y el NPS final.

    Args:
        calificaciones (list): Una lista de puntuaciones de clientes.

    Returns:
        dict: Un diccionario con las estadísticas del NPS.
    """
    detractores = 0
    pasivos = 0
    promotores = 0
    total_calificaciones = len(calificaciones)

    for score in calificaciones:
        if 1 <= score <= 6:
            detractores += 1
        elif 7 <= score <= 8:
            pasivos += 1
        elif 9 <= score <= 10:
            promotores += 1

    porcentaje_detractores = (detractores / total_calificaciones) * 100
    porcentaje_pasivos = (pasivos / total_calificaciones) * 100
    porcentaje_promotores = (promotores / total_calificaciones) * 100

    # Fórmula NPS: % Promotores - % Detractores
    calificacion_nps = ((promotores - detractores) / total_calificaciones) * 100

    return {
        "detractores": detractores,
        "porcentaje_detractores": porcentaje_detractores,
        "pasivos": pasivos,
        "porcentaje_pasivos": porcentaje_pasivos,
        "promotores": promotores,
        "porcentaje_promotores": porcentaje_promotores,
        "calificacion_nps": calificacion_nps,
        "total_calificaciones": total_calificaciones
    }


# Función principal que simula escenarios NPS.
# Aplica algoritmos de ordenamiento y búsqueda, y mide su eficiencia.
def main():
    NUM_SCORES = 10000  # Definimos el número de calificaciones para la simulación
    print(f"Simulación escenario NPS con {NUM_SCORES} calificaciones:\n")

    # 1. Generar Datos Iniciales
    # Se genera una lista original de calificaciones aleatorias.
    calificaciones_originales = generar_scores_nps(NUM_SCORES)

    # 2. Calcular Métricas NPS para la Simulación Actual
    resultados_nps = calcular_nps(calificaciones_originales)

    # Imprimir los resultados del NPS
    print(f"Detractores: {resultados_nps['detractores']} ({resultados_nps['porcentaje_detractores']:.2f}%)")
    print(f"Pasivos: {resultados_nps['pasivos']} ({resultados_nps['porcentaje_pasivos']:.2f}%)")
    print(f"Promotores: {resultados_nps['promotores']} ({resultados_nps['porcentaje_promotores']:.2f}%)")
    print(f"\nEl NPS es de: {resultados_nps['calificacion_nps']:.2f}\n")

    print("Eficiencia del simulador (tiempos de ejecución):\n")

    # 3. Medir Tiempos de Ordenamiento

    # Tiempo de Insertion Sort (usamos timeit.timeit para medir eficiencia temporal)
    setup_code_insertion = f"""
from services.ordenamiento import ordenamiento_insertion_sort
data = {calificaciones_originales} # Usamos las calificaciones generadas exactamente
"""
    tiempo_insertion = timeit.timeit("ordenamiento_insertion_sort(data.copy())", setup=setup_code_insertion, number=1)
    print(f"Tiempo de ordenamiento con Insertion Sort: {tiempo_insertion:.6f} segundos")

    # Tiempo de Quick Sort
    setup_code_quick = f"""
from services.ordenamiento import ordenamiento_quick_sort
data = {calificaciones_originales} # Usamos las calificaciones generadas exactamente
"""
    tiempo_quick = timeit.timeit("ordenamiento_quick_sort(data.copy())", setup=setup_code_quick, number=1)
    print(f"Tiempo de ordenamiento con Quick Sort: {tiempo_quick:.6f} segundos")

    # Determinar qué algoritmo de ordenamiento fue mejor
    mejor_ordenamiento = "Insertion Sort" if tiempo_insertion < tiempo_quick else "Quick Sort"
    if tiempo_insertion == tiempo_quick:
        mejor_ordenamiento = "Ambos fueron igual de eficientes"

    # 4. Medir Tiempos de Búsqueda
    # Para la búsqueda binaria, la lista DEBE estar ordenada.
    # Creamos una copia de las calificaciones originales y la ordenamos con quick_sort.
    # Así, busqueda_binaria se prueba en una lista que está en la misma condición
    # que si hubiera sido ordenada por ordenamiento_quick_sort.
    sorted_scores_for_search = calificaciones_originales.copy()
    ordenamiento_quick_sort(sorted_scores_for_search)

    # Elegimos un elemento para buscar que esté presente en la lista original.
    objetivo_busqueda = random.choice(calificaciones_originales)

    # Tiempo de Búsqueda Lineal
    # Se usa 'number=100' para obtener un tiempo más estable
    setup_code_linear_search = f"""
from services.busqueda import busqueda_lineal
data = {calificaciones_originales} # La búsqueda lineal puede usar la lista desordenada
target = {objetivo_busqueda}
"""
    time_linear = timeit.timeit("busqueda_lineal(data, target)", setup=setup_code_linear_search, number=100)
    print(f"Tiempo de búsqueda con Búsqueda Lineal: {time_linear:.6f} segundos")

    # Tiempo de Búsqueda Binaria
    setup_code_binary_search = f"""
from services.busqueda import busqueda_binaria
data = {sorted_scores_for_search} # La búsqueda binaria necesita datos ordenados
target = {objetivo_busqueda}
"""
    time_binary = timeit.timeit("busqueda_binaria(data, target)", setup=setup_code_binary_search, number=100)
    print(f"Tiempo de búsqueda con Búsqueda Binaria: {time_binary:.6f} segundos")

    # Determinar qué algoritmo de búsqueda fue mejor
    mejor_busqueda = "Búsqueda Lineal" if time_linear < time_binary else "Búsqueda Binaria"
    if time_linear == time_binary:
        mejor_busqueda = "Ambos fueron igual de eficientes"

    # 5. Conclusiones de Eficiencia
    print("\nConclusiones de la eficiencia de esta simulación:")
    print(f"El algoritmo de ordenamiento más eficiente fue: {mejor_ordenamiento}")
    print(f"El algoritmo de búsqueda más eficiente fue: {mejor_busqueda}")


if __name__ == "__main__":
    main()
