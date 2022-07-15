from cgi import test
from cgitb import text
from email.mime import image
from itertools import count
from re import I, L
from struct import pack
import tkinter
from tkinter import *
from random import *
from tkinter import ttk
import time
import os
import tkinter.messagebox
from Class_Estoque import *
from Class_Gerenciar_Estoque import * 
import posiciona

class Interface:
    def __init__(self):
        self.catalogo = Estoque()
        self.catalogo1 = Gerenciador()
        self.catalogo1.gerenciar = self.catalogo

        self.meu_estoque = Tk()
        self.meu_estoque.title('Gestão de Estoque')
        self.meu_estoque.geometry('1000x700+200+200')
        self.meu_estoque.resizable(width=False, height=False)

        self.meu_estoque.bind('<Button-1>', posiciona.inicio_place)
        self.meu_estoque.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, self.meu_estoque))
        self.meu_estoque.bind('<Button-2>', lambda arg: posiciona.para_geometry(self.meu_estoque))
        
        self.tela_menu = PhotoImage(file='Imagens/tela_menu.png')
        self.bt_menu_f = PhotoImage(file='Imagens/botao_cadas_fabri_menu.png')
        self.bt_menu_p = PhotoImage(file='Imagens/botao_cadas_pro_menu.png')
        self.bt_menu_pr = PhotoImage(file='Imagens/botao_procura_menu.png')
        self.bt_menu_alt = PhotoImage(file='Imagens/botao_altera_info_menu.png')
        self.bt_menu_delet = PhotoImage(file='Imagens/botao_deletar_menu.png')
        self.bt_menu_ent = PhotoImage(file='Imagens/botao_entrada_menu.png')
        self.bt_menu_said = PhotoImage(file='Imagens/botao_saida_menu.png')
        self.bt_sair = PhotoImage(file='Imagens/botao_sair.png')
        self.bt_salvar = PhotoImage(file='Imagens/botao_salvar.png')
        self.bt_procura = PhotoImage(file='Imagens/botao_procurar.png')
        self.tela_cadas_f = PhotoImage(file='Imagens/tela_cadas_f.png')

        self.f1 = Frame(self.meu_estoque)
        self.f1.pack()
        self.f2 = Frame(self.meu_estoque)
        self.f3 = Frame(self.meu_estoque)
        self.f4 = Frame(self.meu_estoque)
        self.f5 = Frame(self.meu_estoque)
        self.f6 = Frame(self.meu_estoque)
        self.f7 = Frame(self.meu_estoque)
        self.f8 = Frame(self.meu_estoque)
        self.f9 = Frame()
        self.f10 = Frame()
        self.f11 = Frame()

        self.menu_label = Label(self.f1, image=self.tela_menu)
        self.menu_label.pack()
        self.bcadastrof = Button(self.f1, image=self.bt_menu_f, bd=0, command=lambda: self.fabricante())
        self.bcadastrof.place(width=245, height=65, x=146, y=203)
        self.bcadastrop = Button(self.f1, image=self.bt_menu_p, bd=0, command=lambda: self.produto())
        self.bcadastrop.place(width=245, height=65, x=146, y=293)
        self.bprocurarp = Button(self.f1, image=self.bt_menu_pr, bd=0, command=lambda: self.procurar())
        self.bprocurarp.place(width=245, height=65, x=146, y=381)
        self.balterainf = Button(self.f1, image=self.bt_menu_alt, bd=0, command=lambda: self.alterar())
        self.balterainf.place(width=245, height=65, x=146, y=470)
        self.bdeletacad = Button(self.f1, image=self.bt_menu_delet, bd=0, command=lambda: self.deletar())
        self.bdeletacad.place(width=245, height=65, x=146, y=561)
        self.babastecer = Button(self.f1, image=self.bt_menu_ent, bd=0, command=lambda: self.abastecer())
        self.babastecer.place(width=245, height=65, x=608, y=204)
        self.bretirarpd = Button(self.f1, image=self.bt_menu_said, bd=0, command=lambda: self.retirar())
        self.bretirarpd.place(width=245, height=65, x=608, y=293)
        self.bhistgeral = Button()
        self.bhistentra = Button()
        self.bhistsaida = Button()
        self.botaosair  = Button(self.f1, image=self.bt_sair, bd=0, command=lambda: self.meu_estoque.destroy())
        self.botaosair.place(width=117, height=41, x=442, y=648)

        self.cadastro_fabri = Label(self.f2, image=self.tela_cadas_f)
        self.cadastro_fabri.pack()
        self.nome = Entry(self.f2, font=("Calibri", 15), bd=0)
        self.nome.place(width=622, height=32, x=188, y=249)
        self.cnpj = Entry(self.f2, font=("Calibri", 15), bd=0)
        self.cnpj.place(width=622, height=32, x=188, y=346)
        self.razao_s = Entry(self.f2, font=("Calibri", 15), bd=0)
        self.razao_s.place(width=622, height=32, x=188, y=442)
        self.bsalvarf = Button(self.f2, image=self.bt_salvar, bd=0, command=lambda: self.salvar_fabri())
        self.bsalvarf.place(width=115, height=37, x=364, y=648)
        self.botaosairf = Button(self.f2, image=self.bt_sair, bd=0, command=lambda: [self.f2.forget(), self.f1.pack()])
        self.botaosairf.place(width=115, height=37, x=522, y=648)

        self.cadastro_produto = Label(self.f3, text='Cadastrar Produto')
        self.descricao = Entry(self.f3, font=("Calibri", 15))
        self.codigo_fabricante = Entry(self.f3, font=("Calibri", 15))
        self.valor = Entry(self.f3, font=("Calibri", 15))
        self.bsalvarp = Button(self.f3)
        self.botaosairp = Button(self.f3, command=lambda: [self.f3.forget(), self.f1.pack()])

        self.procurar_label = Label(self.f4, text='Procurar Produto')
        self.codi = Entry(self.f4, font=("Calibri", 15))
        self.bprocurando = Button(self.f4)
        self.botaosairpro = Button(self.f4, command=lambda: [self.f4.forget(), self.f1.pack()])

        self.alterar_label = Label(self.f4, text='Alterar Informações')
        self.codi = tkinter.IntVar()
        self.bselecionap = Radiobutton(self.f4, variable=self.codi, value=1)
        self.bselecionaf = Radiobutton(self.f4, variable=self.codi, value=2)
        
        self.meu_estoque.mainloop()
        
    def fabricante(self):
        self.f1.forget()    
        self.f2.pack()
        
    def salvar_fabri(self):
        codigo = None
        nome = self.nome.get()
        cnpj = self.cnpj.get()
        razao_social = self.razao_s.get()
        self.catalogo.cadastrar_fabricantes(codigo, nome, cnpj, razao_social)
                
    def produto(self):
        self.f1.forget()
        self.f3.pack()
    
    def salvar_pro(self):
        cod = None
        quantidade = 0
        self.catalogo.cadastrar_produtos(cod, self.descricao.get(), self.codigo_fabricante.get(), self.valor.get(), quantidade)

    def procurar(self):
        self.f1.forget()
        self.f4.pack()

    def alterar(self):
        self.f1.forget()
        self.f5.pack()

    def deletar(self):
        self.f1.forget()
        self.f6.pack()

    def abastecer(self):
        self.f1.forget()
        self.f7.pack()

    def retirar(self):
        self.f1.forget()
        self.f8.pack()
        
janela = Interface()