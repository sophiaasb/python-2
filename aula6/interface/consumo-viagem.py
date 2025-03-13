import customtkinter as ctk

janela = ctk.CTk('light blue')
janela.geometry('450x600')
janela.resizable(False,False)
janela.title('App Consumo de Viagem')

ctk.CTkLabel(janela,text='App Consumo Viagem',
             font=('Arial',30,'bold'),
             text_color='dark blue').pack(pady=20)

distancia = ctk.CTkEntry(janela,width=400,
                     height=40,
                     placeholder_text='Digite a distância percorrida',
                     font=('arial',20))

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
