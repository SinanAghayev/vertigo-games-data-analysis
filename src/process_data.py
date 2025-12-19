import pandas as pd
import glob

files = glob.glob("data/raw/*.csv.gz")

dfs = [pd.read_csv(f, compression="gzip") for f in files]
df = pd.concat(dfs)

print("read the data")
df = df.groupby("country").agg(
    user_count=("user_id", "nunique"),
    total_session_count=("total_session_count", "sum"),
    total_session_duration=("total_session_duration", "sum"),
    match_start_count=("match_start_count", "sum"),
    match_end_count=("match_end_count", "sum"),
    ad_revenue=("ad_revenue", "sum"),
    iap_revenue=("iap_revenue", "sum"),
)
df["total_revenue"] = df["ad_revenue"] + df["iap_revenue"]
df.sort_values("total_revenue", ascending=False, inplace=True)
df[df["total_revenue"] > 10]


df.to_excel("data/processed/processed_data.xlsx")
