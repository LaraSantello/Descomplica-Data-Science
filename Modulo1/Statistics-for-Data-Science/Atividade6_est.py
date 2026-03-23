import pandas as pd
import matplotlib.pyplot as plt
import numpy as np # Para gerar dados contínuos de exemplo

# Dados de exemplo: Notas dos alunos (dados quantitativos discretos)
notas = [7, 8, 6, 7, 9, 5, 7, 8, 6, 7, 5, 7, 8, 9, 6, 7, 8, 6, 7, 8]

print("--- 1. Distribuição de Frequências ---")

# Criando uma Series Pandas para facilitar o cálculo das frequências
series_notas = pd.Series(notas)

# Frequência Absoluta: Contagem de cada nota
frequencia_absoluta = series_notas.value_counts().sort_index()
print("Frequência Absoluta:\n", frequencia_absoluta)

# Frequência Relativa: Proporção de cada nota
frequencia_relativa = series_notas.value_counts(normalize=True).sort_index()
print("\nFrequência Relativa:\n", frequencia_relativa)

# Frequência Acumulada Absoluta: Soma progressiva das frequências absolutas
frequencia_acumulada_absoluta = frequencia_absoluta.cumsum()
print("\nFrequência Acumulada Absoluta:\n", frequencia_acumulada_absoluta)

# Frequência Acumulada Relativa: Soma progressiva das frequências relativas
frequencia_acumulada_relativa = frequencia_relativa.cumsum()
print("\nFrequência Acumulada Relativa:\n", frequencia_acumulada_relativa)

# Criando um DataFrame para a tabela de frequências completa e formatada
df_frequencias = pd.DataFrame({
    'Frequência Absoluta (f)': frequencia_absoluta,
    'Frequência Relativa (fr)': frequencia_relativa.map('{:.2%}'.format), # Formata como porcentagem
    'Frequência Acumulada (F)': frequencia_acumulada_absoluta,
    'Frequência Acumulada Relativa (Fr)': frequencia_acumulada_relativa.map('{:.2%}'.format)
})
print("\nTabela de Frequências Completa:\n", df_frequencias)

print("\n--- 2. Representação Gráfica ---")

# Gráfico de Barras (para notas - dados quantitativos discretos, tratado como categorias neste caso)
plt.figure(figsize=(8, 5))
frequencia_absoluta.plot(kind='bar', color='skyblue')
plt.title('Frequência de Notas dos Alunos')
plt.xlabel('Nota')
plt.ylabel('Frequência Absoluta')
plt.xticks(rotation=0) # Mantém os rótulos do eixo X retos
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de Setores (Pizza) - para dados categóricos/discretos com poucas opções
plt.figure(figsize=(8, 8))
frequencia_absoluta.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribuição Percentual das Notas')
plt.ylabel('') # Remove o rótulo do eixo Y que o Pandas adiciona por padrão
plt.show()

# Histograma (para dados quantitativos contínuos)
# Gerando dados de exemplo para alturas, que são contínuos
np.random.seed(42) # Para resultados reprodutíveis
dados_altura = np.random.normal(170, 10, 1000) # Média 170cm, desvio padrão 10cm, 1000 observações

plt.figure(figsize=(10, 6))
plt.hist(dados_altura, bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
plt.title('Histograma de Alturas (cm)')
plt.xlabel('Altura (cm)')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de Linhas (para dados ao longo do tempo ou ordem)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [150, 180, 220, 190, 250, 230]

plt.figure(figsize=(9, 5))
plt.plot(meses, vendas, marker='o', linestyle='-', color='purple')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Número de Vendas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()