# importanto as bibliotecas
# from cgitb import text
from tkinter import *
from tkinter import font
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import messagebox

# Importando views
from views import *


# cores #
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + céu azul


# criando janela

janela = Tk()  # Abrir janela vazia
janela.title("")  # Titulo da janela
janela.geometry('1043x453')  # Criando a parte geometrica da janela
janela.configure(background=co9)  # Definindo a cor do background da janela
# Bloquear a alteração de altura da pagina
janela.resizable(width=False, height=False)

# Dividindo a janela

# Criando a parte de cima da janela - configuração
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief="flat")
frame_cima.grid(row=0, column=0)

# Criando a parte de baixo da janela - configuração
frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

# Criando  parte da direita
frame_direita = Frame(janela, width=588, height=403, bg=co1, relief="flat")
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


# Label Cima
app_nome = Label(frame_cima, text='Formulario de Consultoria',
                 anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief="flat")
app_nome.place(x=10, y=20)

# variavel tree global
global tree

# Função inserir


def inserir():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    dia = e_cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()

    lista = [nome, email, tel, dia, estado, assunto]

    if nome == '':
        messagebox.showerror('Erro', 'Onome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

# Função Atualizar


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_cal.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_assunto.insert(0, tree_lista[6])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_tel.get()
            dia = e_cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()

            lista_atualizar = [nome, email, tel, dia, estado, assunto, valor]

            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualizar_info(lista_atualizar)
                messagebox.showinfo(
                    'Sucesso', 'Os dados foram atualizados com sucesso!')

                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                e_cal.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_assunto.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        b_confirmar = Button(frame_baixo, command=update, text=' Confirmar', width=10,
                             font=('Ivy 7 bold'), bg=co2, fg=co1, relief="raised", overrelief='ridge')
        b_confirmar.place(x=110, y=370)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')


# Função atualizar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor = [tree_lista[0]]

        deletar_info(valor)
        messagebox.showinfo(
            'Sucesso', 'Os dados foram deletedados da tabela com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados da tabela')


# Configurando Frame baixo Nome
e_nome = Label(frame_baixo, text='Nome *', anchor=NW,
               font=('Ivy 10 bold'), bg=co1, fg=co4, relief="flat")
e_nome.place(x=10, y=10)

# Criando a parte do Input Nome
e_nome = Entry(frame_baixo, width=45, justify='left',
               relief="solid")  # Configuração da janela de input
e_nome.place(x=15, y=40)


# Configurando Frame baixo Email
e_email = Label(frame_baixo, text='Email *', anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4, relief="flat")
e_email.place(x=10, y=70)

# Criando a parte do Input Email
e_email = Entry(frame_baixo, width=45, justify='left',
                relief="solid")  # Configuração da janela de input
e_email.place(x=15, y=100)


# Configurando Frame baixo Telefone
e_tel = Label(frame_baixo, text='Telefone *', anchor=NW,
              font=('Ivy 10 bold'), bg=co1, fg=co4, relief="flat")
e_tel.place(x=10, y=130)

# Criando a parte do Input Telefone
e_tel = Entry(frame_baixo, width=45, justify='left',
              relief="solid")  # Configuração da janela de input
e_tel.place(x=15, y=160)


# Configurando Frame baixo Consulta
l_cal = Label(frame_baixo, text='Data da Consulta *', anchor=NW,
              font=('Ivy 10 bold'), bg=co1, fg=co4, relief="flat")
l_cal.place(x=10, y=190)

# Criando a parte do Input Consulta
e_cal = DateEntry(frame_baixo, width=12, background='darkblue',
                  foreground='white', borderwidth=2)
e_cal.place(x=15, y=220)


# Configurando Frame baixo estado
e_estado = Label(frame_baixo, text='Estado da consulta *', anchor=NW,
                 font=('Ivy 10 bold'), bg=co1, fg=co4, relief="flat")
e_estado.place(x=160, y=190)

# Criando a parte do Input estado
e_estado = Entry(frame_baixo, width=20, justify='left',
                 relief="solid")  # Configuração da janela de input
e_estado.place(x=160, y=220)


# Configurando Frame baixo sobre
e_assunto = Label(frame_baixo, text='Informação extra *', anchor=NW,
                  font=('Ivy 10 bold'), bg=co1, fg=co4, relief="flat")
e_assunto.place(x=15, y=260)

# Criando a parte do Input sobre
e_assunto = Entry(frame_baixo, width=45, justify='left',
                  relief="solid")  # Configuração da janela de input
e_assunto.place(x=15, y=290)


# Botão inserir
b_inserir = Button(frame_baixo, command=inserir, text=' Inserir', width=10,
                   font=('Ivy 9 bold'), bg=co6, fg=co1, relief="raised", overrelief='ridge')
b_inserir.place(x=15, y=340)

# Botão Atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text=' Atualizar', width=10,
                     font=('Ivy 9 bold'), bg=co2, fg=co1, relief="raised", overrelief='ridge')
b_atualizar.place(x=105, y=340)


# Botão Deletar
b_deletar = Button(frame_baixo, command=deletar, text=' Deletar', width=10,
                   font=('Ivy 9 bold'), bg=co7, fg=co1, relief="raised", overrelief='ridge')
b_deletar.place(x=195, y=340)


# Frame direita
def mostrar():

    global tree

    lista = mostrar_info()

    # lista para cabeçario
    tabela_head = ['ID', 'Nome', 'email',
                   'Telefone', 'Data', 'Estado', 'Sobre']

    tree = ttk.Treeview(frame_direita, selectmode="extended",
                        columns=tabela_head, show="headings")

    # Vertical Scroollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # Horizontal Scroolbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # Ajuste da coluna
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


# Chamando a função mostrar , que mostra a tabela
mostrar()


janela.mainloop()  # Sempre preciso ter a janela.mainlop , senão a janela não abre
