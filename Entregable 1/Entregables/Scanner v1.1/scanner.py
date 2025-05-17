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
    0: {' ': 0, '\n': 0, 'w': 101, 'b': 110, 'r': 118, 'i': 130, 'c': 143, 's': 156, 'o': 166, 'a': 174, 't': 190, 'g': 202, 'e': 211, 'm': 227, 'n': 263, 'x': 266, 'f': 272, 'd': 283, 'k': 297, 'p': 304, 'h': 330, 'j': 336,
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

    # Estado 1: WORLDNAME, BEDROCK, RESOURCEPACK, INVENTORY, RECIPE, CRAFTINGTABLE
    1: {' ': 0},
    # Estado 2: SPAWNPOINT
    2: {' ': 0},
    # Estado 3: 
    3: {' ': 0},
    # Estado 4: 
    4: {' ': 0},
    # Estado 5: 
    5: {' ': 0},
    # Estado 6: 
    6: {' ': 0},
    # Estado 7: 
    7: {' ': 0},
    # Estado 8: OBSIDIAN
    8: {' ': 0},
    # Estado 9: ANVIL
    9: {' ': 0},
    # Estado 10: STACK
    10: {' ': 0},
    # Estado 11: RUNE
    11: {' ': 0},
    # Estado 12: SPIDER
    12: {' ': 0},
    # Estado 13: TORCH
    13: {' ': 0},
    # Estado 14: CHEST
    14: {' ': 0},
    # Estado 15: BOOK
    15: {' ': 0},
    # Estado 16: GHAST
    16: {' ': 0},
    # Estado 17: SHELF
    17: {' ': 0},
    # Estado 18: ENTITY
    18: {' ': 0},
    # Estado 19: ON / OFF
    19: {' ': 0},
    # Estado 20: SOULSAND / MAGMA
    20: {' ': 0},
    # Estado 21: ISENGRAVED / ISINSCRIBED / ETCUP / ETCHDOWN
    21: {' ': 0},
    # Estado 22: AND / OR / NOT / XOR
    22: {' ': 0},
    # Estado 23: BIND / FROM / EXCEPT / SEEK
    23: {' ': 0},
    # Estado 24: ADD / DROP / ITEM / FEED / MAP / BIOM / KILL
    24: {' ': 0},
    # Estado 25: IS / ISNOT
    25: {' ': 0},
    # Estado 26: POLLOCRUDO
    26: {' ': 0},
    # Estado 27: POLLOASADO
    27: {' ': 0},
    # Estado 28: REPEATER
    28: {' ': 0},
    # Estado 29: CRAFT
    29: {' ': 0},
    # Estado 30: TARGET
    30: {' ': 0},
    # Estado 31: HIT
    31: {' ': 0},
    # Estado 32: MISS
    32: {' ': 0},
    # Estado 33: JUKEBOX
    33: {' ': 0},
    # Estado 34: DISK
    34: {' ': 0},
    # Estado 35: SPAWNER
    35: {' ': 0},
    # Estado 36: EXHAUSTED
    36: {' ': 0},
    # Estado 37: WALK
    37: {' ': 0},
    # Estado 38: SET
    38: {' ': 0},
    # Estado 39: TO
    39: {' ': 0},
    # Estado 40: STEP
    40: {' ': 0},
    # Estado 41: WITHER
    41: {' ': 0},
    # Estado 42: CREEPER / ENDERPEARL / RAGEQUIT
    42: {' ': 0},
    # Estado 43: SPELL
    43: {' ': 0},
    # Estado 44: RITUAL
    44: {' ': 0},
    # Estado 45: RESPAWN
    45: {' ': 0},
    # Estado 46: CHUNK
    46: {' ': 0},
    # Estado 47: HOPPER
    47: {' ': 0},
    # Estado 48: DROPPER
    48: {' ': 0},
    # Estado 49: WORLDSAVE
    49: {' ': 0},
    # Estado 50: Numeros
    50: {' ': 0},
    # Estado 51: Identificadores
    51: {' ': 0},
    # Estado 52: Asignacion
    52: {' ': 0, '+': 52, '-': 52, '*': 52, '/': 52, '%': 52},
    # Estado 53: Operaciones aritmeticas
    53: {' ': 0},
    # Estado 54: Operaciones de comparacion
    54: {' ': 0, '=': 54},
    # Estado 55: Terminador
    55: {' ': 0},
    # Estado 56: Coma
    56: {' ': 0},
    # Estado 57: Abre parentesis
    57: {' ': 0},
    # Estado 58: Cierra parentesis
    58: {' ': 0},
    # Estado 59: Abre llave
    59: {' ': 0},
    # Estado 60: Cierra llave
    60: {' ': 0},
    # Separador
    61: {' ': 0},
    # terminador
    61: {' ': 0},

    # worldname
    101: {'o': 102, 'a': 255, 'i': 261}, 
    102: {'r': 103}, 
    103: {'l': 104}, 
    104: {'d': 105}, 
    105: {'n': 106, 's': 409}, 
    106: {'a': 107}, 
    107: {'m': 108},
    108: {'e': 1},
    # bedrock
    110: {'e': 111, 'o': 199, 'i': 269}, 
    111: {'d': 112}, 
    112: {'r': 113}, 
    113: {'o': 114}, 
    114: {'c': 115},
    115: {'k': 1},
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
    128: {'k': 1},
    # inventory
    130: {'n': 131, 's': 232, 't': 288}, 
    131: {'v': 132}, 
    132: {'e': 133}, 
    133: {'n': 134}, 
    134: {'t': 135}, 
    135: {'o': 136}, 
    136: {'r': 137},
    137: {'y': 1},
    # recipe
    139: {'i': 140}, 
    140: {'p': 141},
    141: {'e': 1},
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
    154: {'e': 1},
    # spawnpoint
    156: {'p': 157, 't': 179, 'h': 207, 'o': 220, 'e': 280}, 
    157: {'a': 158, 'i': 186, 'e': 286}, 
    158: {'w': 159}, 
    159: {'n': 160}, 
    160: {'p': 161, 'e': 246}, 
    161: {'o': 162}, 
    162: {'i': 163}, 
    163: {'n': 164},
    164: {'t': 2},
    # obsidian
    166: {'b': 167, 'n': 19, 'f': 216, 'r': 22}, 
    167: {'s': 168}, 
    168: {'i': 169}, 
    169: {'d': 170}, 
    170: {'i': 171}, 
    171: {'a': 172},
    172: {'n': 8},
    # anvil
    174: {'n': 175, 'd': 283}, 
    175: {'v': 176, 'd': 22}, 
    176: {'i': 177},
    177: {'l': 9},
    # stack
    179: {'a': 180, 'e': 259}, 
    180: {'c': 181},
    181: {'k': 10},
    # rune
    183: {'n': 184},
    184: {'e': 11},
    # spider
    186: {'d': 187}, 
    187: {'e': 188},
    188: {'r': 12},
    # torch
    190: {'o': 191, 'a': 225}, 
    191: {'r': 192, ' ': 39}, 
    192: {'c': 193},
    193: {'h': 13},
    # chest
    195: {'e': 196, 'u': 298}, 
    196: {'s': 197},
    197: {'t': 14},
    # book
    199: {'o': 200},
    200: {'k': 15},
    # ghast
    202: {'h': 203}, 
    203: {'a': 204}, 
    204: {'s': 205},
    205: {'t': 16},
    # shelf
    207: {'e': 208}, 
    208: {'l': 209},
    209: {'f': 17},
    # entity
    211: {'n': 212, 't': 250, 'x': 276}, 
    212: {'t': 213, 'd': 271}, 
    213: {'i': 214}, 
    214: {'t': 215},
    215: {'y': 18},
    # on
    #19

    # off
    216: {'f': 19},

    # soulsand
    220: {'u': 221}, 
    221: {'l': 222}, 
    222: {'s': 223},
    223: {'a': 224},
    224: {'n': 225},
    225: {'d': 20},
    # magma
    227: {'a': 228, 'i': 233}, 
    228: {'g': 229, 'p': 24}, 
    229: {'m': 230},
    230: {'a': 20},
    # isengraved
    232: {'e': 233, 'i': 241, ' ': 25, 'n': 301}, 
    233: {'n': 234}, 
    234: {'g': 235}, 
    235: {'r': 236}, 
    236: {'a': 237}, 
    237: {'v': 238}, 
    238: {'e': 239}, #21
    239: {'d': 21},
    # isinscribed
    241: {'n': 242}, 
    242: {'s': 243}, 
    243: {'c': 244}, 
    244: {'r': 245}, 
    245: {'i': 246}, 
    246: {'b': 247}, 
    247: {'e': 248},
    248: {'d': 21},

    # etchup
    250: {'c': 251}, 
    251: {'h': 252}, 
    252: {'u': 253, 'd': 255},
    253: {'p': 21},

    # etchdown
    255: {'o': 256}, 
    256: {'w': 257},
    257: {'n': 21},
    # and
    259: {' ': 0},
    # or
    262: {' ': 0},
    # not
    263: {'o': 264},
    264: {'t': 22},
    # xor
    266: {'o': 267},
    267: {'r': 22},
    # bind
    269: {'n': 270, 'o': 294},
    270: {'d': 23},
    # from
    272: {'r': 273, 'e': 291, 'e': 291}, 
    273: {'o': 274},
    274: {'m': 23},
    # except
    276: {'c': 277, 'h': 248}, 
    277: {'e': 278},
    278: {'p': 279},
    279: {'t': 23},
    # seek
    280: {'e': 281, 't': 38},
    281: {'k': 23},

    # add
    283: {'d': 24, 'i': 243, 'r': 285}, 
    284: {' ': 0},
    # drop
    285: {'o': 286}, 
    286: {'p': 24},
    #este no se si tengo que borrarlo
    287: {'p': 306},
    # item
    288: {'e': 289},
    289: {'m': 24},
    # feed
    291: {'e': 292}, 
    292: {'d': 24},
    # map
    293: {'p': 24},

    # biom
    294: {'m': 24},

    # kill
    297: {'i': 298}, 
    298: {'l': 299},
    299: {'l': 24},
    # is -> 232
    
    # isnot
    301: {'o': 302}, 
    302: {'t': 25},
    # pollocrudo
    304: {'o': 305}, 
    305: {'l': 306}, 
    306: {'l': 307}, 
    307: {'o': 308}, 
    308: {'c': 309, 'a': 314}, 
    309: {'r': 310}, 
    310: {'u': 311}, 
    311: {'d': 312}, 
    312: {'o': 26},
    # polloasado
    314: {'s': 315}, 
    315: {'a': 316}, 
    316: {'d': 317}, 
    317: {'o': 27},
    # repeater
    319: {'e': 320}, 
    320: {'a': 321}, 
    321: {'t': 322}, 
    322: {'e': 323}, 
    323: {'r': 28},
    # craft -> 143

    # target
    325: {'r': 326}, 
    326: {'g': 327}, 
    327: {'e': 328}, 
    328: {'t': 30},
    # hit
    330: {'i': 331, 'o': 301}, 
    331: {'t': 31},
    # miss
    333: {'s': 334}, 
    334: {'s': 32},
    # jukebox
    336: {'u': 337}, 
    337: {'k': 338}, 
    338: {'e': 339}, 
    339: {'b': 340}, 
    340: {'o': 341}, 
    341: {'x': 33},
    # disk
    343: {'s': 344}, 
    344: {'k': 34},
    # spawner
    346: {'r': 35},
    # exhausted
    348: {'a': 349}, 
    349: {'u': 350}, 
    350: {'s': 351}, 
    351: {'t': 352}, 
    352: {'e': 353}, 
    353: {'d': 36},
    # walk
    355: {'l': 356}, 
    356: {'k': 37},
    # set -> 280

    # to -> 190

    # step
    359: {'p': 40},
    # wither
    361: {'t': 362}, 
    362: {'h': 363}, 
    363: {'e': 364}, 
    364: {'r': 41},
    # creeper
    366: {'e': 367}, 
    367: {'p': 368}, 
    368: {'e': 369}, 
    369: {'r': 42},
    # enderpearl
    371: {'e': 372}, 
    372: {'r': 373}, 
    373: {'p': 374}, 
    374: {'e': 375}, 
    375: {'a': 376}, 
    376: {'r': 377}, 
    377: {'l': 42},
    # ragequit
    379: {'g': 380}, 
    380: {'e': 381}, 
    381: {'q': 382}, 
    382: {'u': 383}, 
    383: {'i': 384}, 
    384: {'t': 42},
    # spell
    386: {'l': 387}, 
    387: {'l': 43},
    # ritual
    389: {'t': 390}, 
    390: {'u': 391}, 
    391: {'a': 392}, 
    392: {'l': 44},
    # respawn
    394: {'a': 395}, 
    395: {'w': 396}, 
    396: {'n': 45},
    # chunk
    398: {'n': 399}, 
    399: {'k': 46},
    # hopper
    401: {'p': 402}, 
    402: {'p': 403}, 
    403: {'e': 404}, 
    404: {'r': 47},
    # dropper
    406: {'e': 407}, 
    407: {'r': 48},
    # worldsave
    409: {'a': 410}, 
    410: {'v': 411}, 
    411: {'e': 49},

    # disk
    413: {' ': 0},
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
        # Limpiar el contenido y cerrar el archivo
        self.buffer = ""
        self.position = 0
        print("El scanner ha sido finalizado y los recursos han sido liberados.")

    def DemeElSiguienteCaracter(self):
        # Esta es una funcion que devuelve el siguiente carácter del buffer
        if self.position < len(self.buffer):
            token = self.buffer[self.position]
            self.position += 1
            self.columna += 1
            if token == "\n":
                self.linea += 1
                self.columna = 0
            return token
        return None
    
    def TomeEsteCaracter(self):
        # Si el caracter acutual ya no es parte del lexema, lo regresamos al buffer
        if self.position > 0:
            self.position -= 1
            self.columna -= 1
            if self.buffer[self.position] == '\n':
                self.linea -= 1
            return self.buffer[self.position]
        return None
    

    def DemeToken(self):
        # Esta funcion va a ser como el analizador lexico, que va a ir leyendo el buffer y devolviendo tokens
        # Utilizara el DemeElSiguienteCaracter y el TomeEsteCaracter para ir leyendo el buffer
        # y devolviendo tokens
        lexema = ""
        estado_actual = 0  # Comienza en el estado inicial

        token = Token(0, "", self.linea, self.columna, self.columna)  # Inicializamos el token
        while True:
            char = self.DemeElSiguienteCaracter()

            # Si el caracter es None, significa que el buffer 
            # ha sido leido completamente
            if char is None:
                if token.lexema != "":
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
                    if token.lexema != "" and transiciones[estado_actual][' '] == 0:
                        break
                    else:
                        print(f"Error: Lexema {token.lexema} no válido")
                        return token

            elif char == '\n':
                try:
                    if token.lexema != "" and '\n' in transiciones[estado_actual]:
                        #Corregir esta parte para que lance un error por saltos de linea
                        if transiciones[estado_actual]['\n'] != 0:
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
                    if token.lexema != "" and transiciones[estado_actual]['\n'] == 0:
                        break
                    else:
                        print(f"Error: Lexema {token.lexema} no válido")
                        return token

            # Consultamos la tabla de transiciones según el estado actual
            if char in transiciones[estado_actual]:
                estado_actual = transiciones[estado_actual][char]
                if estado_actual != 0:
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

