import pandas as pd

# Load dataset
df = pd.read_csv(r'D:\pi164\heart.csv')

# Features and target
X = df.drop('target', axis=1)
y = df['target']

# Display output
print(df.head())
print("\nX shape:", X.