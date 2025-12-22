import pandas as pd
import glob

files = glob.glob("data/raw/*.csv.gz")

# Import data
dfs = [pd.read_csv(f, compression="gzip") for f in files]
df = pd.concat(dfs)

# Aggregate data on user_id
df = df.groupby("user_id").agg(
    platform=("platform", "first"),
    install_date=("install_date", "first"),
    country=("country", "first"),
    total_session_count=("total_session_count", "sum"),
    total_session_duration=("total_session_duration", "sum"),
    match_start_count=("match_start_count", "sum"),
    match_end_count=("match_end_count", "sum"),
    victory_count=("victory_count", "sum"),
    defeat_count=("defeat_count", "sum"),
    ad_revenue=("ad_revenue", "sum"),
    iap_revenue=("iap_revenue", "sum"),
)
# Add total_revenue column
df["total_revenue"] = df["ad_revenue"] + df["iap_revenue"]

df.to_csv("data/processed/aggregated_player_data.csv")
