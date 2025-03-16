import pandas as pd

# Load raw data
raw_df = pd.read_csv("/Users/junyaoren/Desktop/ResaleflatpricesfromJan2017onwards.csv")

# Convert month to datetime
raw_df['month'] = pd.to_datetime(raw_df['month'])

# Filter for target towns
target_towns = ["JURONG WEST", "BUKIT MERAH", "CENTRAL AREA", "TAMPINES", "WOODLANDS"]
filtered = raw_df[raw_df['town'].isin(target_towns)]

# Filter dates between 2020 and 2025
filtered = filtered[filtered['month'].between('2020-01-01', '2025-03-01')]

# Calculate monthly averages
monthly_avg = filtered.groupby(['month', 'town'])['resale_price'].mean().reset_index()

# Save processed data
monthly_avg.to_csv("/Users/junyaoren/Desktop/multi_town_avg.csv", index=False)
