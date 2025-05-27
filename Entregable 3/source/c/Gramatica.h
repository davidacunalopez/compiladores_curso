/*
 * Gramatica.h
 *
 * 2025/05/27 09:24:37
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
	#define TERMINAL(X)  ((0 <= (X)) && ((X) <= 10))
	#define NO_TERMINAL(X)  ((11 <= (X)) && ((X) <= 16))
	#define MARCA_DERECHA 10
	#define NO_TERMINAL_INICIAL 11
	#define MAX_LADO_DER 4

	/* Constantes con las rutinas semánticas */
	/* NO SE DETECTARON SÍMBOLOS SEMÁNTICOS EN LA GRAMÁTICA */

	/* Prototipos de las tablas */
	extern const int TablaParsing[6][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[12][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
