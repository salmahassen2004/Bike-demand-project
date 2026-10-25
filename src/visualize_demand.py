from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Load the hourly demand data
input_file = project_folder / "data" / "processed" / "hourly_demand.csv"

df = pd.read_csv(input_file)

print("Hourly demand data loaded!")

# Calculate average trips for each hour across all dates
average_by_hour = (
    df.groupby("hour")["trip_count"]
    .mean()
)

# Display the results
print("\nAverage trips starting in each hour:")
print(average_by_hour.round(2))

# Find the busiest hour
busiest_hour = average_by_hour.idxmax()
busiest_average = average_by_hour.max()

print(f"\nBusiest hour: {busiest_hour}:00")
print(f"Average trips during this hour: {busiest_average:.2f}")

# Create the graph
plt.figure(figsize=(10, 6))
average_by_hour.plot(kind="line", marker="o")

plt.title("Average Oslo City Bike Trip Starts by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Number of Trips")
plt.xticks(range(24))
plt.grid(True)
plt.tight_layout()

# Save the graph
output_file = project_folder / "data" / "processed" / "average_demand_by_hour.png"
plt.savefig(output_file, dpi=300)

print(f"\nGraph saved to: {output_file}")

# Display the graph
plt.show()