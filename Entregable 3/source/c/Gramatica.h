/*
 * Gramatica.h
 *
 * 2025/05/30 13:08:38
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
	#define NO_TERMINAL(X)  ((99 <= (X)) && ((X) <= 184))
	#define MARCA_DERECHA 98
	#define NO_TERMINAL_INICIAL 99
	#define MAX_LADO_DER 10

	/* Constantes con las rutinas semánticas */
	#define CrearTLG 185
	#define AlmacenarTipoConstante 186
	#define ValidarExistenciaIdentificadorConstante 187
	#define ValidarTipoValorConstante 188
	#define ValidarExistenciaIdentificadorTipo 189
	#define ValidarValorTipo 190
	#define AlmacenarTipoVariable 191
	#define BorrarTipoVariable 192
	#define AlmacenarFuncion 193
	#define AlmacenarTipoFuncion 194
	#define AlmacenarProcedimiento 195
	#define BorrarIdentificador 196
	#define AlmacenarTipoParametroFormal 197
	#define ValidarExistenciaIdentificadorParametroFormal 198
	#define ValidarExistenciaIdentificadorVariable 199
	#define ValidarTipoValorVariable 200

	/* Prototipos de las tablas */
	extern const int TablaParsing[86][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[182][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
