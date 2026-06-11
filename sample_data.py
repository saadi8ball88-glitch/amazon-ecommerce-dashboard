import pandas as pd

# Original dataset load karo
df = pd.read_csv("amazon_ecommerce_1M.csv")

# 50,000 random rows lo
sample_df = df.sample(n=50000, random_state=42)

# New file save karo
sample_df.to_csv("amazon_dashboard_data.csv", index=False)

print("New Dataset Shape:", sample_df.shape)
print("File Created Successfully!")