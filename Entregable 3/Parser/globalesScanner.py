AUTOMATA = {
    # INICIO: WORLDNAME
    0: {' ': 100},
    # SECCION: BEDROCK, RESOURCEPACK, INVENTORY, RECIPE, CRAFTINGTABLE
    1: {' ': 100},
    # PUNTO_ENTRADA: SPAWPOINT
    2: {' ': 100},
    # SISTEMA_ASIGNACION_CONSTANTE: OBSIDIAN
    3: {' ': 100},
    # SISTEMA_ASIGNACION_TIPOS: ANVIL 
    4: {' ': 100},
    # TIPO: STACK, RUNE, SPIDER, TORCH, CHEST, BOOK, GHAST, SHELF, ENTITY
    5: {' ': 100},
    # LITERAL_BOOLEANO: ON, OFF 
    6: {' ': 100},
    # OPERACION_INCRE_DECRE: SOULSAND, MAGMA
    7: {' ': 100},
    # OPERACION_CARACTER: isengraved, isinscribed, etchup, etchdown
    8: {' ': 100},
    # OPERACION_LOGICA: AND, OR, NOT, XOR
    9: {' ': 100},
    # Estado 10: 
    10: {' ': 100},
    # Estado 11: 
    11: {' ': 100},
    # OPERACION_COMPARACION: <, >, >=, <=, IS, ISNOT
    12: {' ': 100, '=': 54},
    # BLOQUE: POLLOCRUDO
    13: {' ': 100},
    # BLOQUE: POLLOASADO
    14: {' ': 100},
    # CICLO: REPEATER
    15: {' ': 100},
    # CRAFT
    16: {' ': 100},
    # IF_THEN_ELSE
    17: {' ': 100},
    # HIT, MISS
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
    # '+': 27, '-': 28, '*': 29, '/': 30, '%': 31,
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
    46: {' ': 100, '=' : 48},
    # Estado 47: HOPPER
    47: {' ': 100, '=' : 49},
    # Estado 48: DROPPER
    48: {' ': 100},
    # Estado 49: WORLDSAVE
    49: {' ': 100},
    # Estado 50: Numeros
    50: {' ': 100},
    # Estado 51: Identificadores
    51: {' ': 100},
    # Estado 52: Asignacion
    52: {' ': 100},
    # Estado 53: Operaciones aritmeticas
    53: {' ': 100},
    # Estado 54: Operaciones de comparacion
    54: {' ': 100},
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
    61: {' ': 100, '\n': 100},
    # terminador
    62: {' ': 100},
    # Estado 63: Flecha
    63: {' ': 100},
    64: {' ': 100},
    65: {' ': 100},
    66: {' ': 100},
    67: {' ': 100},
    68: {' ': 100},
    69: {' ': 100},
    70: {' ': 100},
    71: {' ': 100},
    72: {' ': 100},
    73: {' ': 100},
    74: {' ': 100},
    75: {' ': 100},
    76: {' ': 100},
    77: {' ': 100},
    78: {' ': 100},
    79: {' ': 100},
    80: {' ': 100},
    81: {' ': 100},
    82: {' ': 100},
    83: {' ': 100},
    84: {' ': 100},
    85: {' ': 100},
    86: {' ': 100},
    87: {' ': 100},
    88: {' ': 100},
    89: {' ': 100},
    90: {' ': 100},
    91: {' ': 100},
    92: {' ': 100},
    93: {' ': 100},
    94: {' ': 100},
    95: {' ': 100},
    96: {' ': 100},
    97: {' ': 100},
    98: {' ': 100},
    99: {' ': 100},
    100: {' ': 100, '\n': 100, 'w': 101, 'b': 110, 'r': 118, 'i': 130, 'c': 143, 's': 156, 'o': 166, 'a': 174, 't': 190, 'g': 202, 'e': 211, 'm': 227, 'n': 263, 'x': 266, 'f': 272, 'd': 283, 'k': 297, 'p': 304, 'h': 330, 'j': 336,
        # Espacios y saltos de línea
        #'1': 50, '2': 50, '3': 50, '4': 50, '5': 50, '6': 50, '7': 50, '8': 50, '9': 50, '0': 50,  
        # Asignacion y aritmetica
        '=': 26, 
        #Operaciones aritmeticas
        #'+': 27, '-': 28, '*': 29, '/': 30, '%': 31,
        # Operacores de comparacion
        '<': 46, '>': 47, 
        #terminador
        ';': 76, ':': 94,
        # Abre parentesis
        '(': 70, 
        # Cierra parentesis
        ')': 71,
        # Abre llave
        '{': 59,
        # Cierra llave
        '}': 60,
        # Comilla
        ',': 89,
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
    128: {'k': 2},
    # inventory
    130: {'n': 131, 's': 232, 't': 288}, 
    131: {'v': 132}, 
    132: {'e': 133}, 
    133: {'n': 134}, 
    134: {'t': 135}, 
    135: {'o': 136}, 
    136: {'r': 137},
    137: {'y': 3},
    # recipe
    139: {'i': 140}, 
    140: {'p': 141},
    141: {'e': 4},
    # craftingtable
    143: {'r': 144, 'h': 195}, 
    144: {'a': 145, 'e': 266}, 
    145: {'f': 146}, 
    146: {'t': 147}, 
    147: {'i': 148, ' ': 54}, 
    148: {'n': 149}, 
    149: {'g': 150}, 
    150: {'t': 151}, 
    151: {'a': 152}, 
    152: {'b': 153}, 
    153: {'l': 154},
    154: {'e': 5},
    # spawnpoint
    156: {'p': 157, 't': 179, 'h': 207, 'o': 220, 'e': 280}, 
    157: {'a': 158, 'i': 186, 'e': 286}, 
    158: {'w': 159}, 
    159: {'n': 160}, 
    160: {'p': 161, 'e': 246}, 
    161: {'o': 162}, 
    162: {'i': 163}, 
    163: {'n': 164},
    164: {'t': 6},
    # obsidian
    166: {'b': 167, 'n': 18, 'f': 216, 'r': 22}, 
    167: {'s': 168}, 
    168: {'i': 169}, 
    169: {'d': 170}, 
    170: {'i': 171}, 
    171: {'a': 172},
    172: {'n': 7},
    # anvil
    174: {'n': 175, 'd': 283}, 
    175: {'v': 176, 'd': 22}, 
    176: {'i': 177},
    177: {'l': 8},
    # stack
    179: {'a': 180, 'e': 259}, 
    180: {'c': 181},
    181: {'k': 9},
    # rune
    183: {'n': 184},
    184: {'e': 10},
    # spider
    186: {'d': 187}, 
    187: {'e': 188},
    188: {'r': 11},
    # torch
    190: {'o': 191, 'a': 225}, 
    191: {'r': 192, ' ': 93}, 
    192: {'c': 193},
    193: {'h': 12},
    # chest
    195: {'e': 196, 'u': 298}, 
    196: {'s': 197},
    197: {'t': 13},
    # book
    199: {'o': 200},
    200: {'k': 14},
    # ghast
    202: {'h': 203}, 
    203: {'a': 204}, 
    204: {'s': 205},
    205: {'t': 15},
    # shelf
    207: {'e': 208}, 
    208: {'l': 209},
    209: {'f': 16},
    # entity
    211: {'n': 212, 't': 250, 'x': 276}, 
    212: {'t': 213, 'd': 271}, 
    213: {'i': 214}, 
    214: {'t': 215},
    215: {'y': 17},
    # on
    #6

    # off
    216: {'f': 19},

    # soulsand
    220: {'u': 221}, 
    221: {'l': 222}, 
    222: {'s': 223},
    223: {'a': 224},
    224: {'n': 225},
    225: {'d': 32},

    # magma
    227: {'a': 228, 'i': 233}, 
    228: {'g': 229, 'p': 24}, 
    229: {'m': 230},
    230: {'a': 33},
    
    # 12 es de comparacion solicitada
    # isengraved
    232: {'e': 233, 'i': 241, ' ': 50, 'n': 301}, 
    233: {'n': 234}, 
    234: {'g': 235}, 
    235: {'r': 236}, 
    236: {'a': 237}, 
    237: {'v': 238}, 
    238: {'e': 239}, #21
    239: {'d': 34},

    # isinscribed
    241: {'n': 242}, 
    242: {'s': 243}, 
    243: {'c': 244}, 
    244: {'r': 245}, 
    245: {'i': 246}, 
    246: {'b': 247}, 
    247: {'e': 248},
    248: {'d': 35},

    # etchup
    250: {'c': 251}, 
    251: {'h': 252}, 
    252: {'u': 253, 'd': 255},
    253: {'p': 36},

    # etchdown
    255: {'o': 256}, 
    256: {'w': 257},
    257: {'n': 37},
    # and
    259: {' ': 38},
    # or
    262: {' ': 39},
    # not
    263: {'o': 264},
    264: {'t': 40},
    # xor
    266: {'o': 267},
    267: {'r': 41},
    # bind
    269: {'n': 270, 'o': 294},
    270: {'d': 42},
    # from
    272: {'r': 273, 'e': 291, 'e': 291}, 
    273: {'o': 274},
    274: {'m': 43},
    # except
    276: {'c': 277, 'h': 248}, 
    277: {'e': 278},
    278: {'p': 279},
    279: {'t': 44},
    # seek
    280: {'e': 281, 't': 92},
    281: {'k': 45},

    # add
    283: {'d': 11, 'i': 243, 'r': 285}, 
    284: {' ': 100},
    # drop
    285: {'o': 286}, 
    286: {'p': 11},
    #este no se si tengo que borrarlo
    287: {'p': 306},
    # item
    288: {'e': 289},
    289: {'m': 11},
    # feed
    291: {'e': 292}, 
    292: {'d': 11},
    # map
    293: {'p': 11},

    # biom
    294: {'m': 11},

    # kill
    297: {'i': 298}, 
    298: {'l': 299},
    299: {'l': 11},
    # is -> 232
    
    # isnot
    301: {'o': 302}, 
    302: {'t': 51},
    # pollocrudo
    304: {'o': 305}, 
    305: {'l': 306}, 
    306: {'l': 307}, 
    307: {'o': 308}, 
    308: {'c': 309, 'a': 314}, 
    309: {'r': 310}, 
    310: {'u': 311}, 
    311: {'d': 312}, 
    312: {'o': 52},
    # polloasado
    314: {'s': 315}, 
    315: {'a': 316}, 
    316: {'d': 317}, 
    317: {'o': 53},
    # repeater
    319: {'e': 320}, 
    320: {'a': 321}, 
    321: {'t': 322}, 
    322: {'e': 323}, 
    323: {'r': 57},
    # craft -> 143

    # target
    325: {'r': 326}, 
    326: {'g': 327}, 
    327: {'e': 328}, 
    328: {'t': 58},
    # hit
    330: {'i': 331, 'o': 301}, 
    331: {'t': 98},
    # miss
    333: {'s': 334}, 
    334: {'s': 55},
    # jukebox
    336: {'u': 337}, 
    337: {'k': 338}, 
    338: {'e': 339}, 
    339: {'b': 340}, 
    340: {'o': 341}, 
    341: {'x': 59},
    # disk
    343: {'s': 344}, 
    344: {'k': 60},
    # spawner
    346: {'r': 61},
    # exhausted
    348: {'a': 349}, 
    349: {'u': 350}, 
    350: {'s': 351}, 
    351: {'t': 352}, 
    352: {'e': 353}, 
    353: {'d': 90},
    # walk
    355: {'l': 356}, 
    356: {'k': 62},
    # set -> 280

    # to -> 190

    # step
    359: {'p': 63},
    # wither
    361: {'t': 362}, 
    362: {'h': 363}, 
    363: {'e': 364}, 
    364: {'r': 64},
    # creeper
    366: {'e': 367}, 
    367: {'p': 368}, 
    368: {'e': 369}, 
    369: {'r': 91},
    # enderpearl
    371: {'e': 372}, 
    372: {'r': 373}, 
    373: {'p': 374}, 
    374: {'e': 375}, 
    375: {'a': 376}, 
    376: {'r': 377}, 
    377: {'l': 87},
    # ragequit
    379: {'g': 380}, 
    380: {'e': 381}, 
    381: {'q': 382}, 
    382: {'u': 383}, 
    383: {'i': 384}, 
    384: {'t': 0},
    # spell
    386: {'l': 387}, 
    387: {'l': 68},
    # ritual
    389: {'t': 390}, 
    390: {'u': 391}, 
    391: {'a': 392}, 
    392: {'l': 69},
    # respawn
    394: {'a': 395}, 
    395: {'w': 396}, 
    396: {'n': 72},
    # chunk
    398: {'n': 399}, 
    399: {'k': 73},
    # hopper
    401: {'p': 402}, 
    402: {'p': 403}, 
    403: {'e': 404}, 
    404: {'r': 74},
    # dropper
    406: {'e': 407}, 
    407: {'r': 75},
    # worldsave
    409: {'a': 410}, 
    410: {'v': 411}, 
    411: {'e': 77},

    # disk
    413: {' ': 60},
}


TERMINALES = ["WORLDNAME",
    "BEDROCK",
    "RESOURCEPACK",
    "INVENTORY",
    "RECIPE",
    "CRAFTINGTABLE",
    "SPAWNPOINT",
    "OBSIDIAN",
    "ANVIL",
    "STACK",
    "RUNE",
    "SPIDER",
    "TORCH",
    "CHEST",
    "BOOK",
    "GHAST",
    "SHELF",
    "ENTITY",
    "ON",
    "OFF",
    "LITERAL_FLOTANTE",
    "LITERAL_ENTERO",
    "LITERAL_CARACTER",
    "LITERAL_STRING",
    "LITERAL_ARREGLO",
    "LITERAL_REGISTRO",
    "=",
    "+",
    "-",
    "*",
    "/",
    "%",
    "SOULSAND",
    "MAGMA",
    "ISENGRAVED",
    "ISINSCRIBED",
    "ETCHUP",
    "ETCHDOWN",
    "AND",
    "OR",
    "NOT",
    "XOR",
    "BIND",
    "FROM",
    "EXCEPT",
    "SEEK",
    "<",
    ">",
    "<=",
    ">=",
    "IS",
    "ISNOT",
    "POLLOCRUDO",
    "POLLOASADO",
    "CRAFT",
    "MISS",
    "SILENCE",
    "REPEATER",
    "TARGET",
    "JUKEBOX",
    "DISK",
    "SPAWNER",
    "WALK",
    "STEP",
    "WITHER",
    "BREAK",
    "CONTINUE",
    "HALT",
    "SPELL",
    "RITUAL",
    "(",
    ")",
    "RESPAWN",
    "CHUNK",
    "HOPPER",
    "DROPPER",
    ";",
    "WORLDSAVE",
    "->",
    "REF",
    "DATO",
    ">>",
    "[",
    "]",
    "@",
    "IDENTIFICADOR",
    "VALOR",
    "LITERAL",
    "::",
    ",",
    "EXHAUSTED",
    "VARIABLE",
    "SET",
    "TO",
    ":",
    "REFERENCIA",
    ".",
    "CONDICION",
    "EXPRESION",
    " EOF "]
