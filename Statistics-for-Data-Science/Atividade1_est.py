import random # Módulo para funções aleatórias

# --- 1. Definindo a População ---
# Vamos imaginar uma população de 15 "notas de alunos".
# Esta é a nossa população completa de interesse.
populacao_notas = [6.5, 7.0, 8.0, 5.5, 9.0, 7.5, 6.0, 8.5, 7.0, 9.5, 6.0, 5.0, 7.0, 8.0, 9.0]

print("--- Nossa População ---")
print(f"População de notas: {populacao_notas}")
print(f"Tamanho da população: {len(populacao_notas)}")

# Calculando a média da população (um Parâmetro)
media_populacao = sum(populacao_notas) / len(populacao_notas)
print(f"Média da população (Parâmetro): {media_populacao:.2f}")

# --- 2. Tirando uma Amostra ---
# Agora, vamos selecionar uma pequena parte dessa população para estudar.
# Vamos tirar uma amostra aleatória de 5 notas.
tamanho_amostra = 7

# Usamos random.sample() para escolher notas aleatoriamente da população.
# 'random.sample(lista, k)' escolhe 'k' itens únicos da 'lista'.
amostra_notas = random.sample(populacao_notas, tamanho_amostra)

print("\n--- Nossa Amostra ---")
print(f"Amostra de notas: {amostra_notas}")
print(f"Tamanho da amostra: {len(amostra_notas)}")

# Calculando a média da amostra (uma Estatística)
media_amostra = sum(amostra_notas) / len(amostra_notas)
print(f"Média da amostra (Estatística): {media_amostra:.2f}")

# --- 3. Comparando População e Amostra ---
print("\n--- Comparação ---")
print(f"Média da População (Parâmetro): {media_populacao:.2f}")
print(f"Média da Amostra (Estatística): {media_amostra:.2f}")
print(f"Diferença entre as médias: {(media_amostra - media_populacao):.2f}")

## Observe como a média da amostra é uma estimativa da média da população, mas geralmente não é idêntica a ela.
## Quanto maior a amostra (e se for bem selecionada), mais próxima ela tende a ser da população.