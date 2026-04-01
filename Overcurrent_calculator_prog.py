import tkinter as tk
from tkinter import ttk, messagebox
from Funções.functions import verifica_curva, float_valor, float_corrente_teste, calcula_tempo  # noqa: F403

def calcular():

    curva = curva_input.get()
    pickup = pickup_input.get()
    dial = dial_input.get()
    corrente = corrente_input.get()
    
    if verifica_curva(curva) is None:  # noqa: F405
    
        messagebox.showerror('Erro de parâmetro', 'Selecione um tipo de curva')
    
    elif float_valor(pickup) is None:  # noqa: F405

        messagebox.showerror('Erro de parâmetro', 'Valor de pickup inválido - Entre com um número maior que zero')
    
    elif float_valor(dial) is None:  # noqa: F405

        messagebox.showerror('Erro de parâmetro', 'Dial de tempo inválido - Entre com um número maior que zero')

    elif float_corrente_teste(corrente, float_valor(pickup)) is None:

        messagebox.showerror('Erro de parâmetro', f'Corrente de falta inválida - Entre com um valor maior que {float_valor(pickup)}')
    
    else:

        float_pickup = float_valor(pickup)
        float_dial = float_valor(dial)
        float_corrente = float_corrente_teste(corrente, float_pickup)
        tempo_de_atuação = calcula_tempo(curva, float_pickup, float_dial, float_corrente)

        result_label.config(text=f"Tempo de atuação: {tempo_de_atuação:.3f} s") 
        
tela = tk.Tk()
tela.title('Cálculo da função 51')
tela.geometry("300x380")
tela.configure(bg="#f2f2f5")

fonte=("Segoe UI", 10, "bold")

curvas = ["Normal inverse","Very Inverse","Extremely inverse",
"Long Time inverse",
"Short-Time Inverse"]


# Seleção do tipo da curva
tk.Label(tela, text = 'Tipo da curva', font = fonte).pack()
curva_input = ttk.Combobox(tela, values= curvas)
curva_input.pack(pady = 10)

# Solicita o valor do pickup da função
tk.Label(tela,text= 'Pickup - [A] secundário', font = fonte).pack()
pickup_input = tk.Entry(tela, justify= 'center')
pickup_input.pack(pady = 10)

# Solicita o valor do dial de tempo da curva
tk.Label(tela,text= 'Dial de tempo da curva', font = fonte).pack()
dial_input = tk.Entry(tela,justify='center')
dial_input.pack(pady = 10)

# Solicita o valor da corrente de teste
tk.Label(tela,text= 'Corrente de falta - [A] secundário', font = fonte, pady = 10).pack()
corrente_input = tk.Entry(tela,justify='center')
corrente_input.pack(pady = 10)

#Botão para executar o cálculo

click = tk.Button(tela, text='Calcular tempo de atuação', font = fonte, command = calcular,)
click.pack(pady = 10)


result_label = tk.Label(tela, text="", fg="blue", font = fonte)
result_label.pack(pady=10)

tela.mainloop()
