from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Find the raw and processed data folders
raw_folder = project_folder / "data" / "raw"
processed_folder = project_folder / "data" / "processed"

# Find all CSV files in the raw data folder
files = sorted(raw_folder.glob("*.csv"))

if not files:
    print("No CSV files found in data/raw.")
else:
    dataframes = []

    # Load each monthly CSV file
    for file_path in files:
        print(f"Reading {file_path.name}...")
        df = pd.read_csv(file_path)
        dataframes.append(df)

    # Combine all monthly files into one dataset
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Create the processed folder if it does not exist
    processed_folder.mkdir(parents=True, exist_ok=True)

    # Save the combined dataset
    output_file = processed_folder / "all_trips.csv"
    combined_df.to_csv(output_file, index=False)

    # Show a summary
    print("\nCombining complete!")
    print(f"Number of files combined: {len(files)}")
    print(f"Total number of trips: {len(combined_df):,}")
    print(f"Number of columns: {len(combined_df.columns)}")
    print(f"Saved to: {output_file}")

    # Convert start timestamps to datetime
    combined_df["started_at"] = pd.to_datetime(
        combined_df["started_at"],
        errors="coerce",
        utc=True
    )

    # Check the date range
    print("\nTrip start date range (UTC):")
    print("First trip:", combined_df["started_at"].min())
    print("Last trip:", combined_df["started_at"].max())