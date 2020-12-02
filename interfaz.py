from tkinter import *
import php_parserLP as pp
import AnalizadorLexico as ll

window = Tk()
window.resizable(0,0)
window.title("LP | Proyecto")

window.config(width=800,height=600)
window.config(bg="black")
window.config(cursor="")         # Tipo de cursor
window.config(relief="sunken")   # relieve del frame hundido
window.config(bd=25)

lbltitle = Label(window, text="PHP",bg="black", fg='white', font="monospace 32 bold")
lbltitle.place(x=330,y=20)

lblide = Label(window, text="IDE:",bg="black", fg='white', font="monospace 18 bold")
lblide.place(x=65,y=75)

lblconsole = Label(window, text="CONSOLE:",bg="black", fg='white', font="monospace 18 bold")
lblconsole.place(x=420,y=75)

lblc = Text(window, height=22, width=40, wrap="none")

scrollbar = Scrollbar(window,command=lblc.yview,width=14)
scrollbar.place(in_=lblc,relx=1,relheight=1)
lblc.place(x=400,y=120)

T = Text(window, height=22 , width=40)
T.place(x=70,y=120)

def flexico():
   borrarText()
   input = T.get("1.0", "end-1c")
   r = ll.l(input)
   lblc.insert(INSERT,r)

buttonL = Button(window, text = 'A. LÉXICO', highlightbackground='#3E4149', height=1, width=15, command = flexico)

buttonL.place(x=420,y=510)


def fsintactico():
   borrarText()
   input = T.get("1.0", "end-1c")
   resultado = pp.p(input)
   lblc.insert(INSERT,resultado)

buttonS = Button(window, text = 'A. SINTÁCTICO', highlightbackground='#3E4149', height=1, width=15, command = fsintactico)

buttonS.place(x=585,y=510)

def borrarTodo():
   T.delete(1.0, "end")
   lblc.delete("1.0","end")

buttonT = Button(window, text='CLEAR TEXT', highlightbackground='#3E4149', height=1, width=35, command=borrarTodo)
buttonT.place(x=90, y=510)

def borrarText():
   lblc.delete("1.0","end")

window.mainloop()
