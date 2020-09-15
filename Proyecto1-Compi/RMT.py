from tkinter.font import Font


class RMT:
    def __init__(self, entrada):
        self.entrada = entrada
        self.error = False
        cadena = [x for x in self.entrada if x in "()"]
        if len(cadena) % 2 != 0 or len(cadena) == 0:
            self.error = True
        else:
            self.errorx = False
            i = 0
            while 0 < len(cadena) and self.error == False:
                if cadena[i] in "(":
                    i += 1
                else:
                    if cadena[i - 1] + cadena[i] in '()':
                        cadena = cadena[:i - 1] + cadena[i + 1:]
                        i -= 1
                    else:
                        self.error = True
