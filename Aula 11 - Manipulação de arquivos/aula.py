# Ana	0	2000
# Paulo	30	200
# Fernanda	25	3000

#CSV

# # Abre o arquivo para escrita (cria/substitui)
# arquivo = open("dados.txt", "w")
# arquivo.write("Linha 1\n")
# arquivo.write("Linha 2\n")
# arquivo.close()


# x  = open('arquivo.txt','w')
# x.write('fhsjkdfhjksdhfjkshdjkfhjsdhfjshdfjkhsjdfksd\n')
# x.close()


# x = open('arquivo.txt', 'a')
# x.write('adiocione....')
# x.close()


# 1
# arquivo = open('cadastro.csv', 'r')
# for linha in arquivo:
#     dados = linha.strip().split(',')
#     nome =  dados[0]
#     idade = dados[1]
#     venda = dados[2]
#     #print('Nome', nome, 'idade', idade, 'vendas', venda)


# arquivo.close()


# # 2
# with open('cadastro.csv', 'r') as c:
#     conteudo = c.read()
#     #print(conteudo)

# # 3

# arquivo = open('cadastro.csv', 'r')

# c = 0
# for linha in arquivo:
#      arquivo = open('cadastro.csv', 'r')
#      linha = arquivo.readline()
#      print(linha)
#      c = c + 1
#      print(c)
# arquivo.close()

# arquivo = open("cadastro.csv", "r")
# linha = arquivo.readline()
# c = 0
# while linha:
#     print(linha.strip())  # strip remove a quebra de linha
#     linha = arquivo.readline()
#     c = c + 1
#     print(c) 
# arquivo.close()

# 4


nome_arquivo =  input('Nome do arquivo: ')
palavra =  input('Palavra: ')


# arquivo = open(nome_arquivo, 'w')
# arquivo = open(nome_arquivo, 'a')
# arquivo.write(palavra)


arquivo = open(nome_arquivo,'r')
contador  =  0


for linha in arquivo:
    linha  =  linha.lower()
    contador =  contador + linha.count(palavra.lower())


arquivo.close()


print('contador da palavra', contador)



# n =  'teste'


# print(n.count('s'))