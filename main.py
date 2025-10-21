from avltree import AvlTree
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from scipy.stats import norm
from statistics_analysis import generate_statistical_report
from visualization import plot_confidence_intervals, plot_correlation_heatmap, plot_species_distributions


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
    return np.mean(row[iris.feature_names])


# -----------------------------
# Criar árvores AVL
# -----------------------------
species_trees = {s: AvlTree() for s in df['species'].unique()}

for index, row in df.iterrows():
    species = row['species']
    composite_index = calculate_composite_index(row)
    species_trees[species].insert(composite_index, index)


# -----------------------------
# Análise estatística com SciPy
# -----------------------------
print("\n=== Relatório Estatístico ===")
generate_statistical_report(df)


# -----------------------------
# Visualizações
# -----------------------------
plot_confidence_intervals(df)
plot_correlation_heatmap(df)
plot_species_distributions(df)


# -----------------------------
# Estrutura das Árvores
# -----------------------------
print("\n=== Estrutura das Árvores AVL ===")
for species, tree in species_trees.items():
    print(f"{species}: Altura = {tree.height()}, Nós = {tree.size()}")
