from pathlib import Path
import pandas as pd

# Find the project and raw data folders
project_folder = Path(__file__).resolve().parent.parent
raw_folder = project_folder / "data" / "raw"

# Find all CSV files
files = sorted(raw_folder.glob("*.csv"))

# Check whether CSV files were found
if not files:
    print("No CSV files found in data/raw.")
else:
    # Inspect each monthly file
    for file_path in files:
        print("\n------------------------------")
        print("File:", file_path.name)
        print("------------------------------")

        # Load the data
        df = pd.read_csv(file_path)

        # Check the number of rows and columns
        print("\nRows and columns:")
        print(df.shape)

        # Display the first five rows
        print("\nFirst five rows:")
        print(df.head())

        # Check the column names and data types
        print("\nColumn names and data types:")
        print(df.info())

        # Count missing values
        print("\nMissing values:")
        print(df.isna().sum())