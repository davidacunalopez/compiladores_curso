/*
 * Gramatica.c
 *
 * 2025/05/29 09:00:37
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */
#include "Gramatica.h"

/* Tabla de parsing */
const int TablaParsing[2][NO_TERMINAL_INICIAL] =
{
	/* <inicio> */ {0,-1,-1,-1},
	/* <identificador> */ {-1,1,-1,-1}
};

/* Tabla de lados derechos */
const int LadosDerechos[2][MAX_LADO_DER] =
{
	{7,2,5,0,6},
	{1,-1,-1,-1,-1}
};
