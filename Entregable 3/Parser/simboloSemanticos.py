CrearTLG = 185
EmpezarAnalizarReturn = 186
ComprobarReturn = 187
AlmacenarTipoConstante = 188
ValidarExistenciaIdentificadorConstante = 189
ValidarTipoValorConstante = 190
ValidarExistenciaIdentificadorTipo = 191
ValidarValorTipo = 192
AlmacenarTipoVariable = 193
BorrarTipoVariable = 194
AlmacenarFuncion = 195
AlmacenarTipoFuncion = 196
AlmacenarProcedimiento = 197
BorrarIdentificador = 198
AlmacenarTipoParametroFormal = 199
ValidarExistenciaIdentificadorParametroFormal = 200
ValidarExistenciaIdentificadorParametroReal = 201
ValidarExistenciaIdentificadorVariable = 202
ValidarTipoValorVariable = 203
ValidarIdentificadorIncrementoDecremento = 204
AntesVerificarAsignacion = 205
VerificarAsignacion = 206
ValidarOperacionEntero = 207
ValidarOperacionComparacion = 208
ValidarOperacionCaracter = 209
ValidarOperacionString = 210
SiHayReturn = 211
ValidarCondicionWhile = 212
ValidarIdentificadorForRecorrido = 213
ValidarLiteralEnteraFor = 214
ValidarTopeFor = 215
ValidarCondicionRepeat = 216
ValidarIdentificadorWith = 217
EmpezarAnalizarDefaultSwitch = 218
HayDefaultSwitch = 219
SiHayDefaultSwitch = 220
ValidarOperacionLogica = 221
ValidarValorIdentificador = 222
ValidarValorValor = 223
ValidarTipoEntera = 224
ValidarTipoFlotante = 225
ValidarTipoString = 226



cola = []

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
    "SHELF": [21]
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












