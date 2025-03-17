import customtkinter as ctk

janela = ctk.CTk('hot pink')
janela.geometry('500x300')
janela.resizable(False,False)
janela.title('Sistema de Acesso 2025')

ctk.CTkLabel(janela,text='Sistema de Acesso',
             font=('Arial',50,'bold'),
             text_color='dark blue').pack(pady=20)

login = ctk.CTkEntry(janela,width=400,
                     height=40,
                     placeholder_text='Digite o seu login',
                     font=('arial',20))

senha = ctk.CTkEntry(janela,width=400,
                     height=40,
                     placeholder_text='Digite a sua senha',
                     font=('arial',20),
                     show=('********'))
botao = ctk.CTkButton(janela,width=150,
                      height=40, fg_color='purple',
                      text_color='white',
                      text='Acessar',font=('arial',18,'bold'),
                      hover_color='cyan')

login.pack()
senha.pack(pady=10)
botao.pack(pady=10)

janela.mainloop()