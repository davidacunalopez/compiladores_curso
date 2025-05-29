/*
 * GTablaFollows.java
 *
 * 2025/05/29 09:00:37
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */

package Gramatica;

/**
 * Esta clase contiene la tabla de follows
 * y los métodos necesarios para acceder a ella
 */
abstract class GTablaFollows
{
	/**
	 * Tabla de follows
	 * Contiene los números de los terminales
	 * de los follows de cada no-terminal (filas)
	 */
	private static final int[][] TablaFollows =
	{
		/* <inicio> */ {Gramatica.MARCA_DERECHA,-1},
		/* <identificador> */ {Gramatica.MARCA_DERECHA,2}
	};

	/**
	 * Método getTablaFollows
			Obtiene el número de terminal del follow del no-terminal
	 * @param numNoTerminal
			Número de no-terminal
	 * @param numColumna
			Número de columna
	 */
	static final int getTablaFollows(int numNoTerminal, int numColumna)
	{
		return TablaFollows[numNoTerminal][numColumna];
	}
}
