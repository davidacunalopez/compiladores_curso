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
    # Estado 0: Estado inicial
        # Palabras reservadas
    0: {' ': 0, '\n': 0, 'w': 1, 'b': 10, 'r': 18, 'i': 30, 'c': 43, 's': 56, 'o': 66, 'a': 74, 't': 90, 'g': 102, 'e' : 111, 'm': 127, 'n': 163, 'x': 166, 'f': 172, 'd': 183, 'k': 197, 'p': 204, 'h': 230, 'j': 236,
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
    1: {'o': 2, 'a': 255, 'i': 261}, 2: {'r': 3}, 3: {'l': 4}, 4: {'d': 5}, 5: {'n': 6, 's': 309}, 6: {'a': 7}, 7: {'m': 8}, 8: {'e': 9}, 9: {' ': 0},
    # bedrock
    10: {'e': 11, 'o': 99, 'i': 169}, 11: {'d': 12}, 12: {'r': 13}, 13: {'o': 14}, 14: {'c': 15}, 15: {'k': 16}, 16: {' ': 0},
    # resourcepack
    18: {'e': 19, 'u': 83, 'a': 279, 'i': 289}, 19: {'s': 20, 'c': 39, 'p': 219}, 20: {'o': 21, 'p': 294}, 21: {'u': 22}, 22: {'r': 23}, 23: {'c': 24}, 24: {'e': 25}, 25: {'p': 26}, 26: {'a': 27}, 27: {'c': 28}, 28: {'k': 29}, 29: {' ': 0},
    # inventory
    30: {'n': 31, 's': 132, 't': 188}, 31: {'v': 32}, 32: {'e': 33}, 33: {'n': 34}, 34: {'t': 35}, 35: {'o': 36}, 36: {'r': 37}, 37: {'y': 38}, 38: {' ': 0},
    # recipe
    39: {'i': 40}, 40: {'p': 41}, 41: {'e': 42}, 42: {' ': 0},
    # craftingtable
    43: {'r': 44, 'h': 95}, 44: {'a': 45, 'e': 266}, 45: {'f': 46}, 46: {'t': 47}, 47: {'i': 48, ' ': 0}, 48: {'n': 49}, 49: {'g': 50}, 50: {'t': 51}, 51: {'a': 52}, 52: {'b': 53}, 53: {'l': 54}, 54: {'e': 55}, 55: {' ': 0},
    # spawnpoint
    56: {'p': 57, 't': 79, 'h': 107, 'o': 120, 'e': 180}, 57: {'a': 58, 'i': 86, 'e': 286}, 58: {'w': 59}, 59: {'n': 60}, 60: {'p': 61, 'e': 246}, 61: {'o': 62}, 62: {'i': 63}, 63: {'n': 64}, 64: {'t': 65}, 65: {' ': 0},
    # obsidian
    66: {'b': 67, 'n': 117, 'f': 118, 'r': 162}, 67: {'s': 68}, 68: {'i': 69}, 69: {'d': 70}, 70: {'i': 71}, 71: {'a': 72}, 72: {'n': 73}, 73: {' ': 0},
    # anvil
    74: {'n': 75, 'd': 183}, 75: {'v': 76, 'd':159}, 76: {'i': 77}, 77: {'l': 78}, 78: {' ': 0},
    # stack
    79: {'a': 80, 'e': 259}, 80: {'c': 81}, 81: {'k': 82}, 82: {' ': 0},
    # rune
    83: {'n': 84}, 84: {'e': 85}, 85: {' ': 0},
    # spider
    86: {'d': 87}, 87: {'e': 88}, 88: {'r': 89}, 89: {' ': 0},
    # torch
    90: {'o': 91, 'a': 225}, 91: {'r': 92, ' ': 0}, 92: {'c': 93}, 93: {'h': 94}, 94: {' ': 0},
    # chest
    95: {'e': 96, 'u': 298}, 96: {'s': 97}, 97: {'t': 98}, 98: {' ': 0},
    # book
    99: {'o': 100}, 100: {'k': 101}, 101: {' ': 0},
    # ghast
    102: {'h': 103}, 103: {'a': 104}, 104: {'s': 105}, 105: {'t': 106}, 106: {' ': 0},
    # shelf
    107: {'e': 108}, 108: {'l': 109}, 109: {'f': 110}, 110: {' ': 0},
    # entity
    111: {'n': 112, 't': 150, 'x': 176}, 112: {'t': 113, 'd': 271}, 113: {'i': 114}, 114: {'t': 115}, 115: {'y': 116}, 116: {' ': 0},
    # on
    117: {' ': 0},
    # off
    118: {'f': 119}, 119: {' ': 0},
    # soulsand
    120: {'u': 121}, 121: {'l': 122}, 122: {'s': 123}, 123: {'a': 124}, 124: {'n': 125}, 125: {'d': 126}, 126: {' ': 0},
    # magma
    127: {'a': 128, 'i': 233}, 128: {'g': 129, 'p': 194}, 129: {'m': 130}, 130: {'a': 131}, 131: {' ': 0},
    # isengraved
    132: {'e': 133, 'i': 141, ' ':404, 'n': 201}, 133: {'n': 134}, 134: {'g': 135}, 135: {'r': 136}, 136: {'a': 137}, 137: {'v': 138}, 138: {'e': 139}, 139: {'d': 140}, 140: {' ': 0},
    # isinscribed
    141: {'n': 142}, 142: {'s': 143}, 143: {'c': 144}, 144: {'r': 145}, 145: {'i': 146}, 146: {'b': 147}, 147: {'e': 148}, 148: {'d': 149}, 149: {' ': 0},
    # etchup
    150: {'c': 151}, 151: {'h': 152}, 152: {'u': 153, 'd': 155}, 153: {'p': 154}, 154: {' ': 0},
    # etchdown
    155: {'o': 156}, 156: {'w': 157}, 157: {'n': 158}, 158: {' ': 0},
    # and
    159: {' ': 0}, #queda un hueco
    # or
    162: {' ': 0},
    # not
    163: {'o': 164}, 164: {'t': 165}, 165: {' ': 0},
    # xor
    166: {'o': 167}, 167: {'r': 168}, 168: {' ': 0},
    # bind
    169: {'n': 170, 'o': 195}, 170: {'d': 171}, 171: {' ': 0},
    # from
    172: {'r': 173, 'e': 191, 'e': 191}, 173: {'o': 174}, 174: {'m': 175}, 175: {' ': 0},
    # except
    176: {'e': 177, 'h': 248}, 177: {'p': 178}, 178: {'t': 179}, 179: {' ': 0},
    # seek
    180: {'e': 181, 't': 258}, 181: {'k': 182}, 182: {' ': 0},
    # add
    183: {'d': 184, 'i': 243, 'r': 185}, 184: {' ': 0},
    # drop
    185: {'o': 186}, 186: {'p': 187}, 187: {' ': 0, 'p': 306},
    # item
    188: {'e': 189}, 189: {'m': 190}, 190: {' ': 0},
    # feed
    191: {'e': 192}, 192: {'d': 193}, 193: {' ': 0},
    # map
    194: {' ': 0},
    # biom
    195: {'m': 196}, 196: {' ': 0},
    # kill
    197: {'i': 198}, 198: {'l': 199}, 199: {'l': 200}, 200: {' ': 0},
    # is -> 132
    
    # isnot
    201: {'o': 202}, 202: {'t': 404},
    # pollocrudo
    204: {'o': 205}, 205: {'l': 206}, 206: {'l': 207}, 207: {'o': 208}, 208: {'c': 209, 'a': 214}, 209: {'r': 210}, 210: {'u': 211}, 211: {'d': 212}, 212: {'o': 213}, 213: {' ': 0},
    # polloasado
    214: {'s': 215}, 215: {'a': 216}, 216: {'d': 217}, 217: {'o': 218}, 218: {' ': 0},
    # repeater
    219: {'e': 220}, 220: {'a': 221}, 221: {'t': 222}, 222: {'e': 223}, 223: {'r': 224}, 224: {' ': 0},
    # craft -> 43

    # target
    225: {'r': 226}, 226: {'g': 227}, 227: {'e': 228}, 228: {'t': 229}, 229: {' ': 0},
    # hit
    230: {'i': 231, 'o': 301}, 231: {'t': 232}, 232: {' ': 0},
    # miss
    233: {'s': 234}, 234: {'s': 235}, 235: {' ': 0},
    # jukebox
    236: {'u': 237}, 237: {'k': 238}, 238: {'e': 239}, 239: {'b': 240}, 240: {'o': 241}, 241: {'x': 242}, 242: {' ': 0},
    # disk
    243: {'s': 244}, 244: {'k': 245}, 245: {':': 313},
    # spawner
    246: {'r': 247}, 247: {' ': 0},
    # exhausted
    248: {'a': 249}, 249: {'u': 250}, 250: {'s': 251}, 251: {'t': 252}, 252: {'e': 253}, 253: {'d': 254}, 254: {' ': 0},
    # walk
    255: {'l': 256}, 256: {'k': 257}, 257: {' ': 0},
    # set
    258: {' ': 0},
    # to -> 90

    # step
    259: {'p': 260}, 260: {' ': 0},
    # wither
    261: {'t': 262}, 262: {'h': 263}, 263: {'e': 264}, 264: {'r': 265}, 265: {' ': 0},
    # creeper
    266: {'e': 267}, 267: {'p': 268}, 268: {'e': 269}, 269: {'r': 270}, 270: {' ': 0},
    # enderpearl
    271: {'e': 272}, 272: {'r': 273}, 273: {'p': 274}, 274: {'e': 275}, 275: {'a': 276}, 276: {'r': 277}, 277: {'l': 278}, 278: {' ': 0},
    # ragequit
    279: {'g': 280}, 280: {'e': 281}, 281: {'q': 282}, 282: {'u': 283}, 283: {'i': 284}, 284: {'t': 285}, 285: {' ': 0},
    # spell
    286: {'l': 287}, 287: {'l': 288}, 288: {' ': 0},
    # ritual
    289: {'t': 290}, 290: {'u': 291}, 291: {'a': 292}, 292: {'l': 293}, 293: {' ': 0},
    # respawn
    294: {'a': 295}, 295: {'w': 296}, 296: {'n': 297}, 297: {' ': 0},
    # chunk
    298: {'n': 299}, 299: {'k': 300}, 300: {' ': 0},
    # hopper
    301: {'p': 302}, 302: {'p': 303}, 303: {'e': 304}, 304: {'r': 305}, 305: {' ': 0},
    # dropper
    306: {'e': 307}, 307: {'r': 308}, 308: {' ': 0},
    # worldsave
    309: {'a': 310}, 310: {'v': 311}, 311: {'e': 312}, 312: {' ': 0},

    # disk
    313: {' ': 0},
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
    # 
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
            if char is None:
                if token.lexema != "":
                    self.tokens.append(token)  
                return True
            
            if char == '$':
                lexema += char
                char = self.DemeElSiguienteCaracter()
                if char == '$' or char == '*':
                    lexema += char
                    continue
                else:
                    print(f"Error: Caracter '{char}' no válido después de '$'")
                    return False

            if lexema == "$$" or lexema == "$*":
                if char == "\n" and lexema == "$$":
                    lexema = ""
                    token.col_inicio = self.columna
                    token.col_final = self.columna
                elif char == "*":
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

