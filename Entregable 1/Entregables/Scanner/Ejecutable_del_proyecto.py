import scanner as Scanner
import sys, random
'''
scanner = Scanner.AnalizadorLexico()
scanner.InicializarScanner("C:/Users/USUARIO/OneDrive - Estudiantes ITCR/Compiladores/Proyecto/Etapa 1/Entregables/scanner/prueba_gordita.ne")

while not scanner.DemeToken():
    continue  # Continuar leyendo tokens hasta que no haya más

scanner.imprimirTokens()
scanner.FinalizarScanner()
'''

def color_random():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

def elegir_color(token):

    #Se definen rangos según las familias
    if token.codigo == 0:
        return 'white'  # Espacios, separadores
    elif token.codigo < 400:
        return color_random()  # Palabras reservadas
    elif token.codigo == 400:
        return 'blue'  # Números, operadores, terminadores
    elif token.codigo == 401:
        return 'gray'  # Identificadores
    elif token.codigo == 402:
        return 'orange'
    elif token.codigo == 403:
        return 'purple'
    elif token.codigo == 404:
        return 'green'
    elif token.codigo == 405:
        return 'pink'
    elif token.codigo == 406:
        return 'yellow'
    elif token.codigo == 407:
        return 'cyan'
    else:
        return 'red'  # Error o desconocido

def generar_muro_html(tokens):
    with open('muro_ladrillos.html', 'w', encoding='utf-8') as f:
        f.write('<html><head><title>Muro de Ladrillos</title></head><body>\n')
        f.write('<div style="display: flex; flex-wrap: wrap;">\n')

        for token in tokens:
            color = elegir_color(token)
            lexema_html = token.lexema.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            f.write(f'<div style="width: 100px; height: 50px; margin: 2px; background-color: {color}; display: flex; align-items: center; justify-content: center; font-size: 12px; text-align: center;">')
            f.write(f'{lexema_html}</div>\n')

        f.write('</div>\n')
        mostrar_estadisticas(tokens, f)
        f.write('</body></html>')

def mostrar_estadisticas(tokens, f):
    from collections import Counter

    familias = Counter()

    for token in tokens:
        if token.codigo >= 400:
            if token.codigo == 400:
                familias["Entero"] += 1
            elif token.codigo == 401:
                familias["Identificador"] += 1
            elif token.codigo == 402:
                familias["Asignación"] += 1
            elif token.codigo == 403:
                familias["Aritmética"] += 1
            elif token.codigo == 404:
                familias["Comparación"] += 1
            elif token.codigo == 405:
                familias["Terminador"] += 1
            elif token.codigo == 406:
                familias["Abre parentesis"] += 1
            elif token.codigo == 407:
                familias["Cierra parentesis"] += 1
        elif token.codigo == 0:
            pass 
        else:
            familias["Palabra Reservada"] += 1

    total_lineas = max((token.linea for token in tokens), default=0)
    total_caracteres = sum(len(token.lexema) for token in tokens)
    total_tokens = len(tokens)

    f.write('<h2>📊 Estadísticas del Análisis Léxico</h2>\n')
    f.write('<ul>\n')
    if total_tokens > 0:
        f.write(f'<li><strong>Total de tokens:</strong> {total_tokens}</li>\n')
    if total_lineas > 0:
        f.write(f'<li><strong>Total de líneas:</strong> {total_lineas}</li>\n')
    if total_caracteres > 0:
        f.write(f'<li><strong>Total de caracteres:</strong> {total_caracteres}</li>\n')

    for familia, cantidad in familias.items():
        if cantidad > 0:
            f.write(f'<li><strong>{familia}:</strong> {cantidad}</li>\n')
    f.write('</ul>\n')

#Función principal para ejecutar el escáner y generar el muro de ladrillos
def main():
    scanner = Scanner.AnalizadorLexico()
    scanner.InicializarScanner("prueba_gordita.ne")

    # Me genera todos los tokens
    while not (scanner.DemeToken()):
        continue

    generar_muro_html(scanner.tokens)

    scanner.FinalizarScanner()

if __name__ == "__main__":
    main()
