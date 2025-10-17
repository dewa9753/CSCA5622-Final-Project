import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from lib.settings import DATA_ROOT

if __name__ == '__main__':
    df = pd.read_csv(f'{DATA_ROOT}/final_data.csv')

    """
    print("Description of numerical features:")
    print(df[['q1','q2','q3', 'prevFinalTime', 'prevFastestLapTime']].describe())

    print("Showing pairplot of all numerical variables with hue of finalPosition")
    sns.pairplot(df, vars=['q1','q2','q3', 'prevFinalTime', 'prevFastestLapTime'], hue='finalPosition')
    plt.show()

    print("Plotting prevFinalTime vs finalPosition")
    sns.scatterplot(data=df, x='finalPosition', y='prevFinalTime')
    plt.show()

    print("Showing histogram plot of finalPosition vs constructorPosition")
    sns.histplot(df, x='constructorPosition', y='finalPosition')
    plt.show()

    print("Showing correlation matrix of all features.")
    sns.heatmap(df.corr(), annot=True, cmap='cool', fmt='.2f')
    plt.show()
    
    print("Showing contingency table between driverId and finalPosition")
    sns.heatmap(pd.crosstab(df['driverId'], df['finalPosition']))
    plt.show()
    print("Showing contingency table between constructorPosition and finalPosition")
    sns.heatmap(pd.crosstab(df['constructorPosition'], df['finalPosition']))
    plt.show()

    print("Showing contingency table between gridPosition and finalPosition")
    sns.heatmap(pd.crosstab(df['gridPosition'], df['finalPosition']))
    plt.show()

    print("Showing contingency table between constructorId and finalPosition")
    sns.heatmap(pd.crosstab(df['constructorId'], df['finalPosition']))
    plt.show()
    """
    print("Seeing how much of the data I can keep. I need the value_counts to be reasonably high for each category in finalPosition.")
    val_counts = df['finalPosition'].value_counts().sort_index()
    print(val_counts)
    sns.barplot(x=val_counts.index, y=val_counts.values)
    plt.show()

    print("Removing rows with finalPosition > 12 to keep more data per category.")
    df = df[df['finalPosition'] <= 12]

    # EDA showed that q3 is the best choice out of the q features, and that all the q features are highly correlated to each other
    # constructorPosition and finalPosition are also correlated enough to be useful
    # prevFinalTime is not useful because it is uncorrelated with finalPosition
    # prevFastestLapTime is highly correlated with q3
    # driverId is weakly correlated with finalPosition and everything else, but I think I'll keep it since we don't have many features
    print("Based on the EDA, selected features are: driverId, constructorId, constructorPosition, gridPosition, q3")
    df = df[['driverId', 'constructorId', 'constructorPosition', 'gridPosition', 'q3', 'finalPosition']]
    df.to_csv(f'{DATA_ROOT}/final_data.csv', index=False)
    print("Updated final_data.csv with only selected features.")
