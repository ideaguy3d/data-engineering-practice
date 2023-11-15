import seaborn as sns
import pandas

df = sns.load_dataset('anscombe')
df.to_csv('anscombe.csv', index=False)