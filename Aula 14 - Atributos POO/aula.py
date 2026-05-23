# # import random

# # class Jogador:
# #     def escolher(self):
# #         escolha = input("Escolha pedra, papel ou tesoura")
# #         return escolha.lower()

# # class Computador:
# #     def escolher(self):
# #         opcao = ['pedra','papel','tesoura']
# #         return random.choice(opcao)
    
# # class Jogo:
# #     def verificar_vencedor(self, jogador, computador):
# #         if jogador == computador:
# #             return 'empate'
# #         elif jogador == 'pedra' and computador == 'tesoura':
# #             return 'jogador venceu'
# #         elif jogador == 'tesoura' and computador == 'papel':
# #             return 'jogador venceu'
# #         elif jogador == 'papel' and computador == 'pedra':
# #             return 'jogador venceu'
# #         else:
# #             return 'O computador venceu...'
# #     def jogar(self):
# #         jogador = Jogador ()
# #         computador = Computador()
# #         escolha_jogador = jogador.escolher()
# #         escolha_computador = computador.escolher()
# #         print('Jogador escolheu - ', escolha_jogador)
# #         print('Computador escolheu - ', escolha_computador)
# #         resultado = self.verificar_vencedor(escolha_jogador,escolha_computador)
# #         print('RESULTADO: ', resultado)

# # jogo = Jogo()
# # jogo.jogar()                

# # jogo com programação
# # pedra papel com POO
# # import random

# # # jogador
# # class Jogador:
# #     def escolher(self):
# #         escolha = input('Escolha pedra,papel ou tesoura')
# #         return escolha.lower()
# # # computador
# # class Computador:
# #     def escolher(self):
# #         opcao = ['pedra','papel','tesoura']
# #         return random.choice(opcao)
    
# # class Jogo:

# #     def verificar_vencedor(self, jogador, computador):
# #         score_jogador = 0
# #         score_computador = 0
# #         if jogador == computador:
# #             print(score_jogador, 'x', score_computador)
# #             return 'empate'
# #         if jogador == 'pedra' and computador == 'tesoura':
# #             score_jogador =  score_jogador + 1
# #             print(score_jogador, 'x', score_computador)
# #             return 'Jogador venceu'
# #         elif jogador == 'tesoura' and computador  == 'papel':
# #             score_jogador =  score_jogador + 1
# #             print(score_jogador, 'x', score_computador)
# #             return 'Jogador venceu'
# #         elif jogador == 'papel'  and computador == 'pedra':
# #             score_jogador =  score_jogador + 1
# #             print(score_jogador, 'x', score_computador)
# #             return 'Jogador venceu'
# #         else:
# #             score_computador =  score_computador + 1
# #             print(score_jogador, 'x', score_computador)
# #             print()
# #             return 'Computador venceu...'
# #     def jogar(self):
            
# #             while True:
# #                 jogador  = Jogador()
# #                 computador = Computador()
# #                 escolha_jogador  = jogador.escolher()
# #                 escolha_computador  = computador.escolher()
# #                 print('Jogador escolheu - ', escolha_jogador)
# #                 print('Computador escolheu - ', escolha_computador)
# #                 resultado = self.verificar_vencedor(escolha_jogador, escolha_computador)
# #                 print('RESULTADO', resultado)
        
# # jogo = Jogo()
# # jogo.jogar()


# # class

# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.emprestado = False
        
#     def emprestar(self):
#         if not self.emprestado:
#             self.emprestado = True
#             return self.emprestado
            
            
#     def devolver(self):
#         self.emprestado = False         
#         return self.emprestado
    
#     def __str__(self):
#         return f'{self.titulo} {self.autor} {self.ano}'

# titulo, autor, ano = input('Livro: '), input('autor: '), input('ano ')

# l1 =  Livro(titulo, autor, ano)

# print('Emprestado? - ', l1.emprestar())

# print('Emprestado? - ',l1.devolver())

# print(l1)


# class Contador:
#     total_contadores = 0
#     def __init__(self):
#         Contador.total_contadores += 1
        
#     def exibir_total(self):
#         print(Contador.total_contadores)
        
# c1 =  Contador()
# c2 =  Contador()
# c3 =  Contador()
# c4 =  Contador()
        

# c1.exibir_total()


# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self._nome = nome
#         self._preco = preco
#         self._quantidade  =  quantidade
        
#     @property
#     def nome(self):
#         return self._nome
    
#     @property
#     def preco(self):
#         return self._preco
    
#     @property
#     def quantidade(self):
#          return self._quantidade
    
#     def aplicar_desconto(self, percentual):
#         desconto = self._preco * percentual
#         novo = self._preco  - desconto
#         if self._preco >= 0:
#             self._preco = novo
            
            

# p =  Produto('HD', 100.0,1)
# p.aplicar_desconto(0.10)
# print(p)
# print(p.nome, p.preco)

# class ContaBancaria:
#     def __init__(self):
#         self.__saldo = 0

#     def teste(self):
#         return self.__saldo    
        
#     def depositar(self, valor):
#         self.__saldo += valor
        
#     def sacar(self, valor):
#         if valor <= self.__saldo:
#             self.__saldo -= valor
#         else:
#             print('Saldo insuficiente...')
        
