/*
 * Gramatica.java
 *
 * 2025/05/30 19:49:06
 *
 * Archivo generado por GikGram 2.0
 *
 * Copyright � Olminsky 2011 Derechos reservados
 * Reproducci�n sin fines de lucro permitida
 */

package Gramatica;

/**
 * Esta clase contiene:
 * - Constantes necesarias para el driver de parsing
 * - Constantes con las rutinas sem�nticas
 * - Y los m�todos necesarios para el driver de parsing
 */
public abstract class Gramatica
{
	/* Esta es la �nica clase que se accede fuera del paquete Gramatica */

	/**
	 * Constante que contiene el c�digo de familia del terminal de fin de archivo
	 */
	public static final int MARCA_DERECHA = 98;

	/**
	 * Constante que contiene el n�mero del no-terminal inicial
	 * (el primer no-terminal que aparece en la gram�tica)
	 */
	public static final int NO_TERMINAL_INICIAL = 99;

	/**
	 * Constante que contiene el n�mero m�ximo de columnas que tiene los lados derechos
	 */
	public static final int MAX_LADO_DER = 10;

	/**
	 * Constante que contiene el n�mero m�ximo de follows
	 */
	public static final int MAX_FOLLOWS = 41;

	/* Constantes con las rutinas sem�nticas */
	public static final int CrearTLG = 185;
	public static final int EmpezarAnalizarReturn = 186;
	public static final int ComprobarReturn = 187;
	public static final int AlmacenarTipoConstante = 188;
	public static final int ValidarExistenciaIdentificadorConstante = 189;
	public static final int ValidarTipoValorConstante = 190;
	public static final int ValidarExistenciaIdentificadorTipo = 191;
	public static final int ValidarValorTipo = 192;
	public static final int AlmacenarTipoVariable = 193;
	public static final int BorrarTipoVariable = 194;
	public static final int AlmacenarFuncion = 195;
	public static final int AlmacenarTipoFuncion = 196;
	public static final int AlmacenarProcedimiento = 197;
	public static final int BorrarIdentificador = 198;
	public static final int AlmacenarTipoParametroFormal = 199;
	public static final int ValidarExistenciaIdentificadorParametroFormal = 200;
	public static final int ValidarExistenciaIdentificadorParametroReal = 201;
	public static final int ValidarExistenciaIdentificadorVariable = 202;
	public static final int ValidarTipoValorVariable = 203;
	public static final int ValidarIdentificadorIncrementoDecremento = 204;
	public static final int AntesVerificarAsignacion = 205;
	public static final int VerificarAsignacion = 206;
	public static final int ValidarOperacionEntero = 207;
	public static final int ValidarOperacionComparacion = 208;
	public static final int ValidarOperacionCaracter = 209;
	public static final int ValidarOperacionString = 210;
	public static final int SiHayReturn = 211;
	public static final int ValidarCondicionWhile = 212;
	public static final int ValidarIdentificadorForRecorrido = 213;
	public static final int ValidarLiteralEnteraFor = 214;
	public static final int ValidarTopeFor = 215;
	public static final int ValidarCondicionRepeat = 216;
	public static final int ValidarIdentificadorWith = 217;
	public static final int EmpezarAnalizarDefaultSwitch = 218;
	public static final int HayDefaultSwitch = 219;
	public static final int SiHayDefaultSwitch = 220;
	public static final int ValidarOperacionLogica = 221;
	public static final int ValidarValorIdentificador = 222;
	public static final int ValidarValorValor = 223;
	public static final int ValidarTipoEntera = 224;
	public static final int ValidarTipoFlotante = 225;
	public static final int ValidarTipoString = 226;

	/**
	 * M�todo esTerminal
			Devuelve true si el s�mbolo es un terminal
			o false de lo contrario
	 * @param numSimbolo
			N�mero de s�mbolo
	 */
	public static final boolean esTerminal(int numSimbolo)
	{
		return ((0 <= numSimbolo) && (numSimbolo <= 98));
	}

	/**
	 * M�todo esNoTerminal
			Devuelve true si el s�mbolo es un no-terminal
			o false de lo contrario
	 * @param numSimbolo
			N�mero de s�mbolo
	 */
	public static final boolean esNoTerminal(int numSimbolo)
	{
		return ((99 <= numSimbolo) && (numSimbolo <= 184));
	}

	/**
	 * M�todo esSimboloSemantico
			Devuelve true si el s�mbolo es un s�mbolo sem�ntico
			(incluyendo los s�mbolos de generaci�n de c�digo)
			o false de lo contrario
	 * @param numSimbolo
			N�mero de s�mbolo
	 */
	public static final boolean esSimboloSemantico(int numSimbolo)
	{
		return ((185 <= numSimbolo) && (numSimbolo <= 226));
	}

	/**
	 * M�todo getTablaParsing
			Devuelve el n�mero de regla contenida en la tabla de parsing
	 * @param numNoTerminal
			N�mero del no-terminal
	 * @param numTerminal
			N�mero del terminal
	 */
	public static final int getTablaParsing(int numNoTerminal, int numTerminal)
	{
		return GTablaParsing.getTablaParsing(numNoTerminal, numTerminal);
	}

	/**
	 * M�todo getLadosDerechos
			Obtiene un s�mbolo del lado derecho de la regla
	 * @param numRegla
			N�mero de regla
	 * @param numColumna
			N�mero de columna
	 */
	public static final int getLadosDerechos(int numRegla, int numColumna)
	{
		return GLadosDerechos.getLadosDerechos(numRegla, numColumna);
	}

	/**
	 * M�todo getNombresTerminales
			Obtiene el nombre del terminal
	 * @param numTerminal
			N�mero del terminal
	 */
	public static final String getNombresTerminales(int numTerminal)
	{
		return GNombresTerminales.getNombresTerminales(numTerminal);
	}

	/**
	 * M�todo getTablaFollows
			Obtiene el n�mero de terminal del follow del no-terminal
	 * @param numNoTerminal
			N�mero de no-terminal
	 * @param numColumna
			N�mero de columna
	 */
	public static final int getTablaFollows(int numNoTerminal, int numColumna)
	{
		return GTablaFollows.getTablaFollows(numNoTerminal, numColumna);
	}
}
