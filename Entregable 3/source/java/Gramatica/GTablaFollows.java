/*
 * GTablaFollows.java
 *
 * 2025/05/29 10:02:14
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
		/* <inicio> */ {Gramatica.MARCA_DERECHA,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <seccion> */ {Gramatica.MARCA_DERECHA,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <seccion1_bedrock> */ {Gramatica.MARCA_DERECHA,2,3,4,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <seccion1_resourcepack> */ {Gramatica.MARCA_DERECHA,3,4,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <seccion1_inventory> */ {Gramatica.MARCA_DERECHA,4,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <seccion1_recipe> */ {Gramatica.MARCA_DERECHA,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <seccion1_craftingtable> */ {Gramatica.MARCA_DERECHA,6,52,85,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <sistema_asignacion_constante> */ {Gramatica.MARCA_DERECHA,2,3,4,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <sistema_asignacion_tipos> */ {Gramatica.MARCA_DERECHA,3,4,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <sistema_asignacion_variables> */ {Gramatica.MARCA_DERECHA,4,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <encabezado> */ {Gramatica.MARCA_DERECHA,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <parentesis> */ {Gramatica.MARCA_DERECHA,78,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <parametros> */ {Gramatica.MARCA_DERECHA,71,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <parametros_formales> */ {Gramatica.MARCA_DERECHA,71,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <mas_parametros_formales> */ {Gramatica.MARCA_DERECHA,71,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <parametros_reales> */ {Gramatica.MARCA_DERECHA,71,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <mas_parametros_reales> */ {Gramatica.MARCA_DERECHA,71,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <lista_ids_valores> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <mas_lista_ids_valores> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <tipo> */ {Gramatica.MARCA_DERECHA,85,76,88,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <literal_booleano> */ {Gramatica.MARCA_DERECHA,76,2,3,4,5,6,89,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <literal_flotante> */ {Gramatica.MARCA_DERECHA,31,76,2,3,4,5,6,89,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <literal_entero> */ {Gramatica.MARCA_DERECHA,27,28,29,30,31,38,39,40,41,46,47,48,49,50,51,76,2,3,4,5,6,89},
		/* <literal_caracter> */ {Gramatica.MARCA_DERECHA,34,35,36,37,76,2,3,4,5,6,89,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <literal_string> */ {Gramatica.MARCA_DERECHA,42,43,44,45,76,2,3,4,5,6,89,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <literal_arreglo> */ {Gramatica.MARCA_DERECHA,76,2,3,4,5,6,89,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <literal_registro> */ {Gramatica.MARCA_DERECHA,76,2,3,4,5,6,89,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <punto_entrada> */ {Gramatica.MARCA_DERECHA,77,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <valor> */ {Gramatica.MARCA_DERECHA,89,76,2,3,4,5,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <terminador> */ {Gramatica.MARCA_DERECHA,8,9,10,11,12,13,14,15,16,17,52,85,6,53,5,4,3,-1,-1,-1,-1,-1},
		/* <instruccion> */ {Gramatica.MARCA_DERECHA,53,52,85,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <bloque> */ {Gramatica.MARCA_DERECHA,52,85,53,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <operador> */ {Gramatica.MARCA_DERECHA,21,26,20,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <operacion_incre_decre> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <operacion_caracter> */ {Gramatica.MARCA_DERECHA,22,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <operacion_logica> */ {Gramatica.MARCA_DERECHA,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <operacion_string> */ {Gramatica.MARCA_DERECHA,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <operacion_flotante> */ {Gramatica.MARCA_DERECHA,20,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <operacion_comparacion> */ {Gramatica.MARCA_DERECHA,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <variable> */ {Gramatica.MARCA_DERECHA,53,52,85,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <variable2> */ {Gramatica.MARCA_DERECHA,53,52,85,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <variable_asignacion> */ {Gramatica.MARCA_DERECHA,53,52,85,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <variable_asignacion_operando> */ {Gramatica.MARCA_DERECHA,53,52,85,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <expresion_booleana> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <expresion_flotante> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <mas_expresion_flotante> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <expresion_entera> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <mas_expresion_entera> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <expresion_caracter> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <mas_expresion_caracter> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <expresion_string> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <mas_expresion_string> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <expresion_arreglo> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <expresion_registro> */ {Gramatica.MARCA_DERECHA,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <asignacion_operando> */ {Gramatica.MARCA_DERECHA,20,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <identificador> */ {Gramatica.MARCA_DERECHA,94,26,78,70,89,27,28,29,30,31,32,33,71,-1,-1,-1,-1,-1,-1,-1,-1,-1},
		/* <final> */ {Gramatica.MARCA_DERECHA,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1}
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
