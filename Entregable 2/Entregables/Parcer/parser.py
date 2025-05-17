'''
Etapa dos: Analizador Sintáctico
Grupo: 1
Integrantes:
- David Acuña López - 2020426228
- Deylan Sandoval Sanchez - 2020234274

Este es un analizador sintáctico para Minecraft, que se encarga de 
consumir los tokens del analizador léxico y verificar que la estructura
del código fuente cumpla con la gramática definida. El parser implementa
un análisis LL(1) que utiliza tablas de predicción para determinar las
reglas gramaticales a aplicar en cada paso del análisis.
'''

from scanner import AnalizadorLexico, Token

class Parser:
    def __init__(self):
        self.scanner = AnalizadorLexico()
        self.token_actual = None
        self.pila_parsing = []
        self.tabla_parsing = self.inicializar_tabla_parsing()
        self.tabla_lados_derechos = self.inicializar_tabla_lados_derechos()
        self.simbolo_inicial = "inicio"
        self.error = False
        self.terminales = {
            'WORLDNAME', 'BEDROCK', 'RESOURCEPACK', 'INVENTORY', 'RECIPE', 
            'CRAFTINGTABLE', 'SPAWNPOINT', 'OBSIDIAN', 'ANVIL', 'STACK', 
            'RUNE', 'SPIDER', 'TORCH', 'CHEST', 'BOOK', 'GHAST', 'SHELF', 
            'ENTITY', 'ON', 'OFF', 'SOULSAND', 'MAGMA', 'ISENGRAVED', 
            'ISINSCRIBED', 'ETCHUP', 'ETCHDOWN', 'AND', 'OR', 'NOT', 'XOR',
            'BIND', 'FROM', 'EXCEPT', 'SEEK', 'ADD', 'DROP', 'ITEM', 'FEED',
            'MAP', 'BIOM', 'KILL', 'IS', 'ISNOT', 'POLLOCRUDO', 'POLLOASADO',
            'REPEATER', 'CRAFT', 'TARGET', 'HIT', 'MISS', 'JUKEBOX', 'DISK',
            'SPAWNER', 'EXHAUSTED', 'WALK', 'SET', 'TO', 'STEP', 'WITHER',
            'CREEPER', 'ENDERPEARL', 'RAGEQUIT', 'SPELL', 'RITUAL', 'RESPAWN',
            'CHUNK', 'HOPPER', 'DROPPER', 'WORLDSAVE'
        }
        self.no_terminales = {
            'inicio', 'inicio2', 'seccion', 'punto_entrada', 'sistema_asignacion_constante',
            'sistema_asignacion_tipos', 'sistema_asignacion_variables', 'tipo',
            'literal_booleano', 'literal_flotante', 'literal_entero', 'literal_caracter',
            'literal_string', 'literal_arreglo', 'literal_registro', 'acceso_arreglo',
            'indices', 'mas_indices', 'acceso_string', 'acceso_resgistro', 'asignacion',
            'operador', 'operacion_incre_decre', 'operacion_caracter', 'operacion_logica',
            'operacion_string', 'operacion_flotante', 'operacion_comparacion', 'bloque',
            'ciclo', 'if_then_else', 'if_then_else2', 'switch', 'casos_switch', 'caso',
            'ciclo_for_tipo', 'with', 'break_continue_halt', 'encabezado', 'parametros_formales',
            'parametros', 'lista_parametros_formales', 'lista_parametros_formales2',
            'parametro_formal', 'parametro_formal_tipo', 'parametros_reales',
            'lista_parametros_reales', 'mas_parametros_reales', 'parametro_real',
            'return', 'size_of', 'size_of_tipo', 'cohercion', 'entrada_estandar',
            'salida_estandar', 'terminador', 'final', 'identificador', 'valor',
            'literal', 'separador', 'instrucciones', 'instruccion', 'operacion_en_caracter',
            'operacion_en_string', 'operacion_en_flotante', 'operacion_size_of'
        }

    def inicializar_tabla_parsing(self):
        """Inicializa la tabla de parsing con las reglas de la gramática"""
        tabla = {}
        
        # Reglas para inicio
        tabla[('inicio', 'WORLDNAME')] = 1
        
        # Reglas para inicio2
        tabla[('inicio2', 'SPAWNPOINT')] = 2
        tabla[('inicio2', 'WORLDSAVE')] = 3
        
        # Reglas para seccion
        tabla[('seccion', 'BEDROCK')] = 4
        tabla[('seccion', 'RESOURCEPACK')] = 5
        tabla[('seccion', 'INVENTORY')] = 6
        tabla[('seccion', 'RECIPE')] = 7
        tabla[('seccion', 'CRAFTINGTABLE')] = 8
        
        # Reglas para punto_entrada
        tabla[('punto_entrada', 'SPAWNPOINT')] = 9
        
        # Reglas para sistema_asignacion_constante
        tabla[('sistema_asignacion_constante', 'ANVIL')] = 10
        tabla[('sistema_asignacion_constante', 'BEDROCK')] = 10
        tabla[('sistema_asignacion_constante', 'RESOURCEPACK')] = 10
        tabla[('sistema_asignacion_constante', 'INVENTORY')] = 10
        tabla[('sistema_asignacion_constante', 'RECIPE')] = 10
        tabla[('sistema_asignacion_constante', 'CRAFTINGTABLE')] = 10
        
        # Reglas para sistema_asignacion_tipos
        tabla[('sistema_asignacion_tipos', 'ANVIL')] = 11
        tabla[('sistema_asignacion_tipos', 'BEDROCK')] = 11
        tabla[('sistema_asignacion_tipos', 'RESOURCEPACK')] = 11
        tabla[('sistema_asignacion_tipos', 'INVENTORY')] = 11
        tabla[('sistema_asignacion_tipos', 'RECIPE')] = 11
        tabla[('sistema_asignacion_tipos', 'CRAFTINGTABLE')] = 11
        
        # Reglas para sistema_asignacion_variables
        tabla[('sistema_asignacion_variables', 'STACK')] = 12
        tabla[('sistema_asignacion_variables', 'RUNE')] = 12
        tabla[('sistema_asignacion_variables', 'SPIDER')] = 12
        tabla[('sistema_asignacion_variables', 'TORCH')] = 12
        tabla[('sistema_asignacion_variables', 'CHEST')] = 12
        tabla[('sistema_asignacion_variables', 'BOOK')] = 12
        tabla[('sistema_asignacion_variables', 'GHAST')] = 12
        tabla[('sistema_asignacion_variables', 'SHELF')] = 12
        tabla[('sistema_asignacion_variables', 'ENTITY')] = 12
        tabla[('sistema_asignacion_variables', 'BEDROCK')] = 12
        tabla[('sistema_asignacion_variables', 'RESOURCEPACK')] = 12
        tabla[('sistema_asignacion_variables', 'INVENTORY')] = 12
        tabla[('sistema_asignacion_variables', 'RECIPE')] = 12
        tabla[('sistema_asignacion_variables', 'CRAFTINGTABLE')] = 12
        
        # Reglas para tipo
        tabla[('tipo', 'STACK')] = 13
        tabla[('tipo', 'RUNE')] = 14
        tabla[('tipo', 'SPIDER')] = 15
        tabla[('tipo', 'TORCH')] = 16
        tabla[('tipo', 'CHEST')] = 17
        tabla[('tipo', 'BOOK')] = 18
        tabla[('tipo', 'GHAST')] = 19
        tabla[('tipo', 'SHELF')] = 20
        tabla[('tipo', 'ENTITY')] = 21
        
        # Reglas para literal
        tabla[('literal', 'ON')] = 22
        tabla[('literal', 'OFF')] = 23
        tabla[('literal', 'literal_entero')] = 24
        tabla[('literal', 'literal_flotante')] = 25
        tabla[('literal', 'literal_caracter')] = 26
        tabla[('literal', 'literal_string')] = 27
        tabla[('literal', 'literal_arreglo')] = 28
        tabla[('literal', 'literal_registro')] = 29
        
        # Reglas para operacion
        tabla[('operacion', 'SOULSAND')] = 30
        tabla[('operacion', 'MAGMA')] = 31
        tabla[('operacion', 'ISENGRAVED')] = 32
        tabla[('operacion', 'ISINSCRIBED')] = 33
        tabla[('operacion', 'ETCHUP')] = 34
        tabla[('operacion', 'ETCHDOWN')] = 35
        tabla[('operacion', 'AND')] = 36
        tabla[('operacion', 'OR')] = 37
        tabla[('operacion', 'NOT')] = 38
        tabla[('operacion', 'XOR')] = 39
        tabla[('operacion', 'BIND')] = 40
        tabla[('operacion', 'FROM')] = 41
        tabla[('operacion', 'EXCEPT')] = 42
        tabla[('operacion', 'SEEK')] = 43
        tabla[('operacion', 'IS')] = 44
        tabla[('operacion', 'ISNOT')] = 45
        
        # Reglas para bloque
        tabla[('bloque', 'POLLOCRUDO')] = 46
        
        # Reglas para instrucciones
        tabla[('instrucciones', 'identificador')] = 47
        tabla[('instrucciones', 'REPEATER')] = 47
        tabla[('instrucciones', 'TARGET')] = 47
        tabla[('instrucciones', 'JUKEBOX')] = 47
        tabla[('instrucciones', 'WITHER')] = 47
        tabla[('instrucciones', 'CREEPER')] = 47
        tabla[('instrucciones', 'ENDERPEARL')] = 47
        tabla[('instrucciones', 'RAGEQUIT')] = 47
        tabla[('instrucciones', 'RESPAWN')] = 47
        tabla[('instrucciones', 'CHUNK')] = 47
        tabla[('instrucciones', 'HOPPER')] = 47
        tabla[('instrucciones', 'DROPPER')] = 47
        tabla[('instrucciones', 'POLLOASADO')] = 48
        
        # Reglas para instruccion
        tabla[('instruccion', 'identificador')] = 49
        tabla[('instruccion', 'REPEATER')] = 50
        tabla[('instruccion', 'TARGET')] = 51
        tabla[('instruccion', 'JUKEBOX')] = 52
        tabla[('instruccion', 'WITHER')] = 53
        tabla[('instruccion', 'CREEPER')] = 54
        tabla[('instruccion', 'ENDERPEARL')] = 54
        tabla[('instruccion', 'RAGEQUIT')] = 54
        tabla[('instruccion', 'RESPAWN')] = 55
        tabla[('instruccion', 'CHUNK')] = 56
        tabla[('instruccion', 'HOPPER')] = 57
        tabla[('instruccion', 'DROPPER')] = 58
        
        # Reglas para asignacion
        tabla[('asignacion', 'identificador')] = 59
        
        # Reglas para expresion
        tabla[('expresion', 'ON')] = 60
        tabla[('expresion', 'OFF')] = 60
        tabla[('expresion', 'literal_entero')] = 60
        tabla[('expresion', 'literal_flotante')] = 60
        tabla[('expresion', 'literal_caracter')] = 60
        tabla[('expresion', 'literal_string')] = 60
        tabla[('expresion', 'literal_arreglo')] = 60
        tabla[('expresion', 'literal_registro')] = 60
        tabla[('expresion', 'identificador')] = 61
        tabla[('expresion', 'SOULSAND')] = 62
        tabla[('expresion', 'MAGMA')] = 62
        tabla[('expresion', 'ISENGRAVED')] = 62
        tabla[('expresion', 'ISINSCRIBED')] = 62
        tabla[('expresion', 'ETCHUP')] = 62
        tabla[('expresion', 'ETCHDOWN')] = 62
        tabla[('expresion', 'AND')] = 62
        tabla[('expresion', 'OR')] = 62
        tabla[('expresion', 'NOT')] = 62
        tabla[('expresion', 'XOR')] = 62
        tabla[('expresion', 'BIND')] = 62
        tabla[('expresion', 'FROM')] = 62
        tabla[('expresion', 'EXCEPT')] = 62
        tabla[('expresion', 'SEEK')] = 62
        tabla[('expresion', 'IS')] = 62
        tabla[('expresion', 'ISNOT')] = 62
        
        # Reglas para final
        tabla[('final', 'WORLDSAVE')] = 63
        
        return tabla

    def inicializar_tabla_lados_derechos(self):
        """Inicializa la tabla de lados derechos de la gramática"""
        tabla = {}
        # Regla 1: inicio ::= WORLDNAME identificador seccion inicio2 final
        tabla[1] = ['WORLDNAME', 'identificador', ':', 'seccion', 'inicio2', 'final']
        
        # Regla 2: inicio2 ::= punto_entrada
        tabla[2] = ['punto_entrada']
        
        # Regla 3: inicio2 ::= epsilon
        tabla[3] = []
        
        # Regla 4: seccion ::= BEDROCK sistema_asignacion_constante
        tabla[4] = ['BEDROCK', 'sistema_asignacion_constante']
        
        # Regla 5: seccion ::= RESOURCEPACK sistema_asignacion_tipos
        tabla[5] = ['RESOURCEPACK', 'sistema_asignacion_tipos']
        
        # Regla 6: seccion ::= INVENTORY sistema_asignacion_variables
        tabla[6] = ['INVENTORY', 'sistema_asignacion_variables']
        
        # Regla 7: seccion ::= RECIPE encabezado
        tabla[7] = ['RECIPE', 'encabezado']
        
        # Regla 8: seccion ::= CRAFTINGTABLE instrucciones
        tabla[8] = ['CRAFTINGTABLE', 'instrucciones']
        
        # Regla 9: punto_entrada ::= SPAWNPOINT bloque
        tabla[9] = ['SPAWNPOINT', 'bloque']
        
        # Regla 10: sistema_asignacion_constante ::= ANVIL identificador -> tipo
        tabla[10] = ['ANVIL', 'identificador', '->', 'tipo']
        
        # Regla 11: sistema_asignacion_tipos ::= ANVIL identificador -> tipo
        tabla[11] = ['ANVIL', 'identificador', '->', 'tipo']
        
        # Regla 12: sistema_asignacion_variables ::= tipo identificador = literal
        tabla[12] = ['tipo', 'identificador', '=', 'literal']
        
        # Reglas para tipo (13-21)
        tabla[13] = ['STACK']
        tabla[14] = ['RUNE']
        tabla[15] = ['SPIDER']
        tabla[16] = ['TORCH']
        tabla[17] = ['CHEST']
        tabla[18] = ['BOOK']
        tabla[19] = ['GHAST']
        tabla[20] = ['SHELF']
        tabla[21] = ['ENTITY']
        
        # Reglas para literales (22-29)
        tabla[22] = ['ON']  # literal_booleano
        tabla[23] = ['OFF']  # literal_booleano
        tabla[24] = ['literal_entero']  # literal_entero
        tabla[25] = ['literal_flotante']  # literal_flotante
        tabla[26] = ['literal_caracter']  # literal_caracter
        tabla[27] = ['literal_string']  # literal_string
        tabla[28] = ['literal_arreglo']  # literal_arreglo
        tabla[29] = ['literal_registro']  # literal_registro
        
        # Reglas para operaciones (30-39)
        tabla[30] = ['SOULSAND']  # operacion_incre_decre
        tabla[31] = ['MAGMA']  # operacion_incre_decre
        tabla[32] = ['ISENGRAVED']  # operacion_caracter
        tabla[33] = ['ISINSCRIBED']  # operacion_caracter
        tabla[34] = ['ETCHUP']  # operacion_caracter
        tabla[35] = ['ETCHDOWN']  # operacion_caracter
        tabla[36] = ['AND']  # operacion_logica
        tabla[37] = ['OR']  # operacion_logica
        tabla[38] = ['NOT']  # operacion_logica
        tabla[39] = ['XOR']  # operacion_logica
        
        # Reglas para operaciones de string (40-43)
        tabla[40] = ['BIND']  # operacion_string
        tabla[41] = ['FROM']  # operacion_string
        tabla[42] = ['EXCEPT']  # operacion_string
        tabla[43] = ['SEEK']  # operacion_string
        
        # Reglas para operaciones de comparación (44-45)
        tabla[44] = ['IS']  # operacion_comparacion
        tabla[45] = ['ISNOT']  # operacion_comparacion
        
        # Regla 46: bloque ::= POLLOCRUDO instrucciones POLLOASADO
        tabla[46] = ['POLLOCRUDO', 'instrucciones', 'POLLOASADO']
        
        # Regla 47: instrucciones ::= instruccion instrucciones
        tabla[47] = ['instruccion', 'instrucciones']
        
        # Regla 48: instrucciones ::= epsilon
        tabla[48] = []
        
        # Regla 49: instruccion ::= asignacion
        tabla[49] = ['asignacion']
        
        # Regla 50: instruccion ::= ciclo
        tabla[50] = ['ciclo']
        
        # Regla 51: instruccion ::= if_then_else
        tabla[51] = ['if_then_else']
        
        # Regla 52: instruccion ::= switch
        tabla[52] = ['switch']
        
        # Regla 53: instruccion ::= with
        tabla[53] = ['with']
        
        # Regla 54: instruccion ::= break_continue_halt
        tabla[54] = ['break_continue_halt']
        
        # Regla 55: instruccion ::= return
        tabla[55] = ['return']
        
        # Regla 56: instruccion ::= size_of
        tabla[56] = ['size_of']
        
        # Regla 57: instruccion ::= entrada_estandar
        tabla[57] = ['entrada_estandar']
        
        # Regla 58: instruccion ::= salida_estandar
        tabla[58] = ['salida_estandar']
        
        # Regla 59: asignacion ::= identificador = expresion
        tabla[59] = ['identificador', '=', 'expresion']
        
        # Regla 60: expresion ::= literal
        tabla[60] = ['literal']
        
        # Regla 61: expresion ::= identificador
        tabla[61] = ['identificador']
        
        # Regla 62: expresion ::= operacion
        tabla[62] = ['operacion']
        
        # Regla 63: final ::= WORLDSAVE
        tabla[63] = ['WORLDSAVE']
        
        return tabla

    def calcular_first(self, simbolo):
        """Calcula el conjunto First para un símbolo"""
        if simbolo in self.terminales:
            return {simbolo}
        
        first = set()
        for regla in self.obtener_reglas(simbolo):
            if not regla:  # Regla epsilon
                first.add('epsilon')
            else:
                primer_simbolo = regla[0]
                if primer_simbolo in self.terminales:
                    first.add(primer_simbolo)
                else:
                    first.update(self.calcular_first(primer_simbolo))
        return first

    def calcular_follow(self, simbolo):
        """Calcula el conjunto Follow para un símbolo"""
        follow = set()
        if simbolo == self.simbolo_inicial:
            follow.add('$')  # Marca derecha

        for no_terminal in self.no_terminales:
            for regla in self.obtener_reglas(no_terminal):
                if simbolo in regla:
                    idx = regla.index(simbolo)
                    if idx < len(regla) - 1:
                        # Calcular First del resto de la regla
                        resto_first = self.calcular_first(regla[idx + 1])
                        follow.update(resto_first - {'epsilon'})
                        if 'epsilon' in resto_first:
                            follow.update(self.calcular_follow(no_terminal))
                    else:
                        follow.update(self.calcular_follow(no_terminal))
        return follow

    def calcular_predict(self, no_terminal, regla):
        """Calcula el conjunto Predict para una regla"""
        if not regla:  # Regla epsilon
            return self.calcular_follow(no_terminal)
        
        first = self.calcular_first(regla[0])
        if 'epsilon' in first:
            return first.union(self.calcular_follow(no_terminal)) - {'epsilon'}
        return first

    def obtener_reglas(self, no_terminal):
        """Obtiene todas las reglas para un no terminal"""
        return self.tabla_lados_derechos.get(no_terminal, [])

    def es_terminal(self, simbolo):
        """Determina si un símbolo es terminal"""
        return simbolo in self.terminales

    def obtener_regla(self, no_terminal, terminal):
        """Obtiene la regla de la tabla de parsing"""
        # Si el terminal es None (EOF), retornar -1
        if terminal is None:
            return -1
            
        # Si es un identificador (código 61) y el no-terminal espera un identificador
        if self.token_actual and self.token_actual.codigo == 61:
            if no_terminal == 'identificador':
                return 61
            # También verificar si el no-terminal puede derivar en un identificador
            elif no_terminal in ['expresion', 'asignacion', 'instruccion', 'instrucciones']:
                return self.tabla_parsing.get((no_terminal, 'identificador'), -1)
                
        # Si es un literal (código 50) y el no-terminal espera un literal
        elif self.token_actual and self.token_actual.codigo == 50:
            if no_terminal == 'literal':
                return 50
            # También verificar si el no-terminal puede derivar en un literal
            elif no_terminal in ['expresion']:
                return self.tabla_parsing.get((no_terminal, 'literal'), -1)
                
        # Para otros casos, intentar obtener la regla directamente
        return self.tabla_parsing.get((no_terminal, terminal), -1)

    def aplicar_regla(self, numero_regla):
        """Aplica una regla de la gramática"""
        if numero_regla in self.tabla_lados_derechos:
            # Aplicar la regla en orden inverso para mantener el orden correcto en la pila
            for simbolo in reversed(self.tabla_lados_derechos[numero_regla]):
                self.pila_parsing.append(simbolo)

    def parse(self):
        """Función principal de parsing"""
        print("Iniciando análisis sintáctico...")
        while not self.error and self.pila_parsing:
            elemento_actual = self.pila_parsing.pop()
            print(f"Analizando: {elemento_actual}")
            
            if self.es_terminal(elemento_actual):
                if not self.match(elemento_actual):
                    self.error_sintactico(f"Se esperaba {elemento_actual} pero se encontró {self.token_actual.lexema if self.token_actual else 'EOF'}")
                    self.recuperar_error()
            else:
                # Obtener el terminal actual para la búsqueda en la tabla
                terminal_actual = self.token_actual.lexema if self.token_actual else None
                regla = self.obtener_regla(elemento_actual, terminal_actual)
                
                if regla < 0:
                    self.error_sintactico(f"No hay regla para {elemento_actual} con {terminal_actual}")
                    self.recuperar_error()
                else:
                    print(f"Aplicando regla {regla} para {elemento_actual}")
                    self.aplicar_regla(regla)
        
        if not self.error:
            print("Análisis sintáctico completado exitosamente")
        else:
            print("Análisis sintáctico terminado con errores")

    def inicializar_parser(self, nombre_archivo):
        """Inicializa el parser con un archivo de entrada"""
        if self.scanner.InicializarScanner(nombre_archivo):
            self.token_actual = self.scanner.DemeToken()
            self.inicializar_pila()
            return True
        return False

    def inicializar_pila(self):
        """Inicializa la pila de parsing con el símbolo inicial"""
        self.pila_parsing = [self.simbolo_inicial]

    def match(self, terminal_esperado):
        """Verifica si el token actual coincide con el terminal esperado"""
        if not self.token_actual:
            return False
            
        # Si es un identificador (código 61) y el terminal esperado es 'identificador'
        if self.token_actual.codigo == 61 and terminal_esperado == 'identificador':
            print(f"Match: Identificador '{self.token_actual.lexema}'")
            self.token_actual = self.scanner.DemeToken()
            return True
            
        # Si es un literal (código 50) y el terminal esperado es 'literal'
        elif self.token_actual.codigo == 50 and terminal_esperado == 'literal':
            print(f"Match: Literal '{self.token_actual.lexema}'")
            self.token_actual = self.scanner.DemeToken()
            return True
            
        # Para otros casos, comparar el lexema
        elif self.token_actual.lexema == terminal_esperado:
            print(f"Match: Terminal '{self.token_actual.lexema}'")
            self.token_actual = self.scanner.DemeToken()
            return True
            
        print(f"No match: Se esperaba '{terminal_esperado}' pero se encontró '{self.token_actual.lexema}'")
        return False

    def error_sintactico(self, mensaje):
        """Maneja errores sintácticos"""
        print(f"Error sintáctico: {mensaje}")
        self.error = True

    def finalizar_parser(self):
        """Finaliza el parser y libera recursos"""
        self.scanner.FinalizarScanner()
        self.pila_parsing = []
        self.token_actual = None

    def recuperar_error(self):
        """Intenta recuperarse de un error sintáctico"""
        # Tokens de sincronización por nivel
        tokens_sincronizacion = {
            'inicio': {'WORLDSAVE'},
            'inicio2': {'WORLDSAVE'},
            'seccion': {'WORLDSAVE', 'SPAWNPOINT', 'BEDROCK', 'RESOURCEPACK', 'INVENTORY', 'RECIPE', 'CRAFTINGTABLE'},
            'punto_entrada': {'WORLDSAVE'},
            'sistema_asignacion_constante': {'WORLDSAVE', 'SPAWNPOINT', 'BEDROCK', 'RESOURCEPACK', 'INVENTORY', 'RECIPE', 'CRAFTINGTABLE'},
            'sistema_asignacion_tipos': {'WORLDSAVE', 'SPAWNPOINT', 'BEDROCK', 'RESOURCEPACK', 'INVENTORY', 'RECIPE', 'CRAFTINGTABLE'},
            'sistema_asignacion_variables': {'WORLDSAVE', 'SPAWNPOINT', 'BEDROCK', 'RESOURCEPACK', 'INVENTORY', 'RECIPE', 'CRAFTINGTABLE'},
            'bloque': {'WORLDSAVE', 'SPAWNPOINT'},
            'instrucciones': {'POLLOASADO', 'CRAFT'},
            'instruccion': {'POLLOASADO', 'CRAFT', 'identificador', 'REPEATER', 'TARGET', 'JUKEBOX', 'WITHER', 'CREEPER', 'ENDERPEARL', 'RAGEQUIT', 'RESPAWN', 'CHUNK', 'HOPPER', 'DROPPER'},
            'expresion': {';', ')'}
        }
        
        # Obtener el no-terminal actual de la pila
        no_terminal_actual = None
        for simbolo in reversed(self.pila_parsing):
            if simbolo in self.no_terminales:
                no_terminal_actual = simbolo
                break
        
        if no_terminal_actual:
            # Obtener los tokens de sincronización para este no-terminal
            tokens_sync = tokens_sincronizacion.get(no_terminal_actual, {'WORLDSAVE'})
            
            # Avanzar hasta encontrar un token de sincronización
            while self.token_actual and self.token_actual.lexema not in tokens_sync:
                print(f"Recuperando: Ignorando token '{self.token_actual.lexema}'")
                self.token_actual = self.scanner.DemeToken()
                if not self.token_actual:
                    break
            
            # Si encontramos un token de sincronización, continuamos
            if self.token_actual:
                print(f"Recuperado: Encontrado token de sincronización '{self.token_actual.lexema}'")
                # Limpiar la pila hasta encontrar un no-terminal que pueda seguir
                while self.pila_parsing and self.es_terminal(self.pila_parsing[-1]):
                    self.pila_parsing.pop()
                
                # Si la pila está vacía, reinicializamos con el símbolo inicial
                if not self.pila_parsing:
                    self.inicializar_pila()
            else:
                print("Error: Fin de archivo inesperado durante la recuperación")
                self.error = True
        else:
            print("Error: No se pudo determinar el no-terminal actual para la recuperación")
            self.error = True

# Ejemplo de uso
if __name__ == "__main__":
    parser = Parser()
    if parser.inicializar_parser("/prueba.ne"):
        parser.parse()
        parser.finalizar_parser()
