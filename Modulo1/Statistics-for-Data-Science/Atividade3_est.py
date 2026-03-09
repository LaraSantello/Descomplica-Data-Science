import random
import pandas as pd # Ótima para manipular dados e fazer amostragem
import numpy as np   # Para cálculos estatísticos como média, desvio padrão

print("--- Método Estatístico: Da Coleta à Análise ---")

# --- 1. Coleta de Dados (Simulada) ---
# Vamos simular uma população de "alunos" com suas notas e cursos.
# Imagine que estes são todos os alunos de uma pequena faculdade.
populacao_alunos = pd.DataFrame({
    'ID': range(1, 101),
    'Curso': ['Engenharia'] * 30 + ['Medicina'] * 40 + ['Direito'] * 30,
    'Nota_Final': np.random.randint(50, 101, 100) # Notas de 50 a 100
})

print("1. Coleta de Dados: Nossa População Simulada (primeiras 5 linhas)")
print(populacao_alunos.head())
print(f"\nTamanho total da população: {len(populacao_alunos)} alunos")
print(f"Distribuição de cursos na população:\n{populacao_alunos['Curso'].value_counts()}")

# --- 2. Organização e Apresentação dos Dados ---
# Já estamos usando um DataFrame (organizado). Vamos ver uma apresentação básica.
print("\n2. Organização e Apresentação de Dados:")
print("\nDescrição estatística básica da nota final na população:")
print(populacao_alunos['Nota_Final'].describe()) # Média, desvio padrão, min, max, quartis

# --- 3. Análise dos Dados (Estatística Descritiva e Amostragem) ---
# Vamos agora aplicar técnicas de amostragem e depois análises descritivas nas amostras.

print("\n--- Técnicas de Amostragem ---")

# --- 3.1. Amostragem Aleatória Simples (AAS) ---
# Cada aluno tem a mesma chance de ser selecionado.
tamanho_amostra_aas = 20
amostra_aas = populacao_alunos.sample(n=tamanho_amostra_aas, random_state=42) # random_state para reprodutibilidade

print(f"\n3.1. Amostra Aleatória Simples (n={tamanho_amostra_aas}):")
print(amostra_aas.head())
print(f"Média da Nota Final na Amostra AAS: {amostra_aas['Nota_Final'].mean():.2f}")
print(f"Distribuição de cursos na Amostra AAS:\n{amostra_aas['Curso'].value_counts()}")
print(f"(A distribuição de cursos pode não ser proporcional à população na AAS)")

# --- 3.2. Amostragem Estratificada ---
# Garante que cada "estrato" (grupo, no caso, Curso) seja proporcionalmente representado.
# Queremos uma amostra de 20 alunos, mantendo a proporção dos cursos.
# Calculamos a proporção de cada curso na população e aplicamos na amostra.
# Exemplo: 30% Engenharia, 40% Medicina, 30% Direito

# --- 3.2. Amostragem Estratificada ---

amostra_estratificada = pd.concat([
    populacao_alunos[populacao_alunos['Curso'] == 'Engenharia'].sample(n=6, random_state=42),
    populacao_alunos[populacao_alunos['Curso'] == 'Medicina'].sample(n=8, random_state=42),
    populacao_alunos[populacao_alunos['Curso'] == 'Direito'].sample(n=6, random_state=42)
])

print(f"\n3.2. Amostra Estratificada (n={len(amostra_estratificada)}):")
print(amostra_estratificada.head())
print(f"Média da Nota Final na Amostra Estratificada: {amostra_estratificada['Nota_Final'].mean():.2f}")
print(f"Distribuição de cursos na Amostra Estratificada:\n{amostra_estratificada['Curso'].value_counts(normalize=True)}")

# --- 4. Interpretação dos Resultados ---
print("\n--- 4. Interpretação dos Resultados ---")
print(f"Média da Nota Final da População Inteira: {populacao_alunos['Nota_Final'].mean():.2f}")
print(f"Média da Nota Final da Amostra AAS: {amostra_aas['Nota_Final'].mean():.2f}")
print(f"Média da Nota Final da Amostra Estratificada: {amostra_estratificada['Nota_Final'].mean():.2f}")

print("\nObservação:")
print("- A média da amostra (estatística) é uma estimativa da média da população (parâmetro).")
print("- A amostra estratificada geralmente fornece uma estimativa mais precisa se houver grupos importantes na população que você quer garantir que sejam representados.")
print("- A AAS é mais simples, mas pode não capturar bem a diversidade da população em amostras pequenas.")