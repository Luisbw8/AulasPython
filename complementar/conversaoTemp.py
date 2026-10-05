import tkinter as tk
from tkinter import simpledialog

def calcular_conversao():
    temp = simpledialog.askfloat("Valor Temp.","Insira a Temperatura")
    
    F=(temp*9/5) +32   
    label_resultado.config(text=f"Valor da conversão {F}")

janela = tk.Tk()
janela.title("Conversão")

button = tk.Button(janela, text="Converter", command=calcular_conversao)
button.pack(pady=20)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(padx=20, pady=20)

janela.mainloop()