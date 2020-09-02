
from tkinter.font import Font
from tkinter import Tk, Text, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog, mainloop
import pathlib
import LexicoCSS
import LexicoJS
import LexicoHTML
import LexicoRMT
import Reportes
import os
from LexicoJS import *
from LexicoCSS import *
from LexicoHTML import *
from LexicoRMT import *
from Reportes import *

raiz=Tk()
raiz.title("Compiladores 1")
raiz.resizable(0,0)
raiz.geometry("1000x900")
raiz.config(bg="blue4")
myFont = Font(family="Arial", size=18, weight="bold")
myFont2 = Font(family="Arial", size=12)
myframes = []
mytexts = []
myscrolls = []
s = ttk.Style()
s.configure('TNotebook.Tab', font=myFont2)
archivo = ""
lenguaje = ""



def GenerarSalida(Tokens, path):
    global archivo
    name = os.path.basename(archivo)
    path+=name
    f= open(path,"w+")
    for t in Tokens:
        f.write(t.lexema)
    f.close()

def GenerarPDFErrores(Errores):
    f= open("C:\\Salida\\Errores.html","w+")
    f.write("""<!DOCTYPE html>
    <html>
    <body>
    <h1>REPORTE DE ERRORES</h1>

    <table style="width:100%" border=1>
    <tr>
        <th>No.</th>
        <th>Fila</th> 
        <th>Columna</th>
        <th>Descripción</th>
    </tr>""")
    for e in Errores:
        f.write(""" <tr>
    <th>{}</th>
    <th>{}</th> 
    <th>{}</th>
    <th>El caracter '{}' no pertence al lenguaje</th>
    </tr>""".format(e.numero,e.fila,e.columna,e.error))
    f.write("""</table>
    
    </body>
    </html>
    """)      
    f.close()
    os.startfile("C:\\Salida\\Errores.html",'open')

