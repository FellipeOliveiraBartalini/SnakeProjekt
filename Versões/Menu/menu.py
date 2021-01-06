 from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Jogo da Cobrinha 2.0')
root.geometry('600x600')
root.resizable(0, 0)
root.configure(background='green')

#image_logo = ImageTk.PhotoImage(Image.open('snakelogo.jpg'))

def button_click():
    import SnakeV09
    exit()

vazio1 = Label(root, text='                       ', bg='green')
vazio2 = Label(root, text='                                                   ', bg='green')
vazio3 = Label(root, text='', bg='green')
vazio4 = Label(root, text='', bg='green')
vazio5 = Label(root, text='\n \n \n \n \n \n \n \n \n \n \n', bg='green')

button_Start = Button(root, text='Start Game', padx=30, pady=20, bg='snow', fg='black', command= button_click)
button_Exit = Button(root, text='Exit Game', padx=32.5, pady=20, bg='snow', fg='black', command= root.quit)

vazio1.grid(row=0, column=0)
vazio2.grid(row=1, column=1)
vazio3.grid(row=2, column=1)
vazio4.grid(row=3, column=1)
vazio5.grid(row=4, column=1)

#image_logo.grid(row=8, column=2, columnspan=3)

button_Start.grid(row=6, column=2, columnspan=1)
button_Exit.grid(row=7, column=2, columnspan=1)

root.mainloop()
