class Error:
    def __init__(self, numero, fila, columna, error, tipo, descripcion):
        self.numero = numero
        self.fila = fila
        self.columna = columna
        self.error = error 
        self.tipo = tipo
        self.descripcion = descripcion
    
    def getNumero(self):
        return self.numero
    
    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getError(self):
        return self.error
    
    def getDescripcion(self):
        return self.descripcion
    
    def getTipo(self):
        return self.tipo