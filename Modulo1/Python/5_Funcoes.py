## Uma função em Python é um bloco de código organizado e reutilizável que realiza uma tarefa específica, definido pela palavra-chave def. Elas permitem modularizar programas, evitar repetição de código, aumentar a legibilidade e facilitar a manutenção. Funções podem receber parâmetros de entrada e retornar valores.

def soma():
    txt = "imprimindo função na tela: "
    return  txt
print(soma())

### Segundo exemplo
def soma(a, b):
    c = a + b
    if c % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
print(soma(4,9)) 
print(soma(6,7))
print(soma(23,8))
print(soma(71,9)) ## Se eu não tivesse a função, eu teria que colocar a função, para cada número que eu fizesse

## Funções recursivas - Exemplos práticos
## Fatorial
# Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120

def fatorial (n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(fatorial(5))
print(fatorial(6))
print(fatorial(8))

## Desafio 1: Fazer o sistema de verificação de maioridade usando funções
def maioridade(idade):
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
maioridade(20)
maioridade(17)

## Desafio 2: Fazer uma contagem de 0 a 10 usando recursão
def contagemp (n):
    if n > 10:
        return
    else:
        print(n)
        contagemp(n + 1)
    
## Desafio 3: Fazer a contagem de 10 a 0 usando recursão
def contagemregressiva(n):
    if n < 0:
        return
    else:
        print(n)
        contagemregressiva(n - 1)

### 
def f(a,b,c):
    v = a * b * c
    return v
print(f(1,2,3))
