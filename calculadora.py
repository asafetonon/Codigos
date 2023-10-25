# Importando Tkinter
import tkinter as tk

# Criando uma janela para calculadora e adicionando o título
janela = tk.Tk()
janela.title("Calculadora")

# Criando visor(onde os números e resultado serão exibidos)
visor = tk.Entry(janela, width=20)
visor.grid(row=0, column=0, columnspan=4)

# Criando botões para dígitos, operações e funcionalidades
botoes = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*', 
    'C', '0', '=', '/'
]

# Criando botões à interface
linha = 1
coluna = 0

for botao in botoes:
    tk.Button(janela, text=botao, width=5, command=lambda b=botao: adicionar_ao_visores(b)).grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Função para adicionar números e operadores ao visor
def adicionar_ao_visores(valor):
    if valor == 'C':
        visor.delete(0, tk.END)  # Limpa o visor se o botão 'C' (limpar) for pressionado
    elif valor == '=':
        try:
            expressao = visor.get()
            resultado = str(eval(expressao))
            visor.delete(0, tk.END)
            visor.insert(tk.END, resultado)
        except Exception:
            visor.delete(0, tk.END)
            visor.insert(tk.END, "Erro")
    else:
        visor.insert(tk.END, valor)


janela.mainloop()