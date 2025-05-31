/*
 * Gramatica.h
 *
 * 2025/05/30 19:49:06
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
	#define EmpezarAnalizarReturn 186
	#define ComprobarReturn 187
	#define AlmacenarTipoConstante 188
	#define ValidarExistenciaIdentificadorConstante 189
	#define ValidarTipoValorConstante 190
	#define ValidarExistenciaIdentificadorTipo 191
	#define ValidarValorTipo 192
	#define AlmacenarTipoVariable 193
	#define BorrarTipoVariable 194
	#define AlmacenarFuncion 195
	#define AlmacenarTipoFuncion 196
	#define AlmacenarProcedimiento 197
	#define BorrarIdentificador 198
	#define AlmacenarTipoParametroFormal 199
	#define ValidarExistenciaIdentificadorParametroFormal 200
	#define ValidarExistenciaIdentificadorParametroReal 201
	#define ValidarExistenciaIdentificadorVariable 202
	#define ValidarTipoValorVariable 203
	#define ValidarIdentificadorIncrementoDecremento 204
	#define AntesVerificarAsignacion 205
	#define VerificarAsignacion 206
	#define ValidarOperacionEntero 207
	#define ValidarOperacionComparacion 208
	#define ValidarOperacionCaracter 209
	#define ValidarOperacionString 210
	#define SiHayReturn 211
	#define ValidarCondicionWhile 212
	#define ValidarIdentificadorForRecorrido 213
	#define ValidarLiteralEnteraFor 214
	#define ValidarTopeFor 215
	#define ValidarCondicionRepeat 216
	#define ValidarIdentificadorWith 217
	#define EmpezarAnalizarDefaultSwitch 218
	#define HayDefaultSwitch 219
	#define SiHayDefaultSwitch 220
	#define ValidarOperacionLogica 221
	#define ValidarValorIdentificador 222
	#define ValidarValorValor 223
	#define ValidarTipoEntera 224
	#define ValidarTipoFlotante 225
	#define ValidarTipoString 226

	/* Prototipos de las tablas */
	extern const int TablaParsing[86][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[182][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
