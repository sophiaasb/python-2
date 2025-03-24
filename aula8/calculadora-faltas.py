import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('600x450')
janela.resizable(False, False)
janela.title('Calculadora de porcentagem de Faltas')
janela.iconbitmap('calculator_icon-icons.com_72046.ico')

titulo = ctk.CTkLabel(janela, text='Calculadora de Faltas',
                      font=('Arial', 30, 'bold'),
                      text_color=('white'))

titulo.pack(pady=10)

carga_horaria = ctk.CTkEntry(janela, width=400,
                             height=40,
                             placeholder_text='Digite a carga horária da matéria (em horas)',
                             font=('Arial', 20))

carga_horaria.place(x=100, y=110)

faltas_horas = ctk.CTkEntry(janela, width=400,
                            height=40,
                            placeholder_text='Digite a quantidade de faltas (em horas)',
                            font=('Arial', 20))

faltas_horas.place(x=100, y=180)

horas_por_dia = 4

def calcular():
    try:
        carga = float(carga_horaria.get())
        faltas = float(faltas_horas.get())
        
        faltas_permitidas = carga * 0.25
        
        if faltas > faltas_permitidas:
            messagebox.showinfo("Resultado", "Reprovado devido a faltas superiores a 25% da carga horária.")
        else:
            faltas_restantes = faltas_permitidas - faltas
            porcentagem_restante = (faltas_restantes / carga) * 100
            dias_restantes = faltas_restantes / horas_por_dia

            messagebox.showinfo("Resultado", 
                f"{dias_restantes:.2f} dias. pode faltar {porcentagem_restante:.2f}% da carga horária total.\n")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

botao = ctk.CTkButton(janela, width=150,
                      height=40, fg_color='blue',
                      text_color='white',
                      text='Calcular', font=('Arial', 18, 'bold'),
                      hover_color='red', command=calcular)

botao.pack(pady=180)

janela.mainloop()