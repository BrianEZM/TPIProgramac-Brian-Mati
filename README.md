Trabajo Practico Integrador Programacion1: Algoritmos de Búsqueda y Ordenamiento para Análisis NPS

Link repositorio digital con la entrega: https://drive.google.com/drive/folders/1QyjdXYiwPJ4p0FjCA29J1P0A_ipCzxnn

Descripción del Proyecto:
* Este proyecto es un trabajo práctico integrador de Programación I que explora y compara la eficiencia de algoritmos fundamentales de búsqueda y ordenamiento. El caso práctico se centra en una simulación de Net Promoter Score (NPS), donde se generan 10.000 calificaciones de clientes aleatorias (del 1 al 10) para analizar su distribución (Detractores, Pasivos, Promotores) y calcular el NPS.

El objetivo principal es demostrar cómo la elección de algoritmos de ordenamiento (Insertion Sort y Quick Sort) y búsqueda (Lineal y Binaria) impacta directamente en el rendimiento al procesar grandes volúmenes de datos, utilizando el módulo timeit de Python para medir su eficiencia.

Tecnologías Utilizadas:
* Python 3.x
* Módulos estándar de Python: random, timeit, sys.

Cómo Ejecutar el Proyecto:
* Clona el repositorio: git clone https://github.com/BrianEZM/TPIProgramac-Brian-Mati
* Ejecuta el programa principal: Desde la raíz del proyecto, ejecuta main.py.

Estructura del Proyecto: El proyecto está dividido en tres módulos principales para una clara separación de responsabilidades:
* main.py: Es el punto de entrada del programa.
** Se encarga de la generación de datos (calificaciones NPS).
** Calcula el NPS y sus métricas (detractores, pasivos, promotores).
** Orquesta las llamadas a los algoritmos de ordenamiento y búsqueda.
** Mide los tiempos de ejecución de cada algoritmo utilizando timeit.
** Imprime los resultados y las conclusiones de eficiencia en la consola.

* services/ordenamiento.py: Contiene las implementaciones de los algoritmos de ordenamiento:
** ordenamiento_insertion_sort(arr)
** ordenamiento_quick_sort(arr)

* services/busqueda.py: Contiene las implementaciones de los algoritmos de búsqueda:
** busqueda_lineal(arr, objetivo)
** busqueda_binaria(arr, objetivo)

✍️ Autores:
Brian Zapata Marin + Matias Almeida / Estudiantes de Programación I Tecnicatura UTN 2025

¡Gracias!
