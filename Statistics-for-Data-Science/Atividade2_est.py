import matplotlib
matplotlib.use('Agg')  # Isso diz ao Python para não tentar abrir uma janela visual
import matplotlib.pyplot as plt # Para criar gráficos (histograma)
import collections # Para contar frequências de dados qualitativos
import numpy as np # Para cálculos numéricos (média, desvio padrão)


print("--- Tipos de Dados Estatísticos ---")

# --- 1. Dados Qualitativos (Categóricos) ---
# Representam qualidades ou categorias.

# 1.1. Dados Qualitativos Nominais (sem ordem)
cores_favoritas = ["Azul", "Verde", "Vermelho", "Azul", "Amarelo", "Verde", "Azul", "Vermelho"]
print("\n1.1. Dados Qualitativos Nominais (Ex: Cores Favoritas)")
print(f"Dados: {cores_favoritas}")

# Estatística Descritiva para dados nominais: Contagem de Frequência (Moda)
frequencia_cores = collections.Counter(cores_favoritas)
print(f"Frequência das cores: {frequencia_cores}")
print(f"Moda (cor mais comum): {frequencia_cores.most_common(1)[0][0]}")

# 1.2. Dados Qualitativos Ordinais (com ordem)
niveis_satisfacao = ["Bom", "Ruim", "Excelente", "Bom", "Regular", "Excelente", "Ruim"]
print("\n1.2. Dados Qualitativos Ordinais (Ex: Níveis de Satisfação)")
print(f"Dados: {niveis_satisfacao}")

# Para ordinais, podemos ordenar para ver a distribuição, mas a média não faz sentido.
# A moda ainda é útil.
frequencia_satisfacao = collections.Counter(niveis_satisfacao)
print(f"Frequência dos níveis: {frequencia_satisfacao}")
print(f"Moda (nível mais comum): {frequencia_satisfacao.most_common(1)[0][0]}")


# --- 2. Dados Quantitativos (Numéricos) ---
# Representam quantidades e podem ser medidos ou contados.

# 2.1. Dados Quantitativos Discretos (contagens, geralmente inteiros)
numero_filhos = [0, 1, 2, 1, 3, 0, 1, 2, 1, 0, 2]
print("\n2.1. Dados Quantitativos Discretos (Ex: Número de Filhos)")
print(f"Dados: {numero_filhos}")

# 2.2. Dados Quantitativos Contínuos (medições, podem ter decimais)
alturas_cm = [175.5, 168.2, 180.0, 172.1, 165.9, 178.5, 170.0, 181.3]
print("\n2.2. Dados Quantitativos Contínuos (Ex: Alturas em cm)")
print(f"Dados: {alturas_cm}")


print("\n--- Tipos de Estatística: Estatística Descritiva em Ação ---")
# A Estatística Descritiva resume e organiza os dados.

# Usando dados quantitativos (alturas) para demonstrar medidas descritivas
dados_para_analise = np.array(alturas_cm)

# Medidas de Tendência Central (onde os dados se concentram)
media = np.mean(dados_para_analise)
mediana = np.median(dados_para_analise)

# A moda para dados contínuos pode ser complexa, mas para dados discretos é mais simples.
# Para este exemplo, vamos simplificar a moda para o valor mais frequente.
from scipy import stats
try:
    moda = stats.mode(dados_para_analise)[0][0] # Pega o primeiro valor da moda, se houver
except IndexError: # Caso não haja moda única
    moda = "Não aplicável ou múltiplos valores"

print(f"\nEstatística Descritiva para Alturas:")
print(f"Média: {media:.2f} cm")
print(f"Mediana: {mediana:.2f} cm")
print(f"Moda: {moda}") # A moda pode ser menos relevante para dados contínuos

# Medidas de Dispersão (quão espalhados os dados estão)
desvio_padrao = np.std(dados_para_analise)
amplitude = np.max(dados_para_analise) - np.min(dados_para_analise)

print(f"Desvio Padrão: {desvio_padrao:.2f} cm")
print(f"Amplitude: {amplitude:.2f} cm")

# Visualização de Dados (Histograma) - Uma ferramenta descritiva
plt.figure(figsize=(8, 5))
plt.hist(dados_para_analise, bins=4, edgecolor='black', alpha=0.7, color='purple')
plt.title('Histograma das Alturas (cm)')
plt.xlabel('Altura (cm)')
plt.ylabel('Frequência')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label=f'Média: {media:.2f}')
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.savefig('hist_ativ2.png')


## Estatística Inferencial (Conceito)
## A Estatística Inferencial vai além da descrição. Ela usa dados de uma amostra para fazer generalizações e previsões sobre uma **população** maior.
## Por exemplo, se tivéssemos medido a altura de apenas 100 pessoas e quiséssemos estimar a altura média de todos os brasileiros, isso seria um trabalho de estatística inferencial.
## Ela envolve conceitos mais avançados como testes de hipóteses e intervalos de confiança, que permitem tirar conclusões com um certo nível de certeza, mesmo sem ter todos os dados da população.