CrearTLG = 191
EmpezarAnalizarReturn = 192
ComprobarReturn = 193
AlmacenarTipoConstante = 194
ValidarExistenciaIdentificadorConstante = 195
ValidarTipoValorConstante = 196
ValidarExistenciaIdentificadorTipo = 197
ValidarValorTipo = 198
AlmacenarTipoVariable = 199
BorrarTipoVariable = 200
AlmacenarFuncion = 201
AlmacenarTipoFuncion = 202
AlmacenarProcedimiento = 203
BorrarIdentificador = 204
AlmacenarTipoParametroFormal = 205
ValidarExistenciaIdentificadorParametroFormal = 206
ValidarExistenciaIdentificadorParametroReal = 207
ValidarExistenciaIdentificadorVariable = 208
ValidarTipoValorVariable = 209
ValidarIdentificadorIncrementoDecremento = 210
AntesVerificarAsignacion = 211
VerificarAsignacion = 212
ValidarOperacionCaracter = 213
ValidarOperacionString = 214
SiHayReturn = 215
ValidarCondicionWhile = 216
ValidarIdentificadorForRecorrido = 217
ValidarLiteralEnteraFor = 218
ValidarTopeFor = 219
ValidarCondicionRepeat = 220
ValidarIdentificadorWith = 221
EmpezarAnalizarDefaultSwitch = 222
HayDefaultSwitch = 223
SiHayDefaultSwitch = 224
ValidarOperacionComparacion = 225
ValidarOperacionLogica = 226
ValidarValorIdentificador = 227
ValidarValorValor = 228
ValidarTipoEntera = 229
ValidarTipoFlotante = 230
ValidarTipoString = 231


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












