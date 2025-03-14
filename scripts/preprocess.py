import pandas as pd

# Load raw data
raw_df = pd.read_csv("data/raw/ResaleflatpricesfromJan2017onwards.csv")

# Filter and clean
jurong_data = raw_df[
    (raw_df['town'] == 'JURONG WEST') &
    (pd.to_datetime(raw_df['month']).between('2020-01', '2025-02')
]

# Calculate monthly averages
monthly_avg = jurong_data.groupby('month')['resale_price'].mean().reset_index()

# Save processed data
monthly_avg.to_csv("../data/processed/jurong_west_avg.csv", index=False)
