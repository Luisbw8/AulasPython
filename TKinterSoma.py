import tkinter as tk
from tkinter import simpledialog

def calcular_soma():
    num1 = simpledialog.askinteger("Primeiro Número", "Digite o primeiro número inteiro:")
    
    num2 = simpledialog.askinteger("Segundo Número", "Digite o segundo número inteiro:")
    
    soma = num1 + num2
    
    # Exibe o resultado formatado na janela principal
    label_resultado.config(text=f"A soma de {num1} e {num2} é {soma}.")

# Configuração da janela principal
root = tk.Tk()
root.title("Soma de Inteiros")

# Botão para iniciar o processo
botao_iniciar = tk.Button(root, text="Somar Dois Números", command=calcular_soma)
botao_iniciar.pack(pady=30)

# Label que exibirá o resultado da soma
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=20)

root.mainloop()
