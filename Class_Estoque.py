import mysql.connector
from Class_Produto import *
from Class_Fabricante import *

class Estoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='estoque2')
        self.cursorzinho = self.conexao.cursor()
        
    # Create
    def cadastrar_fabricantes(self, codigo, nome, cnpj, razao_social):
        print('Estou aqui')
        obj_fabricante = Fabricante(codigo, nome, cnpj, razao_social)
        print(obj_fabricante.nome)
        print(obj_fabricante.cnpj)
        print(obj_fabricante.razao_social)
        comando_sql = f'insert into Fabricantes (nome, cnpj, razao_social) value ("{obj_fabricante.nome}", "{obj_fabricante.cnpj}", "{obj_fabricante.razao_social}")'
        self.cursorzinho.execute(comando_sql)
        self.conexao.commit()
        print('\nFabricante cadastrado com sucesso!\n')
    
    # Create
    def cadastrar_produtos(self, cod, descricao, codigo_fabricante, valor, quantidade):
        obj_produto = Produto(cod, descricao, codigo_fabricante, valor, quantidade)
        comando_sql = f'insert into Produtos (descricao, codigo_fabricante, valor, quantidade) value ("{obj_produto.descricao}", "{obj_produto.codigo_fabricante}", "{obj_produto.valor}", {obj_produto.quantidade})'
        try: 
            self.cursorzinho.execute(comando_sql)
            self.conexao.commit()
            print('\nProduto cadastrado com sucesso!\n')
        except:
            print('\nProdutos só podem ser cadastrados se seu fabricantes já for cadastrado no sistema!\n')
        
    # Read
    def mostrar_itens(self, codi):
            comando_sql = f'select Produtos.cod, Produtos.descricao, Fabricantes.nome, Produtos.valor, Produtos.quantidade from Produtos, Fabricantes where Produtos.cod = {codi} and Produtos.codigo_fabricante = Fabricantes.codigo'
            self.cursorzinho.execute(comando_sql)
            lista = self.cursorzinho.fetchall()
            if lista != []:
                for i in lista:
                    print('')
                    print (i)
            
                return lista
        
            elif codi == 0:
                comando_sql = 'select Produtos.cod, Produtos.descricao, Fabricantes.nome, Produtos.valor, Produtos.quantidade from Produtos, Fabricantes where Produtos.codigo_fabricante = Fabricantes.codigo'
                self.cursorzinho.execute(comando_sql)
                lista = self.cursorzinho.fetchall()
                for i in lista:
                    print('')
                    print(i)
            else:
                print('\nCódigo não encontrado!\n')
            
    # Update
    def alterar_informacoes(self, selecionar, atributo, info, codi):
        if selecionar == '1':
            comando_sql = f'update Produtos set {atributo} = "{info}" where cod = {codi}'
            try:
                self.cursorzinho.execute(comando_sql)
                self.conexao.commit()
            except:
                print('\nCódigo não encontrado!\n')
        elif selecionar == '2':
            comando_sql = f'update Fabricantes set {atributo} = "{info}" where codigo = {codi}'
            try:
                self.cursorzinho.execute(comando_sql)
                self.conexao.commit()
            except:
                print('\nCódigo não encontrado!\n')
        
    # Delete
    def excluir_informacoes(self, selecionar, codi):
        if selecionar == '1':
            comando_sql = f'delete from Produtos where cod = {codi}'
            try:
                self.cursorzinho.execute(comando_sql)
                self.conexao.commit()
            except:
                print('\nCódigo não encontrado!\n')
        elif selecionar == '2':
            comando_sql = f'delete from Fabricantes where codigo = {codi}'
            try:
                self.cursorzinho.execute(comando_sql)
                self.conexao.commit()
            except:
                print('\nCódigo não encontrado!\n')
