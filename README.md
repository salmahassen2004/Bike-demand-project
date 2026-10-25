# Predicting Hourly Oslo City Bike Demand

## 1. Project Overview

This project investigates whether historical Oslo City Bike trip records can help predict the number of trips starting in a given hour.

The project focuses on understanding how bike usage changes throughout the day and identifying the hours with the highest and lowest numbers of trip starts.

## 2. Research Question

Can historical Oslo City Bike trip records help predict the number of trips starting in a given hour?

## 3. Dataset

The project uses Oslo City Bike trip records from September 2025 to August 2026.

The dataset contains information about trip start and end times, trip duration, and start and end stations.

The original data files are stored locally in `data/raw/`. The combined and processed datasets are stored in `data/processed/`. These data files are not included in Git.
## 4. Data Analysis Pipeline

The project is organized into several steps:

1. **Data inspection:** Examine the CSV files, their columns, data types, and missing values.
2. **Data combination:** Combine the monthly trip files into one dataset.
3. **Data preparation:** Convert the trip timestamps from UTC to Norwegian local time (`Europe/Oslo`) and identify invalid timestamps.
4. **Hourly analysis:** Count trip starts for each date and hour, including hours with zero recorded trips.
5. **Visualization:** Calculate average trip starts for each hour of the day and create a graph.

### Running the scripts

Run these commands from the project root directory:

```bash
python3 src/inspect_data.py
python3 src/combine_data.py
python3 src/prepare_data.py
python3 src/hourly_analysis.py
python3 src/visualize_demand.py
```

The scripts read the raw data from `data/raw/` and save processed results to `data/processed/`.

## 5. Preliminary Findings

The hourly analysis indicates that trip starts vary throughout the day.

- **Busiest hour:** 16:00, with an average of approximately 357 trip starts.
- **Morning activity:** 08:00 has an average of approximately 317 trip starts.
- **Quietest hour:** 04:00, with an average of approximately 6 trip starts.

These results describe historical trip patterns. Further model evaluation is needed to determine how accurately hourly trip starts can be predicted.

## 6. Limitations

The data represent recorded trips, not all potential demand. For example, they do not directly measure trips that could not start because no bikes were available.

The analysis also depends on the quality and coverage of the recorded data. Invalid timestamps are excluded from the hourly analysis.

## 7. Project Structure

```text
Bike-demand-project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```