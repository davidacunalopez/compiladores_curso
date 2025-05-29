import os
import globalesScanner as G

'''
Etapa dos: Analizador Léxico
Grupo: 1
Integrantes:
- David Acuña López - 2020426228
- Deylan Sandoval Sanchez - 2020234274

Este es un analizador léxico para Minecraft, que se encarga de leer un archivo de texto y 
generar una lista de tokens.
'''
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
        return f"(Codigo: {self.codigo}, Tipo: {self.tipo},Lexema: '{self.lexema}', Linea: {self.linea}, Columna: {self.col_inicio}-{self.col_final})"


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
                    #print(f"Línea {self.linea}: Nueva línea detectada")
                
                # Manejar caracteres especiales
                if char.isspace() and char != "\n":
                    pass
                    #print(f"Línea {self.linea}, Columna {self.columna}: Espacio en blanco")
                
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
            charTemp = char
            if char != None:
                char = char.lower()
            

            # Si el caracter es None, significa que el buffer 
            # ha sido leido completamente
            if char is None:
                if token.lexema != "":
                    #significa que es el final del archivo
                    break
                return None
            
            # Si el caracter es $, significa que es un comentario
            if char == '$' and (lexema != "$$" and lexema != "$*"):
                lexema += charTemp
                char = self.DemeElSiguienteCaracter()
                if char == '$' or char == '*':
                    lexema += charTemp
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
                    if token.lexema != "" and ' ' in G.AUTOMATA[estado_actual]:
                        #Para casos especiales como el is
                        if estado_actual >= 100:
                            estado_actual = G.AUTOMATA[estado_actual][char]
                        token.codigo = estado_actual
                        token.aprobado = True
                        break

                    #Si no se reconoce el automata con ' ', puede ser una literal
                    elif token.lexema != "" and not (char in G.AUTOMATA[estado_actual]):
                        self.identificarTerminal(token, lexema)
                        break
                    token.col_inicio = self.columna
                    token.col_final = self.columna
                    continue
                except Exception as e:
                    if token.lexema != "" and G.AUTOMATA[estado_actual][' '] == 100:
                        break
                    else:
                        print(f"Error: Lexema {token.lexema} no válido")
                        break

            elif char == '\n':
                try:
                    if token.lexema != "" and char in G.AUTOMATA[estado_actual]:
                        #Corregir esta parte para que lance un error por saltos de linea
                        if G.AUTOMATA[estado_actual]['\n'] != 100:
                            token.codigo = G.AUTOMATA[estado_actual]['\n']
                        break
                        # *****************************
                        
                    elif token.lexema != "" and not ('\n' in G.AUTOMATA[estado_actual]):
                        print(f"Error: Lexema {token.lexema} no válido")
                        #return token
                        break
                    token.col_inicio = self.columna
                    token.col_final = self.columna
                    continue
                except Exception as e:
                    if token.lexema != "" and G.AUTOMATA[estado_actual]['\n'] == 100:
                        break
                    else:
                        print(f"Error: Lexema {token.lexema} no válido")
                        return token

            # Consultamos la tabla de G.AUTOMATA según el estado actual
            if char in G.AUTOMATA[estado_actual]:
                estado_actual = G.AUTOMATA[estado_actual][char]
                if estado_actual != 100:
                    lexema += charTemp  # Formamos el lexema
                    token.lexema = lexema  # Agregamos el caracter al lexema
                    token.col_final = self.columna  # Actualizamos la columna final del token
                    token.linea = self.linea
                    token.codigo = estado_actual  # Actualizamos el código del token
                
            else:
                self.identificarTerminalNoTerminado(token, lexema, char)
                break
                    
         

        self.clasificarToken(token)
        self.tokens.append(token)  # Agregamos el token a la lista de tokens
        return token

    #Si el automata se completo, pero hay un espacio en blaco y no se
    #identifica el automata, se utiliza esta funcion
    def identificarTerminal(self, token, lexema):
        if not (lexema.upper() in G.TERMINALES):
            token.codigo = 85 #IDENTIFICADOR
            token.aprobado = True
        else:
            token.codigo = G.AUTOMATA.index(lexema)
            token.aprobado = True

    def identificarTerminalNoTerminado(self, token, lexema, char):
        if lexema == "":
            if char in ['+', '-', '*', '/', '%']:
                charTemp = self.DemeElSiguienteCaracter()
                if charTemp == '>':
                    lexema += (char + charTemp)
                    token.codigo = 78
                    token.aprobado = True
                else:
                    self.TomeEsteCaracter()
                    token.codigo = ['+', '-', '*', '/', '%'].index(char) + 27
                    token.aprobado = True
                    lexema += char 
            elif char == '"': #Reconoce string
                while char != ' ' and char != '\n' and char != None:
                    lexema += char
                    char = self.DemeElSiguienteCaracter()
                    if char == '"':
                        lexema += char
                        break
                if self.es_string_completo(lexema):
                    token.codigo = 23 #Codigo STRING
                    token.aprobado = True
                else:
                    token.codigo = -2 #String mal escrito
                
            elif char == '[': #Reconoce arreglos
                while char != ' ' and char != '\n' and char != None:
                    lexema += char
                    char = self.DemeElSiguienteCaracter()
                    if char == ']':
                        lexema += char
                        break
                #Validar que ERROR de arreglos
                token.codigo = 24 #Codigo ARREGLO
                token.aprobado = True

            elif char.isdigit(): #Reconoce enteros
                while char != ' ' and char != '\n' and char != None:
                    lexema += char
                    char = self.DemeElSiguienteCaracter()
                try: #Se valida que deverdad sea un numero
                    token.codigo = 21 #Codigo ENTERO
                    token.aprobado = True
                except Exception as e:
                    token.codigo = -3 #Entero mal controlado
            else:
                while char != ' ' and char != '\n' and char != None:
                    lexema += char
                    char = self.DemeElSiguienteCaracter()
                
                if lexema.isidentifier():
                    token.codigo = 85
                    token.aprobado = True
                else:
                    token.codigo = -1
            
        else: #Identificador?
            while char != ' ' and char != '\n' and char != None:
                lexema += char
                char = self.DemeElSiguienteCaracter()
                
            if lexema.isidentifier():
                token.codigo = 85
                token.aprobado = True
            else:
                token.codigo = -1
            
        token.lexema = lexema

    def es_string_completo(self, s):
        return len(s) >= 2 and s.startswith('"') and s.endswith('"')
    

    def clasificarToken(self, token):
        if token.codigo == 0:
            token.tipo = "INICIO"
        elif token.codigo == 1:
            token.tipo = "SECCION"
        elif token.codigo == 2:
            token.tipo = "PUNTO_ENTRADA"
        elif token.codigo == 3:
            token.tipo = "SISTEMA_ASIGNACION_CONSTANTE"
        elif token.codigo == 4:
            token.tipo = "SISTEMA_ASIGNACION_TIPOS"
        elif token.codigo == 51:
            token.tipo = "IDENTIFICADOR"
        elif token.codigo == 61:
            token.tipo = "SEPARADOR"
        elif token.codigo == 63:
            token.tipo = "FLECHA"
    
    def imprimirTokens(self):
        # Imprimimos los tokens generados
        for token in self.tokens:
            print(token)

    def TomeToken(self):
        pass

