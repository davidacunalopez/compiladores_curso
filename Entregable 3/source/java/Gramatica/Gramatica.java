/*
 * Gramatica.java
 *
 * 2025/05/30 13:08:38
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright © Olminsky 2011 Derechos reservados
 * Reproducción sin fines de lucro permitida
 */

package Gramatica;

/**
 * Esta clase contiene:
 * - Constantes necesarias para el driver de parsing
 * - Constantes con las rutinas semánticas
 * - Y los métodos necesarios para el driver de parsing
 */
public abstract class Gramatica
{
	/* Esta es la única clase que se accede fuera del paquete Gramatica */

	/**
	 * Constante que contiene el código de familia del terminal de fin de archivo
	 */
	public static final int MARCA_DERECHA = 98;

	/**
	 * Constante que contiene el número del no-terminal inicial
	 * (el primer no-terminal que aparece en la gramática)
	 */
	public static final int NO_TERMINAL_INICIAL = 99;

	/**
	 * Constante que contiene el número máximo de columnas que tiene los lados derechos
	 */
	public static final int MAX_LADO_DER = 10;

	/**
	 * Constante que contiene el número máximo de follows
	 */
	public static final int MAX_FOLLOWS = 41;

	/* Constantes con las rutinas semánticas */
	public static final int CrearTLG = 185;
	public static final int AlmacenarTipoConstante = 186;
	public static final int ValidarExistenciaIdentificadorConstante = 187;
	public static final int ValidarTipoValorConstante = 188;
	public static final int ValidarExistenciaIdentificadorTipo = 189;
	public static final int ValidarValorTipo = 190;
	public static final int AlmacenarTipoVariable = 191;
	public static final int BorrarTipoVariable = 192;
	public static final int AlmacenarFuncion = 193;
	public static final int AlmacenarTipoFuncion = 194;
	public static final int AlmacenarProcedimiento = 195;
	public static final int BorrarIdentificador = 196;
	public static final int AlmacenarTipoParametroFormal = 197;
	public static final int ValidarExistenciaIdentificadorParametroFormal = 198;
	public static final int ValidarExistenciaIdentificadorVariable = 199;
	public static final int ValidarTipoValorVariable = 200;

	/**
	 * Método esTerminal
			Devuelve true si el símbolo es un terminal
			o false de lo contrario
	 * @param numSimbolo
			Número de símbolo
	 */
	public static final boolean esTerminal(int numSimbolo)
	{
		return ((0 <= numSimbolo) && (numSimbolo <= 98));
	}

	/**
	 * Método esNoTerminal
			Devuelve true si el símbolo es un no-terminal
			o false de lo contrario
	 * @param numSimbolo
			Número de símbolo
	 */
	public static final boolean esNoTerminal(int numSimbolo)
	{
		return ((99 <= numSimbolo) && (numSimbolo <= 184));
	}

	/**
	 * Método esSimboloSemantico
			Devuelve true si el símbolo es un símbolo semántico
			(incluyendo los símbolos de generación de código)
			o false de lo contrario
	 * @param numSimbolo
			Número de símbolo
	 */
	public static final boolean esSimboloSemantico(int numSimbolo)
	{
		return ((185 <= numSimbolo) && (numSimbolo <= 200));
	}

	/**
	 * Método getTablaParsing
			Devuelve el número de regla contenida en la tabla de parsing
	 * @param numNoTerminal
			Número del no-terminal
	 * @param numTerminal
			Número del terminal
	 */
	public static final int getTablaParsing(int numNoTerminal, int numTerminal)
	{
		return GTablaParsing.getTablaParsing(numNoTerminal, numTerminal);
	}

	/**
	 * Método getLadosDerechos
			Obtiene un símbolo del lado derecho de la regla
	 * @param numRegla
			Número de regla
	 * @param numColumna
			Número de columna
	 */
	public static final int getLadosDerechos(int numRegla, int numColumna)
	{
		return GLadosDerechos.getLadosDerechos(numRegla, numColumna);
	}

	/**
	 * Método getNombresTerminales
			Obtiene el nombre del terminal
	 * @param numTerminal
			Número del terminal
	 */
	public static final String getNombresTerminales(int numTerminal)
	{
		return GNombresTerminales.getNombresTerminales(numTerminal);
	}

	/**
	 * Método getTablaFollows
			Obtiene el número de terminal del follow del no-terminal
	 * @param numNoTerminal
			Número de no-terminal
	 * @param numColumna
			Número de columna
	 */
	public static final int getTablaFollows(int numNoTerminal, int numColumna)
	{
		return GTablaFollows.getTablaFollows(numNoTerminal, numColumna);
	}
}
