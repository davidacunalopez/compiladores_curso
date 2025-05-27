/*
 * GNombresTerminales.java
 *
 * 2025/05/27 17:00:59
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
		"WORLDSAVE",
		":",
		"ID",
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
