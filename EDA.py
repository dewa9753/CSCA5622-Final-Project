import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from lib.settings import DATA_ROOT

if __name__ == '__main__':
    df = pd.read_csv(f'{DATA_ROOT}/final_data.csv')

    """
    print("Description of numerical features:")
    print(df[['q1','q2','q3']].describe())
    """

    """
    print("Building boxplot of driverId vs gridPosition")
    sns.boxplot(data=df, x='driverId', y='gridPosition')
    plt.show()
    """

    """
    print("Showing pairplot of q1, q2, and q3 (all numerical variables) with hue of finalPosition")
    sns.pairplot(df, vars=['q1','q2','q3'], hue='finalPosition')
    plt.show()
    """

    """
    print("Showing histogram plot of finalPosition vs constructorPosition")
    sns.histplot(df, x='constructorPosition', y='finalPosition')
    plt.show()
    """
    
    """
    print("Showing correlation matrix of features.")
    sns.heatmap(df.corr(), annot=True, cmap='cool', fmt='.2f')
    plt.show()
    """
