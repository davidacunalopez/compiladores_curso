/*
 * GLadosDerechos.java
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
		{12,8,16,0},
		{17,15,13,-1},
		{13,14,-1,-1},
		{-1,-1,-1,-1},
		{1,-1,-1,-1},
		{2,-1,-1,-1},
		{3,-1,-1,-1},
		{4,-1,-1,-1},
		{5,-1,-1,-1},
		{6,-1,-1,-1},
		{-1,-1,-1,-1},
		{9,-1,-1,-1},
		{7,-1,-1,-1}
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
