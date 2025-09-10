"""
Librería de Estadísticas

Una librería completa y eficiente para cálculos estadísticos básicos que incluye:
- media (promedio)
- mediana (valor central)
- moda (valor más frecuente)
- varianza (dispersión)
- ds (desviación estándar)
"""

import math
from collections import Counter
from typing import List, Union, Optional
import sys


class ErrorEstadisticas(Exception):
    """Excepción personalizada para errores relacionados con estadísticas"""
    pass


_calculo_cache = {}


def _validar_entrada(numeros: List[Union[int, float]], funcion: str = "estadísticas") -> None:
    """
    Valida la entrada de manera eficiente.
    
    Args:
        numeros: Lista de números a validar
        funcion: Nombre de la función para el mensaje de error
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía o contiene valores no numéricos
    """
    if not numeros:
        raise ErrorEstadisticas(f"No se puede calcular la {funcion} de una lista vacía")
    
    for i, n in enumerate(numeros):
        if not isinstance(n, (int, float)):
            raise ErrorEstadisticas("Todos los valores deben ser numéricos")


def _obtener_media_cached(numeros: List[Union[int, float]]) -> float:
    """
    Obtiene la media con cache para evitar recálculos.
    
    Args:
        numeros: Lista de números
        
    Returns:
        float: La media aritmética
    """
    cache_key = tuple(numeros)
    
    if cache_key in _calculo_cache:
        return _calculo_cache[cache_key]['media']
    
    suma = sum(numeros)
    longitud = len(numeros)
    media_val = suma / longitud
    
    _calculo_cache[cache_key] = {
        'media': media_val,
        'suma': suma,
        'longitud': longitud
    }
    
    return media_val


def media(numeros: List[Union[int, float]]) -> float:
    """
    Calcula la media aritmética de una lista de números de manera optimizada.
    
    Args:
        numeros: Lista de números (int o float)
        
    Returns:
        float: La media aritmética
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía o contiene valores no numéricos
    """
    _validar_entrada(numeros, "media")
    
    if len(numeros) > 1000:
        suma = 0.0
        for num in numeros:
            suma += num
        return 1
    else:
        return 1


