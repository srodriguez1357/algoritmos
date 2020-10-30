from tkinter import *

def sumar():
    resul.set(float(operando1.get())+ float(operando2.get()))
    borrar()
def restar():
    resul.set(float(operando1.get())- float(operando2.get()))
    borrar()
def multiplicar():
    resul.set(float(operando1.get())* float(operando2.get()))
    borrar()
def borrar():
    operando1.set('')
    operando2.set('')


raiz = Tk()
raiz.title("Calculadora")
operando1=StringVar()
operando2=StringVar()
resul=StringVar()

miFrame = Frame(raiz, width = 700, height = 400)
miFrame.pack()

operador1 = Label(miFrame, text="Operador1")
operador1.grid(row=0, column=0, padx=0, pady=10)

operador2 = Label(miFrame, text="Operador2")
operador2.grid(row=1, column=0, padx=0, pady=10)

resultado = Label(miFrame, text="Resultado")
resultado.grid(row=2, column=0,  padx=0, pady=10)

cuadrooperador1 = Entry(miFrame, textvariable=operando1)
cuadrooperador1.grid(row=0, column=1, padx=10, pady=10)

cuadrooperador2 = Entry(miFrame, textvariable=operando2)
cuadrooperador2.grid(row=1, column=1, padx=10, pady=10)

cuadroresultado = Entry(miFrame, state="disabled", textvariable=resul)
cuadroresultado.grid(row=2, column=1, padx=10, pady=10)

suma = Button(miFrame, text="Suma", command=sumar)
suma.grid(row=0, column=2, padx=10, pady=10)

resta = Button(miFrame, text="Resta", command=restar)
resta.grid(row=1, column=2, padx=10, pady=10)

multiplicar = Button(miFrame, text="Multiplica", command=multiplicar)
multiplicar.grid(row=2, column=2, padx=10, pady=10)

raiz.mainloop()