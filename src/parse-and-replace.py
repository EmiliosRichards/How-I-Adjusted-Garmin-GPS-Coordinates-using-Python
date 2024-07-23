from lxml import etree as ET
import pandas as pd
from pathlib import Path


# Load the resampled coordinates
resampled_folder_path = Path('data')
resampled_file_path = resampled_folder_path / 'resampled_coordinates.txt'
resampled_data = pd.read_csv(resampled_file_path, delimiter='\t')
resampled_coords = list(zip(resampled_data['latitude'], resampled_data['longitude'], resampled_data['distance_meters']))

# Check the first few rows of the dataframe to ensure it's read correctly
print(resampled_data.head())

# Parse the TCX file
tcx_file_path = Path('tcx') / 'activity_16486638003.tcx'
tree = ET.parse(tcx_file_path)
root = tree.getroot()

print(root.tag)

# Define namespaces
namespaces = {
    'tcx': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'
}

# Find all Trackpoints
trackpoints = root.findall('.//tcx:Trackpoint', namespaces)

# Replace latitude, longitude, and distance values
for i, trackpoint in enumerate(trackpoints):
    if i >= len(resampled_coords):
        break
    latitude_elem = trackpoint.find('.//tcx:LatitudeDegrees', namespaces)
    longitude_elem = trackpoint.find('.//tcx:LongitudeDegrees', namespaces)
    distance_elem = trackpoint.find('.//tcx:DistanceMeters', namespaces)
    
    if latitude_elem is not None:
        latitude_elem.text = str(resampled_coords[i][0])
    if longitude_elem is not None:
        longitude_elem.text = str(resampled_coords[i][1])
    if distance_elem is not None:
        distance_elem.text = str(resampled_coords[i][2])

# Save the modified TCX file
modified_tcx_file_path = tcx_file_path = Path('tcx') / 'modified_file.tcx'
tree.write(modified_tcx_file_path, xml_declaration=True, encoding='UTF-8', pretty_print=True)