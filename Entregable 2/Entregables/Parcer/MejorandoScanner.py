import scanner as Scanner

Scanner = Scanner.AnalizadorLexico()

Scanner.InicializarScanner("Entregable 2\Entregables\Parcer\prueba.ne")


while Scanner.DemeToken() != None:
    continue

Scanner.imprimirTokens()
