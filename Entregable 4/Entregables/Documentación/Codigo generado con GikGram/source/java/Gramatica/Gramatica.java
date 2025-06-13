/*
 * Gramatica.java
 *
 * 2025/06/12 18:44:36
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
	public static final int CrearTLG = 191;
	public static final int EmpezarAnalizarReturn = 192;
	public static final int ComprobarReturn = 193;
	public static final int AlmacenarTipoConstante = 194;
	public static final int ValidarExistenciaIdentificadorConstante = 195;
	public static final int ValidarTipoValorConstante = 196;
	public static final int ValidarExistenciaIdentificadorTipo = 197;
	public static final int ValidarValorTipo = 198;
	public static final int AlmacenarTipoVariable = 199;
	public static final int BorrarTipoVariable = 200;
	public static final int AlmacenarFuncion = 201;
	public static final int AlmacenarTipoFuncion = 202;
	public static final int AlmacenarProcedimiento = 203;
	public static final int BorrarIdentificador = 204;
	public static final int AlmacenarTipoParametroFormal = 205;
	public static final int ValidarExistenciaIdentificadorParametroFormal = 206;
	public static final int ValidarExistenciaIdentificadorParametroReal = 207;
	public static final int ValidarExistenciaIdentificadorVariable = 208;
	public static final int ValidarTipoValorVariable = 209;
	public static final int ValidarIdentificadorIncrementoDecremento = 210;
	public static final int AntesVerificarAsignacion = 211;
	public static final int VerificarAsignacion = 212;
	public static final int ValidarOperacionCaracter = 213;
	public static final int ValidarOperacionString = 214;
	public static final int SiHayReturn = 215;
	public static final int ValidarCondicionWhile = 216;
	public static final int ValidarIdentificadorForRecorrido = 217;
	public static final int ValidarLiteralEnteraFor = 218;
	public static final int ValidarTopeFor = 219;
	public static final int ValidarCondicionRepeat = 220;
	public static final int ValidarIdentificadorWith = 221;
	public static final int EmpezarAnalizarDefaultSwitch = 222;
	public static final int HayDefaultSwitch = 223;
	public static final int SiHayDefaultSwitch = 224;
	public static final int ValidarOperacionComparacion = 225;
	public static final int ValidarOperacionLogica = 226;
	public static final int ValidarValorIdentificador = 227;
	public static final int ValidarValorValor = 228;
	public static final int ValidarTipoEntera = 229;
	public static final int ValidarTipoFlotante = 230;
	public static final int ValidarTipoString = 231;

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
		return ((99 <= numSimbolo) && (numSimbolo <= 190));
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
		return ((191 <= numSimbolo) && (numSimbolo <= 231));
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
