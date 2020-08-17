
from tkinter.font import Font
from tkinter import Tk, Text, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog, mainloop
import pathlib
import LexicoCSS
import LexicoJS
import LexicoHTML
from LexicoJS import *
from LexicoCSS import *
from LexicoHTML import *

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

def Analizar():
    idx = 0
    if myNotebook.select():
        idx = myNotebook.index('current')
    if lenguaje.lower() == ".js":
        a = LexicoJS(mytexts[idx].get("1.0",'end-1c'))
        a.Iniciar()
    elif lenguaje.lower() == ".css":
        a = LexicoCSS(mytexts[idx].get("1.0",'end-1c'))
        a.Iniciar()
    elif lenguaje.lower() == ".html":
        a = LexicoHTML(mytexts[idx].get("1.0",'end-1c'))
        a.Iniciar()  
      

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
    archivo = filedialog.askopenfilename(title = "Abrir Archivo", filetypes = (("JavaScript files","*.js"),("CSS files","*.css"),("HTML files","*.html")))
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



mainloop()
