from collections import deque
import scanner as Scanner, globalesParcer as G
import simboloSemanticos as SS
from tablaSimbolos import *


def parser(scanner):
    tlg = None
    scanner.InicializarScanner("Entregable 3\Parser\prueba.ne")
    pila = deque()
    pila.append(G.NO_TERMINAL_INICIAL)

    TA = scanner.DemeToken()

    while pila and TA and TA.codigo != G.TOKEN_EOF:
        EAP = pila.pop()

        # Terminal
        #if isinstance(EAP, int) and EAP in G.TERMINALES:
        if EAP < G.NO_TERMINAL_INICIAL:
            if TA.codigo == EAP:
                print(f"✔️ Token aceptado: {TA.lexema} (código {TA.codigo})")
                TA = scanner.DemeToken()
            else:
                print(f"❌ Error: se esperaba código {EAP}, se recibió {TA.codigo} ('{TA.lexema}')")
                return False

        # No terminal
        else:
            if (99 <= EAP) and (EAP <= 183):
                regla = G.TP[EAP - G.NO_TERMINAL_INICIAL][TA.codigo]
                if regla < 0:
                    print("Error sintactico")
                    return False
                else:
                    i = 0
                    while (G.TLD[regla][i] > -1):
                        pila.append(G.TLD[regla][i])
                        i = i + 1
                        if i >= G.MAX_LADO_DER:
                            break
            if (185 <= EAP) and (EAP <= 200):

                    if EAP == SS.CrearTLG:
                            tlg = TablaSimbolos(tamaño=20)
                    #######################################################################################################
                    #SISTEMA DE ASIGNACION DE COSNTANTES
                    elif EAP == SS.AlmacenarTipoConstante:
                        if TA.lexema.upper() in SS.CodigosTipos:
                            SS.tipoleido = TA.lexema    
                        
                        else:
                            print(f"❌ Error Semantico:[!] El tipo '{TA.lexema}' no es valido.")
                            return False  
                       
                    elif EAP == SS.ValidarExistenciaIdentificadorConstante:
                            nombre = TA.lexema
                            exito = tlg.agregar(nombre.upper())
                            if not exito:
                                print(f"Error Semantico:[!] El identificador '{nombre}' ya existe.")
                                return False
                            else:
                                SS.identificardorLeido =nombre
                                if not  tlg.modificar_atributo(nombre.upper(),"categoria","constante"):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                if not  tlg.modificar_atributo(nombre.upper(),"tipo",SS.tipoleido):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                SS.tipoleido =False
                    
                    elif EAP ==  SS.ValidarTipoValorConstante:
                        if SS.identificardorLeido != False:
                                
                                if tlg.existe(SS.identificardorLeido.upper()):
                                    if  TA.codigo in SS.tiposCodigoLiteral[tlg.buscar(SS.identificardorLeido.upper())["atributos"]["tipo"].upper()]:
                                        if not  tlg.modificar_atributo(SS.identificardorLeido.upper(),"valor",TA.lexema):
                                            print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.")
                                            return False
                                        SS.identificardorLeido =False
                                    else:
                                        print(f"❌ [!] El Valor no es del tipo de la que tiene la constante {SS.identificardorLeido} asignado  {TA.codigo } != { SS.tiposCodigoLiteral[tlg.buscar(SS.identificardorLeido.upper())["atributos"]["tipo"].upper()]}.")
                                        return False
                                else:
                                    print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.")
                                    return False
                        else:
                           print(f"❌ [!] El identificador '{nombre}' no existe.Se necesita para asgnar un valor")
                           return False 
                    #######################################################################################################
                    #SISTEMA DE ASIGNACION DE TIPO
                    elif EAP == SS.ValidarExistenciaIdentificadorTipo:
                            nombre = TA.lexema
                            exito = tlg.agregar(nombre.upper())
                            if not exito:
                                print(f"Error Semantico:[!] El identificador '{nombre}' ya existe.")
                                return False
                            else:
                                SS.identificardorLeido =nombre
                                if not  tlg.modificar_atributo(nombre.upper(),"categoria","tipo"):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                
                    elif EAP ==  SS.ValidarValorTipo:
                        if SS.identificardorLeido != False:
                                
                                if tlg.existe(SS.identificardorLeido.upper()):
                                    if  TA.codigo == SS.CodigosTipos[TA.lexema.upper()]:
                                        if not  tlg.modificar_atributo(SS.identificardorLeido.upper(),"valor",TA.lexema):
                                            print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.")
                                            return False
                                        SS.identificardorLeido =False
                                    else:
                                        print(f"❌ [!] El Valor del tipo {SS.identificardorLeido} no es un tipo valido {TA.lexema}")
                                        return False
                                else:
                                    print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.")
                                    return False
                        else:
                           print(f"❌ [!] El identificador '{nombre}' no existe.Se necesita para asgnar un valor")
                           return False 
                        
                    #######################################################################################################
                    #SISTEMA DE ASIGNACION DE variables
                    elif EAP == SS.AlmacenarTipoVariable:

                        if TA.lexema.upper() in SS.CodigosTipos:
                            SS.tipoleido = TA.lexema    
                        elif tlg.existe(TA.lexema.upper()):
                            existente = tlg.buscar(TA.lexema.upper())
                            if existente:
                               
                                if existente["atributos"]["categoria"] == "tipo":
                                    SS.tipoleido = existente["atributos"]["valor"]
                                else:
                                    print(f"❌ Error Semantico:[!] El tipo '{TA.lexema}' no es valido.porque es {existente["atributos"]["categoria"]}")
                                    return False 
                            else:
                                print(f"❌ Error Semantico:[!] El tipo '{TA.lexema}' no es valido.")
                                return False    
                        else:
                            print(f"❌ Error Semantico:[!] El tipo '{TA.lexema}' no es valido.")
                            return False  

                    elif EAP == SS.BorrarTipoVariable:
                        SS.tipoleido = False  

                    elif EAP == SS.ValidarExistenciaIdentificadorVariable:
                            nombre = TA.lexema
                            exito = tlg.agregar(nombre.upper())
                            if not exito:
                                if SS.tipoleido != False:
                                    print(f"❌ Error Semantico:[!] El identificador '{nombre}' ya existe.")
                                    return False
                                else:
                                    if tlg.buscar(SS.identificardorLeido.upper())["atributos"]["categoria"] == "variable":
                                        SS.identificardorLeido =nombre
                                    else: 
                                        print(f"❌ Error Semantico:[!] El identificador '{nombre}' ya existe.No es una variable es {tlg.buscar(SS.identificardorLeido.upper())["atributos"]["categoria"]}")
                                        return False
                            else:
                                SS.identificardorLeido =nombre
                                if not  tlg.modificar_atributo(nombre.upper(),"categoria","variable"):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                if not  tlg.modificar_atributo(nombre.upper(),"tipo",SS.tipoleido):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                SS.tipoleido =False

                    elif EAP ==  SS.ValidarTipoValorVariable:
                        if SS.identificardorLeido != False:
                                
                                if tlg.existe(SS.identificardorLeido.upper()):
                                    if  TA.codigo in SS.tiposCodigoLiteral[tlg.buscar(SS.identificardorLeido.upper())["atributos"]["tipo"].upper()]:
                                        if not  tlg.modificar_atributo(SS.identificardorLeido.upper(),"valor",TA.lexema):
                                            print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.")
                                            return False
                                        SS.identificardorLeido =False
                                    else:
                                        print(f"❌ [!] El Valor no es del tipo de la que tiene la constante {SS.identificardorLeido} asignado  {TA.codigo } != { SS.tiposCodigoLiteral[tlg.buscar(SS.identificardorLeido.upper())["atributos"]["tipo"].upper()]}.")
                                        return False
                                else:
                                    print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.")
                                    return False
                        else:
                           print(f"❌ [!] El identificador '{nombre}' no existe.Se necesita para asgnar un valor")
                           return False 
                    #######################################################################################################
                    #Creacion de funciones procedimientos

                    elif EAP ==  SS.AlmacenarFuncion:
                            nombre = TA.lexema
                            exito = tlg.agregar(nombre.upper())
                            if not exito:
                                print(f"Error Semantico:[!] El identificador '{nombre}' ya existe.")
                                return False
                            else:
                                SS.identificardorLeido =nombre
                                if not  tlg.modificar_atributo(nombre.upper(),"categoria","funcion"):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                if not  tlg.modificar_atributo(nombre.upper(),"parametros",{}):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                
                    elif EAP ==  SS.AlmacenarProcedimiento:
                            nombre = TA.lexema
                            exito = tlg.agregar(nombre.upper())
                            if not exito:
                                print(f"Error Semantico:[!] El identificador '{nombre}' ya existe.")
                                return False
                            else:
                                SS.identificardorLeido =nombre
                                if not  tlg.modificar_atributo(nombre.upper(),"categoria","procedimiento"):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                if not  tlg.modificar_atributo(nombre.upper(),"parametros",{}):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                
                    elif EAP == SS.AlmacenarTipoParametroFormal:
                        if TA.lexema.upper() in SS.CodigosTipos:
                            SS.tipoleido = TA.lexema    
                        
                        else:
                            print(f"❌ Error Semantico:[!] El tipo '{TA.lexema}' no es valido.")
                            return False  
                        
                    elif EAP == SS.ValidarExistenciaIdentificadorParametroFormal:
                            FunOProc = tlg.buscar(SS.identificardorLeido.upper())
                            if not FunOProc:
                                print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.-")
                                return False
                            if not FunOProc["atributos"]["categoria"] in ["funcion","procedimiento"]:
                                print(f"❌ [!] El identificador '{SS.identificardorLeido}' no es un un procedimiento o funcion.-")
                                return False
                            nombre = TA.lexema
                            parametros = FunOProc["atributos"]["parametros"]
                            if not nombre in parametros:
                                parametros[nombre] = {"tipo":SS.tipoleido, "clase":"formal", }
                                if not  tlg.modificar_atributo(SS.identificardorLeido.upper(),"parametros",parametros):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                                    
                                SS.tipoleido =False
                                
                            else:
                                print(f"❌ Ya existe un parametro formal con el mismo nombre {nombre}")
                                return False
                    
                    elif EAP == SS.AlmacenarTipoFuncion:
                            FunOProc = tlg.buscar(SS.identificardorLeido.upper())
                            if not FunOProc:
                                print(f"❌ [!] El identificador '{SS.identificardorLeido}' no existe.-")
                                return False
                            if not FunOProc["atributos"]["categoria"] in ["funcion"]:
                                print(f"❌ [!] El identificador '{SS.identificardorLeido}' no es una funcion.-")
                                return False
                            nombre = TA.lexema
                            
                            
                            

                            if TA.lexema.upper() in SS.CodigosTipos:
                                SS.tipoleido = TA.lexema    
                                if not  tlg.modificar_atributo(SS.identificardorLeido.upper(),"tiporetorno",TA.lexema):
                                    print(f"❌ [!] El identificador '{nombre}' no existe.")
                                    return False
                            
                            else:
                                print(f"❌ Error Semantico:[!] El tipo '{TA.lexema}' no es valido.")
                                return False  



                                    
                            SS.tipoleido =False

                    elif EAP == SS.BorrarIdentificador:
                        SS.identificardorLeido = False  


                    else:
                        print(f"❌ Simbolo semantico no procesado codigo ({EAP})")
                        return False

        '''
        elif EAP < len(G.TP):  # si es un índice válido
            if TA.codigo < len(G.TP[EAP]):
                regla = G.TP[EAP][TA.codigo]
                if regla == -1:
                    print(f"❌ Error: sin regla para EAP={EAP}, token={TA.codigo}")
                    return False
                produccion = [sim for sim in G.TLD[regla] if sim != -1]
                print(f"📘 Aplicando regla {regla}: {EAP} → {' '.join(map(str, produccion))}")
                for simbolo in reversed(produccion):
                    pila.append(simbolo)
            else:
                print(f"❌ Error: token fuera de rango en TP: {TA.codigo}")
                return False
        else:
            print(f"❌ Símbolo inválido en pila: {EAP}")
            return False
        '''

    if not pila and (not TA or TA.codigo == G.TOKEN_EOF):
        print("✅ Análisis sintáctico exitoso.")
        print("#"*15)
        print("Tabla de simbolos Global")
        tlg.imprimir()
        return True
    else:
        print("❌ Análisis incompleto.")
        return False


