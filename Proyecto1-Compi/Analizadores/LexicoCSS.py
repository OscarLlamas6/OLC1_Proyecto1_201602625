from tkinter.font import Font


class LexicoCSS:
    def __init__(self, entrada):
        self.entrada = entrada
        self.estado = 0
        self.Tokens = []
        self.Errores = []
        self.Reservadas = []
        self.Cadenas = []
        self.Operadores = []
        
    def Iniciar(self):
        print("Analizador CSS!")
