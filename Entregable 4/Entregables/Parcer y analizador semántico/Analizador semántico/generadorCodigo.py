class GeneradorEtiquetas:
    def __init__(self):
        self.contador = 0
    
    def siguiente_etiqueta(self):
        etiqueta = f"Et{self.contador:05d}"
        self.contador += 1
        return etiqueta


class GeneradorCodigo:
    def __init__(self):
        self.generador_etiquetas = GeneradorEtiquetas()
        self.codigo_asm = []
        self.variables = {}

    def agregar_linea(self, linea):
        self.codigo_asm.append(linea)

    def generar_segmento_pila(self):
        self.agregar_linea("; Segmento de Pila")
        self.agregar_linea("pila segment stack 'stack'")
        self.agregar_linea("    dw 4096 dup(?)  ; Espacio para la pila")
        self.agregar_linea("pila ends")

    def generar_segmento_datos(self):
        self.agregar_linea("; Segmento de Datos")
        self.agregar_linea("datos segment para public")
        # Variables globales
        for var, valor in self.variables.items():
            self.agregar_linea(f"    VG_{var} dw {valor}  ; Declaración de {var}")
        self.agregar_linea("datos ends")

    def generar_segmento_codigo(self):
        self.agregar_linea("; Segmento de Código")
        self.agregar_linea("codigo segment")
        self.agregar_linea("    assume cs:codigo, ds:datos")
        self.agregar_linea("    include runtime.asm")
        self.agregar_linea("    ; Inicio del programa")
        
        # Ejemplo de operación de suma
        self.agregar_linea("; Realizando la suma varEntero = 9 + 2")
        self.agregar_linea("    mov ax, VG_varEntero  ; Cargar la variable varEntero")
        self.agregar_linea("    add ax, 9             ; Sumar 9")
        self.agregar_linea("    add ax, 2             ; Sumar 2")
        self.agregar_linea("    mov VG_varEntero, ax  ; Guardar el resultado en varEntero")

        self.agregar_linea("    mov ah, 4Ch")
        self.agregar_linea("    int 21h               ; Fin del programa")
        self.agregar_linea("codigo ends")
        self.agregar_linea("end etiqueta")

    def generar_codigo(self, programa):
        # Comenzamos generando el encabezado
        self.generar_segmento_pila()
        self.generar_segmento_datos()
        self.generar_segmento_codigo()

        # Imprimir el código ASM
        return "\n".join(self.codigo_asm)

    def declarar_variable(self, nombre, valor):
        self.variables[nombre] = valor


# Simulando el código de entrada que nos diste
programa = """
worldname MiEjemplo
inventory
    stack varEntero = 2
spawnpoint
    polloCrudo
    varEntero = 9 + 2
    polloAsado
worldsave
"""

# Generar el código ASM
generador = GeneradorCodigo()
generador.declarar_variable("varEntero", 2)  # Declaramos la variable varEntero con valor 2

codigo_asm = generador.generar_codigo(programa)

# Mostrar el código generado en ASM
print(codigo_asm)
