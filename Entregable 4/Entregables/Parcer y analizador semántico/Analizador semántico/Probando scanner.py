from scanner import AnalizadorLexico

def main():
    # Crear una instancia del analizador léxico
    scanner = AnalizadorLexico()
    
    # Nombre del archivo a analizar (debe tener extensión .ne)
    archivo_prueba = "Entregable 4\Entregables\Parcer y analizador semántico\Analizador semántico\Archivos de prueba\prueba.ne"
    
    # Inicializar el scanner con el archivo
    if scanner.InicializarScanner(archivo_prueba):
        print("\nIniciando análisis léxico...")
        print("-" * 50)
        
        # Procesar tokens hasta que no haya más
        while True:
            token = scanner.DemeToken()
            if token is None:
                break
            print(token)
        
        print("-" * 50)
        print("\nAnálisis léxico completado.")
        
        # Mostrar todos los tokens encontrados
        print("\nLista completa de tokens:")
        print("-" * 50)
        #scanner.imprimirTokens()
        
        # Finalizar el scanner
        scanner.FinalizarScanner()
    else:
        print("No se pudo inicializar el scanner.")

if __name__ == "__main__":
    main()
