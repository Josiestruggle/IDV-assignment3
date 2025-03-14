import pandas as pd

# Load raw data
raw_df = pd.read_csv("/Users/junyaoren/Desktop/ResaleflatpricesfromJan2017onwards.csv")

# Filter and clean
# Convert month to datetime first
raw_df['month'] = pd.to_datetime(raw_df['month'])

# Proper parentheses structure
target_towns = ["JURONG WEST", "BUKIT MERAH", "CENTRAL AREA", "TAMPINES", "WOODLANDS"]
filtered = raw_df[raw_df['town'].isin(target_towns)]

# Calculate monthly averages
monthly_avg = filtered.groupby(['month', 'town'])['resale_price'].mean().reset_index()

# Save processed data
monthly_avg.to_csv("/Users/junyaoren/Desktop/multi_town_avg.csv", index=False)