from Class_Estoque import *
from Class_Entrada import *
from Class_Saida import *
class Gerenciador:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='estoque2')
        self.cursorzinho = self.conexao.cursor()
        self.gerenciar = Estoque()
        
    def entrada(self, cod, observacoes, cod_produtos, info):
        obj_entrada = Entrada(cod, observacoes)
        comando_sql = f'insert into Entrada (observacoes) value ("{obj_entrada.observacoes}")'
        self.cursorzinho.execute(comando_sql)
        self.conexao.commit()
        try:
            entrar = 'select cod from Entrada order by cod desc limit 1'
            self.cursorzinho.execute(entrar)
            lista = self.cursorzinho.fetchall()
            cod_entrada = (lista[0][0])
            comando_sql = f'insert into Entrada_Produtos (cod_entrada, cod_produtos) value ({cod_entrada}, {cod_produtos})'
            self.cursorzinho.execute(comando_sql)
        except:
             print('\nCódigo não encontrado!\n')
        else:
            self.conexao.commit()
            comando_sql = f'update Produtos set quantidade = quantidade + {info} where cod = {cod_produtos}'
            self.cursorzinho.execute(comando_sql)
            self.conexao.commit()
            print('\nEntrada no sistema confirmada!')
                           
    def saida(self, cod, observacoes, cod_produtos, info):
        obj_saida = Saida(cod, observacoes)
        comando_sql = f'insert into Saida (observacoes) value ("{obj_saida.observacoes}")'
        self.cursorzinho.execute(comando_sql)
        self.conexao.commit()
        try:
            sair = 'select cod from Saida order by cod desc limit 1'
            self.cursorzinho.execute(sair)
            lista = self.cursorzinho.fetchall()
            cod_saida = (lista[0][0])
            comando_sql = f'insert into Saida_Produtos (cod_saida, cod_produtos) value ({cod_saida}, {cod_produtos})'
            self.cursorzinho.execute(comando_sql)
        except:
             print('\nCódigo não encontrado!\n')
        else:
            self.conexao.commit()
            quant = f'select quantidade from Produtos where cod = {cod_produtos}'
            self.cursorzinho.execute(quant)
            lista = self.cursorzinho.fetchall()
            quanti = (lista[0][0])
            if quanti > info:
                comando_sql = f'update Produtos set quantidade = quantidade - {info} where cod = {cod_produtos}'
                self.cursorzinho.execute(comando_sql)
                self.conexao.commit()
                print('\nBaixa no sistema confirmada!')
            else:
                print('\nSaida negada!')
                print('\nO valor solicitado excede a quantidade no estoque.\n')

    def imprimir_t(self):
        for i in self.movimentacao:
            print('\n ', i)
            print('')

    def imprimir_e(self):
        for i in self.entrada_p:
            print('\n ', i)
            print('')
            
    def imprimir_s(self):
        for i in self.saida_p:
            print('\n ', i)
            print('')
