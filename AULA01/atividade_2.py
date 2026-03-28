valor = float(input("Qual o preço do seu produto?: "))


desconto = valor * 0.10

valor_total = valor - desconto

menorquecem = valor_total < 100

print(f"Valor do produto: {valor} \nValor do desconto:{desconto} \nValor total: {valor_total}\nÉ menor que cem: {menorquecem} ")