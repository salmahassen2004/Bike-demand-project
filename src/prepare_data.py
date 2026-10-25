from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the combined dataset
input_file = project_folder / "data" / "processed" / "all_trips.csv"

# Load the combined dataset
df = pd.read_csv(input_file)

print("Dataset loaded!")
print(f"Number of trips: {len(df):,}")

# Convert timestamps to datetime
df["started_at"] = pd.to_datetime(
    df["started_at"],
    errors="coerce",
    utc=True
)

df["ended_at"] = pd.to_datetime(
    df["ended_at"],
    errors="coerce",
    utc=True
)

# Convert UTC timestamps to Norwegian local time
df["started_at"] = df["started_at"].dt.tz_convert("Europe/Oslo")
df["ended_at"] = df["ended_at"].dt.tz_convert("Europe/Oslo")

# Check for timestamps that could not be converted
print("\nMissing start timestamps:", df["started_at"].isna().sum())
print("Missing end timestamps:", df["ended_at"].isna().sum())

# Display a few timestamps
print("\nFirst five start timestamps in Norwegian time:")
print(df["started_at"].head())

# Display the date range
print("\nTrip start date range in Norwegian time:")
print("First trip:", df["started_at"].min())
print("Last trip:", df["started_at"].max())