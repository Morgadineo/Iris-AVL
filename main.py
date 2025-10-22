# main.py
from avltree import AvlTree
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from scipy import stats

# -----------------------------
# Função para calcular média e intervalo de confiança para qualquer conjunto de dados
# -----------------------------
def calculate_confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    ci_lower, ci_upper = stats.norm.interval(confidence, loc=mean, scale=std/np.sqrt(len(data)))
    return mean, ci_lower, ci_upper

# -----------------------------
# Carregar e preparar o conjunto Iris
# -----------------------------
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# -----------------------------
# Função para índice composto
# -----------------------------
def calculate_composite_index(row):
    """Calcula a média das quatro características do conjunto Iris."""
    return np.mean(row[iris.feature_names])

# -----------------------------
# Aplica a função a cada espécie do Iris para obter média e IC
# -----------------------------
print("\n=== Intervalos de Confiança por Espécie ===")
species_stats = {}  # armazena média e IC para cada espécie

for species in df['species'].unique():
    data = df[df['species'] == species][iris.feature_names].mean(axis=1)
    mean, ci_lower, ci_upper = calculate_confidence_interval(data)
    species_stats[species] = (mean, ci_lower, ci_upper)
    print(f"{species:>10}: média = {mean:.3f}, IC95% = [{ci_lower:.3f}, {ci_upper:.3f}]")

# -----------------------------
# Função de classificação baseada nos ICs
# -----------------------------
def classify_with_confidence_intervals(row, stats_summary):
    """Classifica uma amostra com base no intervalo de confiança do índice composto."""
    composite_index = calculate_composite_index(row)
    for species, (mean, ci_lower, ci_upper) in stats_summary.items():
        if ci_lower <= composite_index <= ci_upper:
            return species
    return "unknown"

# -----------------------------
# Criar árvores AVL e classificar por media e IC
# -----------------------------
species_trees = {s: AvlTree() for s in df['species'].unique()}
unknown_tree = AvlTree()

for index, row in df.iterrows():
    predicted_species = classify_with_confidence_intervals(row, species_stats)
    composite_index = calculate_composite_index(row)
    
    if predicted_species in species_trees:
        species_trees[predicted_species].insert(composite_index, index)
    else:
        unknown_tree.insert(composite_index, index)


# -----------------------------
# Estrutura das Árvores
# -----------------------------
print("\n=== Estrutura das Árvores AVL ===")
for species, tree in species_trees.items():
    print(f"{species}: Altura = {tree.height()}, Nós = {tree.size()}")
print("\n Classificação e análise concluídas!")