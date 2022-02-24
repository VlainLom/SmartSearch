from tkinter import *

root = Tk()

def recupere_input():
    Valeur_input = textBox.get("1.0", "end-1c")
    input_search = Valeur_input
    print('>> '+input_search)
    from search import value
    value(input_search)
    from gmaps import Execution
    Execution(input_search)
    from google import Execution1
    Execution1(input_search)

bar = Frame(root, width=100, height=30, bg='yellow')
bar.pack()
textBox = Text(root, height=10, width=75 , bg='yellow', fg='black')
text = Label(bar, text='Recherche',fg='black', font=('Helvatrice',14))
text.place(x=1)
textBox.pack()
button_valider = Button(root, height=1, width=10, text="Valider", command=lambda: recupere_input())
button_valider.pack()

mainloop()

