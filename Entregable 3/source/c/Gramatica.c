/*
 * Gramatica.c
 *
 * 2025/05/27 09:24:37
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */
#include "Gramatica.h"

/* Tabla de parsing */
const int TablaParsing[6][NO_TERMINAL_INICIAL] =
{
	/* <inicio> */ {0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
	/* <inicio2> */ {-1,1,1,1,1,1,1,1,-1,-1,-1},
	/* <seccion> */ {-1,2,3,4,5,6,7,7,-1,-1,-1},
	/* <punto_entrada> */ {-1,-1,-1,-1,-1,-1,8,9,-1,-1,-1},
	/* <identificador> */ {-1,-1,-1,-1,-1,-1,-1,-1,-1,10,-1},
	/* <final> */ {-1,-1,-1,-1,-1,-1,-1,11,-1,-1,-1}
};

/* Tabla de lados derechos */
const int LadosDerechos[12][MAX_LADO_DER] =
{
	{12,8,15,0},
	{16,14,13,-1},
	{1,-1,-1,-1},
	{2,-1,-1,-1},
	{3,-1,-1,-1},
	{4,-1,-1,-1},
	{5,-1,-1,-1},
	{-1,-1,-1,-1},
	{6,-1,-1,-1},
	{-1,-1,-1,-1},
	{9,-1,-1,-1},
	{7,-1,-1,-1}
};
