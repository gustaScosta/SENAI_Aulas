num1 = float(input("Digite o primeiro número:"))

num2 = float(input("Digite seu segundo numero:"))


soma = num1 + num2
subtracao = num1 - num2
vezes = num1 * num2
divisao = num1 / num2


igualdade = num2 == num1
maior = num1 > num2
ten1 = (num1 > 10 or num2 > 10)




print("Soma:{}\nSubtração:{}\nVezes:{}\nDivisão:{}".format(soma, subtracao, vezes, divisao))

print(f"São iguais:{igualdade}\nO primeiro é maior:{maior}\nUm é maior que dez:{ten1}")


