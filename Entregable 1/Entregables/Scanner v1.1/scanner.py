import os

'''
Etapa dos: Analizador Léxico
Grupo: 1
Integrantes:
- David Acuña López - 2020426228
- Deylan Sandoval Sanchez - 2020234274

Este es un analizador léxico para Minecraft, que se encarga de leer un archivo de texto y 
generar una lista de tokens.
'''

transiciones = {
    # Estado 0: WORLDNAME, BEDROCK, RESOURCEPACK, INVENTORY, RECIPE, CRAFTINGTABLE
    0: {' ': 100},
    # Estado 1: SPAWNPOINT
    1: {' ': 100},
    # Estado 2: 
    2: {' ': 100},
    # Estado 3: 
    3: {' ': 100},
    # Estado 4: 
    4: {' ': 100},
    # Estado 5: 
    5: {' ': 100},
    # Estado 6: 
    6: {' ': 100},
    # Estado 7: 
    7: {' ': 100},
    # Estado 8: OBSIDIAN
    8: {' ': 100},
    # Estado 9: ANVIL
    9: {' ': 100},
    # Estado 10: STACK
    10: {' ': 100},
    # Estado 11: RUNE
    11: {' ': 100},
    # Estado 12: SPIDER
    12: {' ': 100},
    # Estado 13: TORCH
    13: {' ': 100},
    # Estado 14: CHEST
    14: {' ': 100},
    # Estado 15: BOOK
    15: {' ': 100},
    # Estado 16: GHAST
    16: {' ': 100},
    # Estado 17: SHELF
    17: {' ': 100},
    # Estado 18: ENTITY
    18: {' ': 100},
    # Estado 19: ON / OFF
    19: {' ': 100},
    # Estado 20: SOULSAND / MAGMA
    20: {' ': 100},
    # Estado 21: ISENGRAVED / ISINSCRIBED / ETCUP / ETCHDOWN
    21: {' ': 100},
    # Estado 22: AND / OR / NOT / XOR
    22: {' ': 100},
    # Estado 23: BIND / FROM / EXCEPT / SEEK
    23: {' ': 100},
    # Estado 24: ADD / DROP / ITEM / FEED / MAP / BIOM / KILL
    24: {' ': 100},
    # Estado 25: IS / ISNOT
    25: {' ': 100},
    # Estado 26: POLLOCRUDO
    26: {' ': 100},
    # Estado 27: POLLOASADO
    27: {' ': 100},
    # Estado 28: REPEATER
    28: {' ': 100},
    # Estado 29: CRAFT
    29: {' ': 100},
    # Estado 30: TARGET
    30: {' ': 100},
    # Estado 31: HIT
    31: {' ': 100},
    # Estado 32: MISS
    32: {' ': 100},
    # Estado 33: JUKEBOX
    33: {' ': 100},
    # Estado 34: DISK
    34: {' ': 100},
    # Estado 35: SPAWNER
    35: {' ': 100},
    # Estado 36: EXHAUSTED
    36: {' ': 100},
    # Estado 37: WALK
    37: {' ': 100},
    # Estado 38: SET
    38: {' ': 100},
    # Estado 39: TO
    39: {' ': 100},
    # Estado 40: STEP
    40: {' ': 100},
    # Estado 41: WITHER
    41: {' ': 100},
    # Estado 42: CREEPER / ENDERPEARL / RAGEQUIT
    42: {' ': 100},
    # Estado 43: SPELL
    43: {' ': 100},
    # Estado 44: RITUAL
    44: {' ': 100},
    # Estado 45: RESPAWN
    45: {' ': 100},
    # Estado 46: CHUNK
    46: {' ': 100},
    # Estado 47: HOPPER
    47: {' ': 100},
    # Estado 48: DROPPER
    48: {' ': 100},
    # Estado 49: WORLDSAVE
    49: {' ': 100},
    # Estado 50: Numeros
    50: {' ': 100},
    # Estado 51: Identificadores
    51: {' ': 100},
    # Estado 52: Asignacion
    52: {' ': 100, '+': 52, '-': 52, '*': 52, '/': 52, '%': 52},
    # Estado 53: Operaciones aritmeticas
    53: {' ': 100},
    # Estado 54: Operaciones de comparacion
    54: {' ': 100, '=': 54},
    # Estado 55: Terminador
    55: {' ': 100},
    # Estado 56: Coma
    56: {' ': 100},
    # Estado 57: Abre parentesis
    57: {' ': 100},
    # Estado 58: Cierra parentesis
    58: {' ': 100},
    # Estado 59: Abre llave
    59: {' ': 100},
    # Estado 60: Cierra llave
    60: {' ': 100},
    # Separador
    61: {' ': 100},
    # terminador
    61: {' ': 100},

    100: {' ': 100, '\n': 100, 'w': 101, 'b': 110, 'r': 118, 'i': 130, 'c': 143, 's': 156, 'o': 166, 'a': 174, 't': 190, 'g': 202, 'e': 211, 'm': 227, 'n': 263, 'x': 266, 'f': 272, 'd': 283, 'k': 297, 'p': 304, 'h': 330, 'j': 336,
        # Espacios y saltos de línea
        '1': 50, '2': 50, '3': 50, '4': 50, '5': 50, '6': 50, '7': 50, '8': 50, '9': 50, '0': 50,  
        # Asignacion y aritmetica
        '=': 52, 
        #Operaciones aritmeticas
        '+': 53, '-': 53, '*': 53, '/': 53, '%': 53,
        # Operacores de comparacion
        '<': 54, '>': 54, 
        #terminador
        ';': 61, ':': 61,
        # Abre parentesis
        '(': 57, 
        # Cierra parentesis
        ')': 58,
        # Abre llave
        '{': 59,
        # Cierra llave
        '}': 60,
        },

    # worldname
    101: {'o': 102, 'a': 255, 'i': 261}, 
    102: {'r': 103}, 
    103: {'l': 104}, 
    104: {'d': 105}, 
    105: {'n': 106, 's': 409}, 
    106: {'a': 107}, 
    107: {'m': 108},
    108: {'e': 0},
    # bedrock
    110: {'e': 111, 'o': 199, 'i': 269}, 
    111: {'d': 112}, 
    112: {'r': 113}, 
    113: {'o': 114}, 
    114: {'c': 115},
    115: {'k': 0},
    # resourcepack
    118: {'e': 119, 'u': 183, 'a': 279, 'i': 289}, 
    119: {'s': 120, 'c': 139, 'p': 219}, 
    120: {'o': 121, 'p': 294}, 
    121: {'u': 122}, 
    122: {'r': 123}, 
    123: {'c': 124}, 
    124: {'e': 125}, 
    125: {'p': 126}, 
    126: {'a': 127}, 
    127: {'c': 128},
    128: {'k': 0},
    # inventory
    130: {'n': 131, 's': 232, 't': 288}, 
    131: {'v': 132}, 
    132: {'e': 133}, 
    133: {'n': 134}, 
    134: {'t': 135}, 
    135: {'o': 136}, 
    136: {'r': 137},
    137: {'y': 0},
    # recipe
    139: {'i': 140}, 
    140: {'p': 141},
    141: {'e': 0},
    # craftingtable
    143: {'r': 144, 'h': 195}, 
    144: {'a': 145, 'e': 266}, 
    145: {'f': 146}, 
    146: {'t': 147}, 
    147: {'i': 148, ' ': 29}, 
    148: {'n': 149}, 
    149: {'g': 150}, 
    150: {'t': 151}, 
    151: {'a': 152}, 
    152: {'b': 153}, 
    153: {'l': 154},
    154: {'e': 0},
    # spawnpoint
    156: {'p': 157, 't': 179, 'h': 207, 'o': 220, 'e': 280}, 
    157: {'a': 158, 'i': 186, 'e': 286}, 
    158: {'w': 159}, 
    159: {'n': 160}, 
    160: {'p': 161, 'e': 246}, 
    161: {'o': 162}, 
    162: {'i': 163}, 
    163: {'n': 164},
    164: {'t': 1},
    # obsidian
    166: {'b': 167, 'n': 19, 'f': 216, 'r': 22}, 
    167: {'s': 168}, 
    168: {'i': 169}, 
    169: {'d': 170}, 
    170: {'i': 171}, 
    171: {'a': 172},
    172: {'n': 0},
    # anvil
    174: {'n': 175, 'd': 283}, 
    175: {'v': 176, 'd': 22}, 
    176: {'i': 177},
    177: {'l': 0},
    # stack
    179: {'a': 180, 'e': 259}, 
    180: {'c': 181},
    181: {'k': 0},
    # rune
    183: {'n': 184},
    184: {'e': 0},
    # spider
    186: {'d': 187}, 
    187: {'e': 188},
    188: {'r': 0},
    # torch
    190: {'o': 191, 'a': 225}, 
    191: {'r': 192, ' ': 39}, 
    192: {'c': 193},
    193: {'h': 0},
    # chest
    195: {'e': 196, 'u': 298}, 
    196: {'s': 197},
    197: {'t': 0},
    # book
    199: {'o': 200},
    200: {'k': 0},
    # ghast
    202: {'h': 203}, 
    203: {'a': 204}, 
    204: {'s': 205},
    205: {'t': 0},
    # shelf
    207: {'e': 208}, 
    208: {'l': 209},
    209: {'f': 0},
    # entity
    211: {'n': 212, 't': 250, 'x': 276}, 
    212: {'t': 213, 'd': 271}, 
    213: {'i': 214}, 
    214: {'t': 215},
    215: {'y': 0},
    # on
    #19

    # off
    216: {'f': 0},

    # soulsand
    220: {'u': 221}, 
    221: {'l': 222}, 
    222: {'s': 223},
    223: {'a': 224},
    224: {'n': 225},
    225: {'d': 0},
    # magma
    227: {'a': 228, 'i': 233}, 
    228: {'g': 229, 'p': 24}, 
    229: {'m': 230},
    230: {'a': 0},
    # isengraved
    232: {'e': 233, 'i': 241, ' ': 25, 'n': 301}, 
    233: {'n': 234}, 
    234: {'g': 235}, 
    235: {'r': 236}, 
    236: {'a': 237}, 
    237: {'v': 238}, 
    238: {'e': 239}, #21
    239: {'d': 0},
    # isinscribed
    241: {'n': 242}, 
    242: {'s': 243}, 
    243: {'c': 244}, 
    244: {'r': 245}, 
    245: {'i': 246}, 
    246: {'b': 247}, 
    247: {'e': 248},
    248: {'d': 0},

    # etchup
    250: {'c': 251}, 
    251: {'h': 252}, 
    252: {'u': 253, 'd': 255},
    253: {'p': 0},

    # etchdown
    255: {'o': 256}, 
    256: {'w': 257},
    257: {'n': 0},
    # and
    259: {' ': 100},
    # or
    262: {' ': 100},
    # not
    263: {'o': 264},
    264: {'t': 0},
    # xor
    266: {'o': 267},
    267: {'r': 0},
    # bind
    269: {'n': 270, 'o': 294},
    270: {'d': 0},
    # from
    272: {'r': 273, 'e': 291, 'e': 291}, 
    273: {'o': 274},
    274: {'m': 0},
    # except
    276: {'c': 277, 'h': 248}, 
    277: {'e': 278},
    278: {'p': 279},
    279: {'t': 0},
    # seek
    280: {'e': 281, 't': 38},
    281: {'k': 0},

    # add
    283: {'d': 0, 'i': 243, 'r': 285}, 
    284: {' ': 100},
    # drop
    285: {'o': 286}, 
    286: {'p': 0},
    #este no se si tengo que borrarlo
    287: {'p': 306},
    # item
    288: {'e': 289},
    289: {'m': 0},
    # feed
    291: {'e': 292}, 
    292: {'d': 0},
    # map
    293: {'p': 0},

    # biom
    294: {'m': 0},

    # kill
    297: {'i': 298}, 
    298: {'l': 299},
    299: {'l': 0},
    # is -> 232
    
    # isnot
    301: {'o': 302}, 
    302: {'t': 0},
    # pollocrudo
    304: {'o': 305}, 
    305: {'l': 306}, 
    306: {'l': 307}, 
    307: {'o': 308}, 
    308: {'c': 309, 'a': 314}, 
    309: {'r': 310}, 
    310: {'u': 311}, 
    311: {'d': 312}, 
    312: {'o': 0},
    # polloasado
    314: {'s': 315}, 
    315: {'a': 316}, 
    316: {'d': 317}, 
    317: {'o': 0},
    # repeater
    319: {'e': 320}, 
    320: {'a': 321}, 
    321: {'t': 322}, 
    322: {'e': 323}, 
    323: {'r': 0},
    # craft -> 143

    # target
    325: {'r': 326}, 
    326: {'g': 327}, 
    327: {'e': 328}, 
    328: {'t': 0},
    # hit
    330: {'i': 331, 'o': 301}, 
    331: {'t': 0},
    # miss
    333: {'s': 334}, 
    334: {'s': 0},
    # jukebox
    336: {'u': 337}, 
    337: {'k': 338}, 
    338: {'e': 339}, 
    339: {'b': 340}, 
    340: {'o': 341}, 
    341: {'x': 0},
    # disk
    343: {'s': 344}, 
    344: {'k': 0},
    # spawner
    346: {'r': 0},
    # exhausted
    348: {'a': 349}, 
    349: {'u': 350}, 
    350: {'s': 351}, 
    351: {'t': 352}, 
    352: {'e': 353}, 
    353: {'d': 0},
    # walk
    355: {'l': 356}, 
    356: {'k': 0},
    # set -> 280

    # to -> 190

    # step
    359: {'p': 0},
    # wither
    361: {'t': 362}, 
    362: {'h': 363}, 
    363: {'e': 364}, 
    364: {'r': 0},
    # creeper
    366: {'e': 367}, 
    367: {'p': 368}, 
    368: {'e': 369}, 
    369: {'r': 0},
    # enderpearl
    371: {'e': 372}, 
    372: {'r': 373}, 
    373: {'p': 374}, 
    374: {'e': 375}, 
    375: {'a': 376}, 
    376: {'r': 377}, 
    377: {'l': 0},
    # ragequit
    379: {'g': 380}, 
    380: {'e': 381}, 
    381: {'q': 382}, 
    382: {'u': 383}, 
    383: {'i': 384}, 
    384: {'t': 0},
    # spell
    386: {'l': 387}, 
    387: {'l': 0},
    # ritual
    389: {'t': 390}, 
    390: {'u': 391}, 
    391: {'a': 392}, 
    392: {'l': 0},
    # respawn
    394: {'a': 395}, 
    395: {'w': 396}, 
    396: {'n': 0},
    # chunk
    398: {'n': 399}, 
    399: {'k': 0},
    # hopper
    401: {'p': 402}, 
    402: {'p': 403}, 
    403: {'e': 404}, 
    404: {'r': 0},
    # dropper
    406: {'e': 407}, 
    407: {'r': 0},
    # worldsave
    409: {'a': 410}, 
    410: {'v': 411}, 
    411: {'e': 0},

    # disk
    413: {' ': 100},
}

