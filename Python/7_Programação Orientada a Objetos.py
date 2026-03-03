## Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de objetos, que são instâncias de classes. Uma classe é um modelo ou uma estrutura que define as características e comportamentos de um objeto. A POO permite criar código mais modular, reutilizável e fácil de manter, além de ter segurança de que não vai alterar tudo quando for mexendo nos códigos. Em Python, a POO é amplamente utilizada e é uma parte fundamental da linguagem. A seguir, vamos explorar os conceitos básicos da POO em Python, incluindo classes, objetos, atributos e métodos.

## Definindo uma classe em Python
class Pessoa:
    nome = ""
    idade = 0
    cpf = ""
    email = ""

    ## atributos são variáveis
    ## métodos são funções

    def exibir(self):  ## função self - use o valor da própria classe, ou seja, o valor do nome da própria pessoa
        print(self.nome)

## Criando um objeto a partir da classe Pessoa
pessoa1 = Pessoa()
pessoa1.nome = "João"
pessoa1.idade = 30
pessoa1.cpf = "123.456.789-00"
pessoa1.email = "joao@email.com"

pessoa1.exibir()    ## Isso vai imprimir o nome da pessoa, que é "João". O método exibir() acessa o atributo nome da instância pessoa1 usando self.nome e imprime seu valor.

## Getter e Setter são métodos usados para acessar e modificar os atributos de um objeto. O Getter é usado para obter o valor de um atributo, enquanto o Setter é usado para definir ou modificar o valor de um atributo.
# Getter e Setter são importantes para encapsular os dados de um objeto, permitindo que você controle como os atributos são acessados e modificados. Por exemplo, você pode usar um Setter para validar os dados antes de atribuí-los a um atributo, garantindo que o objeto esteja sempre em um estado válido.

def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    print(self.nome, self.idade)

## O método __init__ é um método especial em Python que é chamado automaticamente quando um objeto é criado a partir de uma classe. Ele é usado para inicializar os atributos do objeto. No exemplo acima, o método __init__ recebe dois parâmetros, nome e idade, e atribui esses valores aos atributos self.nome e self.idade do objeto. Além disso, ele imprime o nome e a idade do objeto quando ele é criado.

## @property é um decorador em Python que é usado para criar métodos getter e setter de forma mais elegante e fácil de usar. Ele permite que você defina um método como uma propriedade, o que significa que você pode acessar o método como se fosse um atributo, sem precisar chamar explicitamente o método. Por exemplo:
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo privado
        self._idade = idade  # Atributo privado

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, valor):
        self._idade = valor 
## No exemplo acima, a classe Pessoa tem dois atributos privados, _nome e _idade. O decorador @property é usado para criar métodos getter para ambos os atributos, permitindo que você acesse o nome e a idade como se fossem atributos normais. O decorador @nome.setter e @idade.setter são usados para criar métodos setter, permitindo que você defina o valor do nome e da idade de forma elegante. Por exemplo:
pessoa1 = Pessoa("João", 30)
print(pessoa1.nome)  # Acessando o nome usando o getter
pessoa1.nome = "Maria"  # Modificando o nome usando o setter
print(pessoa1.nome)  # Acessando o nome novamente para verificar a modificação

## Encapsulamento é um princípio da programação orientada a objetos que consiste em ocultar os detalhes internos de um objeto e fornecer uma interface pública para interagir com ele. Isso ajuda a proteger os dados do objeto e a garantir que ele seja usado de maneira correta. Em Python, o encapsulamento é implementado usando atributos privados (prefixados com um underscore) e métodos públicos (sem prefixo). Por exemplo:

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo privado
        self._idade = idade  # Atributo privado

    def exibir_informacoes(self):  # Método público
        print(f"Nome: {self._nome}, Idade: {self._idade}")
## No exemplo acima, os atributos _nome e _idade são privados, o que significa que eles não podem ser acessados diretamente de fora da classe. 

## Texto Aula 7 - Programação Orientada a Objetos (POO) em Python
# A Programação Orientada a Objetos (POO) é um paradigma de programação que permite estruturar o código em torno de objetos, que são instâncias de classes. As classes, por sua vez, são como moldes que definem as características (atributos) e comportamentos (métodos) dos objetos. Essa abordagem oferece diversas vantagens, como a reutilização de código e o encapsulamento, que protege as informações dentro dos objetos.
# Em Python, a criação de uma classe se dá pela palavra-chave 'class', seguida do nome da classe, que por convenção, deve iniciar com letra maiúscula. Dentro da classe, definimos os atributos, que são as variáveis que armazenam os dados do objeto, e os métodos, que são as funções que definem o comportamento do objeto.
# Os métodos são como funções que operam sobre os dados do objeto. O primeiro parâmetro de um método é sempre 'self', que referencia o próprio objeto. Através do 'self', podemos acessar os atributos e outros métodos da classe.
# O método construtor, definido pela palavra-chave '__init__', é um método especial que é chamado automaticamente quando um objeto da classe é criado. Ele é usado para inicializar os atributos do objeto com valores.
# O encapsulamento é um conceito importante em POO que visa proteger os dados do objeto, controlando o acesso aos seus atributos. Em Python, o encapsulamento não é tão rígido como em outras linguagens, mas podemos usar convenções para indicar a visibilidade dos atributos. Por exemplo, um atributo precedido por um único underscore ('_') é considerado protegido, enquanto um atributo precedido por dois underscores ('__') é considerado privado.
# Getters e setters são métodos especiais que permitem acessar e modificar os atributos de um objeto de forma controlada. Os getters são usados para obter o valor de um atributo, enquanto os setters são usados para definir o valor de um atributo.
# A herança é um mecanismo poderoso da POO que permite criar novas classes a partir de classes existentes, herdando seus atributos e métodos. A classe que herda é chamada de classe filha ou subclasse, enquanto a classe que está sendo herdada é chamada de classe pai ou superclasse.
# A herança permite reutilizar código e criar hierarquias de classes, onde as classes filhas herdam características e comportamentos das classes pais, podendo especializar ou estender suas funcionalidades.
# A POO é um paradigma poderoso que pode ser aplicado em projetos de todos os portes, proporcionando uma forma organizada e eficiente de estruturar o código, facilitando a manutenção e a reutilização. A prática e a experimentação são essenciais para dominar os conceitos da POO e aplicar esse paradigma de forma eficiente no desenvolvimento de software.