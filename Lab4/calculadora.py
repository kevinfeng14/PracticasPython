from tkinter import *

ventana = Tk()

#---Pantalla---

numeroPantalla = StringVar()

pantalla=Entry(ventana, textvariable=numeroPantalla)
pantalla.grid(row=0, column=1, padx=5, pady=5, columnspan=3)

#---clic---

def clic(num):
    numeroPantalla.set(numeroPantalla.get() + num)
    

#---numeros---
Button(ventana, text="7", width=5, command=lambda:clic("7")).grid(row=1, column=1)
Button(ventana, text="8", width=5, command=lambda:clic("8")).grid(row=1, column=2)
Button(ventana, text="9", width=5, command=lambda:clic("9")).grid(row=1, column=3)

Button(ventana, text="4", width=5, command=lambda:clic("4")).grid(row=2, column=1)
Button(ventana, text="5", width=5, command=lambda:clic("5")).grid(row=2, column=2)
Button(ventana, text="6", width=5, command=lambda:clic("6")).grid(row=2, column=3)

Button(ventana, text="1", width=5, command=lambda:clic("1")).grid(row=3, column=1)
Button(ventana, text="2", width=5, command=lambda:clic("2")).grid(row=3, column=2)
Button(ventana, text="3", width=5, command=lambda:clic("3")).grid(row=3, column=3)



ventana.mainloop()