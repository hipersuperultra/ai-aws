import pandas as pd

df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

labels = list(df.columns)

for x in range(0, 6):
    labels[x] = labels[x].replace(' ', '_')

df.columns = labels


def medians(group, field, label):
    median = field.median()
    for i, item in enumerate(field):
        if item >= median:
            df.loc[i, label] = 'high'
        else:
            df.loc[i, label] = 'low'
    group.groupby(label).quality.mean()


medians(df, df.alcohol, 'alcohol')
medians(df, df.pH, 'pH')
medians(df, df.residual_sugar, 'residual_sugar')
medians(df, df.citric_acid, 'citric_acid')
