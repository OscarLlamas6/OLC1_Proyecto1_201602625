from tkinter.font import Font




class LexicoJS:
    def __init__(self, entrada):
        self.entrada = entrada
        self.estado = 0
        self.errorLex = False
        self.repetir = False
        self.anular = False
        self.col = 0
        self.cTokens = 0
        self.cErrores = 0
        self.lexemaact = ""
        self.Tokens = []
        self.Errores = []
        self.Reservadas = []
        self.Cadenas = []
        self.Operadores = []

    def Iniciar(self):
        print("Analizador JavaScript!")
        self.Tokens[:]=[]
        self.errorLex = False
        self.entrada += " \n"
        inputString = self.entrada.splitlines()
        for line in inputString:
            print(line)
       # for c in self.entrada: # iteramos en cada caracter
            