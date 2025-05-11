import os

'''
Etapa uno: Analizador Léxico
Grupo: 1
Integrantes:
- David Acuña López - 2020426228
- Deylan Sandoval Sanchez - 2020234274

Este es un analizador léxico para Minecraft, que se encarga de leer un archivo de texto y 
generar una lista de tokens.
'''

transiciones = {
    # Estado 0: WORLDNAME
    0: {'e': 0, ' ': 100},
    # Estado 1: BEDROCK
    1: {'K':1, ' ': 100},
    # Estado 2: RESOURCEPACK
    2: {'k':2, ' ': 100},
    # Estado 3: INVENTORY
    3: {'y':3, ' ': 100},
    # Estado 4: RECIPE
    4: {'e':4, ' ': 100},
    # Estado 5: CRAFTINGTABLE
    5: {'e':5, ' ': 100},
    # Estado 6: SPAWNPOINT
    6: {'t':6, ' ': 100},

    100: {' ': 0, '\n': 0, 'w': 101, 'b': 110, 'r': 118, 'i': 130, 'c': 143, 's': 156, 'o': 166, 'a': 174, 't': 190, 'g': 202, 'e': 211, 'm': 227, 'n': 263, 'x': 266, 'f': 272, 'd': 283, 'k': 297, 'p': 304, 'h': 330, 'j': 336,
        # Espacios y saltos de línea
        '1': 400, '2': 400, '3': 400, '4': 400, '5': 400, '6': 400, '7': 400, '8': 400, '9': 400, '0': 400,  
        # Asignacion y aritmetica
        '=': 402, 
        #Operaciones aritmeticas
        '+': 403, '-': 403, '*': 403, '/': 403, '%': 403,
        # Operacores de comparacion
        '<': 404, '>': 404, '<': 404, '>': 404,
        #terminador
        ';': 405, ':': 405,
        # Abre parentesis
        '(': 406, 
        # Cierra parentesis
        ')': 407,
        },
    # worldname
    101: {'o': 102, 'a': 255, 'i': 261}, 
    102: {'r': 103}, 
    103: {'l': 104}, 
    104: {'d': 105}, 
    105: {'n': 106, 's': 309}, 
    106: {'a': 107}, 
    107: {'m': 0},
    # bedrock
    110: {'e': 111, 'o': 199, 'i': 269}, 
    111: {'d': 112}, 
    112: {'r': 113}, 
    113: {'o': 114}, 
    114: {'c': 1},
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
    127: {'c': 2},
    # inventory
    130: {'n': 131, 's': 232, 't': 288}, 
    131: {'v': 132}, 
    132: {'e': 133}, 
    133: {'n': 134}, 
    134: {'t': 135}, 
    135: {'o': 136}, 
    136: {'r': 3},
    # recipe
    139: {'i': 140}, 
    140: {'p': 4},
    # craftingtable
    143: {'r': 144, 'h': 195}, 
    144: {'a': 145, 'e': 266}, 
    145: {'f': 146}, 
    146: {'t': 147}, 
    147: {'i': 148, ' ': 0}, 
    148: {'n': 149}, 
    149: {'g': 150}, 
    150: {'t': 151}, 
    151: {'a': 152}, 
    152: {'b': 153}, 
    153: {'l': 5},
    # spawnpoint
    156: {'p': 157, 't': 179, 'h': 207, 'o': 220, 'e': 280}, 
    157: {'a': 158, 'i': 186, 'e': 286}, 
    158: {'w': 159}, 
    159: {'n': 160}, 
    160: {'p': 161, 'e': 246}, 
    161: {'o': 162}, 
    162: {'i': 163}, 
    163: {'n': 6},
    # obsidian
    166: {'b': 167, 'n': 217, 'f': 218, 'r': 262}, 
    167: {'s': 168}, 
    168: {'i': 169}, 
    169: {'d': 170}, 
    170: {'i': 171}, 
    171: {'a': 172}, 
    172: {'n': 173}, 
    173: {' ': 0},
    # anvil
    174: {'n': 175, 'd': 283}, 
    175: {'v': 176, 'd': 259}, 
    176: {'i': 177}, 
    177: {'l': 178}, 
    178: {' ': 0},
    # stack
    179: {'a': 180, 'e': 259}, 
    180: {'c': 181}, 
    181: {'k': 182}, 
    182: {' ': 0},
    # rune
    183: {'n': 184}, 
    184: {'e': 185}, 
    185: {' ': 0},
    # spider
    186: {'d': 187}, 
    187: {'e': 188}, 
    188: {'r': 189}, 
    189: {' ': 0},
    # torch
    190: {'o': 191, 'a': 225}, 
    191: {'r': 192, ' ': 0}, 
    192: {'c': 193}, 
    193: {'h': 194}, 
    194: {' ': 0},
    # chest
    195: {'e': 196, 'u': 298}, 
    196: {'s': 197}, 
    197: {'t': 198}, 
    198: {' ': 0},
    # book
    199: {'o': 200}, 
    200: {'k': 201}, 
    201: {' ': 0},
    # ghast
    202: {'h': 203}, 
    203: {'a': 204}, 
    204: {'s': 205}, 
    205: {'t': 206}, 
    206: {' ': 0},
    # shelf
    207: {'e': 208}, 
    208: {'l': 209}, 
    209: {'f': 210}, 
    210: {' ': 0},
    # entity
    211: {'n': 212, 't': 250, 'x': 276}, 
    212: {'t': 213, 'd': 271}, 
    213: {'i': 214}, 
    214: {'t': 215}, 
    215: {'y': 216}, 
    216: {' ': 0},
    # on
    217: {' ': 0},
    # off
    218: {'f': 219}, 
    219: {' ': 0},
    # soulsand
    220: {'u': 221}, 
    221: {'l': 222}, 
    222: {'s': 223}, 
    223: {'a': 224}, 
    224: {' ': 0},
    # magma
    227: {'a': 228, 'i': 233}, 
    228: {'g': 229, 'p': 294}, 
    229: {'m': 230}, 
    230: {'a': 231}, 
    231: {' ': 0},
    # isengraved
    232: {'e': 233, 'i': 241, ' ': 404, 'n': 301}, 
    233: {'n': 234}, 
    234: {'g': 235}, 
    235: {'r': 236}, 
    236: {'a': 237}, 
    237: {'v': 238}, 
    238: {'e': 239}, 
    239: {'d': 240}, 
    240: {' ': 0},
    # isinscribed
    241: {'n': 242}, 
    242: {'s': 243}, 
    243: {'c': 244}, 
    244: {'r': 245}, 
    245: {'i': 246}, 
    246: {'b': 247}, 
    247: {'e': 248}, 
    248: {'d': 249}, 
    249: {' ': 0},
    # etchup
    250: {'c': 251}, 
    251: {'h': 252}, 
    252: {'u': 253, 'd': 255}, 
    253: {'p': 254}, 
    254: {' ': 0},
    # etchdown
    255: {'o': 256}, 
    256: {'w': 257}, 
    257: {'n': 258}, 
    258: {' ': 0},
    # and
    259: {' ': 0},
    # or
    262: {' ': 0},
    # not
    263: {'o': 264}, 
    264: {'t': 265}, 
    265: {' ': 0},
    # xor
    266: {'o': 267}, 
    267: {'r': 268}, 
    268: {' ': 0},
    # bind
    269: {'n': 270, 'o': 295}, 
    270: {'d': 271}, 
    271: {' ': 0},
    # from
    272: {'r': 273, 'e': 291, 'e': 291}, 
    273: {'o': 274}, 
    274: {'m': 275}, 
    275: {' ': 0},
    # except
    276: {'e': 277, 'h': 248}, 
    277: {'p': 278}, 
    278: {'t': 279}, 
    279: {' ': 0},
    # seek
    280: {'e': 281, 't': 258}, 
    281: {'k': 282}, 
    282: {' ': 0},
    # add
    283: {'d': 284, 'i': 243, 'r': 285}, 
    284: {' ': 0},
    # drop
    285: {'o': 286}, 
    286: {'p': 287}, 
    287: {' ': 0, 'p': 306},
    # item
    288: {'e': 289}, 
    289: {'m': 290}, 
    290: {' ': 0},
    # feed
    291: {'e': 292}, 
    292: {'d': 293}, 
    293: {' ': 0},
    # map
    294: {' ': 0},
    # biom
    295: {'m': 296}, 
    296: {' ': 0},
    # kill
    297: {'i': 298}, 
    298: {'l': 299}, 
    299: {'l': 300}, 
    300: {' ': 0},
    # is -> 232
    
    # isnot
    301: {'o': 302}, 
    302: {'t': 404},
    # pollocrudo
    304: {'o': 305}, 
    305: {'l': 306}, 
    306: {'l': 307}, 
    307: {'o': 308}, 
    308: {'c': 309, 'a': 314}, 
    309: {'r': 310}, 
    310: {'u': 311}, 
    311: {'d': 312}, 
    312: {'o': 313}, 
    313: {' ': 0},
    # polloasado
    314: {'s': 315}, 
    315: {'a': 316}, 
    316: {'d': 317}, 
    317: {'o': 318}, 
    318: {' ': 0},
    # repeater
    319: {'e': 320}, 
    320: {'a': 321}, 
    321: {'t': 322}, 
    322: {'e': 323}, 
    323: {'r': 324}, 
    324: {' ': 0},
    # craft -> 143

    # target
    325: {'r': 326}, 
    326: {'g': 327}, 
    327: {'e': 328}, 
    328: {'t': 329}, 
    329: {' ': 0},
    # hit
    330: {'i': 331, 'o': 301}, 
    331: {'t': 332}, 
    332: {' ': 0},
    # miss
    333: {'s': 334}, 
    334: {'s': 335}, 
    335: {' ': 0},
    # jukebox
    336: {'u': 337}, 
    337: {'k': 338}, 
    338: {'e': 339}, 
    339: {'b': 340}, 
    340: {'o': 341}, 
    341: {'x': 342}, 
    342: {' ': 0},
    # disk
    343: {'s': 344}, 
    344: {'k': 345}, 
    345: {':': 313},
    # spawner
    346: {'r': 347}, 
    347: {' ': 0},
    # exhausted
    348: {'a': 349}, 
    349: {'u': 350}, 
    350: {'s': 351}, 
    351: {'t': 352}, 
    352: {'e': 353}, 
    353: {'d': 354}, 
    354: {' ': 0},
    # walk
    355: {'l': 356}, 
    356: {'k': 357}, 
    357: {' ': 0},
    # set
    358: {' ': 0},
    # to -> 190

    # step
    359: {'p': 360}, 
    360: {' ': 0},
    # wither
    361: {'t': 362}, 
    362: {'h': 363}, 
    363: {'e': 364}, 
    364: {'r': 365}, 
    365: {' ': 0},
    # creeper
    366: {'e': 367}, 
    367: {'p': 368}, 
    368: {'e': 369}, 
    369: {'r': 370}, 
    370: {' ': 0},
    # enderpearl
    371: {'e': 372}, 
    372: {'r': 373}, 
    373: {'p': 374}, 
    374: {'e': 375}, 
    375: {'a': 376}, 
    376: {'r': 377}, 
    377: {'l': 378}, 
    378: {' ': 0},
    # ragequit
    379: {'g': 380}, 
    380: {'e': 381}, 
    381: {'q': 382}, 
    382: {'u': 383}, 
    383: {'i': 384}, 
    384: {'t': 385}, 
    385: {' ': 0},
    # spell
    386: {'l': 387}, 
    387: {'l': 388}, 
    388: {' ': 0},
    # ritual
    389: {'t': 390}, 
    390: {'u': 391}, 
    391: {'a': 392}, 
    392: {'l': 393}, 
    393: {' ': 0},
    # respawn
    394: {'a': 395}, 
    395: {'w': 396}, 
    396: {'n': 397}, 
    397: {' ': 0},
    # chunk
    398: {'n': 399}, 
    399: {'k': 400}, 
    400: {' ': 0},
    # hopper
    401: {'p': 402}, 
    402: {'p': 403}, 
    403: {'e': 404}, 
    404: {'r': 405}, 
    405: {' ': 0},
    # dropper
    406: {'e': 407}, 
    407: {'r': 408}, 
    408: {' ': 0},
    # worldsave
    409: {'a': 410}, 
    410: {'v': 411}, 
    411: {'e': 412}, 
    412: {' ': 0},

    # disk
    413: {' ': 0},
    # SIMBOLOS RESERVADOS 320
    # Numeros:

    # 400 RESERVADO PARA LAS FAMILIAS
    #Numeros
    400: {'0': 400, '1': 400, '2': 400, '3': 400, '4': 400, '5': 400, '6': 400, '7': 400, '8': 400, '9': 400, ' ': 0}, # Numeros
    #Identificadores
    401: {'a': 401, 'b': 401, 'c': 401, 'd': 401, 'e': 401, 'f': 401, 'g': 401, 'h': 401, 'i': 401, 'j': 401, 'k': 401, 'l': 401, 'm': 401, 'n': 401, 'o': 401, 'p': 401, 'q': 401, 'r': 401, 's': 401, 't': 401, 'u': 401, 'v': 401, 'w': 401, 'x': 401, 'y': 401, 'z': 401, ' ': 401,
          'A': 401, 'B': 401, 'C': 401, 'D': 401, 'E': 401, 'F': 401, 'G': 401, 'H': 401, 'I': 401, 'J': 401, 'K': 401, 'L': 401, 'M': 401, 'N': 401, 'O': 401, 'P': 401, 'Q': 401, 'R': 401, 'S': 401, 'T': 401, 'U': 401, 'V': 401, 'W': 401, 'X': 401, 'Y': 401, 'Z': 401, '_': 401,
          '0': 401, '1': 401, '2': 401, '3': 401, '4': 401, '5': 401, '6': 401, '7': 401, '8': 401, '9': 401},
    # Asignacion
    402: {' ': 0, '=': 403, '+': 403, '-': 403, '*': 403, '/': 403, '%': 403},
    403: {' ': 0},
    # Aritmetica
    404: {' ': 0, '<': 404, '>': 404, '=': 404},
    # Terminador
    405: {' ': 0, '\n': 0},
    # Abre parentesis
    406: {' ': 0},
    # Cierra parentesis
    407: {' ': 0},
}

