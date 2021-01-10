from tkinter import *
from PIL import ImageTk, Image
import os

 
ventana=Tk()
ventana.geometry("700x700")
ventana.title ("Ejemplo IMAGEN") # lo que sale arriba de la ventanita
ventana.resizable(0,0)
ventana.config(bg="pink")
    # creamos imagen

dir_path = os.path.dirname(os.path.realpath(__file__))
imagen = ImageTk.PhotoImage(Image.open(str(dir_path)+"/Homero.jpg"))
img = Label(ventana,image=imagen)
img.place(x=0, y=0)


ventana.mainloop()