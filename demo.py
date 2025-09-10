"""
Script de demostración para la librería de estadísticas.

Este script muestra cómo usar todas las funciones de la librería de estadísticas
con varios ejemplos.
"""

from statistics_lib import media, mediana, moda, varianza, ds, ErrorEstadisticas


def main():
    """Demuestra las funciones de la librería de estadísticas"""
    
    print("=== Demostración de la Librería de Estadísticas ===\n")
    
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Conjunto de datos: {numeros}")
    print()
    
    try:
        media_val = media(numeros)
        mediana_val = mediana(numeros)
        moda_val = moda(numeros)
        var_pob = varianza(numeros, poblacion=True)
        var_muest = varianza(numeros, poblacion=False)
        ds_pob = ds(numeros, poblacion=True)
        ds_muest = ds(numeros, poblacion=False)
        
        print("Resultados:")
        print(f"  Media: {media_val}")
        print(f"  Mediana: {mediana_val}")
        print(f"  Moda: {moda_val}")
        print(f"  Varianza (Población): {var_pob:.4f}")
        print(f"  Varianza (Muestra): {var_muest:.4f}")
        print(f"  Desviación Estándar (Población): {ds_pob:.4f}")
        print(f"  Desviación Estándar (Muestra): {ds_muest:.4f}")
        
    except ErrorEstadisticas as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50)
    
    numeros_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5]
    print(f"\nConjunto de datos con duplicados: {numeros_con_duplicados}")
    
    try:
        media_val = media(numeros_con_duplicados)
        mediana_val = mediana(numeros_con_duplicados)
        moda_val = moda(numeros_con_duplicados)
        
        print("Resultados:")
        print(f"  Media: {media_val}")
        print(f"  Mediana: {mediana_val}")
        print(f"  Moda: {moda_val}")
        
    except ErrorEstadisticas as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50)
    
    numeros_flotantes = [1.5, 2.5, 3.5, 4.5, 5.5]
    print(f"\nConjunto de datos flotantes: {numeros_flotantes}")
    
    try:
        media_val = media(numeros_flotantes)
        mediana_val = mediana(numeros_flotantes)
        moda_val = moda(numeros_flotantes)
        var_val = varianza(numeros_flotantes)
        ds_val = ds(numeros_flotantes)
        
        print("Resultados:")
        print(f"  Media: {media_val}")
        print(f"  Mediana: {mediana_val}")
        print(f"  Moda: {moda_val}")
        print(f"  Varianza: {var_val:.4f}")
        print(f"  Desviación Estándar: {ds_val:.4f}")
        
    except ErrorEstadisticas as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50)
    
    print("\nEjemplos de manejo de errores:")
    
    try:
        resultado = media([])
    except ErrorEstadisticas as e:
        print(f"  Error de lista vacía: {e}")
    
    try:
        resultado = media([1, 2, "tres", 4])
    except ErrorEstadisticas as e:
        print(f"  Error de valores no numéricos: {e}")
    
    try:
        resultado = varianza([42], poblacion=False)
    except ErrorEstadisticas as e:
        print(f"  Error de varianza muestral con elemento único: {e}")


if __name__ == "__main__":
    main()
