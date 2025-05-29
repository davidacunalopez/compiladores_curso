/*
 * GNombresTerminales.java
 *
 * 2025/05/29 11:05:14
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */

package Gramatica;

/**
 * Esta clase contiene los nombres de los terminales
 * y los métodos necesarios para acceder a ella
 */
abstract class GNombresTerminales
{
	/**
	 * Contiene los nombres de los terminales
	 */
	private static final String[] NombresTerminales =
	{
		"WORLDNAME",
		"BEDROCK",
		"RESOURCEPACK",
		"INVENTORY",
		"RECIPE",
		"CRAFTINGTABLE",
		"SPAWNPOINT",
		"OBSIDIAN",
		"ANVIL",
		"STACK",
		"RUNE",
		"SPIDER",
		"TORCH",
		"CHEST",
		"BOOK",
		"GHAST",
		"SHELF",
		"ENTITY",
		"ON",
		"OFF",
		"LITERAL_FLOTANTE",
		"LITERAL_ENTERO",
		"LITERAL_CARACTER",
		"LITERAL_STRING",
		"LITERAL_ARREGLO",
		"LITERAL_REGISTRO",
		"=",
		"+",
		"-",
		"*",
		"/",
		"%",
		"SOULSAND",
		"MAGMA",
		"ISENGRAVED",
		"ISINSCRIBED",
		"ETCHUP",
		"ETCHDOWN",
		"AND",
		"OR",
		"NOT",
		"XOR",
		"BIND",
		"FROM",
		"EXCEPT",
		"SEEK",
		"<",
		">",
		"<=",
		">=",
		"IS",
		"ISNOT",
		"POLLOCRUDO",
		"POLLOASADO",
		"CRAFT",
		"MISS",
		"SILENCE",
		"REPEATER",
		"TARGET",
		"JUKEBOX",
		"DISK",
		"SPAWNER",
		"WALK",
		"STEP",
		"WITHER",
		"BREAK",
		"CONTINUE",
		"HALT",
		"SPELL",
		"RITUAL",
		"(",
		")",
		"RESPAWN",
		"CHUNK",
		"HOPPER",
		"DROPPER",
		";",
		"WORLDSAVE",
		"->",
		"REF",
		"DATO",
		">>",
		"[",
		"]",
		"@",
		"IDENTIFICADOR",
		"VALOR",
		"LITERAL",
		"::",
		",",
		"EXHAUSTED",
		"VARIABLE",
		"SET",
		"TO",
		":",
		"REFERENCIA",
		".",
		"CONDICION",
		"EXPRESION",
		" EOF "
	};

	/**
	 * Método getNombresTerminales
			Obtiene el nombre del terminal
	 * @param numTerminal
			Número del terminal
	 */
	static final String getNombresTerminales(int numTerminal)
	{
		return NombresTerminales[numTerminal];
	}
}
