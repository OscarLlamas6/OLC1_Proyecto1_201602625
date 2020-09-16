from tkinter.font import Font
import Token
from Token import *
import Error
from Error import *
import pathlib

class LexicoHTML:
    def __init__(self, entrada, pathline):
        self.entrada = entrada
        self.estado = 0
        self.errorLex = False
        self.repetir = False
        self.anular = False
        self.abrio = False
        self.cerro = False
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
        self.Textos = []
        self.Path = ""
        self.PathLine = "C:" + pathline[9:]
        termina = self.PathLine.endswith('\\')
        if not termina:
            self.PathLine += "\\"
        pathlib.Path(self.PathLine).mkdir(parents=True, exist_ok=True)
    #END    
    
    def Iniciar(self):
        print("Analizador HTML!")
        self.Tokens[:]=[]
        self.errorLex = False
        self.entrada += " \n"   
        self.fila+=3     
        for c in self.entrada: # iteramos en cada caracter           
            self.col+=1        
            self.anular = False
            self.repetir = True
            while self.repetir:
                self.repetir = False
                if self.estado == 0:
                    if c.isspace() or c == '    ':
                        if c == "\n":
                            self.col = 0
                            self.fila+=1
                        self.lexemaact=c
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ESPACIO",self.lexemaact,"Espacio en blanco")) #este token lo guardo para escribir el archivo de salida
                        self.lexemaact = ""
                    elif c == ">":
                        self.lexemaact=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MQ",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                        self.estado = 3
                    elif c == "<":
                        self.lexemaact=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_mQ",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                        self.estado = 0
                    elif c == "/":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_DG",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == "=":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_IG",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c.isalpha(): #letra
                        self.estado = 1
                        self.lexemaact = c
                    elif c == "\"": # Cadenas
                        self.estado = 2
                        self.lexemaact = c
                    else:
                        self.lexemaact = c
                        self.cErrores+=1
                        self.Errores.append(Error(self.cErrores, self.fila, self.col, self.lexemaact, "Léxico", "Elemento léxico desconocido"))
                        self.lexemaact = ""
                        self.errorLex = True
                elif self.estado == 1:
                    if c.isalpha() or c.isdigit():
                        self.estado = 1
                        self.lexemaact+=c   
                    else:
                        if self.lexemaact.lower() == "html":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "head":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "title":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "body":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "h1":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "h2":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "h3":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "h4":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "h5":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "h6":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "p":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "img":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "src":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "a":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "href":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "ul":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "li":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "style":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "table":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "border":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "tr":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "th":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "td":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "caption":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "colgroup":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "col":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "thead":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "tbody":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "tfoot":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "div":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "label":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        if self.lexemaact.lower() == "footer":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_R",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
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
                elif self.estado == 2:
                    if c != "\"":
                        self.estado = 2
                        self.lexemaact += c
                    else:
                        self.lexemaact += c
                        self.cTokens+=1
                        self.Cadenas.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CADENA",self.lexemaact,"Cadena"))
                        self.lexemaact = ""
                        self.estado = 0
                elif self.estado == 3:
                    if c != "<":
                        self.estado = 3
                        self.lexemaact += c
                    else:
                        self.cTokens+=1
                        self.Textos.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_TEXTO",self.lexemaact,"Texto"))
                        self.lexemaact="<"
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_mQ",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                        self.estado = 0
        if self.estado != 0:
            self.cErrores+=1
            self.Errores.append(Error(self.cErrores, self.fila, self.col, self.lexemaact, "Léxico", "Elemento léxico desconocido"))
            self.lexemaact = ""
            self.errorLex = True
            self.estado = 0
            self.repetir = True