def PintarIDs(ids):
    idt = 0
    if myNotebook.select():
        idt = myNotebook.index('current')
    mytexts[idt].tag_remove('found4', '1.0', END)
    for word in ids:
        idx = '1.0'
        while idx:
            idx = mytexts[idt].search(word, idx, nocase=1, stopindex=END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                mytexts[idt].tag_add('found4', idx, lastidx)
                idx = lastidx

    mytexts[idt].tag_config('found4', foreground='black')

def PintarReservadas(reservadas):
    idt = 0
    if myNotebook.select():
        idt = myNotebook.index('current')
    mytexts[idt].tag_remove('found1', '1.0', END)
    for word in reservadas:
        idx = '1.0'
        while idx:
            idx = mytexts[idt].search(word, idx, nocase=1, stopindex=END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                mytexts[idt].tag_add('found1', idx, lastidx)
                idx = lastidx

    mytexts[idt].tag_config('found1', foreground='red')

def PintarCadenas(cadenas):
    idt = 0
    if myNotebook.select():
        idt = myNotebook.index('current')
    mytexts[idt].tag_remove('found', '1.0', END)
    for word in cadenas:
        idx = '1.0'
        while idx:
            idx = mytexts[idt].search(word, idx, nocase=1, stopindex=END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                mytexts[idt].tag_add('found', idx, lastidx)
                idx = lastidx

    mytexts[idt].tag_config('found', foreground='yellow')

def PintarComentarios(comentarios):
    idt = 0
    if myNotebook.select():
        idt = myNotebook.index('current')
    mytexts[idt].tag_remove('found2', '1.0', END)
    for word in comentarios:
        idx = '1.0'
        while idx:
            idx = mytexts[idt].search(word, idx, nocase=1, stopindex=END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                mytexts[idt].tag_add('found2', idx, lastidx)
                idx = lastidx

    mytexts[idt].tag_config('found2', foreground='gray40')

def PintarOperadores(Operadores):
    idt = 0
    if myNotebook.select():
        idt = myNotebook.index('current')
    mytexts[idt].tag_remove('found3', '1.0', END)
    for word in Operadores:
        idx = '1.0'
        while idx:
            idx = mytexts[idt].search(word, idx, nocase=1, stopindex=END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                mytexts[idt].tag_add('found3', idx, lastidx)
                idx = lastidx

    mytexts[idt].tag_config('found3', foreground='orange')

def Analizar():
    idx = 0
    if myNotebook.select():
        idx = myNotebook.index('current')
    if lenguaje.lower() == ".js":
        textoConsola.config(state="normal")
        textoConsola.delete(1.0, END)
        textoConsola.config(state="disabled")
        a = LexicoJS(mytexts[idx].get("1.0",'end-1c'))
        a.Iniciar()
        GenerarSalida(a.Tokens, a.PathLine)
        PintarReservadas(a.Reservadas)
        PintarCadenas(a.Cadenas)
        PintarOperadores(a.Operadores)
        PintarComentarios(a.Comentarios)
        
        if a.errorLex:
            print("Error lexico encontrado")   
            GenerarPDFErrores(a.Errores)  
            #generarpdf de errores   
        else:
            print("Analisis lexico exitoso")       
            if a.EncontroID:
                Reportes.AutomataID()
            if a.EncontroCadena:
                Reportes.AutomataCadena()
            if a.EncontroMultilinea:
                Reportes.AutomataComentarioml()
            if a.EncontroNumero:
                Reportes.AutomataNumero()
            #generar arbol

    elif lenguaje.lower() == ".css":
        textoConsola.config(state="normal")
        textoConsola.delete(1.0, END)
        textoConsola.config(state="disabled")
        a = LexicoCSS(mytexts[idx].get("1.0",'end-1c'))
        a.Iniciar()
        GenerarSalida(a.Tokens, a.PathLine)
        PintarReservadas(a.Reservadas)
        PintarCadenas(a.Cadenas)
        PintarComentarios(a.Comentarios)
        PintarOperadores(a.Operadores)
        PintarIDs(a.IDs)
        if a.errorLex:
            print("Error lexico encontrado")   
            GenerarPDFErrores(a.Errores)
            for er in a.Errores:
                textoConsola.config(state="normal")
                textoConsola.insert(INSERT, "{}. Fila = {}   Col. = {}   Error = \'{}\' no pertenece al lenguaje.\n".format(er.numero, er.fila, er.columna, er.error))
                textoConsola.config(state="disabled")
            #generarpdf de errores   
        else:
            textoConsola.config(state="normal")
            textoConsola.insert(INSERT, "Analisis léxico exitoso!\n\n")
            textoConsola.config(state="disabled")
            if a.EncontroID:
                textoConsola.config(state="normal")
                textoConsola.insert(INSERT, "ID: Estado 0 -> Estado 1 (Estado Aceptación)\n")
                textoConsola.config(state="disabled") 
            if a.EncontroCadena:
                textoConsola.config(state="normal")
                textoConsola.insert(INSERT, "Cadena: Estado 0 -> Estado 10 (Estado Aceptación)\n")
                textoConsola.config(state="disabled")                 
            if a.EncontroMultilinea:
                textoConsola.config(state="normal")
                textoConsola.insert(INSERT, "Multilinea: Estado 0 -> Estado 6 -> Estado 8 - Estado 9(Estado Aceptación)\n")
                textoConsola.config(state="disabled")                  
            if a.EncontroNumero:
                textoConsola.config(state="normal")
                textoConsola.insert(INSERT, "Número: Estado 0 -> Estado 2 (Estado Aceptación)\n")
                textoConsola.config(state="disabled")
            textoConsola.config(state="normal")
            textoConsola.insert(INSERT, "\n")
            textoConsola.config(state="disabled")
            for tk in a.Tokens:
                if tk.token != "TK_ESPACIO":
                    textoConsola.config(state="normal")
                    textoConsola.insert(INSERT, "{}. Fila = {}   Col. = {}   Lexema = {}   Tipo = {}\n".format(tk.numero, tk.fila, tk.columna, tk.lexema, tk.tipo))
                    textoConsola.config(state="disabled")                                 
    elif lenguaje.lower() == ".html":
        a = LexicoHTML(mytexts[idx].get("0.0",'end-1c'))
        a.Iniciar()
    elif lenguaje.lower() == ".rmt":
        textoConsola.config(state="normal")
        textoConsola.delete(1.0, END)
        textoConsola.config(state="disabled")
        a = LexicoRMT(mytexts[idx].get("0.0",'end-1c'))
        a.Iniciar()    
        if a.errorLex:
            textoConsola.config(state="normal")
            textoConsola.insert(INSERT, "ERROR LEXICO ENCONTRADO\n")
            textoConsola.config(state="disabled")  
        else:
            textoConsola.config(state="normal")
            textoConsola.insert(INSERT, "ANALISIS LEXICO EXITOSO\n")
            textoConsola.config(state="disabled")  
          
    
      
def Limpiar():
    if myNotebook.select():
        idx = myNotebook.index('current')
        mytexts[idx].delete(1.0, END)

def nuevo():
    global archivo
    idx = 0
    if myNotebook.select():
        idx = myNotebook.index('current')
    if archivo !="":
        confirmar = messagebox.askyesnocancel("Nuevo", "Desea guardar los cambios?")
        if confirmar is True:
            guardarc = open(archivo, "w", encoding="utf-8")
            guardarc.write(mytexts[idx].get(1.0, END))
            guardarc.close()
            mytexts[idx].delete(1.0, END)
            archivo = ""
        elif confirmar is False:
            mytexts[idx].delete(1.0, END)
            archivo = ""
        elif confirmar is None:
            return
    else:
        if mytexts[idx].compare("end-1c", "==", "1.0"):
            mytexts[idx].delete(1.0, END)
            archivo = ""
        else: 
            confirmar = messagebox.askyesnocancel("Nuevo", "Desea guardar los cambios?")
            if confirmar is True:
                guardarComo()
                mytexts[idx].delete(1.0, END)
                archivo = ""
            elif confirmar is False:
                mytexts[idx].delete(1.0, END)
                archivo = ""
            elif confirmar is None:
                return    

def abrir():
    global archivo
    global lenguaje
    idx = 0
    if myNotebook.select():
        idx = myNotebook.index('current')
    archivo = filedialog.askopenfilename(title = "Abrir Archivo", filetypes = (("JavaScript files","*.js"),("CSS files","*.css"),("HTML files","*.html"),("RMT files","*.rmt")))
    if archivo != '':
        lenguaje = pathlib.Path(archivo).suffix
        entrada = open(archivo, encoding="utf-8")
        content = entrada.read()
        mytexts[idx].delete(1.0, END)
        mytexts[idx].insert(INSERT, content)
        entrada.close()

def salir():
    confirmar = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if confirmar :
        raiz.destroy()

def guardarArchivo():
    global archivo
    idx = 0
    if myNotebook.select():
        idx = myNotebook.index('current')
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w", encoding="utf-8")
        guardarc.write(mytexts[idx].get(1.0, END))
        guardarc.close()

def guardarComo():
    global archivo
    idx = 0
    if myNotebook.select():
        idx = myNotebook.index('current')
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", filetypes = (("JavaScript files","*.js"),("CSS files","*.css"),("HTML files","*.html")))
    if guardar != '':
        fguardar = open(guardar, "w+", encoding="utf-8")
        fguardar.write(mytexts[idx].get(1.0, END))
        fguardar.close()
        archivo = guardar

def AcercaDe():
    messagebox.showinfo(title="Proyecto 1: OLC1", message="Autor: Oscar Alfredo Llamas Lemus\nCarnet: 201602625\nCurso: Compiladores 1 Secc. A")

barraMenu= Menu(raiz)
raiz.config(menu= barraMenu)
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo", command = nuevo)
archivoMenu.add_command(label="Abrir", command = abrir)
archivoMenu.add_command(label="Guardar", command = guardarArchivo)
archivoMenu.add_command(label="Guardar Como...", command = guardarComo)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command = salir)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

archivoMenu2 = Menu(barraMenu, tearoff=0)
archivoMenu2.add_command(label="Analizar entrada", command = Analizar)
archivoMenu2.add_command(label="Limpiar pantalla", command = Limpiar)
barraMenu.add_cascade(label="Acción", menu=archivoMenu2)

archivoMenu3 = Menu(barraMenu, tearoff=0)
archivoMenu3.add_command(label="Acerca de...", command = AcercaDe)
barraMenu.add_cascade(label="Ayuda", menu=archivoMenu3)


myNotebook = ttk.Notebook(raiz)
myNotebook.pack()


for i in range(4):
    valor = i+1
    tabTitle="Lenguaje "+str(valor)
    if i==0:
        myframes.append(Frame(myNotebook, width=1000, height=650, bg="red4"))
    elif i==1:
        myframes.append(Frame(myNotebook, width=1000, height=650, bg="navy"))
    elif i==2:
        myframes.append(Frame(myNotebook, width=1000, height=650, bg="purple4"))
    elif i==3:
        myframes.append(Frame(myNotebook, width=1000, height=650, bg="goldenrod3"))
    myframes[i].pack(fill="x", expand=1)  
    myNotebook.add(myframes[i], text=tabTitle)
    mytexts.append(Text(myframes[i], width=75, height=20))
    mytexts[i].config(fg="black", font=myFont, bg="navajo white")
    mytexts[i].place(x=5,y=35)
    myscrolls.append(Scrollbar(myframes[i], command=mytexts[i].yview))
    myscrolls[i].pack(side=RIGHT, fill=Y)
    myscrolls[i].place(in_=mytexts[i], relx=1, rely=0, relheight=1, anchor='ne', border="outside")
    mytexts[i].configure(yscrollcommand=myscrolls[i].set)

    frameConsola = Frame(raiz, width=985, height=200, bg='blue')
    frameConsola.place(x=5,y=690)
    textoConsola = Text(frameConsola,width=76, height=7)
    textoConsola.config(fg="OliveDrab1", font=myFont, bg="black", state="disabled")
    textoConsola.pack()
    scrollConsola = Scrollbar(frameConsola, command=textoConsola.yview)
    scrollConsola.pack(side=RIGHT, fill=Y)
    scrollConsola.place(in_=textoConsola, relx=1, rely=0, relheight=1, anchor='ne', border="outside")
    textoConsola.configure(yscrollcommand=scrollConsola.set)

mainloop()
