# Librería de Estadísticas

Una librería completa de Python para cálculos estadísticos básicos con código limpio, legible y pruebas unitarias extensivas.

## Características

La librería proporciona las siguientes funciones estadísticas:

- **`media([n1,n2,n3...])`** – Retorna la media aritmética de una lista de números
- **`mediana([n1,n2,n3...])`** – Retorna la mediana de una lista de números  
- **`moda([n1,n2,n3...])`** – Retorna la moda de una lista de números
- **`varianza([n1,n2,n3...])`** – Retorna la varianza de una lista de números
- **`ds([n1,n2,n3...])`** – Retorna la desviación estándar de una lista de números

## Instalación

¡No se requieren dependencias externas! Esta librería usa solo módulos de la librería estándar de Python.

```bash
# Clonar o descargar los archivos
git clone <url-del-repositorio>
cd statistics-ci

# O simplemente copiar los archivos a tu proyecto
```

## Uso

```python
from statistics_lib import media, mediana, moda, varianza, ds

# Conjunto de datos de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular estadísticas
media_val = media(numeros)           # 5.5
mediana_val = mediana(numeros)       # 5.5
moda_val = moda(numeros)             # 1 (primer valor con frecuencia máxima)
var_pob = varianza(numeros)          # Varianza poblacional: 8.25
var_muest = varianza(numeros, poblacion=False)  # Varianza muestral: 9.17
ds_pob = ds(numeros)                 # Desviación estándar poblacional: 2.87
ds_muest = ds(numeros, poblacion=False)  # Desviación estándar muestral: 3.03
```

## Detalles de las Funciones

### `media(numeros)`
Calcula la media aritmética de una lista de números.
- **Parámetros**: `numeros` - Lista de números (int o float)
- **Retorna**: float - La media aritmética
- **Lanza**: `ErrorEstadisticas` si la lista está vacía o contiene valores no numéricos

### `mediana(numeros)`
Calcula la mediana de una lista de números.
- **Parámetros**: `numeros` - Lista de números (int o float)
- **Retorna**: float - El valor de la mediana
- **Lanza**: `ErrorEstadisticas` si la lista está vacía o contiene valores no numéricos

### `moda(numeros)`
Calcula la moda de una lista de números.
- **Parámetros**: `numeros` - Lista de números (int o float)
- **Retorna**: El valor más frecuente (primer valor encontrado si hay empate)
- **Lanza**: `ErrorEstadisticas` si la lista está vacía o contiene valores no numéricos

### `varianza(numeros, poblacion=True)`
Calcula la varianza de una lista de números.
- **Parámetros**: 
  - `numeros` - Lista de números (int o float)
  - `poblacion` - Si True, calcula varianza poblacional (divide por n). Si False, calcula varianza muestral (divide por n-1)
- **Retorna**: float - La varianza
- **Lanza**: `ErrorEstadisticas` si la lista está vacía, tiene solo un elemento (para muestra), o contiene valores no numéricos

### `ds(numeros, poblacion=True)`
Calcula la desviación estándar de una lista de números.
- **Parámetros**: 
  - `numeros` - Lista de números (int o float)
  - `poblacion` - Si True, calcula desviación estándar poblacional. Si False, calcula desviación estándar muestral
- **Retorna**: float - La desviación estándar
- **Lanza**: `ErrorEstadisticas` si la lista está vacía, tiene solo un elemento (para muestra), o contiene valores no numéricos

## Manejo de Errores

La librería incluye manejo de errores comprensivo con excepciones personalizadas `ErrorEstadisticas`:

```python
from statistics_lib import ErrorEstadisticas

try:
    resultado = media([])  # Lista vacía
except ErrorEstadisticas as e:
    print(f"Error: {e}")  # "No se puede calcular la media de una lista vacía"

try:
    resultado = media([1, 2, "tres", 4])  # Valores no numéricos
except ErrorEstadisticas as e:
    print(f"Error: {e}")  # "Todos los valores deben ser numéricos"
```

## Pruebas

La librería incluye pruebas unitarias comprensivas que cubren:

1. **Pruebas de Camino Feliz**: Al menos 2 variaciones por función con diferentes tipos de datos y escenarios
2. **Casos Límite**: Elementos únicos, números negativos, duplicados, varianza cero, etc.
3. **Manejo de Errores**: Listas vacías, valores no numéricos, tamaños de muestra inválidos
4. **Pruebas de Integración**: Verificación de que las funciones trabajen juntas correctamente

Ejecutar las pruebas:

```bash
python -m unittest test_statistics_lib -v
```

### Cobertura de Pruebas

- **38 casos de prueba** cubriendo todas las funciones
- **Variaciones de camino feliz**: Múltiples escenarios de prueba por función
- **Casos límite**: Condiciones de frontera y casos especiales
- **Manejo de errores**: Manejo de excepciones y validación apropiados
- **Pruebas de integración**: Verificación entre funciones

## Demo

Ejecuta el script de demostración para ver la librería en acción:

```bash
python demo.py
```

## Estructura del Proyecto

```
statistics-ci/
├── statistics_lib.py      # Implementación principal de la librería
├── test_statistics_lib.py # Pruebas unitarias comprensivas
├── demo.py               # Script de demostración
├── setup.py              # Configuración del paquete
├── requirements.txt      # Dependencias (ninguna requerida)
└── README.md            # Este archivo
```

## Calidad del Código

- **Código limpio y legible** con documentación comprensiva
- **Pistas de tipo** para mejor claridad del código y soporte de IDE
- **Manejo de errores comprensivo** con mensajes de error significativos
- **Pruebas unitarias extensivas** con 100% de cobertura de funciones
- **Sin dependencias externas** - usa solo la librería estándar de Python

## Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.
