import numpy as np
from scipy import stats

def calculate_confidence_interval(data):
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    ci_lower, ci_upper = stats.norm.interval(0.95, loc=mean, scale=std/np.sqrt(len(data)))
    return mean, ci_lower, ci_upper

def generate_statistical_report(df):
    features = df.columns[:-1]  # todas as colunas menos species
    species_list = df['species'].unique()

    for feature in features:
        print(f"\n📈 {feature}")
        for species in species_list:
            data = df[df['species'] == species][feature]
            mean, ci_lower, ci_upper = calculate_confidence_interval(data)
            print(f"  {species:>10}: média = {mean:.2f}, IC 95% = [{ci_lower:.2f}, {ci_upper:.2f}]")

        # teste ANOVA para ver se há diferença significativa entre espécies
        groups = [df[df['species'] == s][feature] for s in species_list]
        f_stat, p_value = stats.f_oneway(*groups)
        print(f"  → ANOVA F={f_stat:.3f}, p={p_value:.5f}")
        if p_value < 0.05:
            print("    Diferença estatisticamente significativa entre as espécies")
        else:
            print("    Sem diferença significativa")
