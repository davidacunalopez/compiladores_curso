/*
 * Gramatica.h
 *
 * 2025/06/12 18:44:36
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
	#define NO_TERMINAL(X)  ((99 <= (X)) && ((X) <= 190))
	#define MARCA_DERECHA 98
	#define NO_TERMINAL_INICIAL 99
	#define MAX_LADO_DER 10

	/* Constantes con las rutinas semánticas */
	#define CrearTLG 191
	#define EmpezarAnalizarReturn 192
	#define ComprobarReturn 193
	#define AlmacenarTipoConstante 194
	#define ValidarExistenciaIdentificadorConstante 195
	#define ValidarTipoValorConstante 196
	#define ValidarExistenciaIdentificadorTipo 197
	#define ValidarValorTipo 198
	#define AlmacenarTipoVariable 199
	#define BorrarTipoVariable 200
	#define AlmacenarFuncion 201
	#define AlmacenarTipoFuncion 202
	#define AlmacenarProcedimiento 203
	#define BorrarIdentificador 204
	#define AlmacenarTipoParametroFormal 205
	#define ValidarExistenciaIdentificadorParametroFormal 206
	#define ValidarExistenciaIdentificadorParametroReal 207
	#define ValidarExistenciaIdentificadorVariable 208
	#define ValidarTipoValorVariable 209
	#define ValidarIdentificadorIncrementoDecremento 210
	#define AntesVerificarAsignacion 211
	#define VerificarAsignacion 212
	#define ValidarOperacionCaracter 213
	#define ValidarOperacionString 214
	#define SiHayReturn 215
	#define ValidarCondicionWhile 216
	#define ValidarIdentificadorForRecorrido 217
	#define ValidarLiteralEnteraFor 218
	#define ValidarTopeFor 219
	#define ValidarCondicionRepeat 220
	#define ValidarIdentificadorWith 221
	#define EmpezarAnalizarDefaultSwitch 222
	#define HayDefaultSwitch 223
	#define SiHayDefaultSwitch 224
	#define ValidarOperacionComparacion 225
	#define ValidarOperacionLogica 226
	#define ValidarValorIdentificador 227
	#define ValidarValorValor 228
	#define ValidarTipoEntera 229
	#define ValidarTipoFlotante 230
	#define ValidarTipoString 231

	/* Prototipos de las tablas */
	extern const int TablaParsing[92][NO_TERMINAL_INICIAL];
	extern const int LadosDerechos[189][MAX_LADO_DER];

#endif /* INC_Gramatica_h_ */
