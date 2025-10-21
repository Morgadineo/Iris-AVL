import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statistics_analysis import calculate_confidence_interval

def plot_confidence_intervals(df):
    plt.figure(figsize=(8,5))
    features = ['petal length (cm)', 'petal width (cm)', 'sepal length (cm)', 'sepal width (cm)']
    species = df['species'].unique()

    for i, feature in enumerate(features):
        means, lowers, uppers = [], [], []
        for sp in species:
            data = df[df['species'] == sp][feature]
            mean, ci_low, ci_up = calculate_confidence_interval(data)
            means.append(mean)
            lowers.append(ci_low)
            uppers.append(ci_up)
        plt.errorbar(species, means, yerr=[np.subtract(means, lowers), np.subtract(uppers, means)],
                     fmt='o', label=feature, capsize=4)

    plt.title("Intervalos de confiança (95%) por espécie e atributo")
    plt.ylabel("Média com IC95%")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df):
    plt.figure(figsize=(6,5))
    corr = df.iloc[:, :-1].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlação entre características")
    plt.tight_layout()
    plt.show()


def plot_species_distributions(df):
    plt.figure(figsize=(10,6))
    sns.pairplot(df, hue="species", diag_kind="kde")
    plt.suptitle("Distribuição das espécies (Iris Dataset)", y=1.02)
    plt.show()
