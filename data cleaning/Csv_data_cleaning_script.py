import pandas as pd

# Load CSV
df = pd.read_csv("raw_data.csv")

# Drop duplicates
df = df.drop_duplicates()

# Fill missing values with placeholder
df = df.fillna("N/A")

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved as cleaned_data.csv")
