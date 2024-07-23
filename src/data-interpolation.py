import pandas as pd
import numpy as np
from geopy.distance import geodesic
from pathlib import Path

# Read the latitude and longitude data from the txt file
folder = Path('Data')
file = folder / 'coordinatesdata.txt'
data = pd.read_csv(file, delimiter='\t')

# Check the first few rows of the dataframe to ensure it's read correctly
print(data.head())

# Calculate the total distance traveled
def calculate_total_distance(coords):
    total_distance = 0.0
    for i in range(1, len(coords)):
        total_distance += geodesic((coords[i-1][0], coords[i-1][1]), (coords[i][0], coords[i][1])).meters
    return total_distance

coords = list(zip(data['latitude'], data['longitude']))
total_distance = calculate_total_distance(coords)
print(f"Total distance: {total_distance} meters")

# Resample the data to 288 points
def resample_coordinates(coords, num_points):
    cumulative_distances = [0.0]
    for i in range(1, len(coords)):
        cumulative_distances.append(cumulative_distances[-1] + geodesic((coords[i-1][0], coords[i-1][1]), (coords[i][0], coords[i][1])).meters)
    
    new_cumulative_distances = np.linspace(0, cumulative_distances[-1], num_points)
    new_coords = [(coords[0][0], coords[0][1], 0.0)]
    
    for target_distance in new_cumulative_distances[1:]:
        for i in range(1, len(cumulative_distances)):
            if cumulative_distances[i] >= target_distance:
                ratio = (target_distance - cumulative_distances[i-1]) / (cumulative_distances[i] - cumulative_distances[i-1])
                new_lat = coords[i-1][0] + ratio * (coords[i][0] - coords[i-1][0])
                new_lon = coords[i-1][1] + ratio * (coords[i][1] - coords[i-1][1])
            
                
                new_coords.append((new_lat, new_lon, target_distance))
                break

    return new_coords

def format_coordinates(coords, decimal_places, for_dist):
    # Format the coordinates to the specified number of decimal places
    formatted_coords = []
    for lat, lon, dist in coords:
        formatted_lat = f"{lat:.{decimal_places}f}"
        formatted_lon = f"{lon:.{decimal_places}f}"
        formatted_dist = f"{dist:.{for_dist}f}"
        formatted_coords.append((formatted_lat, formatted_lon, formatted_dist))
    return formatted_coords

resampled_coords = resample_coordinates(coords, 288)

# Format the resampled coordinates to 7 decimal places
formatted_coords = format_coordinates(resampled_coords, 15, 14)

# Save the resampled coordinates to a new file
resampled_data = pd.DataFrame(formatted_coords, columns=['latitude', 'longitude', 'distance_meters'])
resampled_data.to_csv(folder / 'resampled_coordinates.txt', index=False, sep='\t')

# Verify the total distance of resampled coordinates
resampled_total_distance = calculate_total_distance(resampled_coords)
print(f"Total distance after resampling: {resampled_total_distance} meters")
