from tkinter.font import Font
import Token
from Token import *
import Error
from Error import *
import Operacion
from Operacion import *
import SintacticoRMT
from SintacticoRMT import *





class LexicoRMT:
    def __init__(self, entrada):
        self.entrada = entrada
        self.estado = 0
        self.errorLex = False
        self.repetir = False
        self.anular = False
        self.col = 0
        self.fila = 0
        self.cTokens = 0
        self.cErrores = 0
        self.lexemaact = ""
        self.Tokens = []
        self.Errores = []
        self.Operaciones = []



    def Iniciar(self):
        self.Operaciones[:]=[]
        self.entrada += " "   
        self.fila = 0     
        self.SplitOperaciones = self.entrada.split("\n")
        for operacion in self.SplitOperaciones:
            self.fila+=1
            operacion+= "  "
            self.Tokens[:]=[]
            self.errorLex = False 
            for c in operacion: # iteramos en cada caracter       
                self.col+=1        
                self.anular = False
                self.repetir = True
                while self.repetir:
                    self.repetir = False
                    if self.estado == 0:
                        if c.isspace():
                            pass
                        elif c == "*":
                            self.lexemaact+=c
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_POR",self.lexemaact,"Operador"))
                            self.lexemaact = ""
                        elif c == "/":
                            self.lexemaact+=c
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_DIV",self.lexemaact,"Operador"))
                            self.lexemaact = ""
                        elif c == "+":
                            self.lexemaact+=c
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MAS",self.lexemaact,"Operador"))
                            self.lexemaact = ""
                        elif c == "-":
                            self.lexemaact+=c
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MENOS",self.lexemaact,"Operador"))
                            self.lexemaact = ""
                        elif c == "(":
                            self.lexemaact+=c
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PA",self.lexemaact,"Simbolo"))
                            self.lexemaact = ""
                        elif c == ")":
                            self.lexemaact+=c
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PC",self.lexemaact,"Simbolo"))
                            self.lexemaact = ""
                        elif c.isalpha() or c == "_": #letra
                            self.estado = 1
                            self.lexemaact = c
                        elif c.isdigit(): #numero
                            self.estado = 2
                            self.lexemaact = c
                        else:
                            self.lexemaact = c
                            self.cErrores+=1
                            self.Errores.append(Error(self.cErrores, self.fila, self.col, self.lexemaact, "Léxico", "Elemento léxico desconocido"))
                            self.lexemaact = ""
                            self.errorLex = True
                    elif self.estado == 1:
                        if c.isalpha() or c.isdigit() or c == '_':
                            self.estado = 1
                            self.lexemaact+=c
                        else:                        
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ID",self.lexemaact,"Identificador"))
                            self.lexemaact = ""
                            self.estado=0
                            if self.anular is False:
                                self.repetir = True
                            elif self.anular is True:
                                self.repetir = False
                                self.anular = False
                            self.lexemaact = ""
                    elif self.estado == 2: #posibles transiciones para el estado 2 (valores numericos)
                        if c.isdigit():
                            self.estado = 2
                            self.lexemaact += c
                        elif c == ".":                    
                            self.estado = 3
                            self.lexemaact += c
                        else:
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_NUM",self.lexemaact,"Valor numérico"))
                            self.lexemaact = ""
                            self.estado = 0
                            self.repetir = True
                    elif self.estado == 3: #posibles transiciones para el estado 3 (numeros decimales con y sin signo)
                        if c.isdigit():
                            self.estado = 4
                            self.lexemaact +=c
                        else:
                            self.cErrores+=1
                            self.Errores.append(Error(self.cErrores, self.fila, self.col, self.lexemaact, "Léxico", "Elemento léxico desconocido"))
                            self.lexemaact = ""
                            self.errorLex = True
                            self.estado = 0
                            self.repetir = True
                    elif self.estado == 4: #posibles transiciones para el estado 4 (numeros decimales con signo)
                        if c.isdigit():
                            self.estado = 4
                            self.lexemaact += c
                        else:
                            self.cTokens+=1
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_NUM",self.lexemaact,"Valor numérico"))
                            self.lexemaact = ""
                            self.estado = 0
                            self.repetir = True
            if self.estado != 0:
                self.errorLex = True
            self.cTokens+=1
            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_#","#","Fin de cadena"))
            if self.errorLex:
                self.Operaciones.append(Operacion(self.fila,operacion,"Incorrecto"))
            else:
                b = SintacticoRMT(self.Tokens)
                if b.Error:
                    self.Operaciones.append(Operacion(self.fila,operacion,"Incorrecto"))
                else:
                    self.Operaciones.append(Operacion(self.fila,operacion,"Correcto"))    
                
        
        
        
        
        
        
               