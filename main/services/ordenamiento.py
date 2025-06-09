import sys

# Se establece un límite de recursión más alto para quick_sort.
sys.setrecursionlimit(20000)


def ordenamiento_insertion_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de Insertion Sort.

    Args:
        arr (lista): La lista de números a ordenar.

    Returns:
        lista: La lista ordenada.
    """
    n = len(arr)
    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        # Mueve los elementos de arr[0..i-1] que son mayores que 'clave'
        # una posición adelante de su posición actual.
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr


def ordenamiento_quick_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de Quick Sort.

    Args:
        arr (list): La lista de números a ordenar.

    Returns:
        list: La lista ordenada.
    """

    # Función auxiliar recursiva para Quick Sort
    def _quick_sort_recursive(arr, min, max):
        if min < max:
            # pi es el índice de partición, arr[pi] está ahora en el lugar correcto
            pi = _partition(arr, min, max)
            # Ordena recursivamente los elementos antes de la partición y después de la partición
            _quick_sort_recursive(arr, min, pi - 1)
            _quick_sort_recursive(arr, pi + 1, max)

    def _partition(arr, min, max):
        # Elegimos el último elemento como pivote
        pivot = arr[max]
        i = (min - 1)  # Índice del elemento más pequeño

        for j in range(min, max):
            # Si el elemento actual es más pequeño o igual que el pivote
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[max] = arr[max], arr[i + 1]
        return i + 1

    # Inicia el proceso de Quick Sort
    _quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr  # Retorna la lista modificada (ordenada)
