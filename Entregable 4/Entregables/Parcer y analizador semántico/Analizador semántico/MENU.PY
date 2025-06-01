import os
import scanner as Scanner
from parser import parser
import simboloSemanticos as S

# Archivos predefinidos para pruebas
ARCHIVOS_PREDEFINIDOS = {
    "1": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/prueba.ne",
    "2": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-01-Estructura del programa.ne",
    "3": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-02-Arreglo.ne",
    "4": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-03-Operaciones de string.ne",
    "5": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-04-Registro.ne",
    "6": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-05-Asignacion y familia.ne",
    "7": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-06-Operaciones enteros.ne",
    "8": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-07-Incremento y decremento.ne",
    "9": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-08-Operaciones caracteres.ne",
    "10": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-09-Operaciones conjuntos.ne",
    "11": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-10-Operaciones archivos.ne",
    "12": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-11-Operaciones flotantes.ne",
    "13": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-12-Operaciones comparacion.ne",
    "14": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-13-While con if-else.ne",
    "15": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-14-For con switch.ne",
    "16": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-15-Repeat until.ne",
    "17": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-16-Procedimiento.ne",
    "18": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-17-Creativo.ne",
    "19": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-19-Logica.ne",
    "20": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-20-Halt-Sizeof.ne",
    "21": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-21-Algunas-asignaciones.ne",
    "22": "Parcer y analizador semántico/Analizador semántico/Archivos de prueba/test-mcr-22-Cuerpo-del-programa.ne"
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("╔═══════════════════════════════════════╗")
    print("║        MENÚ PRINCIPAL                 ║")
    print("╠═══════════════════════════════════════╣")
    print("║ 1. Probar Scanner                     ║")
    print("║ 2. Probar Parser                      ║")
    print("║ 3. Información del análisis semántico ║")
    print("║ 4. Información del Parser             ║")
    print("║ 5. Salir                              ║")
    print("╚═══════════════════════════════════════╝")

def mostrar_menu_archivos():
    print("╔════════════════════════════════════╗")
    print("║     SELECCIÓN DE ARCHIVO           ║")
    print("╠════════════════════════════════════╣")
    print("║ 1. Usar archivo predefinido        ║")
    print("║ 2. Ingresar ruta personalizada     ║")
    print("╚════════════════════════════════════╝")

def mostrar_archivos_predefinidos():
    print("\n╔════════════════════════════════════╗")
    print("║     ARCHIVOS PREDEFINIDOS          ║")
    print("╠════════════════════════════════════╣")
    for key, path in ARCHIVOS_PREDEFINIDOS.items():
        print(f"║ {key}. {path:<25} ║")
    print("╚════════════════════════════════════╝")

def obtener_ruta_archivo():
    mostrar_menu_archivos()
    opcion = input("\nSeleccione una opción (1-2): ")
    
    if opcion == "1":
        mostrar_archivos_predefinidos()
        num_archivo = input("\nSeleccione un archivo (1-22): ")
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
            print("\n✅ Análisis semántico completado exitosamente")
        else:
            print("\n❌ El análisis semántico encontró errores")
            
    except Exception as e:
        print(f"❌ Error al analizar el archivo: {str(e)}")
    
    input("\nPresione Enter para continuar...")

def mostrar_info_analisis():
    limpiar_pantalla()
    print("🔍 INFORMACIÓN DEL ANÁLISIS")
    print("=" * 40)
    print("\nAnálisis Semántico Implementado:")
    print("-" * 40)
    print("1. Verificación de Tipos:")
    print("   - Comprobación de tipos en asignaciones")
    print("   - Validación de operaciones entre tipos compatibles")
    print("   - Control de tipos en expresiones aritméticas y lógicas")
    
    print("\n2. Control de Variables:")
    print("   - Verificación de declaración antes de uso")
    print("   - Validación de ámbito de variables")
    print("   - Comprobación de variables no utilizadas")
    
    print("\n3. Validación de Estructuras:")
    print("   - Control de estructuras de control")
    print("   - Verificación de condiciones en estructuras de control")
    print("   - Validación de bloques de código")
    
    print("\n4. Manejo de Errores:")
    print("   - Detección de errores semánticos")

    print("\nSímbolos Semánticos Utilizados:")
    print("-" * 40)
    print("\nGestión de Tabla de Símbolos:")
    print(f"  CrearTLG ({S.CrearTLG}): Inicializa la tabla de símbolos")
    print(f"  BorrarIdentificador ({S.BorrarIdentificador}): Elimina un identificador de la tabla")
    
    print("\nManejo de Constantes:")
    print(f"  AlmacenarTipoConstante ({S.AlmacenarTipoConstante}): Guarda el tipo de una constante")
    print(f"  ValidarExistenciaIdentificadorConstante ({S.ValidarExistenciaIdentificadorConstante}): Verifica si existe una constante")
    print(f"  ValidarTipoValorConstante ({S.ValidarTipoValorConstante}): Comprueba el tipo de valor de una constante")
    
    print("\nManejo de Variables:")
    print(f"  AlmacenarTipoVariable ({S.AlmacenarTipoVariable}): Guarda el tipo de una variable")
    print(f"  BorrarTipoVariable ({S.BorrarTipoVariable}): Elimina el tipo de una variable")
    print(f"  ValidarExistenciaIdentificadorVariable ({S.ValidarExistenciaIdentificadorVariable}): Verifica si existe una variable")
    print(f"  ValidarTipoValorVariable ({S.ValidarTipoValorVariable}): Comprueba el tipo de valor de una variable")
    
    print("\nManejo de Funciones y Procedimientos:")
    print(f"  AlmacenarFuncion ({S.AlmacenarFuncion}): Guarda información de una función")
    print(f"  AlmacenarTipoFuncion ({S.AlmacenarTipoFuncion}): Guarda el tipo de retorno de una función")
    print(f"  AlmacenarProcedimiento ({S.AlmacenarProcedimiento}): Guarda información de un procedimiento")
    print(f"  EmpezarAnalizarReturn ({S.EmpezarAnalizarReturn}): Inicia el análisis de retorno")
    print(f"  ComprobarReturn ({S.ComprobarReturn}): Verifica el retorno de una función")
    print(f"  SiHayReturn ({S.SiHayReturn}): Comprueba si existe un retorno")
    
    print("\nValidación de Parámetros:")
    print(f"  AlmacenarTipoParametroFormal ({S.AlmacenarTipoParametroFormal}): Guarda tipo de parámetro formal")
    print(f"  ValidarExistenciaIdentificadorParametroFormal ({S.ValidarExistenciaIdentificadorParametroFormal}): Verifica parámetro formal")
    print(f"  ValidarExistenciaIdentificadorParametroReal ({S.ValidarExistenciaIdentificadorParametroReal}): Verifica parámetro real")
    
    print("\nValidación de Operaciones:")
    print(f"  ValidarOperacionEntero ({S.ValidarOperacionEntero}): Valida operaciones con enteros")
    print(f"  ValidarOperacionComparacion ({S.ValidarOperacionComparacion}): Valida operaciones de comparación")
    print(f"  ValidarOperacionCaracter ({S.ValidarOperacionCaracter}): Valida operaciones con caracteres")
    print(f"  ValidarOperacionString ({S.ValidarOperacionString}): Valida operaciones con strings")
    print(f"  ValidarOperacionLogica ({S.ValidarOperacionLogica}): Valida operaciones lógicas")
    
    print("\nControl de Estructuras:")
    print(f"  ValidarCondicionWhile ({S.ValidarCondicionWhile}): Valida condición del while")
    print(f"  ValidarIdentificadorForRecorrido ({S.ValidarIdentificadorForRecorrido}): Valida identificador en for")
    print(f"  ValidarLiteralEnteraFor ({S.ValidarLiteralEnteraFor}): Valida literal en for")
    print(f"  ValidarTopeFor ({S.ValidarTopeFor}): Valida tope del for")
    print(f"  ValidarCondicionRepeat ({S.ValidarCondicionRepeat}): Valida condición del repeat")
    print(f"  ValidarIdentificadorWith ({S.ValidarIdentificadorWith}): Valida identificador en with")
    
    print("\nManejo de Switch:")
    print(f"  EmpezarAnalizarDefaultSwitch ({S.EmpezarAnalizarDefaultSwitch}): Inicia análisis de default")
    print(f"  HayDefaultSwitch ({S.HayDefaultSwitch}): Verifica si hay default")
    print(f"  SiHayDefaultSwitch ({S.SiHayDefaultSwitch}): Confirma presencia de default")
    
    print("\nValidación de Tipos Específicos:")
    print(f"  ValidarTipoEntera ({S.ValidarTipoEntera}): Valida tipo entero")
    print(f"  ValidarTipoFlotante ({S.ValidarTipoFlotante}): Valida tipo flotante")
    print(f"  ValidarTipoString ({S.ValidarTipoString}): Valida tipo string")
    
    input("\nPresione Enter para continuar...")

def mostrar_info_parser():
    limpiar_pantalla()
    print("🔍 INFORMACIÓN DEL PARSER")
    print("=" * 40)
    print("\nImplementación del Parser:")
    print("-" * 40)
    print("El parser implementado utiliza las tablas generadas por GikGram")
    print("especializado en la generación de analizadores semánticos. Las tablas presentes son:")
    
    print("\n1. Tabla de terminales:")
    print("   - Define todas las terminales utilizadas")
    
    print("\n2. Tabla de lados derechos")
    print("   - Contiene los lados derechos de la gramatica")
    
    print("\n3. Tabla de parcing:")
    print("   - Define las reglas gramaticales del lenguaje")
    print("   - Especifica las producciones válidas")
    print("   - Establece la estructura del lenguaje")
    
    print("\n4. Características del Parser:")
    print("   - Implementa análisis LL1")
    print("   - Manejo de errores semánticos")
    print("   - Recuperación de errores")
    
    input("\nPresione Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            probar_scanner()
        elif opcion == "2":
            probar_parser()
        elif opcion == "3":
            mostrar_info_analisis()
        elif opcion == "4":
            mostrar_info_parser()
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el programa!")
            break
        else:
            print("\n❌ Opción no válida. Por favor, seleccione 1, 2, 3, 4 o 5.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
