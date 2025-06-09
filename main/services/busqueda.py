def busqueda_lineal(arr, objetivo):
    """
    Busca un valor objetivo en una lista utilizando el algoritmo de Búsqueda Lineal.

    Args:
        arr (lista): La lista en la que buscar.
        objetivo: El valor a buscar.

    Returns:
        int: El índice del objetivo si se encuentra, de lo contrario -1.
    """
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


def busqueda_binaria(arr, objetivo):
    """
    Busca un valor objetivo en una lista ORDENADA utilizando el algoritmo de Búsqueda Binaria.

    Args:
        arr (lista): La lista ORDENADA en la que buscar.
        objetivo: El valor a buscar.

    Returns:
        int: El índice del objetivo si se encuentra, de lo contrario -1.
    """
    min = 0
    max = len(arr) - 1
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            min = mid + 1
        else:
            max = mid - 1
    return -1