#     # @property
#     # def saldo(self):
#     #     return self.__saldo


# conta  =  ContaBancaria()
# conta.depositar(1000)
# conta.sacar(500)


# # print(conta.teste())
# print(conta.__saldo)


# class Aluno:
#     def __init__(self, nome, matricula):
#         self.nome  = nome
#         self.matricula =  matricula 
#         self.__notas = []

#     def adcionar_notas(self, nota):
#         if 0 <= nota <= 10 :
#             self.__notas.append(nota)
            
#     def calcular_media(self):
#         if len(self.__notas) == 0:
#             return 0
#         return sum(self.__notas) / len(self.__notas)
    
#     def situacao(self):
#         media  =  self.calcular_media()
#         if media >= 7:
#             return 'Aprovado'
#         elif media >= 5:
#             return 'Recuperação'
#         else:
#             return 'Reprovado'

# aluno1 = Aluno('Ana', '1')
# aluno2 = Aluno('Julia', '2')

# aluno1.adcionar_notas(8)
# aluno1.adcionar_notas(5)
# aluno1.adcionar_notas(10)

# aluno2.adcionar_notas(1)
# aluno2.adcionar_notas(2.5)
# aluno2.adcionar_notas(10)

# print('Média',aluno1.nome ,aluno1.calcular_media())
# print('Média',aluno2.nome ,aluno2.calcular_media())

# print(aluno1.situacao())
# print(aluno2.situacao())



# class Data:
#     def __init__(self, dia, mes, ano):
#         self.dia =  dia
#         self.mes  = mes 
#         self.ano =  ano

#     def __str__(self):
#         print(f'{dia}/{mes}/{ano}')    

#     def bissexto(self, ano):
#         if (ano % 400 == 0 or ano % 4 == 0) or (ano % 100 == 0):
#             print('ano bissexto...')
#         else:
#             print('Não é bissexto...')

#     def data_valida(self, dia, mes):
    
#         meses   =  [0,1,2,3,4,5,6,7,8,9,10,11,12]
#         dias_meses = [0,list(range(0,31)),
#                     list(range(1,29)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31))
#                     ]
#         if mes in meses:
#            i =  meses.index(mes)
#         if dia in dias_meses[i]:
#            print('data válida')
#         else:
#            print('Data invalida')

# ano =  int(input('ano: '))
# mes =  int(input('Digite o número do mês: '))
# dia =  int(input('Digite o dia:  '))


# data  =  Data(dia, mes, ano)
# data.bissexto(ano)
# data.data_valida(dia, mes)
# data.__str__()
       

# class Funcionario:
#     def __init__(self, nome, cargo, salario):
#         self.nome  =  nome 
#         self.cargo =  cargo
#         self._salario_base =  salario

#     def aumentar_salario(self, percentual):
#         self._salario_base += self._salario_base * percentual / 100
#         return self._salario_base
    
#     def calcular_bonus(self):
#         return self._salario_base * 0.10

#     @property
#     def salario(self):
#         return self._salario_base

# salario = float(input('Salario: '))
# f  =  Funcionario('Ana', 'DEv', salario)
# aumento = f.aumentar_salario(0.10)
# bonus = f.calcular_bonus()           

# print(aumento + bonus )    


# class Carro:
#     def __init__(self, marca, modelo):
#         self.marca =  marca
#         self.modelo =  modelo
#         self.__velocidade =  0

#     def acelerar(self, valor):
#         self.__velocidade += valor
#         if self.__velocidade > 200:
#             self.__velocidade = 200

#     def frear(self, valor):
#         self.__velocidade -= valor
#         if self.__velocidade < 0:
#             self.__velocidade = 0

#     @property
#     def velocidade(self):
#         return self.__velocidade



# c  =  Carro('Ferrari', 'Ferrari')
# c.acelerar(50)
# c.acelerar(300)
# c.frear(100)

# print(c.velocidade)



# class Estatistica: 


#     soma =  0
#     contagem = 0


#     @classmethod
#     def adcionar(cls, valor):
#         cls.soma  += valor
#         cls.contagem += 1


#     @classmethod
#     def calcular_media(cls):
#         if cls.contagem == 0:
#             return 0
#         return cls.soma/cls.contagem
    


# Estatistica.adcionar(10)
# Estatistica.adcionar(5)
# Estatistica.adcionar(2)


# print(Estatistica.calcular_media())

# class Contato():
#      def __init__(self, nome, telefone, email):
#           self.nome = nome
#           self.telefone =  telefone
#           self.email   =  email


# class Agenda():
#      def __init__(self):
#         self.__contatos =  []



#      def add_contato(self, contato):
#           self.__contatos.append(contato)


#      def lista_contato(self):
#           for c in self.__contatos:
#                print(c.nome, c.telefone, c.email)
     
#      def buscar_contato(self, nome):
#          for c in self.__contatos:
#               if c.nome == nome:
#                    print(c.nome, c.telefone,c.email)




# agenda  = Agenda()


# contato1 = Contato('ana','54464646', 'ana@gmail.com')


# contato2 = Contato('ana2','54464646', 'ana@gmail.com')


# agenda.add_contato(contato1)
# agenda.add_contato(contato2)
# agenda.lista_contato()
# agenda.buscar_contato('ana')