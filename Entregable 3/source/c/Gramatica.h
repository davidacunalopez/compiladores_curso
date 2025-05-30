/*
 * Gramatica.h
 *
 * 2025/05/30 09:32:34
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
	#define MAX_LADO_DER 10

	/* Constantes con las rutinas semánticas */
	#define CrearTLG 184
	#define AlmacenarTipoConstante 185
	#define ValidarExistenciaIdentificadorConstante 186
	#define ValidarTipoValorConstante 187
	#define ValidarExistenciaIdentificadorTipo 188
	#define ValidarValorTipo 189
	#define AlmacenarTipoVariable 190
	#define BorrarTipoVariable 191
	#define AlmacenarFuncion 192
	#define AlmacenarTipoFuncion 193
	#define AlmacenarProcedimiento 194
	#define BorrarIdentificador 195
	#define AlmacenarTipoParametroFormal 196
	#define ValidarExistenciaIdentificadorParametroFormal 197
	#define ValidarExistenciaIdentificadorVariable 198
	#define ValidarTipoValorVariable 199

	/* Prototipos de las tablas */
	extern const int TablaParsing[85][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[178][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
