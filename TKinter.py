import tkinter as tk
import php_parserLP as pp
import AnalizadorLexico as ll
window = tk.Tk()
window.title("LP | Proyecto")
window.geometry('800x600')
window.configure(bg='black')

lbltitle = tk.Label(window, text="PHP",bg="black", fg='white', font="monospace 32 bold")
lbltitle.place(x=365,y=20)

lblide = tk.Label(window, text="IDE:",bg="black", fg='white', font="monospace 18 bold")
lblide.place(x=65,y=70)

lblconsole = tk.Label(window, text="CONSOLE:",bg="black", fg='white', font="monospace 18 bold")
lblconsole.place(x=420,y=70)

lblc = tk.Label(window, text="" ,bg="#332f2c", fg='#149414', font="monospace 18", height=19, width=28)
lblc.place(x=420,y=100)

T = tk.Text(window, height=30 , width=43)
T.place(x=65,y=100)