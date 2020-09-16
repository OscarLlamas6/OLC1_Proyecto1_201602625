class Operacion:
    def __init__(self, numero, oper, resultado):
        self.numero = numero
        self.oper = oper
        self.resultado = resultado

    def getNumero(self):
        return self.numero
    
    def getOper(self):
        return self.oper
    
    def getResultado(self):
        return self.resultado