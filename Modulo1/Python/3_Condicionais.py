# Se chover
#     Saio com guarda-chuva
# Senao
#     Saio de camiseta

### IF/ELSE
idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Você é maior de idade.")
elif idade == 18: ##  elif é usado para verificar outra condição caso a primeira seja falsa e pode ser usado quantas vezes for necessário. Mas sempre entre o if e o else.
    print("Você tem exatamente 18 anos.")
else:
    print("Você é MENOR de idade.")

### Condicional Ternário
# É uma forma mais compacta de escrever um if/else. Ele é usado para atribuir um valor a uma variável com base em uma condição.
# A sintaxe é: valor_se_verdadeiro if condição else valor_se_falso
idade = int(input("Digite sua idade: "))
status = "maior de idade" if idade > 18 else "menor de idade"
print(f"Você é {status}.")  

## O jeito que eu fiz está abaixo
idade = int(input("Digite sua idade: "))
print("Você é maior de idade." if idade > 18 else "Você é menor de idade.") 

### Switch Case (match)
# O switch case é uma estrutura de controle que permite executar diferentes blocos de código com base no valor de uma expressão. Em Python, a partir da versão 3.10, foi introduzida a estrutura match/case, que é uma forma mais poderosa e flexível de implementar o comportamento do switch case.
# A sintaxe básica do match/case é a seguinte:

nome = input("Digite seu nome: ")
match nome:
    case "Alice":
        print("Olá, Alice!")
    case "Bob":
        print("Não é o meu nome, mas tudo bem.")
    case name:
        print(f"Olá, {name}!")  # O caso {name} é um coringa que corresponde a qualquer valor que não tenha sido correspondido pelos casos anteriores.

### Simulando testes condicionais
#### Um algortimo que:
# Peça ao usuário para digitar o seu ano de nascimento - OK
# Peça o ano atual - OK
# Descubra se o usuário é maior de idade - OK
# Se for, peça o título de eleitor dele - OK
# Senão, peça o documento do responsável - OK

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
if idade >= 18:
    print("Digite o número do título de eleitor:")
else:
    print("Digite o número do documento do responsável:")