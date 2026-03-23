import numpy as np # Para cálculos numéricos
import pandas as pd # Para Series e DataFrames (ótimo para tabelas)
import collections # Para a moda (dados não numéricos ou para contagem)
import random # Para simulações de probabilidade

print("--- Medidas de Posição em Python ---")

# Dados de exemplo: Pontuações em um jogo (de 0 a 100)
pontuacoes = [85, 92, 78, 88, 95, 70, 80, 90, 85, 75, 92, 85, 60, 99, 88]

# Convertendo para uma Series do Pandas para facilitar os cálculos
s_pontuacoes = pd.Series(pontuacoes)
print("Pontuacoes")
print(s_pontuacoes)

# 1. Média Aritmética
media_pontuacoes = s_pontuacoes.mean()
print(f"1. Média das pontuações: {media_pontuacoes:.2f}")

# 2. Mediana
mediana_pontuacoes = s_pontuacoes.median()
print(f"2. Mediana das pontuações: {mediana_pontuacoes:.2f}")

# 3. Moda
# collections.Counter é útil para encontrar a moda, especialmente se houver múltiplas modas
contagem_pontuacoes = collections.Counter(pontuacoes)
# A moda(s) são os valores com a maior contagem.
max_frequencia = max(contagem_pontuacoes.values())
modas = [valor for valor, frequencia in contagem_pontuacoes.items() if frequencia == max_frequencia]

if len(modas) == len(pontuacoes): # Todos os valores aparecem apenas uma vez
    print("3. Moda das pontuações: Nenhuma moda (todos os valores são únicos)")
elif len(modas) > 1:
    print(f"3. Moda das pontuações (bimodal/multimodal): {modas}")
else:
    print(f"3. Moda das pontuações: {modas[0]}")

# 4. Quartis e Percentis
q1 = s_pontuacoes.quantile(0.25)
q2 = s_pontuacoes.quantile(0.50) # Mediana
q3 = s_pontuacoes.quantile(0.75)
p90 = s_pontuacoes.quantile(0.90) # 90º Percentil

print(f"\n4. Quartis e Percentis:")
print(f"   Primeiro Quartil (Q1 - 25%): {q1:.2f}")
print(f"   Segundo Quartil (Q2 - 50% / Mediana): {q2:.2f}")
print(f"   Terceiro Quartil (Q3 - 75%): {q3:.2f}")
print(f"   90º Percentil (P90): {p90:.2f}")

# O método describe() do Pandas já mostra várias dessas medidas juntas
print("\nResumo das medidas de posição (e dispersão) com .describe():")
print(s_pontuacoes.describe())

print("\n--- Introdução à Probabilidade em Python (Simulação) ---")

# --- Exemplo 1: Lançamento de uma Moeda ---
# Espaço Amostral: {'Cara', 'Coroa'}
# Evento: Obter 'Cara'

num_lancamentos = 1500 # Quantas vezes vamos lançar a moeda
resultados = []

for _ in range(num_lancamentos):
    resultado = random.choice(['Cara', 'Coroa'])
    resultados.append(resultado)

# Contar a frequência de 'Cara'
contagem_caras = resultados.count('Cara')
probabilidade_cara_simulada = contagem_caras / num_lancamentos

print("\nExemplo 1: Lançamento de Moeda (Simulação)")
print(f"Número de lançamentos: {num_lancamentos}")
print(f"Número de 'Caras' obtidas: {contagem_caras}")
print(f"Probabilidade simulada de 'Cara': {probabilidade_cara_simulada:.2f} (Esperado: 0.50)")
print("Quanto maior o número de lançamentos, mais a probabilidade simulada se aproxima da teórica (Lei dos Grandes Números).")


# --- Exemplo 2: Rolagem de um Dado ---
# Espaço Amostral: {1, 2, 3, 4, 5, 6}
# Evento: Obter um número par ({2, 4, 6})

num_rolagens =1500 # Quantas vezes vamos rolar o dado
resultados_dado = []

for _ in range(num_rolagens):
    resultado = random.randint(1, 6) # Rola um dado de 6 faces
    resultados_dado.append(resultado)

# Contar quantos resultados são pares
contagem_pares = sum(1 for num in resultados_dado if num % 2 == 0)
probabilidade_par_simulada = contagem_pares / num_rolagens

print("\nExemplo 2: Rolagem de Dado (Simulação)")
print(f"Número de rolagens: {num_rolagens}")
print(f"Número de resultados pares: {contagem_pares}")
print(f"Probabilidade simulada de obter um número par: {probabilidade_par_simulada:.2f} (Esperado: 0.50)")