if __name__ == "__main__":
    scanner = Scanner.AnalizadorLexico()
    parser(scanner)


'''from collections import deque
import scanner as Scanner

TERMINALES = {0, 51, 61}
SIMBOLO_INICIAL = 'INICIO'
TOKEN_EOF = -99  # defínilo según lo que retorne el scanner al final

TP = {
    'INICIO': {
        0: 0  # Si TA.codigo = 0 (worldname), usar regla 0: INICIO → DECLARACION ;
    },
    'DECLARACION': {
        0: 1  # Si TA.codigo = 0 (worldname), usar regla 1: DECLARACION → worldname IDENTIFICADOR
    }
}

TLD = {
    0: ['DECLARACION', 61],      # INICIO → DECLARACION ;
    1: [0, 51]                   # DECLARACION → worldname IDENTIFICADOR
}


def parser(scanner):
    scanner.InicializarScanner("Entregable 2/Entregables/Parcer/prueba.ne")
    pila = deque()
    pila.append(SIMBOLO_INICIAL)
    TA = scanner.DemeToken()

    while pila and TA and TA.codigo != TOKEN_EOF:
        EAP = pila.pop()

        # Caso terminal
        if isinstance(EAP, int) or EAP in TERMINALES:
            if TA.codigo == EAP:
                print(f"✔️ Token aceptado: {TA.lexema}")
                TA = scanner.DemeToken()
            else:
                print(f"❌ Error: se esperaba token código {EAP}, se recibió '{TA.lexema}'")
                return False

        # Caso no terminal
        elif EAP in TP:
            if TA.codigo in TP[EAP]:
                regla = TP[EAP][TA.codigo]
                print(f"📘 Aplicando regla {regla}: {EAP} → {' '.join(map(str, TLD[regla]))}")
                for simbolo in reversed(TLD[regla]):
                    pila.append(simbolo)
            else:
                print(f"❌ Error: token inesperado '{TA.lexema}' para no terminal {EAP}")
                return False
        else:
            print(f"❌ Error interno: símbolo desconocido '{EAP}'")
            return False

    if not pila and (not TA or TA.codigo == TOKEN_EOF):
        print("✅ Análisis sintáctico exitoso.")
        return True
    else:
        print("❌ Error: análisis incompleto.")
        return False


if __name__ == "__main__":
    scanner = Scanner.AnalizadorLexico()
    parser(scanner)
'''