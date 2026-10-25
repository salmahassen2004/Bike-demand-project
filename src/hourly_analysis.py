from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the combined dataset
input_file = project_folder / "data" / "processed" / "all_trips.csv"

# Locate the output folder
output_folder = project_folder / "data" / "processed"

# Load the combined dataset
df = pd.read_csv(input_file)

print("Dataset loaded!")
print(f"Total trips before cleaning: {len(df):,}")

# Convert start timestamps to datetime
df["started_at"] = pd.to_datetime(
    df["started_at"],
    errors="coerce",
    utc=True
)

# Convert timestamps to Norwegian local time
df["started_at"] = df["started_at"].dt.tz_convert("Europe/Oslo")

# Count trips with missing or invalid start timestamps
missing_start_times = df["started_at"].isna().sum()
print(f"Trips with missing start timestamps: {missing_start_times:,}")

# Keep trips with valid start timestamps
df = df.dropna(subset=["started_at"])

print(f"Trips included in hourly analysis: {len(df):,}")

# Extract the date and hour for each trip
df["date"] = df["started_at"].dt.date
df["hour"] = df["started_at"].dt.hour

# Count trips starting in each hour of each day
hourly_demand = (
    df.groupby(["date", "hour"])
    .size()
    .reset_index(name="trip_count")
)

# Save the hourly results
output_file = output_folder / "hourly_demand.csv"
hourly_demand.to_csv(output_file, index=False)

print("\nHourly analysis complete!")
print(f"Number of date-hour combinations: {len(hourly_demand):,}")
print(f"Saved results to: {output_file}")

# Show the first few results
print("\nFirst 10 rows:")
print(hourly_demand.head(10))