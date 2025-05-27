from collections import deque
import globales as G
import scanner as Scanner

SIMBOLO_INICIAL = 0
TOKEN_EOF = -99


def parser(scanner):
    # Inicializar el scanner
    scanner.InicializarScanner("Entregable 2\Entregables\Parcer\parcer3.0\prueba.ne")

    # Obtener el primer token
    TA = scanner.DemeToken()

    # Crear la pila de parsing
    pila = deque()
    pila.append(SIMBOLO_INICIAL)

    while pila and TA and TA.codigo != TOKEN_EOF:
        EAP = pila.pop()

        # --------TERMINAL --------
        if isinstance(EAP, int) or EAP in G.TERMINALES:
            if TA.codigo == EAP:
                print(f"✔️ Token aceptado: {TA.lexema}")
                TA = scanner.DemeToken()
            else:
                print(f"❌ Error sintáctico: se esperaba el token código {EAP}, se recibió '{TA.lexema}'")
                return False

        # -------- NO TERMINAL --------
        elif EAP in G.TP:
            fila = G.TP[EAP]
            if TA.codigo in fila:
                regla = fila[TA.codigo]
                if regla < 0:
                    print(f"❌ Error sintáctico: regla inválida {regla}")
                    return False
                produccion = [sim for sim in G.TLD[regla] if sim != -1]
                print(f"📘 Aplicando regla {regla}: {EAP} → {' '.join(map(str, produccion))}")
                for simbolo in reversed(produccion):
                    pila.append(simbolo)
            else:
                print(f"❌ Error sintáctico: token inesperado '{TA.lexema}' para no terminal {EAP}")
                return False

        # -------- DESCONOCIDO --------
        else:
            print(f"❌ Error interno: símbolo '{EAP}' no reconocido")
            return False

    # -------- VALIDACIÓN FINAL --------
    if pila:
        print("❌ Error sintáctico: fin de archivo inesperado (quedó algo en la pila)")
        return False
    else:
        print("✅ Análisis sintáctico exitoso.")
        return True

if __name__ == "__main__":
    scanner = Scanner.AnalizadorLexico()
    parser(scanner)