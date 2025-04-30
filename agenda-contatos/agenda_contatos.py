import tkinter as tk
from tkinter import messagebox

arquivo_contatos = "contatos.txt"

def carregar_contatos():
    contatos = []
    try:
        with open(arquivo_contatos, "r", encoding="utf-8") as arquivo:
            for linha in arquivo.readlines():
                contatos.append(linha.strip())
    except FileNotFoundError:
        open(arquivo_contatos, "w", encoding="utf-8").close()
    return contatos

def salvar_contatos(contatos):
    with open(arquivo_contatos, "w", encoding="utf-8") as arquivo:
        for contato in contatos:
            arquivo.write(contato + "\n")

def adicionar_contato():
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    if nome and telefone and email:
        contato = f"{nome} | {telefone} | {email}"
        listbox_contatos.insert(tk.END, contato)
        salvar_contatos(listbox_contatos.get(0, tk.END))
        limpar_campos()
    else:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos!")

def excluir_contato():
    selecionado = listbox_contatos.curselection()
    if selecionado:
        listbox_contatos.delete(selecionado)
        salvar_contatos(listbox_contatos.get(0, tk.END))
    else:
        messagebox.showwarning("Nenhuma seleção", "Selecione um contato para excluir.")

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)

janela = tk.Tk()
janela.geometry('300x350')
janela.resizable(False, False)
janela.title("Agenda de Contatos")

cor_fundo = "#CAE1FF"
cor_fundo_label = "#CAE1FF"

janela.configure(bg=cor_fundo)

tk.Label(janela, text="Nome:", bg=cor_fundo_label, fg="black", width=10).grid(row=0, column=0, padx=5, pady=2, sticky="w")
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.grid(row=0, column=1, padx=5, pady=2)

tk.Label(janela, text="Telefone:", bg=cor_fundo_label, fg="black", width=10).grid(row=1, column=0, padx=5, pady=2, sticky="w")
entrada_telefone = tk.Entry(janela, width=30)
entrada_telefone.grid(row=1, column=1, padx=5, pady=2)

tk.Label(janela, text="Email:", bg=cor_fundo_label, fg="black", width=10).grid(row=2, column=0, padx=5, pady=2, sticky="w")
entrada_email = tk.Entry(janela, width=30)
entrada_email.grid(row=2, column=1, padx=5, pady=2)

btn_adicionar = tk.Button(janela, text="Adicionar Contato", command=adicionar_contato)
btn_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

listbox_contatos = tk.Listbox(janela, width=48, height=10)
listbox_contatos.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btn_excluir = tk.Button(janela, text="Excluir Contato Selecionado", command=excluir_contato)
btn_excluir.grid(row=5, column=0, columnspan=2, pady=5)

for contato in carregar_contatos():
    listbox_contatos.insert(tk.END, contato)

janela.mainloop()
