import os

DOTid = '''digraph D {
  rankdir=LR
  A [shape=circle, label="So"]
  B [shape=doublecircle, label="S1"]
  A->B[label="LETRA"] 
  B->B[label="LETRA|DIGITO|_"]
}'''

DOTcadena = '''digraph D {
  rankdir=LR
  A [shape=circle, label=S0]
  B [shape=circle, label=S1]
  C [shape=doublecircle, label=S2]
  A->B[label="\\""]
  B->B[label="[^\\"]"]
  B->C[label="\\""]
 }
'''

DOTcomentarioml = '''digraph D {
  rankdir=LR
  A [shape=circle, label=S0]
  B [shape=circle, label=S1]
  C [shape=circle, label=S2]
  D [shape=circle, label=S3]
  E [shape=doublecircle, label=S4]
  A->B[label="/"]
  B->C[label="*"]
  C->C[label="[^*]"]
  C->D[label="*"]
  D->C[label="[^/]"]
  D->E[label="/"]
}'''

DOTnumero = '''digraph D {
  rankdir=LR
  A [shape=circle, label=S0]
  B [shape=doublecircle, label=S1]
  C [shape=circle, label=S2]
  D [shape=circle, label=S3]
  E [shape=doublecircle, label=S4]  
  A->B[label=DIGITO]
  A->C[label="+|-"]
  B->B[label=DIGITO]
  C->B[label=DIGITO]
  B->D[label=PUNTO]
  D->E[label=DIGITO]
  E->E[label=DIGITO]  
}'''

def AutomataID():  
    f = open('C:\\Salida\\CodigoID.dot','w')
    f.write(DOTid)
    f.close()
    os.system('dot {} -Tpng -o {}'.format('C:\\Salida\\CodigoID.dot','C:\\Salida\\ID.png'))
    os.startfile('C:\\Salida\\ID.png','open')
#END

def AutomataCadena():  
    f = open('C:\\Salida\\CodigoCadena.dot','w')
    f.write(DOTcadena)
    f.close()
    os.system('dot {} -Tpng -o {}'.format('C:\\Salida\\CodigoCadena.dot','C:\\Salida\\Cadena.png'))
    os.startfile('C:\\Salida\\Cadena.png','open')
#END

def AutomataComentarioml():  
    f = open('C:\\Salida\\CodigoComentml.dot','w')
    f.write(DOTcomentarioml)
    f.close()
    os.system('dot {} -Tpng -o {}'.format('C:\\Salida\\CodigoComentml.dot','C:\\Salida\\Comentml.png'))
    os.startfile('C:\\Salida\\Comentml.png','open')
#END

def AutomataNumero():  
    f = open('C:\\Salida\\CodigoNum.dot','w')
    f.write(DOTnumero)
    f.close()
    os.system('dot {} -Tpng -o {}'.format('C:\\Salida\\CodigoNum.dot','C:\\Salida\\Num.png'))
    os.startfile('C:\\Salida\\Num.png','open')
#END