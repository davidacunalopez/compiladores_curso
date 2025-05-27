/*
 * Gramatica.c
 *
 * 2025/05/27 17:00:59
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */
#include "Gramatica.h"

/* Tabla de parsing */
const int TablaParsing[7][NO_TERMINAL_INICIAL] =
{
	/* <inicio> */ {0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
	/* <inicio2> */ {-1,1,1,1,1,1,1,1,-1,-1,-1},
	/* <seccion> */ {-1,2,2,2,2,2,3,3,-1,-1,-1},
	/* <seccion1> */ {-1,4,5,6,7,8,-1,-1,-1,-1,-1},
	/* <punto_entrada> */ {-1,-1,-1,-1,-1,-1,9,10,-1,-1,-1},
	/* <identificador> */ {-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1},
	/* <final> */ {-1,-1,-1,-1,-1,-1,-1,12,-1,-1,-1}
};

/* Tabla de lados derechos */
const int LadosDerechos[13][MAX_LADO_DER] =
{
	{12,8,16,0},
	{17,15,13,-1},
	{13,14,-1,-1},
	{-1,-1,-1,-1},
	{1,-1,-1,-1},
	{2,-1,-1,-1},
	{3,-1,-1,-1},
	{4,-1,-1,-1},
	{5,-1,-1,-1},
	{6,-1,-1,-1},
	{-1,-1,-1,-1},
	{9,-1,-1,-1},
	{7,-1,-1,-1}
};
