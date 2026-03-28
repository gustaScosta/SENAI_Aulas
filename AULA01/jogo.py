import random

#lista = ['😊','😂','❤️','👌']

#aleatorio = random.choice(lista)

#print(aleatorio)



# lista_pc = ['😊','😂','❤️','👌']

# nossa_lista = ['😊','😂','❤️','👌']

# aleatorio = random.choice(lista_pc)

# escolha_personagem = input("Teste: ")

# resultado = aleatorio == escolha_personagem

# print("Acertou:", resultado)
# print("Escolha da máquina:", aleatorio)
# print("Minha ecolha:", escolha_personagem)

# 1. Qual país tem mais ilhas no mundo?
# Resposta: Suécia (tem mais de 220.000). 

# 2. Qual é a montanha mais alta do mundo?
# Resposta: Monte Everest. 

# 3. Quem foi a primeira pessoa a viajar no Espaço?
# Resposta: Yuri Gagarin. 

# 4. Quantos fusos horários existem na Rússia?
# Resposta: 11. 

# 5. Qual é a única parte do corpo que está totalmente formada no nascimento?
# Resposta: Os olhos. 

# 6. Onde se localiza Machu Picchu?
# Resposta: Peru. 

# 7. Qual país tem o formato de uma bota? 
# Resposta: Itália. 

# 8. Quantos pontos podemos encontrar em um par de dados (soma de todas as faces)?
# Resposta: 42. 

# 9. Quem inventou a lâmpada?
# Resposta: Thomas Edison. 

# 10. Qual animal é considerado o mais forte em relação ao peso corporal?
# Resposta: Besouro do esterco. 

lista_perguntas = [
    '',
    '1. Qual país tem mais ilhas no mundo?',
    '2. Qual é a montanha mais alta do mundo?',
    '3. Quem foi a primeira pessoa a viajar no Espaço?',
    '4. Quantos fusos horários existem na Rússia?',
    '5. Qual é a única parte do corpo que está totalmente formada no nascimento?',
    '6. Onde se localiza Machu Picchu?',
    '7. Qual país tem o formato de uma bota?',
    '8. Quantos pontos podemos encontrar em um par de dados (soma de todas as faces)?',
    '9. Quem inventou a lâmpada?',
    '10. Qual animal é considerado o mais forte em relação ao peso corporal?'
]

lista_respostas = [
    '',
    'Resposta: Suécia (tem mais de 220.000).',
    'Resposta: Monte Everest.',
    'Resposta: Yuri Gagarin.',
    'Resposta: 11.',
    'Resposta: Os olhos.',
    'Resposta: Peru.',
    'Resposta: Itália.',
    'Resposta: 42.',
    'Resposta: Thomas Edison.',  
    'Resposta: Besouro do esterco.'  
]


pergunta = random.choice(lista_perguntas)
print(pergunta)

print(lista_respostas[1:])
resposta = int(input('Digite o número da resposta: '))

i = lista_perguntas.index(pergunta)

pontos = 0

pontos += (resposta == i)

print("Resltado acertou?", resposta == i )
print("Resposta correta: ", lista_respostas[i])
print("Pontuação: ", pontos)


