import os
import scanner as Scanner
from parser import parser

# Archivos predefinidos para pruebas
ARCHIVOS_PREDEFINIDOS = {
    "1": "Entregable 3/Parser/Archivos de prueba/prueba.ne",
    "2": "Entregable 3/Parser/Archivos de prueba/test-mcr-01-Estructura del programa.ne"
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("╔════════════════════════════════════╗")
    print("║        MENÚ PRINCIPAL             ║")
    print("╠════════════════════════════════════╣")
    print("║ 1. Probar Scanner                 ║")
    print("║ 2. Probar Parser                  ║")
    print("║ 3. Salir                          ║")
    print("╚════════════════════════════════════╝")

def mostrar_menu_archivos():
    print("╔════════════════════════════════════╗")
    print("║     SELECCIÓN DE ARCHIVO          ║")
    print("╠════════════════════════════════════╣")
    print("║ 1. Usar archivo predefinido       ║")
    print("║ 2. Ingresar ruta personalizada    ║")
    print("╚════════════════════════════════════╝")

def mostrar_archivos_predefinidos():
    print("\n╔════════════════════════════════════╗")
    print("║     ARCHIVOS PREDEFINIDOS         ║")
    print("╠════════════════════════════════════╣")
    for key, path in ARCHIVOS_PREDEFINIDOS.items():
        print(f"║ {key}. {path:<25} ║")
    print("╚════════════════════════════════════╝")

def obtener_ruta_archivo():
    mostrar_menu_archivos()
    opcion = input("\nSeleccione una opción (1-2): ")
    
    if opcion == "1":
        mostrar_archivos_predefinidos()
        num_archivo = input("\nSeleccione un archivo (1-3): ")
        if num_archivo in ARCHIVOS_PREDEFINIDOS:
            return ARCHIVOS_PREDEFINIDOS[num_archivo]
        else:
            print("\n❌ Opción no válida")
            return None
    elif opcion == "2":
        ruta = input("\n📂 Ingrese la ruta del archivo: ")
        return ruta
    else:
        print("\n❌ Opción no válida")
        return None

def probar_scanner():
    limpiar_pantalla()
    print("🔍 MODO SCANNER")
    print("=" * 40)
    
    ruta_archivo = obtener_ruta_archivo()
    if not ruta_archivo:
        input("\nPresione Enter para continuar...")
        return
    
    try:
        scanner = Scanner.AnalizadorLexico()
        scanner.InicializarScanner(ruta_archivo)
        
        print("\n📝 Resultados del análisis léxico:")
        print("-" * 40)
        
        while True:
            token = scanner.DemeToken()
            if token == None:  # EOF
                break
            print(f"Token: {token.lexema:<20} Código: {token.codigo}")
            
    except Exception as e:
        print(f"❌ Error al analizar el archivo: {str(e)}")
    
    input("\nPresione Enter para continuar...")

def probar_parser():
    limpiar_pantalla()
    print("🔍 MODO PARSER")
    print("=" * 40)
    
    ruta_archivo = obtener_ruta_archivo()
    print(ruta_archivo)
    if not ruta_archivo:
        input("\nPresione Enter para continuar...")
        return
    
    try:
        scanner = Scanner.AnalizadorLexico()
        resultado = parser(scanner, ruta_archivo)
        
        if resultado:
            print("\n✅ Análisis sintáctico completado exitosamente")
        else:
            print("\n❌ El análisis sintáctico encontró errores")
            
    except Exception as e:
        print(f"❌ Error al analizar el archivo: {str(e)}")
    
    input("\nPresione Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == "1":
            probar_scanner()
        elif opcion == "2":
            probar_parser()
        elif opcion == "3":
            print("\n👋 ¡Gracias por usar el programa!")
            break
        else:
            print("\n❌ Opción no válida. Por favor, seleccione 1, 2 o 3.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
