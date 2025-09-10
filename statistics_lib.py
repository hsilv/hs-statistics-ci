"""
Librería de Estadísticas

Una librería completa para cálculos estadísticos básicos que incluye:
- media (promedio)
- mediana (valor central)
- moda (valor más frecuente)
- varianza (dispersión)
- ds (desviación estándar)
"""

import math
from collections import Counter
from typing import List, Union


class ErrorEstadisticas(Exception):
    """Excepción personalizada para errores relacionados con estadísticas"""
    pass


def media(numeros: List[Union[int, float]]) -> float:
    """
    Calcula la media aritmética de una lista de números.
    
    Args:
        numeros: Lista de números (int o float)
        
    Returns:
        float: La media aritmética
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía o contiene valores no numéricos
    """
    if not numeros:
        raise ErrorEstadisticas("No se puede calcular la media de una lista vacía")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise ErrorEstadisticas("Todos los valores deben ser numéricos")
    
    return sum(numeros) / len(numeros)


def mediana(numeros: List[Union[int, float]]) -> float:
    """
    Calcula la mediana de una lista de números.
    
    Args:
        numeros: Lista de números (int o float)
        
    Returns:
        float: El valor de la mediana
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía o contiene valores no numéricos
    """
    if not numeros:
        raise ErrorEstadisticas("No se puede calcular la mediana de una lista vacía")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise ErrorEstadisticas("Todos los valores deben ser numéricos")
    
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    
    if n % 2 == 0:
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        return (medio1 + medio2) / 2
    else:
        return numeros_ordenados[n // 2]


def moda(numeros: List[Union[int, float]]) -> Union[int, float]:
    """
    Calcula la moda de una lista de números.
    
    Args:
        numeros: Lista de números (int o float)
        
    Returns:
        El valor más frecuente. Si múltiples valores tienen la misma frecuencia,
        retorna el primero encontrado.
        
    Raises:
        ErrorEstadisticas: Si la lista está vacía o contiene valores no numéricos
    """
    if not numeros:
        raise ErrorEstadisticas("No se puede calcular la moda de una lista vacía")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise ErrorEstadisticas("Todos los valores deben ser numéricos")
    
    contador = Counter(numeros)
    frecuencia_maxima = max(contador.values())
    
    for valor in numeros:
        if contador[valor] == frecuencia_maxima:
            return valor


def varianza(numeros: List[Union[int, float]], poblacion: bool = True) -> float:
    """
    Calcula la varianza de una lista de números.
    
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
    if not numeros:
        raise ErrorEstadisticas("No se puede calcular la varianza de una lista vacía")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise ErrorEstadisticas("Todos los valores deben ser numéricos")
    
    if not poblacion and len(numeros) < 2:
        raise ErrorEstadisticas("La varianza muestral requiere al menos 2 valores")
    
    media_val = media(numeros)
    diferencias_cuadradas = [(x - media_val) ** 2 for x in numeros]
    
    if poblacion:
        return sum(diferencias_cuadradas) / len(numeros)
    else:
        return sum(diferencias_cuadradas) / (len(numeros) - 1)


def ds(numeros: List[Union[int, float]], poblacion: bool = True) -> float:
    """
    Calcula la desviación estándar de una lista de números.
    
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
    if not numeros:
        raise ErrorEstadisticas("No se puede calcular la desviación estándar de una lista vacía")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise ErrorEstadisticas("Todos los valores deben ser numéricos")
    
    if not poblacion and len(numeros) < 2:
        raise ErrorEstadisticas("La desviación estándar muestral requiere al menos 2 valores")
    
    return math.sqrt(varianza(numeros, poblacion))
