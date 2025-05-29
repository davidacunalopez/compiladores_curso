/*
 * GTablaParsing.java
 *
 * 2025/05/29 09:19:24
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */

package Gramatica;

/**
 * Esta clase contiene la tabla de parsing
 * y los métodos necesarios para acceder a ella
 */
abstract class GTablaParsing
{
	/**
	 * Tabla de parsing
	 * Contiene los números de regla que hay que ejecutar
	 * con base a los no-terminales (filas) y los terminales (columnas)
	 */
	private static final int[][] TablaParsing =
	{
		/* <inicio> */ {0,-1,-1,-1},
		/* <identificador> */ {-1,1,-1,-1}
	};

	/**
	 * Método getTablaParsing
			Devuelve el número de regla contenida en la tabla de parsing
	 * @param numNoTerminal
			Número del no-terminal
	 * @param numTerminal
			Número del terminal
	 */
	static final int getTablaParsing(int numNoTerminal, int numTerminal)
	{
		return TablaParsing[numNoTerminal][numTerminal];
	}
}
