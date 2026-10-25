# Predicting Hourly Oslo City Bike Demand

## 1. Project Overview

This project investigates whether historical Oslo City Bike trip records can help predict the number of trips starting in a given hour.

The project uses exploratory data analysis (EDA) to understand bike usage patterns, including changes throughout the day, differences between weekdays and weekends, seasonal variations, trip durations, and popular starting stations.

## 2. Research Question

Can historical Oslo City Bike trip records help predict the number of trips starting in a given hour?

## 3. Dataset

The project uses Oslo City Bike trip records from September 2025 to September 2026.

The dataset contains information about trip start and end times, trip duration, and start and end stations.

The original data files are stored locally in `data/raw/`. The combined and processed datasets are stored in `data/processed/`. These data files are not included in Git.

## 4. Data Analysis Pipeline

The project is organized into several steps:

1. **Data inspection:** Examine the CSV files, their columns, data types, and missing values.
2. **Data combination:** Combine the monthly trip files into one dataset.
3. **Data preparation:** Convert trip timestamps from UTC to Norwegian local time (`Europe/Oslo`) and identify invalid timestamps.
4. **Hourly analysis:** Count trip starts for each date and hour, including hours with zero recorded trips.
5. **Exploratory data analysis:** Examine trip durations, popular starting stations, weekday patterns, and monthly trip counts.
6. **Visualization:** Create graphs to explore hourly demand and other trip patterns.

### Running the scripts

Run these commands from the project root directory:

```bash
python3 src/inspect_data.py
python3 src/combine_data.py
python3 src/prepare_data.py
python3 src/hourly_analysis.py
python3 src/visualize_demand.py
```

The scripts read raw data from `data/raw/` and save processed results to `data/processed/`.

## 5. Preliminary Findings

The exploratory data analysis reveals several patterns in recorded Oslo City Bike trips.

- **Hourly demand:** The hourly analysis shows peaks in recorded trip starts around 08:00 and 16:00. In the earlier analysis, these hours averaged approximately 317 and 357 trip starts, respectively. The updated graph should be used for the final reported values.
- **Trip duration:** The average calculated trip duration is approximately 12.13 minutes, while the median is approximately 9.04 minutes. The distribution is right-skewed, with most trips being relatively short and a smaller number lasting much longer.
- **Starting stations:** Alexander Kiellands Plass has the highest number of recorded trip starts among the ten most popular starting stations in the updated analysis.
- **Weekday patterns:** The total number of recorded trips is higher on weekdays than on weekends. Wednesday has the highest total among the weekdays shown.
- **Seasonal patterns:** Monthly trip counts are much lower during winter and increase during spring and summer. August 2026 has the highest monthly total in the updated dataset, with 187,181 recorded trips.

These findings describe historical trip patterns. Further analysis and model evaluation are needed to determine how accurately hourly trip starts can be predicted.

## 6. Limitations

The data represent recorded trips, not all potential demand. For example, they do not directly measure trips that could not start because no bikes were available.

The analysis also depends on the quality and coverage of the recorded data. Trips with invalid start timestamps are excluded from the hourly analysis. Some unusually long calculated durations may require further investigation.

## 7. Project Structure

```text
Bike-demand-project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── inspect_data.py
│   ├── combine_data.py
│   ├── prepare_data.py
│   ├── hourly_analysis.py
│   └── visualize_demand.py
├── README.md
├── requirements.txt
└── .gitignore
```