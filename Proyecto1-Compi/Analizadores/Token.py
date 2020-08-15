class Token:
    def __init__(self, numero, fila, columna, token, lexema, tipo):
        self.numero = numero
        self.fila = fila
        self.columna = columna
        self.token = token
        self.lexema = lexema
        self.tipo = tipo
    
    def getToken(self):
        return self.token
    
    def getLexema(self):
        return self.lexema
    
    def getTipo(self):
        return self.tipo
