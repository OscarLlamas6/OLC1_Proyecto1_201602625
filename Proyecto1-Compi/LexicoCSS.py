from tkinter.font import Font
import Token
from Token import *
import Error
from Error import *


class LexicoCSS:
    def __init__(self, entrada):
        self.entrada = entrada
        self.estado = 0
        self.errorLex = False
        self.repetir = False
        self.anular = False
        self.EncontroID = False
        self.EncontroNumero = False
        self.EncontroCadena = False
        self.EncontroUnilinea = False
        self.EncontroMultilinea = False
        self.col = 0
        self.fila = 0
        self.cTokens = 0
        self.cErrores = 0
        self.lexemaact = ""
        self.Tokens = []
        self.Errores = []
        self.Reservadas = []
        self.Cadenas = []
        self.Operadores = []
        self.Comentarios = []
        self.IDs = []
        self.Path = ""
        self.PathLine = '''C:\Salida\\'''
        #self.PathLine = pathline[10:]
        
    def Iniciar(self):
        print("Analizador CSS!")
        self.Tokens[:]=[]
        self.errorLex = False
        self.entrada += " \n"   
        self.fila+=2     
        for c in self.entrada: # iteramos en cada caracter
            self.col+=1        
            self.anular = False
            self.repetir = True
            while self.repetir:
                self.repetir = False
                if self.estado == 0:
                    if c.isspace():
                        if c == "\n":
                            self.col = 0
                            self.fila+=1
                        self.lexemaact=c
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ESPACIO",self.lexemaact,"Espacio en blanco")) #este token lo guardo para escribir el archivo de salida
                        self.lexemaact = ""
                    elif c == "{":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_LA",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == "}":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_LC",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == "=":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_IGUAL",self.lexemaact,"Operador"))
                        self.lexemaact = ""
                    elif c == "*":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ASTERISCO",self.lexemaact,"Operador"))
                        self.lexemaact = ""
                    elif c == ":":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_DOSPUNTOS",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == ".":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PUNTO",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""   
                    elif c == ";":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PUNTOYCOMA",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == ",":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_COMA",self.lexemaact,"Simbolo"))
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
                    elif c == "#":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_NUMERAL",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == "%":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PORCENTAJE",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c.isalpha() or c == "_": #letra
                        self.estado = 1
                        self.lexemaact = c
                    elif c.isdigit(): #numero
                        self.estado = 2
                        self.lexemaact = c
                    elif c == "+" or c == "-" : #numero con signo u operadores +/-
                        self.estado = 5
                        self.lexemaact = c
                    elif c == "/": # \ comentarios o simbolo slash
                        self.estado = 6
                        self.lexemaact = c
                    elif c == "\"": # \ cadenas
                        self.estado = 10
                        self.lexemaact = c
                    elif c == "'": # \ cadenas y char
                        self.estado = 11
                        self.lexemaact = c
                    else:
                        self.lexemaact = c
                        self.cErrores+=1
                        self.Errores.append(Error(self.cErrores, self.fila, self.col, self.lexemaact, "Léxico", "Elemento léxico desconocido"))
                        self.lexemaact = ""
                        self.errorLex = True
                elif self.estado == 1:
                    if c.isalpha() or c.isdigit() or c == '_' or c == '-':
                        self.estado = 1
                        self.lexemaact+=c
                    else:
                        self.EncontroID = True
                        if self.lexemaact == "var":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_VAR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "color":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_COLOR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = "" 
                        elif self.lexemaact == "red":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_RED",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "font-size":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FONTSIZE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "background-color":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BKGCOLOR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "gray":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_GRAY",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""   
                        elif self.lexemaact == "text-aling":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_TXTAL",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "center":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CENTER",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "yellow":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_YELLOW",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "margin-top":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MARGINTOP",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "margin-bottom":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MARGIONBOTTOM",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "before":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BEFORE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""                  
                        elif self.lexemaact == "after":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_AFTER",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "em":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_EM",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "position":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_POS",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "hover":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_HOVER",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "purple":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PURPLE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "px":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PX",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "width":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_WIDTH",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "absolute":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ABS",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "body":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BODY",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "border":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BORDER",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "font-wight":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FW",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "padding-left":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PL",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "padding-top":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "line-height":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_LH",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "margin-left":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ML",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "display":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_DISPLAY",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "top":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_TOP",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "float":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FLOAT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "min-width":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MW",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "Opacity":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_OPACITY",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "font-family":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FONTF",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "padding-right":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PADR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "padding":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PADDING",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "width":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_WIDTH",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "margin-right":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MARGINRIGHT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "margin":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MARGIN",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "right":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_RIGHT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "clear":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CLEAR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "max-height":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ME",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "background-image":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BACKIMAG",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "background":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BACK",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "font-style":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FONTSTYLE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "font":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FONT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "padding-bottom":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PADB",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "height":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_HEIGHT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "border-style":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BORDERS",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "bottom":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BOTTOM",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "left":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_LEFT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "max-width":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MAXWIDTH",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "min-height":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MINH",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "relative":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_RELATIVE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "inline-block":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_IB",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "vh":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_VH",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "vw":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_WV",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "in":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_IN",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "cm":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CM",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "mm":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MM",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "pt":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "pc":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PC",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "rgba":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_RGBA",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "url":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_URL",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "content":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CONTENT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "solid":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_SOLID",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "border-top":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "inherit":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_INHERIT",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "rem":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_REM",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        else:
                            self.cTokens+=1
                            self.IDs.append(self.lexemaact)
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
                        self.EncontroNumero = True
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_NUMERO",self.lexemaact,"Valor numérico"))
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
                        self.EncontroNumero = True
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_NUMERO",self.lexemaact,"Valor numérico"))
                        self.lexemaact = ""
                        self.estado = 0
                        self.repetir = True
                elif self.estado == 5: #posibles transiciones para +/- (números con signo u operadores)
                    if c.isdigit():
                        self.estado = 2
                        self.lexemaact +=c
                    else:    
                        if self.lexemaact == "+":
                            self.cTokens+=1
                            self.Operadores.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_SUMA",self.lexemaact,"Operador"))
                            self.lexemaact = ""
                            self.estado = 0
                            self.repetir = True
                        elif self.lexemaact == "-":
                            self.cTokens+=1
                            self.Operadores.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_RESTA",self.lexemaact,"Operador"))
                            self.lexemaact = ""
                            self.estado = 0
                            self.repetir = True
                elif self.estado == 6: #posibles transiciones para '/' (comentarios de linea, multilinea u operador de divison)
                    if c == "*":
                        self.estado = 8
                        self.lexemaact += c
                    else:
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_DIVISION",self.lexemaact,"Operador"))
                        self.lexemaact = ""
                        self.estado = 0
                        self.repetir = True
                elif self.estado == 8:
                    if c != "*":
                        if c == "\n":
                            self.col = 0
                            self.fila+=1
                        self.estado = 8
                        self.lexemaact+=c
                    else:
                        self.estado = 9
                        self.lexemaact += c
                elif self.estado == 9:
                    if c != "/":
                        self.estado = 8
                        self.lexemaact += c
                    else:
                        self.EncontroMultilinea = True
                        self.lexemaact += c
                        self.cTokens+=1
                        self.Comentarios.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_COMENTARIO_MULTILINEA",self.lexemaact,"Comentario"))
                        self.lexemaact = ""
                        self.estado = 0
                elif self.estado == 10:
                    if c != "\"":
                        self.estado = 10
                        self.lexemaact += c
                    else:
                        self.EncontroCadena = True
                        self.lexemaact += c
                        self.cTokens+=1
                        self.Cadenas.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CADENA",self.lexemaact,"Cadena"))
                        self.lexemaact = ""
                        self.estado = 0
                elif self.estado == 11:
                    if c != "'":
                        self.estado = 11
                        self.lexemaact += c
                    else:
                        self.EncontroCadena = True
                        self.lexemaact += c
                        self.cTokens+=1
                        self.Cadenas.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CADENA",self.lexemaact,"Cadena"))
                        self.lexemaact = ""
                        self.estado = 0