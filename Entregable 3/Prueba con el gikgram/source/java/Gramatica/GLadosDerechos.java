/*
 * GLadosDerechos.java
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
 * Esta clase contiene la tabla de lados derechos
 * y los métodos necesarios para acceder a ella
 */
abstract class GLadosDerechos
{
	/**
	 * Tabla de lados derechos
	 * Contiene el lado derecho de las reglas de la gramática
	 */
	private static final int[][] LadosDerechos =
	{
		{7,2,5,0,6},
		{1,-1,-1,-1,-1}
	};

	/**
	 * Método getLadosDerechos
			Obtiene un símbolo del lado derecho de la regla
	 * @param numRegla
			Número de regla
	 * @param numColumna
			Número de columna
	 */
	static final int getLadosDerechos(int numRegla, int numColumna)
	{
		return LadosDerechos[numRegla][numColumna];
	}
}
