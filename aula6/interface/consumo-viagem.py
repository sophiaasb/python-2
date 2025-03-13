import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')

janela = ctk.CTk('dark blue')
janela.geometry('600x450')
janela.resizable(False,False)
janela.title('App Consumo de Viagem')
janela.iconbitmap('ic_local_gas_station_128_28461.ico')

ctk.CTkLabel(janela, text='App Consumo Viagem',
             font=('Arial',30,'bold'),
             text_color=('white').pack(pady=10))

ctk.CTkLabel(janela, text='03/2025 - SENAI Bahia',
             font=('Arial',30,'bold'),
             text_color=('white').pack(pady=10))

distancia = ctk.CTkEntry(janela, width=400,
                     height=40,
                     placeholder_text='Digite a distância percorrida',
                     font=('arial',20)
                     ).place(x=300,y=255)

litros = ctk.CTkEntry(janela,width=400,
                     height=40,
                     placeholder_text='Digite o consumo em litros',
                     font=('arial',20))

preco = ctk.CTkEntry(janela,width=400,
                     height=40,
                     placeholder_text='Digite o preço',
                     font=('arial',20))

botao = ctk.CTkButton(janela,width=150,
                      height=40, fg_color='purple',
                      text_color='white',
                      text='Calcular o valor',font=('arial',18,'bold'),
                      hover_color='cyan')

distancia.pack(pady=5)
litros.pack(pady=5)
preco.pack(pady=5)
botao.pack(pady=3)

janela.mainloop()