class Token:
    def __init__(self, codigo, lexema, linea, col_inicio, col_final):
        self.codigo = codigo     # Código numérico del tipo de token
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
                return True
            
            # Si el caracter es $, significa que es un comentario
            if char == '$':
                lexema += char
                char = self.DemeElSiguienteCaracter()
                if char == '$' or char == '*':
                    lexema += char
                    continue
                else:
                    print(f"Error: Caracter '{char}' no válido después de '$'")
                    return False

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

            if char == ' ' or char == '\n':
                try:
                    if token.lexema != "" and ' ' in transiciones[estado_actual]:
                        if transiciones[estado_actual][' '] != 0:
                            token.codigo = transiciones[estado_actual][' ']
                        break
                            
                        
                    elif token.lexema != "" and not (' ' in transiciones[estado_actual]):
                        print(f"Error: Lexema {token.lexema} no válido")
                        return False
                    token.col_inicio = self.columna
                    token.col_final = self.columna
                    continue
                except Exception as e:
                    if token.lexema != "" and transiciones[estado_actual][' '] == 0:
                        break
                    else:
                        print(f"Error: Lexema {token.lexema} no válido")
                        return False
                

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
                if estado_actual == 400:
                    print(f"Error: Lexema {lexema} no válido")
                    return False
                
                estado_actual = 401
                lexema += char
                
            


        self.tokens.append(token)  # Agregamos el token a la lista de tokens
        return False
    
    
    def imprimirTokens(self):
        # Imprimimos los tokens generados
        for token in self.tokens:
            print(token)

    def TomeToken(self):
        pass

