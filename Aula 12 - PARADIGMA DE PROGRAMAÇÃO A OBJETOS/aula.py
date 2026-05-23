# #1

# # class Pessoa:
# #     def __init__(self, nome, idade):
# #         self.nome = nome
# #         self.idade  = idade
# # # criei o método
# #     def apresentar(self):
# #         print(f'Olá, meu nome é {self.nome}, eu tenho {self.idade}')
# # # instaciei a classe --
# # pessoa1 =  Pessoa('Kaio',20)
# # pessoa2 =  Pessoa('Maria',22)
# # # usei o método na instancia --
# # pessoa1.apresentar()
# # pessoa2.apresentar()

# #2

# # class Retangulo:
# #     def __init__(self, largura, comprimento):
# #         self.comprimento = comprimento
# #         self.largura = largura
# #         self.area = largura * comprimento
# #         self.perimetro = 2*largura + 2*comprimento

# #     def apresentar(self):
# #         print(f'A area é {self.area} e o comprimento é {self.perimetro}')

# # retangulo = Retangulo(10,20)

# # retangulo.apresentar()

# #3

# # class ContaBancaria:
# #     def __init__(self, titular, saldo, depositar, sacar):
# #         self.titular = titular       
# #         self.saldo = saldo + depositar - sacar
# #         self.depositar = depositar
# #         self.sacar = sacar

# #     def apresentar(self):
# #         print(f'O titular {self.titular} atualmente tem {self.saldo} na conta')

            
# # conta = ContaBancaria("Paulo" , 0 , 300 , 100)

# # conta.apresentar() 

# #4 - Meu

# # class Produto:
# #     def __init__(self, nome, preco, quantidade_estoque, adicionar, remover):
# #         self.nome = nome 
# #         self.preco = preco
# #         self.quantidade_estoque = quantidade_estoque
# #         self.total_estoque = quantidade_estoque + adicionar - remover
# #         self.adcionar = adicionar
# #         self.remover = remover
# #         self.total_valor = self.total_estoque * 4 
    
# #     def apresentar(self):
# #         print(f'O produto {self.nome} tem {self.total_estoque} de estoque e todas custam {self.total_valor} reais.')

# # estoque = Produto("Banana", 4, 900, 200, 100)

# # estoque.apresentar()

# # 4 - correto 
# class Produto:
#     def __init__(self, nome, preco, quantidade_estoque):
#         self.nome = nome 
#         self.preco = preco
#         self.quantidade_estoque = quantidade_estoque

#     def aumentar_quantidade(self, adicionar):
#         adicionar = input("Quanto deseja adicionar:")
#         return self.quantidade_estoque + adicionar
    
#     def remover_quantidade(self, remover):
#         remover = input('Quanto deseja remover:')
#         return self.quantidade_estoque - remover
    

#     def total_estoque(self):
#         return  self.aumentar_quantidade -self.remover_quantidade + self.quantidade_estoque
        
#     def preco_estoque(self):
#         return self.preco * self.total_estoque_estoque
    
#     def apresentar(self):
#         print(f'O produto {self.nome} tem {self.total_estoque} de estoque e todas custam {self.preco_estoque} reais.')
    

# estoque = Produto("Banana", 4, 900)

# estoque.apresentar()
    
# #5

# # class Aluno:
# #     def __init__(self, nome, matricula, nota1, nota2, media, resultado):
# #         self.nome = Paulo
# #         self.matricula = 2507
# #         self.nota1 = 8
# #         self.nota2 = 
# #         self.media = 
# #         self.resultado = 


# class Caneta:
#     def __init__(self):
#         self.cor = 'azul'
#         self.ponta = 0.7
#         self.tamanho = 13.0
#         self.material = 'plastico'


#     def escrever(self):
#         pass


# caneta = Caneta()
# print(caneta.ponta)


# class Pessoa:
#     def __init__(self, idade):
#         self.idade = idade

#     def cerificar_idade(self)
#         if self.idade <=14:
#             print('Criança')
#         elif self.idade >=15 and self.idade <=18:
#             print('Adolescente')
#         elif self.idade >=19 and self.idade <=34:
#             print('Adulto')
#         else:
#             print('Idoso')

# pessoa = Pessoa(17)
# pessoa.verificar_idade






# # Crie uma classe Pessoa com os atributos nome e idade. Adicione um método apresentar() que exiba "Olá, meu nome é [nome] e tenho [idade] anos." Crie duas pessoas diferentes e chame o método.


# # criei a classe
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade  = idade
# # criei o método
#     def apresentar(self):
#         print(f'Olá, meu nome é {self.nome}, eu tenho {self.idade}')
# # instaciei a classe
# pessoa1 =  Pessoa('Kaio',20)
# pessoa2 =  Pessoa('Maria',22)
# # usei o método na instancia 
# pessoa1.apresentar()
# pessoa2.apresentar()