class Token:
    def __init__(self, codigo, lexema, linea, col_inicio, col_final):
        self.codigo = codigo     # Código numérico del tipo de token
        self.tipo = "no_definido"          
        self.lexema = lexema     # El valor real del token
        self.linea = linea       # Línea donde aparece el token
        self.col_inicio = col_inicio  # Columna de inicio del token
        self.col_final = col_final  # Columna de fin del token
        self.error = False  # Bandera para indicar si hubo un error en el token
        self.aprobado = False  # Bandera para indicar si el token fue aprobado

    def __str__(self):
        return f"({self.codigo}, '{self.lexema}', Linea: {self.linea}, Columna: {self.col_inicio}-{self.col_final})"


class AnalizadorLexico:
    def __init__(self):
        self.nombre_archivo = None
        self.buffer = ""
        self.position = 0
        self.linea = 1
        self.columna = 0
        self.tokens = []  # Lista para almacenar los tokens generados

    def InicializarScanner(self, nombre_archivo):
        # Verificar si el archivo tiene la extensión .ne
        if not nombre_archivo.endswith(".ne"):
            print(f"Error: El archivo {nombre_archivo} no tiene la extensión .ne")
            return False
        
        # Guardar el nombre del archivo
        self.nombre_archivo = nombre_archivo
        
        # Abrimos el archivo
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                self.buffer = archivo.read()  # Leer todo el contenido del archivo
                print(f"Éxito: El archivo {nombre_archivo} ha sido abierto correctamente.")
                # print(self.buffer)
                return True
        except FileNotFoundError:
            print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
            return False
        except Exception as e:
            print(f"Error: Ocurrió un problema al intentar abrir el archivo: {e}")
            return False

    def FinalizarScanner(self):
        """
        Finaliza el scanner y libera todos los recursos utilizados.
        Reinicia todas las variables de estado a sus valores iniciales.
        """
        try:
            # Limpiar el buffer y la posición
            self.buffer = ""
            self.position = 100
            
            # Reiniciar contadores
            self.linea = 1
            self.columna = 0
            
            # Limpiar la lista de tokens
            self.tokens.clear()
            
            # Reiniciar el nombre del archivo
            self.nombre_archivo = None
            
            print("El scanner ha sido finalizado y los recursos han sido liberados correctamente.")
            return True
        except Exception as e:
            print(f"Error al finalizar el scanner: {str(e)}")
            return False

    def DemeElSiguienteCaracter(self):
        """
        Obtiene el siguiente carácter del buffer y actualiza la posición actual.
        
        Returns:
            str: El siguiente carácter del buffer, o None si se ha llegado al final.
            
        Raises:
            ValueError: Si el buffer no está inicializado.
        """
        try:
            # Verificar si el buffer está inicializado
            if not hasattr(self, 'buffer') or self.buffer is None:
                raise ValueError("El buffer no está inicializado")
            
            # Verificar si hay más caracteres para leer
            if self.position < len(self.buffer):
                # Obtener el carácter actual
                char = self.buffer[self.position]
                
                # Actualizar la posición
                self.position += 1
                self.columna += 1
                
                # Manejar saltos de línea
                if char == "\n":
                    self.linea += 1
                    self.columna = 0
                    print(f"Línea {self.linea}: Nueva línea detectada")
                
                # Manejar caracteres especiales
                if char.isspace() and char != "\n":
                    print(f"Línea {self.linea}, Columna {self.columna}: Espacio en blanco")
                
                return char
            
            # Si llegamos al final del buffer
            print(f"Fin del archivo alcanzado en línea {self.linea}, columna {self.columna}")
            return None
            
        except Exception as e:
            print(f"Error al leer el siguiente carácter: {str(e)}")
            return None
    
    def TomeEsteCaracter(self):
        """
        Retrocede un carácter en el buffer y actualiza la posición actual.
        Útil para deshacer la lectura de un carácter cuando no es parte del lexema actual.
        
        Returns:
            str: El carácter anterior en el buffer, o None si no se puede retroceder.
            
        Raises:
            ValueError: Si el buffer no está inicializado o la posición es inválida.
        """
        try:
            # Verificar si el buffer está inicializado
            if not hasattr(self, 'buffer') or self.buffer is None:
                raise ValueError("El buffer no está inicializado")
            
            # Verificar si podemos retroceder
            if self.position <= 0:
                print("No se puede retroceder más allá del inicio del buffer")
                return None
                
            # Obtener el carácter anterior
            char = self.buffer[self.position - 1]
            
            # Actualizar la posición
            self.position -= 1
            self.columna -= 1
            
            # Manejar saltos de línea al retroceder
            if char == '\n':
                self.linea -= 1
                # Calcular la columna correcta al retroceder una línea
                # Buscar el último salto de línea anterior
                last_newline = self.buffer.rfind('\n', 0, self.position)
                if last_newline != -1:
                    self.columna = self.position - last_newline - 1
                else:
                    self.columna = self.position
                print(f"Retrocediendo a línea {self.linea}, columna {self.columna}")
            
            print(f"Carácter '{char}' retrocedido en línea {self.linea}, columna {self.columna}")
            return char
            
        except Exception as e:
            print(f"Error al retroceder el carácter: {str(e)}")
            return None
    
    def demeTokenError(self, token, codigo):
        """
        Maneja diferentes tipos de errores en los tokens.
        
        Args:
            token: El token que contiene el error (pasado por referencia)
            codigo: Código de error específico (-1 a -8)
        """
        token.error = True
        token.codigo = codigo
        
        if codigo == -1:
            # Error: Identificador no válido
            token.tipo = "ERROR_IDENTIFICADOR"
            pass
            
        elif codigo == -2:
            # Error: Símbolo mal colocado
            token.tipo = "ERROR_SIMBOLO"
            pass
            
        elif codigo == -3:
            # Error: Comentario no cerrado
            token.tipo = "ERROR_COMENTARIO"
            pass
            
        elif codigo == -4:
            # Error: Número no válido
            token.tipo = "ERROR_NUMERO"
            pass
            
        elif codigo == -5:
            # Error: Palabra reservada no válida
            token.tipo = "ERROR_PALABRA_RESERVADA"
            pass
            
        elif codigo == -6:
            # Error: Operador no válido
            token.tipo = "ERROR_OPERADOR"
            pass
            
        elif codigo == -7:
            # Error: Carácter no reconocido
            token.tipo = "ERROR_CARACTER"
            pass
            
        elif codigo == -8:
            # Error: Fin de archivo inesperado
            token.tipo = "ERROR_EOF"
            pass

    def DemeToken(self):
        # Esta funcion va a ser como el analizador lexico, que va a ir leyendo el buffer y devolviendo tokens
        # Utilizara el DemeElSiguienteCaracter y el TomeEsteCaracter para ir leyendo el buffer
        # y devolviendo tokens
        lexema = ""
        estado_actual = 100  # Comienza en el estado inicial

        token = Token(99, "", self.linea, self.columna, self.columna)  # Inicializamos el token
        while True:
            char = self.DemeElSiguienteCaracter()

            # Si el caracter es None, significa que el buffer 
            # ha sido leido completamente
            if char is None:
                if token.lexema != "":
                    #significa que es el final del archivo
                    self.tokens.append(token)  
                return token
            
            # Si el caracter es $, significa que es un comentario
            if char == '$':
                lexema += char
                char = self.DemeElSiguienteCaracter()
                if char == '$' or char == '*':
                    lexema += char
                    continue
                else:
                    # ERROR: Simbolo mal colocado
                    self.demeTokenError(token, -2)
                    self.tokens.append(token) 
                    print(f"Error: Caracter '{char}' no válido después de '$'")
                    return token

            # Manejo de comentarios de línea ($$)
            if lexema == "$$":
                if char == "\n":
                    lexema = ""
                    token.col_inicio = self.columna
                    token.col_final = self.columna
                continue

            # Manejo de comentarios de bloque ($*)
            if lexema == "$*":
                if char == "*":
                    char = self.DemeElSiguienteCaracter()
                    if char == "$":
                        lexema = ""
                        token.col_inicio = self.columna
                        token.col_final = self.columna
                continue
            
            # Caracter clave, este reconoce si el lexema es valido o no
            # Tambien reconoce si simplemente se esta haciendo un espacio si el lexema se encuentra vacío
            if char == ' ':
                try:
                    if token.lexema != "" and ' ' in transiciones[estado_actual]:
                        token.codigo = estado_actual
                        token.aprobado = True
                        break

                    elif token.lexema != "" and not (' ' in transiciones[estado_actual]):
                        print(f"Error: Lexema {token.lexema} no válido")
                        return token
                    token.col_inicio = self.columna
                    token.col_final = self.columna
                    continue
                except Exception as e:
                    if token.lexema != "" and transiciones[estado_actual][' '] == 100:
                        break
                    else:
                        print(f"Error: Lexema {token.lexema} no válido")
                        return token

            elif char == '\n':
                try:
                    if token.lexema != "" and '\n' in transiciones[estado_actual]:
                        #Corregir esta parte para que lance un error por saltos de linea
                        if transiciones[estado_actual]['\n'] != 100:
                            token.codigo = transiciones[estado_actual]['\n']
                        break
                        # *****************************
                        
                    elif token.lexema != "" and not ('\n' in transiciones[estado_actual]):
                        print(f"Error: Lexema {token.lexema} no válido")
                        return token
                    token.col_inicio = self.columna
                    token.col_final = self.columna
                    continue
                except Exception as e:
                    if token.lexema != "" and transiciones[estado_actual]['\n'] == 100:
                        break
                    else:
                        print(f"Error: Lexema {token.lexema} no válido")
                        return token

            # Consultamos la tabla de transiciones según el estado actual
            if char in transiciones[estado_actual]:
                estado_actual = transiciones[estado_actual][char]
                if estado_actual != 100:
                    lexema += char  # Formamos el lexema
                    token.lexema = lexema  # Agregamos el caracter al lexema
                    token.col_final = self.columna  # Actualizamos la columna final del token
                    token.linea = self.linea
                    token.codigo = estado_actual  # Actualizamos el código del token
                
            else:
                while char != ' ' and char != '\n' and char != None:
                    lexema += char
                    char = self.DemeElSiguienteCaracter()
                    
                if char == ' ' or char == '\n':
                    if lexema.isidentifier():
                        token.codigo = 51
                    else:
                        token.codigo = -1
                if char is None:
                    return token
                token.lexema = lexema
                break
                    
         

        token.lexema = token.lexema.upper()
        self.tokens.append(token)  # Agregamos el token a la lista de tokens
        return token
    
    def definirTipo():
        pass
    
    def imprimirTokens(self):
        # Imprimimos los tokens generados
        for token in self.tokens:
            print(token)

    def TomeToken(self):
        pass

