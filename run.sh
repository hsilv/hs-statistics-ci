#!/bin/bash

echo "=========================================="
echo "    LIBRERÍA DE ESTADÍSTICAS"
echo "=========================================="
echo ""

opcion_seleccionada=0
total_opciones=4

mostrar_menu() {
    local opciones=(
        "🎯 Ejecutar demostración (demo.py)"
        "🧪 Ejecutar pruebas unitarias (test_statistics_lib.py)"
        "🚀 Ejecutar ambos (demo + pruebas)"
        "👋 Salir"
    )
    
    echo "¿Qué deseas ejecutar? (Usa ↑↓ para navegar, Enter para seleccionar)"
    echo ""
    
    for i in "${!opciones[@]}"; do
        if [ $i -eq $opcion_seleccionada ]; then
            echo "▶ ${opciones[$i]}"
        else
            echo "  ${opciones[$i]}"
        fi
    done
    echo ""
}

leer_tecla() {
    local key
    IFS= read -rsn1 key
    
    if [[ $key == $'\e' ]]; then
        IFS= read -rsn2 key
        case $key in
            '[A')
                if [ $opcion_seleccionada -gt 0 ]; then
                    ((opcion_seleccionada--))
                fi
                return 1
                ;;
            '[B')
                if [ $opcion_seleccionada -lt $((total_opciones - 1)) ]; then
                    ((opcion_seleccionada++))
                fi
                return 1
                ;;
        esac
    elif [[ $key == "" ]]; then
        return 0
    fi
    
    return 1
}

ejecutar_demo() {
    echo ""
    echo "🎯 EJECUTANDO DEMOSTRACIÓN..."
    echo "=========================================="
    python3 demo.py
    echo ""
    echo "✅ Demostración completada"
    echo ""
}

ejecutar_pruebas() {
    echo ""
    echo "🧪 EJECUTANDO PRUEBAS UNITARIAS..."
    echo "=========================================="
    python3 -m unittest test_statistics_lib -v
    echo ""
    echo "✅ Pruebas completadas"
    echo ""
}


verificar_dependencias() {
    echo "🔧 Verificando dependencias..."
    
    if ! command -v python3 &> /dev/null; then
        echo "❌ Error: Python3 no está instalado"
        exit 1
    fi
    
    echo "✅ Python3 encontrado: $(python3 --version)"
    
    if [ ! -f "statistics_lib.py" ]; then
        echo "❌ Error: statistics_lib.py no encontrado"
        exit 1
    fi
    
    if [ ! -f "demo.py" ]; then
        echo "❌ Error: demo.py no encontrado"
        exit 1
    fi
    
    if [ ! -f "test_statistics_lib.py" ]; then
        echo "❌ Error: test_statistics_lib.py no encontrado"
        exit 1
    fi
    
    echo "✅ Todos los archivos necesarios encontrados"
    echo ""
}

mostrar_info() {
    echo "📊 Información del Proyecto:"
    echo "   - Librería: statistics-ci"
    echo "   - Versión: 1.0.0"
    echo "   - Funciones: media, mediana, moda, varianza, ds"
    echo "   - Pruebas: 38 casos de prueba"
    echo "   - Idioma: Español"
    echo ""
}

main() {
    verificar_dependencias
    mostrar_info
    
    while true; do
        clear
        echo "=========================================="
        echo "    LIBRERÍA DE ESTADÍSTICAS"
        echo "=========================================="
        echo ""
        mostrar_menu
        
        while true; do
            if leer_tecla; then
                case $opcion_seleccionada in
                    0)
                        ejecutar_demo
                        break
                        ;;
                    1)
                        ejecutar_pruebas
                        break
                        ;;
                    2)
                        ejecutar_demo
                        ejecutar_pruebas
                        break
                        ;;
                    3)
                        echo ""
                        echo "👋 ¡Hasta luego!"
                        echo "=========================================="
                        exit 0
                        ;;
                esac
            else
                clear
                echo "=========================================="
                echo "    LIBRERÍA DE ESTADÍSTICAS"
                echo "=========================================="
                echo ""
                mostrar_menu
            fi
        done
        
        echo ""
        echo "Presiona Enter para continuar..."
        read -r
    done
}

main
