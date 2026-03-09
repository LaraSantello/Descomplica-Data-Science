## Exemplode Manipulação de Arquivos e Tratamento de Erros
# open("arquivo.txt", "w")  ## O modo "w" é usado para abrir um arquivo para escrita. Se o arquivo já existir, ele será sobrescrito. Se o arquivo não existir, ele será criado.

# R = Read
# W = Write
# A = Append
# X = eXecute
# R+
# WB

# open("arquivo.txt", "x")  ## O modo "x" é usado para abrir um arquivo para escrita exclusiva. Se o arquivo já existir, uma exceção será levantada. Se o arquivo não existir, ele será criado.

# a = open("arquivo.txt", "r") ## O modo "r" é usado para abrir um arquivo para leitura. Se o arquivo não existir, uma exceção será levantada.

# a.write("Olá, mundo!\n")  ## O método write() é usado para escrever uma string no arquivo. No exemplo acima, a string "Olá, mundo!\n" é escrita no arquivo "arquivo.txt". O "\n" é um caractere de nova linha, que faz com que o próximo texto seja escrito em uma nova linha.

# a.write("Bem-vindo à manipulação de arquivos em Python.\n")  ## O método write() pode ser chamado várias vezes para escrever várias linhas no arquivo.

# print(a.read())  ## O método read() é usado para ler o conteúdo de um arquivo. No exemplo acima, o conteúdo do arquivo "arquivo.txt" é lido e impresso na tela.

# a.close()  ## O método close() é usado para fechar o arquivo. É importante fechar o arquivo após terminar de usá-lo para liberar os recursos do sistema.

## Manipulação de arquivos em nuvem

# Ler arquivos da internet usando a biblioteca requests
import requests
r = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")  ## O método get() da biblioteca requests é usado para fazer uma requisição HTTP GET para a URL especificada. No exemplo acima, a URL "https://www.example.com" é acessada e o conteúdo da página é armazenado na variável r.
print(r)
print(r.text)  ## O atributo text da resposta r contém o conteúdo da página em formato de string. No exemplo acima, o conteúdo da página "https://www.example.com" é impresso na tela.

# wb = Write Binary
with open("arquivo2.txt", "wb") as a:  ## O modo "wb" é usado para abrir um arquivo para escrita em modo binário. No exemplo acima, o arquivo "arquivo.txt" é aberto para escrita em modo binário e o objeto de arquivo é atribuído à variável a. O bloco with é usado para garantir que o arquivo seja fechado automaticamente após o bloco ser executado.
    a.write(r.content)  ## O método write() é usado para escrever os bytes do conteúdo da resposta r no arquivo "arquivo.txt". O atributo content da resposta r contém o conteúdo da página em formato de bytes.

## Tratamento de erros
## Erro vai dar um erro na sua tela, enquanto a falha vai ser como unexpected, ou seja, algo que não era esperado, mas que não necessariamente é um erro. Por exemplo, se você tentar acessar um índice que não existe em uma lista, isso vai gerar um erro. Já se você tentar acessar um índice que existe, mas que tem um valor inesperado, isso pode ser considerado uma falha.

## O que são Excessões?
## Exceções são eventos que ocorrem durante a execução de um programa e que interrompem o fluxo normal do programa. Elas são usadas para lidar com situações inesperadas ou erros que podem ocorrer durante a execução do programa. Por exemplo, se você tentar acessar um índice que não existe em uma lista, isso vai gerar uma exceção do tipo IndexError. As exceções podem ser tratadas usando blocos try-except para evitar que o programa seja interrompido abruptamente e para fornecer mensagens de erro mais amigáveis ao usuário.

a = int(input("Digite um número: "))  ## O código acima tenta converter a entrada do usuário para um número inteiro usando a função int(). Se o usuário digitar algo que não pode ser convertido para um inteiro, isso vai gerar uma exceção do tipo ValueError.
b = int(input("Digite outro número: "))

resultado = a / b  ## O código acima tenta dividir o número a pelo número b. Se o usuário digitar zero para b, isso vai gerar uma exceção do tipo ZeroDivisionError.
print("O resultado da divisão é:", resultado)

## Tentando blindar o código para evitar que ele quebre quando o usuário digitar algo errado, usando blocos try-except.
try:
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    resultado = a / b
    print("O resultado da divisão é:", resultado)
except ValueError:  ## O bloco except ValueError é usado para capturar a exceção do tipo ValueError, que ocorre quando o usuário digita algo que não pode ser convertido para um inteiro. Se essa exceção ocorrer, a mensagem "Por favor, digite um número válido." será impressa na tela.
    print("Por favor, digite um número válido.")    
except ZeroDivisionError:  ## O bloco except ZeroDivisionError é usado para capturar a exceção do tipo ZeroDivisionError, que ocorre quando o usuário digita zero para b. Se essa exceção ocorrer, a mensagem "Não é possível dividir por zero." será impressa na tela.
    print("Não é possível dividir por zero.")


## Exemplo 2: 
# a = int(input("Digite um número: "))
# b = int(input("Digite outro número: "))

# if b == 0:
#     print("Não é possível dividir por zero")
# else:
#     resultado = a / b
#     print(resultado)
