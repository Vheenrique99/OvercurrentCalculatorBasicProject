import tkinter as tk
from tkinter import ttk, messagebox
from functions import verifica_curva, float_valor, float_corrente_teste, calcula_tempo 

def calcular():

    modelo_curva = modelo_curva_input.get()
    curva = curva_input.get()
    pickup = pickup_input.get()
    dial = dial_input.get()
    corrente = corrente_input.get()
    
    if verifica_curva(modelo_curva) is None:

        messagebox.showerror('Erro de parâmetro', 'Selecione o modelo para as curvas')
    
    elif verifica_curva(curva) is None:  
    
        messagebox.showerror('Erro de parâmetro', 'Selecione um tipo de curva')

    elif float_valor(pickup) is None:  

        messagebox.showerror('Erro de parâmetro', 'Valor de pickup inválido - Entre com um número maior que zero')
    
    elif float_valor(dial) is None:  

        messagebox.showerror('Erro de parâmetro', 'Dial de tempo inválido - Entre com um número maior que zero')

    elif float_corrente_teste(corrente, float_valor(pickup)) is None:

        messagebox.showerror('Erro de parâmetro', f'Corrente de falta inválida - Entre com um valor maior que {float_valor(pickup)*1.1}')
    
    else:

        float_pickup = float_valor(pickup)
        float_dial = float_valor(dial)
        float_corrente = float_corrente_teste(corrente, float_pickup)
        tempo_de_atuação = calcula_tempo(curva, float_pickup, float_dial, float_corrente, modelo_curva)

        result_label.config(text=f"Tempo de atuação: {tempo_de_atuação:.3f} s") 
        
tela = tk.Tk()
tela.title('Cálculo da função 51')
tela.geometry("300x480")
tela.configure(bg="#f2f2f5")

fonte=("Segoe UI", 10, "bold")

modelos_curvas = ["IEC", "ANSI/IEE", "US type"]

curvas_IEC = ["Normal inverse","Very Inverse","Extremely inverse",
            "Long Time inverse", "Short-Time Inverse"]

curvas_ANSI_IEE = ['Inverse', 'Short Inverse','Long Inverse', 'Moderately Inverse', 'Very Inverse',
                   'Extremely Inverse', 'Definite Inverse']

curvas_US_type = ['US Moderately Inverse','US Inverse', 'US Very inverse','US Extremely Inverse','US Short-Time Inverse']


def selecao_modelo_curva(event):

    modelo_selecionado = modelo_curva_input.get()

    if modelo_selecionado == "IEC":
    
        curva_input["values"] = curvas_IEC
        curva_input.set("")
    
    elif modelo_selecionado == "ANSI/IEE":

        curva_input["values"] = curvas_ANSI_IEE
        curva_input.set("")
    
    elif modelo_selecionado == "US type":
        
        curva_input["values"] = curvas_US_type
        curva_input.set("")


# Seleção da característica das curvas
tk.Label(tela, text = 'Selecione o modelo das curvas', font = fonte).pack()
modelo_curva_input = ttk.Combobox(tela, values= modelos_curvas, state = 'readonly')
modelo_curva_input.pack(pady = 10)
modelo_curva_input.bind("<<ComboboxSelected>>", selecao_modelo_curva)

# Seleção do tipo da curva
tk.Label(tela, text = 'Tipo da curva', font = fonte).pack()
curva_input = ttk.Combobox(tela, state = 'readonly')
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
