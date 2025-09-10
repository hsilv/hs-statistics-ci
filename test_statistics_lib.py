"""
Pruebas unitarias para la librería de estadísticas.

Las pruebas cubren:
1. Al menos 2 variaciones de casos exitosos por función
2. Casos límite y manejo de errores
3. Verificación de que las pruebas fallan cuando las funciones no funcionan correctamente
"""

import unittest
import math
from statistics_lib import (
    media, mediana, moda, varianza, ds, ErrorEstadisticas
)


class TestMedia(unittest.TestCase):
    """Casos de prueba para la función media (promedio)"""
    
    def test_media_camino_feliz_enteros(self):
        """Prueba cálculo de media con enteros - camino feliz 1"""
        numeros = [1, 2, 3, 4, 5]
        resultado = media(numeros)
        self.assertEqual(resultado, 3.0)
    
    def test_media_camino_feliz_floats(self):
        """Prueba cálculo de media con flotantes - camino feliz 2"""
        numeros = [1.5, 2.5, 3.5, 4.5]
        resultado = media(numeros)
        self.assertEqual(resultado, 3.0)
    
    def test_media_camino_feliz_tipos_mixtos(self):
        """Prueba cálculo de media con tipos mixtos int/float - camino feliz 3"""
        numeros = [1, 2.5, 3, 4.5, 5]
        resultado = media(numeros)
        self.assertEqual(resultado, 3.2)
    
    def test_media_caso_limite_elemento_unico(self):
        """Prueba media con elemento único"""
        numeros = [42]
        resultado = media(numeros)
        self.assertEqual(resultado, 42.0)
    
    def test_media_caso_limite_numeros_negativos(self):
        """Prueba media con números negativos"""
        numeros = [-1, -2, -3, -4, -5]
        resultado = media(numeros)
        self.assertEqual(resultado, -3.0)
    
    def test_media_error_lista_vacia(self):
        """Prueba que lista vacía lance ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            media([])
        self.assertEqual(str(contexto.exception), "No se puede calcular la media de una lista vacía")
    
    def test_media_error_no_numerico(self):
        """Prueba que valores no numéricos lancen ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            media([1, 2, "tres", 4])
        self.assertEqual(str(contexto.exception), "Todos los valores deben ser numéricos")


class TestMediana(unittest.TestCase):
    """Casos de prueba para la función mediana"""
    
    def test_mediana_camino_feliz_conteo_impar(self):
        """Prueba mediana con número impar de elementos - camino feliz 1"""
        numeros = [1, 3, 5, 7, 9]
        resultado = mediana(numeros)
        self.assertEqual(resultado, 5)
    
    def test_mediana_camino_feliz_conteo_par(self):
        """Prueba mediana con número par de elementos - camino feliz 2"""
        numeros = [1, 2, 3, 4, 5, 6]
        resultado = mediana(numeros)
        self.assertEqual(resultado, 3.5)
    
    def test_mediana_camino_feliz_no_ordenados(self):
        """Prueba mediana con números no ordenados - camino feliz 3"""
        numeros = [5, 1, 3, 2, 4]
        resultado = mediana(numeros)
        self.assertEqual(resultado, 3)
    
    def test_mediana_caso_limite_elemento_unico(self):
        """Prueba mediana con elemento único"""
        numeros = [42]
        resultado = mediana(numeros)
        self.assertEqual(resultado, 42)
    
    def test_mediana_caso_limite_duplicados(self):
        """Prueba mediana con valores duplicados"""
        numeros = [1, 1, 2, 2, 2, 3, 3]
        resultado = mediana(numeros)
        self.assertEqual(resultado, 2)
    
    def test_mediana_error_lista_vacia(self):
        """Prueba que lista vacía lance ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            mediana([])
        self.assertEqual(str(contexto.exception), "No se puede calcular la mediana de una lista vacía")
    
    def test_mediana_error_no_numerico(self):
        """Prueba que valores no numéricos lancen ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            mediana([1, 2, "tres", 4])
        self.assertEqual(str(contexto.exception), "Todos los valores deben ser numéricos")


