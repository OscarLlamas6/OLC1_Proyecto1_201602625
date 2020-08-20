from tkinter.font import Font
import Token
from Token import *
import Error
from Error import *





class LexicoJS:
    def __init__(self, entrada, pathline):
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
        self.Reservadas = []
        self.Cadenas = []
        self.Operadores = []
        self.Comentarios = []
        self.Path = ""
        self.PathLine = pathline[10:]



    def Iniciar(self):
        print("Analizador JavaScript!")
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
                    elif c == "<":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MENOR",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == ">":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MAYOR",self.lexemaact,"Simbolo"))
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
                    elif c == "!":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_NEGACION",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == "&":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_AMPERSAND",self.lexemaact,"Simbolo"))
                        self.lexemaact = ""
                    elif c == "|":
                        self.lexemaact+=c
                        self.cTokens+=1
                        self.Operadores.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PLECA",self.lexemaact,"Simbolo"))
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
                    if c.isalpha() or c.isdigit() or c == '_':
                        self.estado = 1
                        self.lexemaact+=c
                    else:
                        if self.lexemaact == "var":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_VAR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "if":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_IF",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "else":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_ELSE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "for":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FOR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "while":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_WHILE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "do":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_DO",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "continue":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CONTINUE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "return":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_RETURN",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "false":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FALSE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "function":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_FUNCTION",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "constructor":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CONSTRUCTOR",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "class":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CLASS",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "this":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_THIS",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "Math":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_MATH",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "pow":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_POW",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "true":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_TRUE",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "PATHL":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PATHL",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "PATHW":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_PATHW",self.lexemaact,"Palabra reservada"))
                            self.lexemaact = ""
                        elif self.lexemaact == "break":
                            self.cTokens+=1
                            self.Reservadas.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_BREAK",self.lexemaact,"Palabra reservada"))
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
                elif self.estado == 2: #posibles transiciones para el estado 2 (valores numericos)
                    if c.isdigit():
                        self.estado = 2
                        self.lexemaact += c
                    elif c == ".":
                        
                        self.estado = 3
                        self.lexemaact += c
                    else:
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
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_SUMA",self.lexemaact,"Valor numérico"))
                            self.lexemaact = ""
                            self.estado = 0
                            self.repetir = True
                        elif self.lexemaact == "-":
                            self.cTokens+=1
                            self.Operadores.append(self.lexemaact)
                            self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_RESTA",self.lexemaact,"Valor numérico"))
                            self.lexemaact = ""
                            self.estado = 0
                            self.repetir = True
                elif self.estado == 6: #posibles transiciones para '/' (comentarios de linea, multilinea u operador de divison)
                    if c == "/":
                        self.estado = 7
                        self.lexemaact += c
                    elif c == "*":
                        self.estado = 8
                        self.lexemaact += c
                    else:
                        self.cTokens+=1
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_DIVISION",self.lexemaact,"Operador"))
                        self.lexemaact = ""
                        self.estado = 0
                        self.repetir = True
                elif self.estado == 7: 
                    if c != "\n":
                        self.estado = 7
                        self.lexemaact += c
                    else:  
                        self.lexemaact+=c                     
                        self.cTokens+=1
                        self.Comentarios.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_COMENTARIO_UNILINEA",self.lexemaact,"Comentario"))
                        self.col = 0
                        self.fila+=1
                        self.lexemaact = ""
                        self.estado = 0
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
                        self.lexemaact += c
                        self.cTokens+=1
                        self.Cadenas.append(self.lexemaact)
                        self.Tokens.append(Token(self.cTokens, self.fila, self.col,"TK_CADENA",self.lexemaact,"Cadena"))
                        self.lexemaact = ""
                        self.estado = 0
                    
                    
                 
                
                

                    





                


                        

                    