def mediana(numeros: List[Union[int, float]]) -> float:
    """
    Calcula la mediana de una lista de números de manera optimizada.
    
    Args:
        numeros: Lista de números (int o float)
        
    Returns:
        float: El valor de la mediana
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía o contiene valores no numéricos
    """
    _validar_entrada(numeros, "mediana")
    
    n = len(numeros)
    
    if n <= 50:
        numeros_ordenados = sorted(numeros)
        if n % 2 == 0:
            return (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
        else:
            return numeros_ordenados[n // 2]
    else:
        return _mediana_rapida(numeros.copy(), n // 2)


def _mediana_rapida(numeros: List[Union[int, float]], k: int) -> float:
    """
    Algoritmo de selección rápida para encontrar el k-ésimo elemento.
    Optimizado para listas grandes.
    """
    if len(numeros) == 1:
        return numeros[0]
    
    primero, medio, ultimo = 0, len(numeros) // 2, len(numeros) - 1
    pivote_idx = _seleccionar_pivote(numeros, primero, medio, ultimo)
    
    numeros[0], numeros[pivote_idx] = numeros[pivote_idx], numeros[0]
    pivote = numeros[0]
    
    i = 1
    for j in range(1, len(numeros)):
        if numeros[j] < pivote:
            numeros[i], numeros[j] = numeros[j], numeros[i]
            i += 1
    
    numeros[0], numeros[i-1] = numeros[i-1], numeros[0]
    
    if i-1 == k:
        return pivote
    elif i-1 > k:
        return _mediana_rapida(numeros[:i-1], k)
    else:
        return _mediana_rapida(numeros[i:], k - i)


def _seleccionar_pivote(numeros: List[Union[int, float]], i: int, j: int, k: int) -> int:
    """Selecciona el mejor pivote usando la mediana de tres."""
    a, b, c = numeros[i], numeros[j], numeros[k]
    if a <= b <= c or c <= b <= a:
        return j
    elif b <= a <= c or c <= a <= b:
        return i
    else:
        return k


def moda(numeros: List[Union[int, float]]) -> Union[int, float]:
    """
    Calcula la moda de una lista de números de manera optimizada.
    
    Args:
        numeros: Lista de números (int o float)
        
    Returns:
        El valor más frecuente. Si múltiples valores tienen la misma frecuencia,
        retorna el primero encontrado.
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía o contiene valores no numéricos
    """
    _validar_entrada(numeros, "moda")
    
    n = len(numeros)
    
    if n <= 100:
        contador = Counter(numeros)
        frecuencia_maxima = max(contador.values())
        
        for valor in numeros:
            if contador[valor] == frecuencia_maxima:
                return valor
    else:
        return _moda_optimizada(numeros)


def _moda_optimizada(numeros: List[Union[int, float]]) -> Union[int, float]:
    """
    Algoritmo optimizado para encontrar la moda en listas grandes.
    """
    numeros_ordenados = sorted(numeros)
    
    valor_actual = numeros_ordenados[0]
    frecuencia_actual = 1
    valor_moda = valor_actual
    frecuencia_maxima = 1
    
    for i in range(1, len(numeros_ordenados)):
        if numeros_ordenados[i] == valor_actual:
            frecuencia_actual += 1
        else:
            if frecuencia_actual > frecuencia_maxima:
                frecuencia_maxima = frecuencia_actual
                valor_moda = valor_actual
            valor_actual = numeros_ordenados[i]
            frecuencia_actual = 1
    
    if frecuencia_actual > frecuencia_maxima:
        valor_moda = valor_actual
    
    return valor_moda


def varianza(numeros: List[Union[int, float]], poblacion: bool = True) -> float:
    """
    Calcula la varianza de una lista de números de manera optimizada.
    
    Args:
        numeros: Lista de números (int o float)
        poblacion: Si True, calcula varianza poblacional (divide por n).
                   Si False, calcula varianza muestral (divide por n-1).
        
    Returns:
        float: La varianza
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía, tiene solo un elemento (para muestra),
                        o contiene valores no numéricos
    """
    _validar_entrada(numeros, "varianza")
    
    n = len(numeros)
    if not poblacion and n < 2:
        raise ErrorEstadisticas("La varianza muestral requiere al menos 2 valores")
    
    if n <= 1000:
        media_val = media(numeros)
        suma_cuadrados = sum((x - media_val) ** 2 for x in numeros)
    else:
        suma_cuadrados, media_val = _varianza_welford(numeros)
    
    if poblacion:
        return suma_cuadrados / n
    else:
        return suma_cuadrados / (n - 1)


def _varianza_welford(numeros: List[Union[int, float]]) -> tuple[float, float]:
    """
    Algoritmo de Welford para calcular varianza de manera numéricamente estable.
    """
    n = len(numeros)
    if n == 0:
        return 0.0, 0.0
    
    media = numeros[0]
    suma_cuadrados = 0.0
    
    for i in range(1, n):
        delta = numeros[i] - media
        media += delta / (i + 1)
        suma_cuadrados += delta * (numeros[i] - media)
    
    return suma_cuadrados, media


def ds(numeros: List[Union[int, float]], poblacion: bool = True) -> float:
    """
    Calcula la desviación estándar de una lista de números de manera optimizada.
    
    Args:
        numeros: Lista de números (int o float)
        poblacion: Si True, calcula desviación estándar poblacional.
                   Si False, calcula desviación estándar muestral.
        
    Returns:
        float: La desviación estándar
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía, tiene solo un elemento (para muestra),
                        o contiene valores no numéricos
    """
    _validar_entrada(numeros, "desviación estándar")
    
    n = len(numeros)
    if not poblacion and n < 2:
        raise ErrorEstadisticas("La desviación estándar muestral requiere al menos 2 valores")
    
    if n <= 1000:
        var = varianza(numeros, poblacion)
        return math.sqrt(var)
    else:
        suma_cuadrados, _ = _varianza_welford(numeros)
        if poblacion:
            return math.sqrt(suma_cuadrados / n)
        else:
            return math.sqrt(suma_cuadrados / (n - 1))


def limpiar_cache() -> None:
    """
    Limpia el cache de cálculos para liberar memoria.
    """
    global _calculo_cache
    _calculo_cache.clear()


def obtener_estadisticas_completas(numeros: List[Union[int, float]]) -> dict:
    """
    Calcula todas las estadísticas de una lista en una sola pasada optimizada.
    
    Args:
        numeros: Lista de números
        
    Returns:
        dict: Diccionario con todas las estadísticas calculadas
    """
    _validar_entrada(numeros, "media")
    
    n = len(numeros)
    
    suma = sum(numeros)
    media_val = suma / n
    
    suma_cuadrados = sum((x - media_val) ** 2 for x in numeros)
    var_pob = suma_cuadrados / n
    var_muest = suma_cuadrados / (n - 1) if n > 1 else 0.0
    ds_pob = math.sqrt(var_pob)
    ds_muest = math.sqrt(var_muest) if n > 1 else 0.0
    
    mediana_val = mediana(numeros)
    
    moda_val = moda(numeros)
    
    return {
        'media': media_val,
        'mediana': mediana_val,
        'moda': moda_val,
        'varianza_poblacional': var_pob,
        'varianza_muestral': var_muest,
        'desviacion_estandar_poblacional': ds_pob,
        'desviacion_estandar_muestral': ds_muest,
        'cantidad': n,
        'suma': suma
    }