class TestModa(unittest.TestCase):
    """Casos de prueba para la función moda"""
    
    def test_moda_camino_feliz_moda_clara(self):
        """Prueba moda con valor más frecuente claro - camino feliz 1"""
        numeros = [1, 2, 2, 2, 3, 4]
        resultado = moda(numeros)
        self.assertEqual(resultado, 2)
    
    def test_moda_camino_feliz_modas_multiples(self):
        """Prueba moda con múltiples valores con misma frecuencia - camino feliz 2"""
        numeros = [1, 1, 2, 2, 3]
        resultado = moda(numeros)
        # Debe retornar el primer valor encontrado con frecuencia máxima
        self.assertEqual(resultado, 1)
    
    def test_moda_camino_feliz_todos_iguales(self):
        """Prueba moda cuando todos los valores son iguales - camino feliz 3"""
        numeros = [5, 5, 5, 5, 5]
        resultado = moda(numeros)
        self.assertEqual(resultado, 5)
    
    def test_moda_caso_limite_elemento_unico(self):
        """Prueba moda con elemento único"""
        numeros = [42]
        resultado = moda(numeros)
        self.assertEqual(resultado, 42)
    
    def test_moda_caso_limite_floats(self):
        """Prueba moda con valores flotantes"""
        numeros = [1.5, 2.5, 1.5, 3.5, 1.5]
        resultado = moda(numeros)
        self.assertEqual(resultado, 1.5)
    
    def test_moda_error_lista_vacia(self):
        """Prueba que lista vacía lance ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            moda([])
        self.assertEqual(str(contexto.exception), "No se puede calcular la moda de una lista vacía")
    
    def test_moda_error_no_numerico(self):
        """Prueba que valores no numéricos lancen ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            moda([1, 2, "tres", 4])
        self.assertEqual(str(contexto.exception), "Todos los valores deben ser numéricos")


