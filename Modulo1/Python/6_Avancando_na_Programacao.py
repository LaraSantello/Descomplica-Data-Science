## Exemplo de Lista abaixo!
a = [1,2,3]
a. append(4)
print(a)

## Uma tupla é imutável, ou seja, não pode ser alterada depois de criada. Essa é a diferença entre uma lista e uma tupla. A tupla é criada usando parênteses () em vez de colchetes []. Não consigo adicionar nem excluir elementos de uma tupla depois de criada. Por exemplo: 
b = (1,2,3)
print(b)
#b.append(4) # Isso vai gerar um erro, pois tuplas não têm o método append.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
if 8 in tupla:
    print("O número 8 está presente na tupla.")
else:    
    print("O número 8 não está presente na tupla.")   ## Isso serve para quando estamos fazendo uma consulta e queremos verificar se um elemento específico está presente em uma tupla. O operador in é usado para verificar a presença do elemento na tupla, e o resultado é um valor booleano (True ou False). No exemplo acima, verificamos se o número 8 está presente na tupla e imprimimos uma mensagem correspondente. Como se fosse uma lista real/ banco de dados.

## Dicionário é um conjunto de pares chave-valor, onde cada chave é única e está associada a um valor. Ele é criado usando chaves {} e os pares chave-valor são separados por dois pontos :. Por exemplo:
dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(dicionario)
print(dicionario["nome"], dicionario["idade"])  # Acessando o valor associado à chave "nome" e "idade"

## Conceito de Conjuntos - é uma estrutura padrão que você aplica em vetores ou matrizes, ou seja, uma estrutura que você consegue aplicar em uma lista, uma tuplan, um dicionário.

a = {1,3,5,6}
b = {2,4,6}

print(set(a.intersection(b)))   # A função intersection() retorna um novo conjunto que contém apenas os elementos que estão presentes em ambos os conjuntos a e b. No exemplo acima, como não há elementos comuns entre os conjuntos a e b, o resultado será um conjunto vazio. Se houvesse elementos comuns, eles seriam incluídos no conjunto resultante.
print(set(a.difference(b)))     # A função difference() retorna um novo conjunto que contém os elementos que estão presentes no conjunto a, mas não estão presentes no conjunto b. No exemplo acima, o resultado será um conjunto contendo os elementos {1, 3, 5}, pois esses são os elementos que estão presentes no conjunto a, mas não estão presentes no conjunto b. Se houvesse elementos comuns entre os conjuntos a e b, eles seriam excluídos do conjunto resultante.
print(set(a.union(b)))    # A função union() retorna um novo conjunto que contém todos os elementos de ambos os conjuntos a e b, sem repetição. No exemplo acima, o resultado será um conjunto contendo os elementos {1, 2, 3, 4, 5, 6}.    

lista = []
for i in range(5):
    lista.append(input("Digite um número: "))
print(lista)

## Desafio: Criar uma função recursiva (ou não) para verificar se o valor "Descomplica" está presente entre um dos nomes inseridos na lista, caso o nome tenha sido inseridom exibir apenas o nome Descomplica, senão, exibir todos os nomes inseridos.
def verificar_descomplica(lista):
    if "Descomplica" in lista:
        return "Descomplica"
    else:
        return lista
nomes = []
for i in range(5):  
    nome = input("Digite um nome: ")
    nomes.append(nome)  
resultado = verificar_descomplica(nomes)
print(resultado)

#########
a = 10
b = 20
c = 30
d = 40

e = a + b + c + d

## ou

e = a + b
f = c + d
g = f + e

print(g) 