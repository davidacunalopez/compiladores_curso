/*
 * Gramatica.h
 *
 * 2025/05/30 02:03:15
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
	#define TERMINAL(X)  ((0 <= (X)) && ((X) <= 98))
	#define NO_TERMINAL(X)  ((99 <= (X)) && ((X) <= 183))
	#define MARCA_DERECHA 98
	#define NO_TERMINAL_INICIAL 99
	#define MAX_LADO_DER 7

	/* Constantes con las rutinas semánticas */
	/* NO SE DETECTARON SÍMBOLOS SEMÁNTICOS EN LA GRAMÁTICA */

	/* Prototipos de las tablas */
	extern const int TablaParsing[85][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[178][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
