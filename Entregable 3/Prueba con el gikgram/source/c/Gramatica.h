/*
 * Gramatica.h
 *
 * 2025/05/29 09:00:37
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */
#pragma once

#ifndef INC_Gramatica_h_
	#define INC_Gramatica_h_

	/* Constantes necesarias para un driver de parsing */
	#define TERMINAL(X)  ((0 <= (X)) && ((X) <= 3))
	#define NO_TERMINAL(X)  ((4 <= (X)) && ((X) <= 5))
	#define MARCA_DERECHA 3
	#define NO_TERMINAL_INICIAL 4
	#define MAX_LADO_DER 5

	/* Constantes con las rutinas semánticas */
	#define CreaTSG 6
	#define TerminaTSG 7

	/* Prototipos de las tablas */
	extern const int TablaParsing[2][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[2][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
