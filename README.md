Modelo Integrador: Algoritmos de Búsqueda y Ordenamiento para Análisis NPS

✍️ Autores
Brian Zapata Marin - Alumno UTN
Matias Almeida - Alumno UTN

📝 Descripción del Proyecto
Este proyecto es un trabajo práctico integrador de Programación I que explora y compara la eficiencia de algoritmos fundamentales de búsqueda y ordenamiento. El caso práctico se centra en una simulación de Net Promoter Score (NPS), donde se generan 10.000 calificaciones de clientes aleatorias (del 1 al 10) para analizar su distribución (Detractores, Pasivos, Promotores) y calcular el NPS.

El objetivo principal es demostrar cómo la elección de algoritmos de ordenamiento (Insertion Sort y Quick Sort) y búsqueda (Lineal y Binaria) impacta directamente en el rendimiento al procesar grandes volúmenes de datos, utilizando el módulo timeit de Python para medir su eficiencia.

✨ Características
Simulación de NPS: Genera 10.000 calificaciones de clientes aleatorias y calcula el Net Promoter Score.

Clasificación de Clientes: Identifica y cuantifica Detractores (1-6), Pasivos (7-8) y Promotores (9-10).

Algoritmos de Ordenamiento Implementados:

Insertion Sort: Para entender el rendimiento en casos de O(n2).
Quick Sort: Un algoritmo eficiente de "divide y vencerás" (O(nlogn)).

Algoritmos de Búsqueda Implementados:

Búsqueda Lineal: Una búsqueda secuencial simple (O(n)).
Búsqueda Binaria: Una búsqueda logarítmica eficiente para listas ordenadas (O(logn)).

Medición de Eficiencia: Utiliza el módulo timeit para comparar los tiempos de ejecución de cada algoritmo.
Análisis de Rendimiento: Presenta conclusiones sobre qué algoritmo de ordenamiento y búsqueda es más eficiente en el contexto de la simulación.
Generación de Gráficos Comparativos: Capacidad de generar dos gráficos separados (uno para ordenamiento y otro para búsqueda) para una visualización clara del rendimiento.

Diseño Modular: El código está organizado en módulos separados (main, ordenamiento, busqueda) para una mejor estructura y mantenibilidad.

🛠️ Tecnologías Utilizadas
Python 3.x
Módulos estándar de Python: random, timeit, sys, json.
Librerías externas: matplotlib (para la generación de gráficos).
Para instalar matplotlib: pip install matplotlib

🚀 Cómo Ejecutar el Proyecto
Clona el repositorio e instala dependencias con pip install

Ejecuta el programa principal:
Desde la raíz del proyecto, ejecuta main.py. Esto realizará la simulación y guardará los resultados de rendimiento en resultados_de_performance.json.
python main.py

📊 Generación de Gráficos de Rendimiento
Después de ejecutar main.py (lo cual generará el archivo resultados_de_performance.json), puedes generar los gráficos visuales de la comparación de rendimiento:

Ejecuta el script de gráfico:
python generar_grafico.py
Esto creará dos archivos de imagen: ordenamiento_performance_grafico.png y busqueda_performance_grafico.png en el mismo directorio.

📂 Estructura del Proyecto
El proyecto está dividido en módulos para una clara separación de responsabilidades:

main.py:
Es el punto de entrada del programa.
Se encarga de la generación de datos (calificaciones NPS).
Calcula el NPS y sus métricas (detractores, pasivos, promotores).
Orquesta las llamadas a los algoritmos de ordenamiento y búsqueda.
Mide los tiempos de ejecución de cada algoritmo utilizando timeit.
Imprime los resultados y las conclusiones de eficiencia en la consola.
Guarda los tiempos de ejecución en performance_results.json.

generar_grafico.py:
Lee los tiempos de ejecución desde performance_results.json.
Utiliza matplotlib para crear y guardar dos gráficos de barras comparativos: sorting_performance_chart.png y search_performance_chart.png.

services/ordenamiento.py:
Contiene las implementaciones de los algoritmos de ordenamiento:
ordenamiento_insertion_sort(arr)
ordenamiento_quick_sort(arr)

services/busqueda.py:
Contiene las implementaciones de los algoritmos de búsqueda:
busqueda_lineal(arr, objetivo)
busqueda_binaria(arr, objetivo)

Consideraciones Adicionales:
- Ordenamiento: Para grandes volúmenes de datos (como 10,000 elementos), Quick Sort suele ser
significativamente más rápido que Insertion Sort debido a su complejidad de tiempo promedio
($O(n \log n)$) versus ($O(n^2)$) para Insertion Sort.
- Búsqueda: La Búsqueda Binaria ($O(\log n)$) es drásticamente más eficiente que la Búsqueda Lineal
($O(n)$) en listas grandes y ordenadas. Sin embargo, la Búsqueda Binaria requiere que la lista esté previamente
ordenada, lo cual implica un costo adicional de ordenamiento. Como se observa en algunas ejecuciones,
para rangos de valores pequeños y distribuciones específicas (1-10), la búsqueda lineal puede
resultar marginalmente más rápida que la binaria debido a la sobrecarga de comparaciones y cálculos
de punto medio en la binaria, y a la eficiencia del hardware con patrones de acceso lineal.
-> Esta simulación muestra cómo la elección del algoritmo correcto puede impactar drásticamente el
rendimiento de una aplicación, especialmente con grandes conjuntos de datos.
(Nota: Los números exactos de detractores, pasivos, promotores, NPS y tiempos de ejecución variarán en cada ejecución debido a la generación aleatoria de datos.)

📊 Gráficos de Rendimiento
Aquí puedes ver ejemplos de los gráficos de rendimiento generados por el script generar_grafico.py:
Rendimiento de Algoritmos de Ordenamiento
Rendimiento de Algoritmos de Búsqueda

📈 Conclusiones Clave
Quick Sort es generalmente superior a Insertion Sort para ordenar grandes conjuntos de datos desordenados, gracias a su eficiencia logarítmica.
La Búsqueda Binaria es drásticamente más rápida que la Búsqueda Lineal en listas grandes y ordenadas. No obstante, es importante notar que para conjuntos de datos con un rango muy limitado de valores (como del 1 al 10) y ciertas distribuciones, o debido a la sobrecarga inherente de la recursión y las divisiones, la Búsqueda Lineal puede, en algunos casos específicos, mostrar un rendimiento marginalmente superior en entornos de ejecución real. Esto subraya la importancia de la prueba empírica junto con el análisis teórico de complejidad.
Este proyecto ilustra cómo la correcta selección de algoritmos, junto con la consideración de las características específicas de los datos, es crucial para el rendimiento y la escalabilidad de las aplicaciones.

✍️ Autores
Brian Zapata Marin - Alumno UTN
Matias Almeida - Alumno UTN
