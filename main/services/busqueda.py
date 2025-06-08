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
            return i  # Retorna el índice si se encuentra
    return -1  # Retorna -1 si no se encuentra


def busqueda_binaria(arr, objetivo):
    """
    Busca un valor objetivo en una lista ORDENADA utilizando el algoritmo de Búsqueda Binaria.

    Args:
        arr (lista): La lista ORDENADA en la que buscar.
        objetivo: El valor a buscar.

    Returns:
        int: El índice del objetivo si se encuentra, de lo contrario -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            low = mid + 1
        else:
            high = mid - 1
    return -1
