import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Login Rial")
#janela.iconbitmap("ico.ico")
janela.resizable(False, False)

#img = PhotoImage(file="bg.png")
#label_img = customtkinter.CTkLabel(janela, image=img, width=20)
#label_img.place(x=0, y=0)


def clique():
    msg_lbl.configure(text="")
    if not email:
        msg_lbl.configure(text="Favor inserir E-mail")
        return



texto = customtkinter.CTkLabel(janela,  text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua Senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela,text="Lembrar Login")
checkbox.pack(padx=10,  pady=10)

botao = customtkinter.CTkButton(janela, text="Login",  command=clique)
botao.pack(padx=10, pady=10)

msg_lbl = customtkinter.CTkLabel(janela, text='', text_color="white")
msg_lbl.place(x=10, y=10)

janela.mainloop()