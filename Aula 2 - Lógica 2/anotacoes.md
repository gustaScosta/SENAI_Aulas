# Aula 2 - Logica 2

## Introducao a logica de programacao com Python

Logica de programacao e a forma de organizar instrucoes para que um computador consiga resolver um problema.

Um programa normalmente segue esta estrutura:

```text
Entrada -> Processamento -> Saida
```

Exemplo:

```text
Usuario digita um numero
Programa soma 10
Resultado e exibido
```

## Tipos de dados primitivos em Python

Tipos primitivos sao os dados mais basicos da linguagem.

| Tipo | Descricao | Exemplo |
| --- | --- | --- |
| `int` | numeros inteiros | `10` |
| `float` | numeros decimais | `3.14` |
| `str` | texto | `"Python"` |
| `bool` | verdadeiro ou falso | `True` |

Exemplo:

```python
idade = 20
altura = 1.75
nome = "Maria"
aprovado = True
```

## Variaveis

Variaveis sao espacos na memoria usados para armazenar valores.

Estrutura:

```python
nome_da_variavel = valor
```

Exemplo:

```python
nome = "Joao"
idade = 25
```

## Funcao print()

A funcao `print()` e usada para mostrar informacoes na tela.

Exemplo:

```python
print("Ola mundo")
```

Exemplo com variavel:

```python
nome = "Ana"
print(nome)
```

Saida:

```text
Ana
```

## Funcao input()

A funcao `input()` permite receber dados digitados pelo usuario.

Exemplo:

```python
nome = input("Digite seu nome: ")
print(nome)
```

## Conversao de tipos

O `input()` sempre retorna texto, ou seja, um valor do tipo `str`.

Quando precisamos trabalhar com numeros, devemos converter o valor.

Exemplos:

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

Conversoes comuns:

- `int()`: converte para numero inteiro.
- `float()`: converte para numero decimal.
- `str()`: converte para texto.
- `bool()`: converte para verdadeiro ou falso.

## Exemplo completo

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Seu nome e:", nome)
print("Sua idade e:", idade)
```

## Resumo

- Logica de programacao organiza passos para resolver problemas.
- Um programa pode ser pensado como entrada, processamento e saida.
- Variaveis guardam valores na memoria.
- Python possui tipos como `int`, `float`, `str` e `bool`.
- `print()` mostra informacoes.
- `input()` recebe informacoes do usuario.
- Valores recebidos por `input()` precisam ser convertidos quando forem usados como numeros.
