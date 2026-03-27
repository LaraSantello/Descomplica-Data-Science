# Não usaremos uma biblioteca completa de RBs aqui, mas sim o princípio do Teorema de Bayes

print("\n--- Conceito de Rede Bayesiana (Atualização de Crença Bayesiana) ---")

# Cenário: Qual a probabilidade de um paciente ter uma doença rara D,
# dado que ele apresentou um sintoma S?

# 1. Probabilidades a priori (conhecimento inicial)
P_D = 0.01  # Probabilidade a priori de ter a Doença D (1%)
P_nao_D = 1 - P_D # Probabilidade de NÃO ter a Doença D (99%)

# 2. Verossimilhanças (probabilidade do sintoma dado a doença/não doença)
P_S_dado_D = 0.90 # Probabilidade de ter o Sintoma S SE tiver a Doença D (90%)
P_S_dado_nao_D = 0.05 # Probabilidade de ter o Sintoma S SE NÃO tiver a Doença D (5% - falso positivo)

# 3. Probabilidade marginal da Evidência (P(S))
# P(S) = P(S|D) * P(D) + P(S|não D) * P(não D)
P_S = (P_S_dado_D * P_D) + (P_S_dado_nao_D * P_nao_D)

# 4. Probabilidade a posteriori (P(D|S) - Nosso objetivo!)
# Usando o Teorema de Bayes: P(D|S) = [P(S|D) * P(D)] / P(S)
P_D_dado_S = (P_S_dado_D * P_D) / P_S

print(f"Probabilidade a priori de ter a doença (P(D)): {P_D:.2%}")
print(f"Probabilidade de ter o sintoma se tiver a doença (P(S|D)): {P_S_dado_D:.2%}")
print(f"Probabilidade de ter o sintoma se NÃO tiver a doença (P(S|não D)): {P_S_dado_nao_D:.2%}")
print(f"Probabilidade do sintoma ocorrer (P(S)): {P_S:.2%}")
print(f"\nProbabilidade a posteriori de ter a doença D dado o sintoma S (P(D|S)): {P_D_dado_S:.2%}")
print("Apesar do sintoma, a doença ainda é rara, mas a probabilidade aumentou bastante em relação à probabilidade a priori!")