/*
 * GTablaFollows.java
 *
 * 2025/05/27 09:24:37
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright � Olminsky 2011 Derechos reservados
 * Reproducci�n sin fines de lucro permitida
 */

package Gramatica;

/**
 * Esta clase contiene la tabla de follows
 * y los m�todos necesarios para acceder a ella
 */
abstract class GTablaFollows
{
	/**
	 * Tabla de follows
	 * Contiene los n�meros de los terminales
	 * de los follows de cada no-terminal (filas)
	 */
	private static final int[][] TablaFollows =
	{
		/* <inicio> */ {Gramatica.MARCA_DERECHA,-1,-1},
		/* <inicio2> */ {Gramatica.MARCA_DERECHA,-1,-1},
		/* <seccion> */ {Gramatica.MARCA_DERECHA,6,7},
		/* <punto_entrada> */ {Gramatica.MARCA_DERECHA,7,-1},
		/* <identificador> */ {Gramatica.MARCA_DERECHA,8,-1},
		/* <final> */ {Gramatica.MARCA_DERECHA,-1,-1}
	};

	/**
	 * M�todo getTablaFollows
			Obtiene el n�mero de terminal del follow del no-terminal
	 * @param numNoTerminal
			N�mero de no-terminal
	 * @param numColumna
			N�mero de columna
	 */
	static final int getTablaFollows(int numNoTerminal, int numColumna)
	{
		return TablaFollows[numNoTerminal][numColumna];
	}
}
