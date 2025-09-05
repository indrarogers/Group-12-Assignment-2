# Tristan Storey Temperatures 

# Imports (os for giving access to the temperature files) (pandas as pd to allow to read the files) 
import os
import pandas as pd

# list to catigorize months into Australian seasons 
SEASONS = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# loading and reshaping the csv files so each temperature reading becomes a single row, making it easy to filter, group, and analyze across months, seasons, and stations for further calculations.

def load_and_reshape(folder_path):
    all_data = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(folder_path, file))
            melted = df.melt(
                id_vars=['STATION_NAME', 'STN_ID', 'LAT', 'LON'],
                value_vars=MONTHS,
                var_name='Month',
                value_name='Temperature'
            )
            all_data.append(melted)
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df

# Assign season based on month
def assign_season(month):
    for season, months in SEASONS.items():
        if month in months:
            return season
    return None 

# Calculate each seasonal average using basic math (sum of tempitues divided by number of tempriture readngs within that season)
def calculate_seasonal_averages(df):
    df["Season"] = df["Month"].apply(assign_season)
    season_avgs = df.groupby("Season")["Temperature"].mean().dropna().round(1)
#opens a txt files that prints out the average temperature for each season 
    with open("average_temp.txt", "w") as f:
        for season in ['Summer', 'Autumn', 'Winter', 'Spring']: 
            avg = season_avgs.get(season)
            if avg is not None:
                f.write(f"{season}: {avg}°C\n")

    return season_avgs.to_dict()

# Find stations with largest temperature range
def find_largest_temp_range(df):
    ranges = {}
    grouped = df.groupby('STATION_NAME')
    for station, group in grouped:
        temps = group['Temperature'].dropna()
        if not temps.empty:
            max_temp = temps.max()
            min_temp = temps.min()
            range_temp = max_temp - min_temp
            ranges[station] = (range_temp, max_temp, min_temp)

    max_range = max(ranges.values(), key=lambda x: x[0])[0]
#opens a txt files that prints out the largest temperature range 
    with open("largest_temp_range_station.txt", "w") as f:
        for station, (r, max_t, min_t) in ranges.items():
            if r == max_range:
                f.write(f"{station}: Range {r:.1f}°C (Max: {max_t:.1f}°C, Min: {min_t:.1f}°C)\n")

    return {station: data for station, data in ranges.items() if data[0] == max_range}

# Find most stable and most variable stations
def find_temperature_stability(df):
    stddevs = {}
    grouped = df.groupby('STATION_NAME')
    for station, group in grouped:
        temps = group['Temperature'].dropna()
        if not temps.empty:
            stddev = temps.std()
            stddevs[station] = round(stddev, 1)

    min_std = min(stddevs.values())
    max_std = max(stddevs.values())
#opens a txt files that prints out the most stable and unstable locations and tempriture variation
    with open("temperature_stability_stations.txt", "w") as f:
        for station, std in stddevs.items():
            if std == min_std:
                f.write(f"Most Stable: {station}: StdDev {std}°C\n")
        for station, std in stddevs.items():
            if std == max_std:
                f.write(f"Most Variable: {station}: StdDev {std}°C\n")

    return {
        "Most Stable": [s for s, std in stddevs.items() if std == min_std],
        "Most Variable": [s for s, std in stddevs.items() if std == max_std]
    }

# Main function
def main():
    folder_path = "Question 2/temperatures"
    df = load_and_reshape(folder_path)

    print("Data loaded and reshaped.")

    seasonal_averages = calculate_seasonal_averages(df)
    print("\nSeasonal Averages:")
    for season, avg in seasonal_averages.items():
        print(f"{season}: {avg}°C")

    largest_range = find_largest_temp_range(df)
    print("\n📈 Largest Temperature Range:")
    for station, (r, max_t, min_t) in largest_range.items():
        print(f"{station}: Range {r:.1f}°C (Max: {max_t:.1f}°C, Min: {min_t:.1f}°C)")

    stability = find_temperature_stability(df)
    print("\n📊 Temperature Stability:")
    print(f"Most Stable: {', '.join(stability['Most Stable'])}")
    print(f"Most Variable: {', '.join(stability['Most Variable'])}")

if __name__ == "__main__":
    main()
#issues i couldnt find a way to redirect the location of the txtx file to print within the same folder 