class TestVarianza(unittest.TestCase):
    """Casos de prueba para la función varianza"""
    
    def test_varianza_camino_feliz_poblacion(self):
        """Prueba cálculo de varianza poblacional - camino feliz 1"""
        numeros = [1, 2, 3, 4, 5]
        resultado = varianza(numeros, poblacion=True)
        esperado = 2.0  # (0+1+4+1+0)/5 = 2.0
        self.assertAlmostEqual(resultado, esperado, places=10)
    
    def test_varianza_camino_feliz_muestra(self):
        """Prueba cálculo de varianza muestral - camino feliz 2"""
        numeros = [1, 2, 3, 4, 5]
        resultado = varianza(numeros, poblacion=False)
        esperado = 2.5  # (0+1+4+1+0)/4 = 2.5
        self.assertAlmostEqual(resultado, esperado, places=10)
    
    def test_varianza_camino_feliz_floats(self):
        """Prueba varianza con valores flotantes - camino feliz 3"""
        numeros = [1.5, 2.5, 3.5, 4.5]
        resultado = varianza(numeros, poblacion=True)
        esperado = 1.25  # (2.25+0.25+0.25+2.25)/4 = 1.25
        self.assertAlmostEqual(resultado, esperado, places=10)
    
    def test_varianza_caso_limite_elemento_unico_poblacion(self):
        """Prueba varianza poblacional con elemento único"""
        numeros = [42]
        resultado = varianza(numeros, poblacion=True)
        self.assertEqual(resultado, 0.0)
    
    def test_varianza_caso_limite_numeros_negativos(self):
        """Prueba varianza con números negativos"""
        numeros = [-2, -1, 0, 1, 2]
        resultado = varianza(numeros, poblacion=True)
        esperado = 2.0
        self.assertAlmostEqual(resultado, esperado, places=10)
    
    def test_varianza_error_lista_vacia(self):
        """Prueba que lista vacía lance ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            varianza([])
        self.assertEqual(str(contexto.exception), "No se puede calcular la varianza de una lista vacía")
    
    def test_varianza_error_muestra_elemento_unico(self):
        """Prueba que varianza muestral con elemento único lance ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            varianza([42], poblacion=False)
        self.assertEqual(str(contexto.exception), "La varianza muestral requiere al menos 2 valores")
    
    def test_varianza_error_no_numerico(self):
        """Prueba que valores no numéricos lancen ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            varianza([1, 2, "tres", 4])
        self.assertEqual(str(contexto.exception), "Todos los valores deben ser numéricos")


class TestDS(unittest.TestCase):
    """Casos de prueba para la función ds (desviación estándar)"""
    
    def test_ds_camino_feliz_poblacion(self):
        """Prueba cálculo de desviación estándar poblacional - camino feliz 1"""
        numeros = [1, 2, 3, 4, 5]
        resultado = ds(numeros, poblacion=True)
        esperado = math.sqrt(2.0)  # sqrt(2.0) ≈ 1.414
        self.assertAlmostEqual(resultado, esperado, places=10)
    
    def test_ds_camino_feliz_muestra(self):
        """Prueba cálculo de desviación estándar muestral - camino feliz 2"""
        numeros = [1, 2, 3, 4, 5]
        resultado = ds(numeros, poblacion=False)
        esperado = math.sqrt(2.5)  # sqrt(2.5) ≈ 1.581
        self.assertAlmostEqual(resultado, esperado, places=10)
    
    def test_ds_camino_feliz_floats(self):
        """Prueba desviación estándar con valores flotantes - camino feliz 3"""
        numeros = [1.5, 2.5, 3.5, 4.5]
        resultado = ds(numeros, poblacion=True)
        esperado = math.sqrt(1.25)  # sqrt(1.25) ≈ 1.118
        self.assertAlmostEqual(resultado, esperado, places=10)
    
    def test_ds_caso_limite_elemento_unico_poblacion(self):
        """Prueba desviación estándar poblacional con elemento único"""
        numeros = [42]
        resultado = ds(numeros, poblacion=True)
        self.assertEqual(resultado, 0.0)
    
    def test_ds_caso_limite_varianza_cero(self):
        """Prueba desviación estándar cuando todos los valores son iguales"""
        numeros = [5, 5, 5, 5, 5]
        resultado = ds(numeros, poblacion=True)
        self.assertEqual(resultado, 0.0)
    
    def test_ds_error_lista_vacia(self):
        """Prueba que lista vacía lance ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            ds([])
        self.assertEqual(str(contexto.exception), "No se puede calcular la desviación estándar de una lista vacía")
    
    def test_ds_error_muestra_elemento_unico(self):
        """Prueba que desviación estándar muestral con elemento único lance ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            ds([42], poblacion=False)
        self.assertEqual(str(contexto.exception), "La desviación estándar muestral requiere al menos 2 valores")
    
    def test_ds_error_no_numerico(self):
        """Prueba que valores no numéricos lancen ErrorEstadisticas"""
        with self.assertRaises(ErrorEstadisticas) as contexto:
            ds([1, 2, "tres", 4])
        self.assertEqual(str(contexto.exception), "Todos los valores deben ser numéricos")


class TestIntegracion(unittest.TestCase):
    """Pruebas de integración para verificar que las funciones trabajen juntas correctamente"""
    
    def test_relacion_varianza_ds(self):
        """Prueba que la desviación estándar es la raíz cuadrada de la varianza"""
        numeros = [1, 2, 3, 4, 5]
        var_pob = varianza(numeros, poblacion=True)
        ds_pob = ds(numeros, poblacion=True)
        self.assertAlmostEqual(ds_pob, math.sqrt(var_pob), places=10)
        
        var_muest = varianza(numeros, poblacion=False)
        ds_muest = ds(numeros, poblacion=False)
        self.assertAlmostEqual(ds_muest, math.sqrt(var_muest), places=10)


if __name__ == '__main__':
    unittest.main()
