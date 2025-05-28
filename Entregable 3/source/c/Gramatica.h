/*
 * Gramatica.h
 *
 * 2025/05/28 13:53:55
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
	#define TERMINAL(X)  ((0 <= (X)) && ((X) <= 99))
	#define NO_TERMINAL(X)  ((100 <= (X)) && ((X) <= 157))
	#define MARCA_DERECHA 99
	#define NO_TERMINAL_INICIAL 100
	#define MAX_LADO_DER 7

	/* Constantes con las rutinas semánticas */
	/* NO SE DETECTARON SÍMBOLOS SEMÁNTICOS EN LA GRAMÁTICA */

	/* Prototipos de las tablas */
	extern const int TablaParsing[58][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[125][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
