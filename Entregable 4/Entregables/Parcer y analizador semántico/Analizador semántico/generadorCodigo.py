import datetime
'''
Generador de código para el compilador Notch Engine
=======================================================

Crado por: David Acuña y Deylan Sandoval
Fecha: 12 de junio de 2025
Materia: Compiladores e interpretes
'''

def crear_encabezado_compilador(nombre_compilador):
    # Abrimos el archivo de salida en modo escritura (w) o creamos uno nuevo
    archivo_salida = "codigo_generado.asm"

    # Fecha de generación del código
    fecha_generacion = datetime.datetime.now().strftime("%Y-%m-%d")

    # Verificamos si el archivo ya existe y lo eliminamos si es necesario
    try:
        with open(archivo_salida, 'x') as f:
            pass  # Creamos el archivo si no existe
    except FileExistsError:
        print(f"El archivo '{archivo_salida}' ya existe. Se sobrescribirá.")
    
    # Creamos el archivo y escribimos el encabezado
    with open(archivo_salida, 'w') as f:
        f.write("; --------------------------------------------------------\n")
        f.write(f"; Código generado por el compilador {nombre_compilador}\n")
        f.write(f"; Fecha de generación: {fecha_generacion}\n")
        f.write("; Este archivo ha sido generado automáticamente por el compilador.\n")
        f.write("; Autores: David Acuña y Deylan Sandoval\n")
        f.write("; Materia: Compiladores e intérpretes\n")
        f.write("; --------------------------------------------------------\n")
        f.write("\n")  # Línea en blanco para separar el encabezado del código posterior
    
    return archivo_salida


def generar_codigo_ensamblador(archivo_generado):
    # Abrimos el archivo para agregar el código
    with open(archivo_generado, 'a') as f:
        # Segmento de pila
        f.write("\npila segment stack 'stack'\n")
        f.write("    dw 4096 dup(?)  ; Espacio para la pila\n")
        f.write("pila ends\n")

        # Segmento de datos
        f.write("\ndatos segment para public\n")
        f.write("    ; Variables globales\n")
        f.write("    VG_varEntero dw 2  ; Declaración de la variable varEntero\n")
        f.write("datos ends\n")
        
        # Segmento de código
        f.write("\ncodigo segment\n")
        f.write("    assume cs:codigo, ds:datos\n")
        f.write("    ; Inicio del programa\n")
        f.write("    ; Operación de suma varEntero = 9 + 2\n")
        f.write("    mov ax, VG_varEntero  ; Cargar la variable varEntero\n")
        f.write("    add ax, 9             ; Sumar 9\n")
        f.write("    add ax, 2             ; Sumar 2\n")
        f.write("    mov VG_varEntero, ax  ; Guardar el resultado en varEntero\n")
        f.write("    mov ah, 4Ch\n")
        f.write("    int 21h               ; Fin del programa\n")
        f.write("codigo ends\n")
        f.write("end etiqueta\n")

    print(f"Código de ensamblador generado y guardado en '{archivo_generado}'.")

# Llamamos a la función para generar el código en ensamblador




# Llamamos a la función para generar el encabezado
nombre_compilador = "Notch Engine"
archivo_generado = crear_encabezado_compilador(nombre_compilador)
print(f"Archivo '{archivo_generado}' creado con éxito con el encabezado.")
generar_codigo_ensamblador(archivo_generado)