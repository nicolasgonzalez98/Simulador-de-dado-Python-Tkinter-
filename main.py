##Librerias
import random as rn
import tkinter as tk
from PIL import Image, ImageTk
##Inicio
root = tk.Tk()
root.geometry('400x400')
root.title('Gira el dado!')
##Linea negra
BlankLine = tk.Label(root, text="")
BlankLine.pack()

##Header
headerLabel = tk.Label(root,text='Bienvenidos al Proyecto de Nicolas',bg = 'Gray',fg='Brown',font = "Helvetica 16 bold italic")
headerLabel.pack()

##Imagenes
dado = ['dado1.png', 'dado2.png', 'dado3.png', 
    'dado4.png', 'dado5.png', 'dado6.png']
#simulando el numero de imagen
DadoImagen = ImageTk.PhotoImage(Image.open(rn.choice(dado)))
# construir label para la imagen
ImageLabel = tk.Label(root, image=DadoImagen)
ImageLabel.image = DadoImagen
# ubicar imagen con pack 
ImageLabel.pack(expand=True)
##Funciones

def girar_dado(event=None):
    #simulando el numero de imagen
    DadoImagen = ImageTk.PhotoImage(Image.open(rn.choice(dado)))
    # construir label para la imagen
    ImageLabel.configure(image=DadoImagen)
    ImageLabel.image = DadoImagen
    
##Insertar boton
boton_girar = tk.Button(root,text='Girar dado!',command=girar_dado)
boton_girar.pack(expand=True)

##Eventos
root.bind('<Return>', girar_dado)

root.mainloop()
