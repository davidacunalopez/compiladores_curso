CrearTLG = 184 #Crear TSG
AlmacenarTipoConstante = 185 #almacena tipo para creacion de constante
ValidarExistenciaIdentificadorConstante = 186 #crear constante
ValidarTipoValorConstante = 187 #Valida que el tipo de la literal sea igual al tipo de la constante
ValidarExistenciaIdentificadorTipo = 188 #crear tipo
ValidarValorTipo = 189 #Valida que el valor sea un tipo
AlmacenarTipoVariable = 190  #almacena tipo para creacion de variable
BorrarTipoVariable = 191  #borra el tipo almacenado para creacion de variable
AlmacenarFuncion = 192 #Crear funcion
AlmacenarProcedimiento = 193 #crear procedimiento
AlmacenarTipoParametroFormal = 194 #guarda eltipo del parametro formal actual
ValidarExistenciaIdentificadorParametroFormal = 195 #crea el parametro formal
ValidarExistenciaIdentificadorVariable = 196  #crear variable
ValidarTipoValorVariable = 197 #Valida que el tipo de la literal sea igual al tipo de la variable

CrearTLG = 185
AlmacenarTipoConstante = 186
ValidarExistenciaIdentificadorConstante = 187
ValidarTipoValorConstante = 188
ValidarExistenciaIdentificadorTipo = 189
ValidarValorTipo = 190
AlmacenarTipoVariable = 191
BorrarTipoVariable = 192
AlmacenarFuncion = 193
AlmacenarTipoFuncion = 194
AlmacenarProcedimiento = 195
BorrarIdentificador = 196
AlmacenarTipoParametroFormal = 197
ValidarExistenciaIdentificadorParametroFormal = 198
ValidarExistenciaIdentificadorVariable = 199
ValidarTipoValorVariable = 200
VerificarAsignacion = 201




cola = [None,None,None,None]

def insertar_cola(dato):
    cola = cola[1:]+[dato]




#Variables auxiliares
tipoleido = None
identificardorLeido = False
tiposCodigoLiteral = {
    "STACK": [21],
    "RUNE": [22],
    "SPIDER": [23],
    "TORCH": [18,19],
    "CHEST": [24],
}
CodigosTipos = {
    "STACK":9,
    "RUNE":10,
    "SPIDER":11,
    "TORCH":12,
    "CHEST":13,
    "BOOK":14,
    "GHAST":15,
    "SHELF":16,
    "ENTITY":17,
    
}












