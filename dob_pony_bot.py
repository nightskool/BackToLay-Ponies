# DOB In-Play Trading Bot: BackToLay Ponies
# Strategy: Identify front-runners likely to drop 50%+ in-play odds (DOB = Double or Bust)
# Repo: https://github.com/nightskool/BackToLay-Ponies

import pandas as pd
import numpy as np

# Placeholder for loading race data (replace with actual CSV/Excel path)
df = load_race_data("data/historical_races.csv")
top_dob = get_top_dob_runners(df, "2025-07-23")
print(top_dob.head(10))


# Basic DOB candidate scoring
# Looks for horses with BSP 9.0–20.0 and strong in-play low prices

def score_dob_candidates(df):
    df['DOB_Eligible'] = df['BSP'].between(9.0, 20.0)
    df['PriceDrop'] = df['BSP'] / df['InPlayLow']
    df['DOB_Hit'] = df['PriceDrop'] >= 2.0
    return df[df['DOB_Eligible'] == True]

# Display top candidates for a given day
def get_top_dob_runners(df, date):
    today_df = df[df['RaceDate'] == date]
    scored = score_dob_candidates(today_df)
    top = scored.sort_values(by='PriceDrop', ascending=False)
    return top[['HorseName', 'BSP', 'InPlayLow', 'PriceDrop']]

# Sample test run (stub)
if __name__ == "__main__":
    print("🏇 BackToLay Ponies | DOB Filter Initializing...\n")
    # df = load_race_data("historical_races.csv")
    # top_dob = get_top_dob_runners(df, "2025-07-23")
    # print(top_dob.head(10))

    print("✨ Data engine ready for analysis. Connect your dataset and let the ponies gallop.")

    # Clever Virgos would appreciate clean logic and modular design 😉
    # To-do: Add DOB heatmap, signal scoring by trainer/jockey/course, Telegram notifier?
