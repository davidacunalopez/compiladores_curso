from collections import deque
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
