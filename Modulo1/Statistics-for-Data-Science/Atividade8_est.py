import numpy as np
import random

print("--- Simulação de um Modelo de Markov: Previsão do Tempo ---")

# 1. Definir os Estados
estados = ['Sol', 'Nublado', 'Chuva']
print(f"Estados possíveis do tempo: {estados}")

# 2. Definir a Matriz de Transição
# As linhas somam 1.0 (probabilidades de sair de um estado)
# Matriz de Transição (Probabilidade de ir de [linha] para [coluna])
#           Sol  Nublado  Chuva
transicoes = {
    'Sol':     {'Sol': 0.7, 'Nublado': 0.2, 'Chuva': 0.1},
    'Nublado': {'Sol': 0.3, 'Nublado': 0.4, 'Chuva': 0.3},
    'Chuva':   {'Sol': 0.2, 'Nublado': 0.3, 'Chuva': 0.5}
}

print("\nMatriz de Transição (Prob. de ir de [linha] para [coluna]):")
for estado, prob in transicoes.items():
    print(f"De {estado}: {prob}")

# 3. Definir o Estado Inicial (onde estamos começando)
estado_atual = random.choice(estados) # Começa aleatoriamente
# Ou podemos fixar: estado_atual = 'Sol'
print(f"\nComeçando com o tempo: {estado_atual}")

# 4. Simular a Sequência de Eventos
num_dias = 10 # Quantos dias queremos simular
historico_tempo = [estado_atual]

print(f"\nPrevisão do tempo para os próximos {num_dias} dias:")

for dia in range(num_dias):
    # Obter as probabilidades de transição do estado_atual
    proximas_probabilidades = transicoes[estado_atual]

    # Obter os possíveis próximos estados e suas probabilidades
    proximos_estados = list(proximas_probabilidades.keys())
    probabilidades = list(proximas_probabilidades.values())

    # Escolher o próximo estado com base nas probabilidades
    proximo_estado = random.choices(proximos_estados, weights=probabilidades, k=1)[0]

    historico_tempo.append(proximo_estado)
    estado_atual = proximo_estado # Atualiza o estado para a próxima iteração

print(f"Sequência de tempo simulada: {historico_tempo}")

print("\n--- Analisando Frequências na Simulação ---")
from collections import Counter
frequencias_simuladas = Counter(historico_tempo)
print(f"Frequência de ocorrência dos estados na simulação: {frequencias_simuladas}")