import tkinter as tk

def clicar(numero):
    entrada.insert(tk.END, str(numero))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 14), command=calcular).grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 14), command=lambda t=texto: clicar(t)).grid(row=linha, column=coluna, padx=5, pady=5)

tk.Button(janela, text="LIMPAR", width=22, height=2, font=("Arial", 14), command=limpar).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

janela.mainloop()
