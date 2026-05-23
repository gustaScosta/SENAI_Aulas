# # nome = str(input("Qual o seu nome:"))

# # senha = int(input("Sua senha:"))


# # autorizacao = (nome == "admin" and senha == 1234) and 'Acesso autorizado' or 'Acesso negado'

# # print(autorizacao)

# compra = float(input("Qual o valor da compra:"))

# vip = (input("É vip? True or False:"))

# desconto = compra * 0.9

# valor_final = (compra > 100 and vip == ('True')) and f"Sua  compra com desconto é de:{desconto}" or f"Você não atendeu aos requisitos de desconto\nSua compra ficou no valor de:{compra}" 

# print(valor_final)

# nome = "Paulo"

# idade = "18"

# altura = 172


# print("Seu nome é: {} \nSua idade é: {} \nSua altura é: {}\n".format(nome,idade,altura))

# # compra = float(input("Qual o valor da compra:"))

# # vip = (input("É vip? True or False:"))

# # desconto = compra * 0.9

# # valor_final = (compra > 100 and vip == ('True')) and f"Sua  compra com desconto é de:{desconto}" or f"Você não atendeu aos requisitos de desconto\nSua compra ficou no valor de:{compra}" 

# # print(valor_final)

# # t =float(input('Qual a tempratura atual:')) 

# # u = int(input("Qual a umidade atual: "))

# # g = int(input("Gás presente? True(1) ou False (0): "))

# # # o * serve como, se existe verdaeiro e falo (0 ou 1) se for falso entrega 0 pois multiplicou por 0 a questão seguinte, mas se for verdadeiro multiplica por 1 e aparece a questão.
# # risco =( 
# #     (t > 40 and u > 80 and g == 1) * 'Nível crítico' or
# #     (t > 40 and u > 80 and g == 0) and 'Nível alto' or
# #     (t >=25 and t <=40 and u >= 50 and u <=80 and g == 0) and 'nivel medio' 
# #     or 'nível baixo'
# # )
# # print(risco)

# # # vip = str(input("Você é VIP? sim ou não: "))
# # # compra = float(input("Valor da compra: "))
# # # primeira_mes = str(input("É a primeira compra do mes? sim ou não:"))

# # # cupom = (vip == "sim" and compra >= 200 and primeira_mes == 'sim') and 'Cupom liberado' or 'Sem cupom'

# # # print(cupom)
# # # feedback = str(input("Deixe sua avalização:"))
# # # print("Feedback enviado!!!")


# # dados = {
# #     'vip' : 0,
# #     'valor_compra' : 0,
# #     'primeira_compra' : 0,
# #     'reclamacao' : 0
# # }

# # vip = (input('VIP - sim ou nao'))
# # valor_compra = float(input('R$'))
# # primeira_compra = input('primeira compra sim ou  nao')
# # reclamacao = bool(input('True or False'))

# # dados['primeira_compra'] = primeira_compra
# # dados['valor_compra'] = valor_compra
# # dados['primeira_compra'] = primeira_compra
# # dados['reclamacao'] = reclamacao

# # v1 = [dados['vip']] == 'sim'
# # v2 = [dados['valor_compra']] > 200
# # v3 = [dados['reclamacao']] == False
# # v4 = [dados['primeira_compra']] == 'sim'

# # verificacao = (v1 and v2 and v3 and v4) * 'Cupom liberado' or 'Sem cupom'

# # print(verificacao)

# # idade = int(input("Qual a sua idade:"))

# # peso = float(input("Qual o seu peso: "))


# # pode_doar = (idade >15 and idade <70) and (peso > 50) and 'Você pode doar' or 'Você não pode doar'
# # # verifiacao_idade = (idade >=16 and idade <=69 ) and 'Idade permitida' or 'Idade não permitida'

# # # verificacao_peso = (peso >= 50) and "Peso ideal" or "Peso não ideal"

# # # pode_doar = verifiacao_idade == 'Idade permitida' and verificacao_peso == 'Peso ideal' and 'Você pode doar' or 'Você não pode doar' 

# # print(pode_doar)

# # idade = int(input('Qual a sua idade: '))


# # classificacao = idade < 12 and 'Criança' or idade >= 12 and idade <=17 and 'Adolescente' or idade >= 18 and 'Adulto'

# # print(classificacao)

# # ano = int(input("Insira o ano:"))


# # bissexto = (ano % 4 == 0 and ano % 400 == 0) and not ano % 100 == 0 and 'É bissexto' or 'Não é bissexto'

# # print(bissexto)

# # # Primitivos 


# # # Crie um sistema onde precisamos verifica a idade do usuario
# # # se é maior de idade



# # # idade  = int(input('Idade: '))


# # # # verificação
# # # # and - e  or - ou  not - não
# # # # sinais aritméticos  ----  matemática  -  + | - | * |  / | // | % 
# # # # sinais lógicos  ----                  > |  <  |  >= | <= |  == | 
# # # print(idade >= 18)


# # # # True -  1
# # # # False -  0



# # # verifico =  idade >= 18 and 'Maior de idade' or 'Menor de idade'
                  
# # # print(verifico)

# # # verifico =  idade >= 18 and 'Maior de idade' or 'Menor de idade'
                  
# # # print(verifico)



# # # idade =  25
# # # nome  = 'José'
# # # logica =  True
# # # real_decimal = 5.2

# # # conta_banco = float(input(">>>"))

# # # verifico2 = conta_banco <= 0 and 'Conta zerada' or f'Você possui {conta_banco}'

# # #print(verifico2)

# # #Verificar senha para entrar no sistema

# # # senha = input("Digite sua senha:")

# # # verifica3 = senha and senha == '1234' and 'Acesso autorizado' or 'acesso negado'

# # # print(verifica3)

# # peso = float(input('Coloque seu peso:')) 


# # altura = float(input('Coloque sua altura: '))


# # imc = peso / altura ** 2


# # ideal = imc >= 18.5 and imc <= 24.9 and 'Peso normal' or 'Peso fora do normal'

# # print(ideal)

# # temperatura = float(input('Qual a temperatura: ')) 

# # umidade = int(input('Qual a umidade: '))


# # condicao = (temperatura < 35 and umidade < 70) and 'Condição normal' or 'Condição anormal'

# # print(condicao)

# # temperatura = float(input('Qual a temperatura: ')) 

# # umidade = int(input('Qual a umidade: '))


# # condicao = (temperatura < 35 and umidade < 70) and 'Condição normal' or 'Condição anormal'

# # print(condicao)

# # idade = int(input("Coloque sua idade:"))

# # autorizacao = (input("Tem auorização?"))

# # verificacao = (idade >= 18 and autorizacao == bool('True')) and "Pode participar" or "Não pode participar"