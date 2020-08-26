from consArbol import consArbol
from tranTabla import tranTabla
import json
import sigTabla
import hojas


class principal:

    def __init__(self, ER, name):
        self.name = name
        self.ER = ER + "#"
        sigTabla.tabla = []
        hojas.lista = []
        self.ca = consArbol(self.ER)
        self.raiz = self.ca.getRaiz()
        self.raiz.getNodo()
        self.raiz.siguientes()
        print("==============================TABLA SEGUIENTES==============================")
        sigTabla.impTabla()
        self.tran = tranTabla(self.raiz)
        print("=============================TABLA TRANSICIONES=============================")
        self.tran.impTabla()
        self.tran.grafo(self.name)
    #END
#END

'''#ER para ID's -> ..L*||DLG
#ER para numeros -> ....||MmεD*D|..PD*Dε
#ER para cadenas -> ...C*TC
#ER para comentario unilinea -> ....//*TS
#ER para comentario multilinea -> ...../A*TA/
if __name__ == "__main__":
    ER = "...../A*TA/"
    p = principal(ER)'''
