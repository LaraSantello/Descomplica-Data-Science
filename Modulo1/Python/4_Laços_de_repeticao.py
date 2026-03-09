### Laço de repetição - While
# a = 1
# while a <= 10:
#     print("Teste")
#     a = a + 1

# ## Laço de repetição - For
# a = 1
# for a in range(5):
#     print("Teste")

# a = ["Maria", "João", "Pedro", "Ana", "Lucas"]
# for a in a:
#     print(a)

# a = "Descomplica"
# for a in a:
#     print(a)

# ### Laços e variáveis
# a = []
# b = 1
# print(a)
# while b <= 3:
#     a.append(input("Digite um nome de aluno:"))
#     b = b + 1
# print(a)

# a = ["Márcio", "Bruna"]
# print(a[0])

# a.insert(0, "Maria") ## aqui conseguimos inserir um elemento em uma posição específica da lista, nesse caso, na posição 0, ou seja, no início da lista.
# print(a)

# a.remove("Bruna") ## aqui conseguimos remover um elemento específico da lista, nesse caso, o elemento "Bruna".
# print(a)

## Desafio - Desenvolver algoritmo
# Diretor cadastra alunos com os dados:
# Nome, CPF, E-mail, Matrícula - OK
# Para cada aluno cadastrado, o diretor pode lançar 3 notas - OK
# Se a média for maior ou igual a 6, escrever:
# Aluno X, você foi aprovado com a média Y, Seu diploma terá os seguintes dados: Nome, CPF, E-mail, Matrícula, Média.
# Se a média for menor que 6, o sistema vai pedir para lançar uma nota adicional e tirar nova média, somando as 4 notas e dividindo por 4. Se a média for maior ou igual a 6, escrever:
# Aluno X, você foi aprovado com a média Y, Seu diploma terá os seguintes dados: Nome, CPF, E-mail, Matrícula, Média. Senão, escrever: "Você foi reprovado, estude mais e tente novamente no próximo semestre."

# Cadastro do aluno
nome_aluno      = input("Digite o nome do aluno: ")
cpf_aluno       = input("Digite o CPF do aluno: ")
email_aluno     = input("Digite o e-mail do aluno: ")
matricula_aluno = input("Digite o número da matricula do aluno: ")

# Inserção das notas dos alunos
notas = []
for i in range(3):
    notas.append(float(input("Digite a nota do aluno: ")))
    media = sum(notas)/len(notas)
    print(f"A media do {nome_aluno} é = {media}")

# Verificação das notas
if media >= 6:
    print(f"Você foi aprovado com a {media}!. Seu diploma terá os seguintes dados: Nome: {nome_aluno}, CPF: {cpf_aluno}, E-mail: {email_aluno} e o número da matrícula: {matricula_aluno}")
else:
    nota_adicional = float(input("Digite a sua nota adicional: "))
    nova_media = (nota_adicional + media)/4
    print(nova_media)
if nova_media >= 6:
    print(f"Você foi aprovado com a {media}!. Seu diploma terá os seguintes dados: Nome: {nome_aluno}, CPF: {cpf_aluno}, E-mail: {email_aluno} e o número da matrícula: {matricula_aluno}")
else:
    print(f"Você foi reprovado com a média = {nova_media}! Estude mais e tente novamente no próximo semestre")


## Resolução de outra maneira:

# Cadastro os alunos
nome_aluno = input("Digite o nome do aluno: ")
cpf_aluno = input("Digite o CPF do aluno: ") 
email_aluno = input("Digite o e-mail do aluno: ")
matricula_aluno = input("Digite a matrícula do aluno: ")

# Lançamento das notas
notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i + 1} do aluno: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f"A média do aluno {nome_aluno} é: {media:.2f}")

# Verificação da média
if media >= 6:
    print(f"Aluno {nome_aluno}, você foi aprovado com a média {media:.2f}. Seu diploma terá os seguintes dados: Nome: {nome_aluno}, CPF: {cpf_aluno}, E-mail: {email_aluno}, Matrícula: {matricula_aluno}, Média: {media:.2f}.  ")
else:    nota_adicional = float(input("Digite a nota adicional do aluno: "))
notas.append(nota_adicional)
nova_media = sum(notas) / len(notas)
print(f"A nova média do aluno {nome_aluno} é: {nova_media:.2f}")
if nova_media >= 6:   
    print(f"Aluno {nome_aluno}, você foi aprovado com a média {nova_media:.2f}. Seu diploma terá os seguintes dados: Nome: {nome_aluno}, CPF: {cpf_aluno}, E-mail: {email_aluno}, Matrícula: {matricula_aluno}, Média: {nova_media:.2f}.  ")
else:
    print("Você foi reprovado, estude mais e tente novamente no próximo semestre.")