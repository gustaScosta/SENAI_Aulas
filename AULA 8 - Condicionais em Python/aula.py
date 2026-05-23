# dia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
# mes = [1,2,3,4,5,6,7,8,9,10,11,12]

# ano = int(input('Ano:'))

# if (ano % 400 == 0 and ano % 4 == 0) or (ano % 100 == 0):
#     print("bissexto")
# else:
#     print("Não é bissexto")

#     lado1 = int(input("Lado menor: "))

# lado2 = int(input("Lado mediano : "))

# lado3 = int(input("Lado maior: "))

# soma = lado1 + lado2


# if soma > lado3:
#     print('É triângulo:')
# else: 
#     print('Não é triâgulo')

# if lado1 and lado2 == lado3:
#     print("Equilatero")
# elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
#     print("Escaleno")
# else:
#     print("É isóceles")

# peso = float(input('Qual o seu peso:'))

# altura = float(input('Qual a sua altura:'))

# imc = peso/(altura*2)

# if imc < 18.5:
#     print("Abaixo do peso")
# elif imc >= 18.5 and imc <25:
#     print("Peso normal")
# elif imc >=25 and imc <30:
#     print("Sobrepeso")
# else:
#     print("Obesidade")

# salario = float(input("Informe seu salário: "))



# inss = salario * 0.11

# com_inss = salario - inss

# if inss >1500:
#     inss = 1500
# else: 
#     inss = inss

# if salario <= 2500:
#     print(com_inss)
# elif salario >2500 and salario <= 3500:
#     total = com_inss * 0.925
#     print(total)
# elif salario >3500 and salario <= 5000:
#     total = com_inss * 0.85
#     print(total)
# else:
#     total = com_inss * 0.72,5
#     print(total)

# import random

# jokenpo = []

# #jokenpo.append('pedra')
# jokenpo.append('papel')
# #okenpo.append('tesoura')

# jogada1 = input('Escolha pedra, pepel ou tesoura:')


# jogada2 = random.choice(jokenpo)
# print(jogada2)

# if jogada2 == jogada1:
#     print("Empate!!")
# elif jogada2 != jogada1:
#     if jogada1 == 'pedra' and jogada2 =='tesoura':
#         print("Você ganhou!")
#     elif jogada1 == 'tesoura' and jogada2 == 'papel':
#         print("Você Ganhou!!")
#     elif jogada1 == 'papel' and jogada2 == 'pedra':
#         print("Você Ganhou!!!")
#     else:
#         print("Você perdeu!!!!!")
 

#  n1 = float(input("Nota1:"))
# n2 = float(input("Nota2:"))

# media = (n1+n2)/2

# if media > 7:
#     print("Você passou!!!")
#     situação = 1
# else:
#     print("Recuperação")
#     situação = 2

# if situação == 2:
#     nota_recuperacao = float(input("Qual a nota de recuperação: "))
#     nota_final = (media + nota_recuperacao)/2
#     if nota_final >= 5:
#         print("Você passou! Ufa!")
#     else:
#         print("Repitiu mané")

# sexo = int(input("Sexo M/F:")) 

# nascimento = int(input("Ano de nascimento:"))   

# deficiencia = input("Possui deficiência S/N:")


# if sexo == 'f':
#     print('Não obrigatório')
# elif sexo =='m':
#     idade = 2026 - nascimento 
#     if deficiencia == 'S':
#         print('Não pode se alistar')
#     if idade == 18 and deficiencia== 'n':
#         print("Alistamento imediato")
#     elif idade >=18 and idade >=45:
#         print("Passou do prazo")
#     else:
#         print("Não tem idade")
    


# idade =  int(input('Idade: '))
# carta_m =  input('POssui carta sim ou não?')
# decisao =  idade>=18 and carta_m == 'sim' and 'Pode dirigir' or 'não pode...'
# print(decisao)

# if idade >= 18 and carta_m == 'sim':
#     print('Pode ')
# else:
#     print('Não pode')
    
# if idade >= 18:
#    if carta_m == 'sim':
#        print('Pode ')
# else:
#     print('Não pode')
    
    
# if idade >= 18 and carta_m == 'sim':
#    print('Pode ')
# elif idade >= 18 and carta_m == 'não':
#    print('pode tirar a carta')
# else:
#    print('Não pode')


# print('SISTEMA DE NOTAS')


# lista_nomes = []
# aluno2 = input("Nome do aluno 2:")
# aluno1 = input("Nome do aluno 1:")

# lista_nomes.append(aluno1)
# lista_nomes.append(aluno2)
# print(lista_nomes)

# print('lista de alunos:', lista_nomes)

# notas_aluno1 = [float(input('nota1:')), float(input('nota2:'))]
# notas_aluno2 = [float(input('nota1:')), float(input('nota2:'))]

# media_aluno1 = sum(notas_aluno1)/len(notas_aluno1)
# media_aluno2 = sum(notas_aluno2)/len(notas_aluno2)

# print('Aluno', aluno1, 'Media: ',media_aluno1)
# print('Aluno', aluno2, 'Media: ',media_aluno2)


# if media_aluno1 >= 6:
#     print('Aluno aprovado')
# elif media_aluno1 < 6 and media_aluno1 >= 4:
#     print('Está de recuperação')
# else:
#     print('Aluno reprovado')


# aluno1 = input('Nome do aluno: ')

# nota_aluno = float(input('Nota do aluno:'))

# if nota_aluno >=9:
#     print("Excelente")
# elif nota_aluno >= 7 and nota_aluno <9:
#     print("Bom")
# elif nota_aluno >= 5 and nota_aluno < 7:
#     print("Regular")
# if nota_aluno < 5:
#     print("Insuficiente")
    