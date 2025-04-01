import customtkinter as ctk

# ----- funções -----

def calcular():
    p = int(peso.get())
    a = float(altura.get())
    imc = p/(a*a)

    if(imc<18.5):
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você está magro!',text_color='yellow')
    elif(imc>=18.5 and imc<25):
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você está saudável!',text_color='lightgreen')
    elif(imc>=25 and imc<30):
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você com sobrepeso!',text_color='yellow')
    else:
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você está obeso!',text_color='red')

def limpar():
    resultado.configure(text='')
    nome.delete(0)
    
# -------------------


ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.minsize(600,500)
janela.maxsize(700,550)
janela.title('Aplicativo Saúde')
janela.iconbitmap('medical-08_icon-icons.com_73945.ico')

texto = ctk.CTkLabel(janela,text='Aplicativo Saúde',font=('Arial',30),text_color='yellow')
texto.pack(padx=0, pady=10)

nome = ctk.CTkEntry(janela,placeholder_text='Digite o seu nome',font=('Arial',20),fg_color='white', width=400, height=50,text_color='black')
nome.pack(padx=20, pady=20)

peso = ctk.CTkEntry(janela,placeholder_text='Digite o seu peso',font=('Arial',20),fg_color='white', width=400, height=50,text_color='black')
peso.pack(padx=20, pady=20)

altura = ctk.CTkEntry(janela,placeholder_text='Digite a sua altura',font=('Arial',20),fg_color='white', width=400, height=50,text_color='black')
altura.pack(padx=20, pady=20)

botao =ctk.CTkButton(janela,text='Calcular',fg_color='blue', text_color='white', hover_color='cyan', height=60,command=calcular)
botao.place(x=150,y=350)

botao2 =ctk.CTkButton(janela,text='Limpar',fg_color='darkred', text_color='white', hover_color='red', height=60,command=limpar)
botao2.place(x=300,y=350)

resultado = ctk.CTkLabel(janela,text='',text_color='yellow',font=('verdana',20),)

resultado.place(x=5,y=450)

janela.mainloop()