from tkinter.font import Font
import Token
from Token import *


class SintacticoRMT:
    def __init__(self, Tokens):
        self.Tokens = Tokens
        self.Error = False         
        self.NumToken = -1
        self.TokenAux = self.SiguienteToken()
        self.S()
        
    #END

    
    def Expresion(self):
        if self.TokenAux is not None:
            if self.TokenAux.token == "TK_MAS":
                self.Parea("TK_MAS")
            elif self.TokenAux.token == "TK_MENOS":
                self.Parea("TK_MENOS")
        self.Termino()
        self.Expresion_Prima()
    #END
    
    def Termino(self):
        self.Factor()
        self.Termino_Prima()
    #END
    
    def Expresion_Prima(self):
        if self.TokenAux is not None:
            if self.TokenAux.token == "TK_MAS":
                self.Parea("TK_MAS")
                self.Termino()
                self.Expresion_Prima()
            elif self.TokenAux.token == "TK_MENOS":
                self.Parea("TK_MENOS")
                self.Termino()
                self.Expresion_Prima()
    #END        
    
    def Termino_Prima(self):
        if self.TokenAux is not None:
            if self.TokenAux.token == "TK_POR":
                self.Parea("TK_POR")
                self.Factor()
                self.Termino_Prima()
            elif self.TokenAux.token == "TK_DIV":
                self.Parea("TK_DIV")
                self.Factor()
                self.Termino_Prima()          
    #END
    
    def Factor(self):
        if self.TokenAux is not None:
            if self.TokenAux.token == "TK_PA":
                self.Parea("TK_PA")
                self.Expresion()
                self.Parea("TK_PC")
            elif self.TokenAux.token == "TK_NUM":
                self.Parea("TK_NUM")
            elif self.TokenAux.token == "TK_ID":
                self.Parea("TK_ID")
            else:
                self.Error = True
        else:
            self.Error = True
    #END
    
    def S(self):
        self.Expresion()
        self.Parea("TK_#")
    
    def Parea(self,terminal):
        if self.TokenAux is not None:
            if self.TokenAux.token == terminal:
                self.TokenAux = self.SiguienteToken()
            else:
                self.Error = True
        else:
            self.Error = True
    #ENS
    
    def SiguienteToken(self):
        if self.NumToken < (len(self.Tokens)-1):
            self.NumToken+=1
            return self.Tokens[self.NumToken]
        else:
            return None