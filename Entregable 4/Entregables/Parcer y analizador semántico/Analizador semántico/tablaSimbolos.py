class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
       
        self.atributos = {}
        self.siguiente = None

class TablaSimbolos:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    def funcion_hash(self, nombre):
        suma = 0
        for i, c in enumerate(nombre):
            suma += ord(c) * (i + 1)  # Peso según la posición
        return suma % self.tamaño

    def crear_tabla(self):
        self.tabla = [None] * self.tamaño

    def existe(self, nombre):
        nodo = self._buscar_nodo(nombre)
        return nodo is not None

    def buscar(self, nombre):
        nodo = self._buscar_nodo(nombre)
        if nodo:
            return {'nombre': nodo.nombre, 'atributos': nodo.atributos}
        return None

    def agregar(self, nombre):
        indice = self.funcion_hash(nombre)
        nuevo = Nodo(nombre)

        actual = self.tabla[indice]
        anterior = None

        while actual and actual.nombre < nombre:
            anterior = actual
            actual = actual.siguiente

        if actual and actual.nombre == nombre:
            
            return False

        if anterior is None:
            nuevo.siguiente = self.tabla[indice]
            self.tabla[indice] = nuevo
        else:
            nuevo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo
        return True

    def modificar_atributo(self, nombre, clave, valor):
        nodo = self._buscar_nodo(nombre)
        if nodo:
            nodo.atributos[clave] = valor
            return True
        else:
            return False
            

    def eliminar_tabla(self):
        self.tabla = [None] * self.tamaño

    def borrar_simbolo(self, nombre):
        indice = self.funcion_hash(nombre)
        actual = self.tabla[indice]
        anterior = None

        while actual:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.tabla[indice] = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def _buscar_nodo(self, nombre):
        indice = self.funcion_hash(nombre)
        actual = self.tabla[indice]
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None
    
    def imprimir(self):
        for nodo in self.tabla:
            if nodo != None:
                print(nodo.nombre + str(nodo.atributos))
