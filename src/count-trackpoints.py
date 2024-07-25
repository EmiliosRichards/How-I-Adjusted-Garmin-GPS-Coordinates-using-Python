import xml.etree.ElementTree as ET
from pathlib import Path

# Read the latitude and longitude data from the txt file
folder = Path('tcx')
file = folder / 'activity_16486638003.tcx.txt'

def count_relevant_trackpoints(tcx_file_path):
    # Parse the TCX file
    tree = ET.parse(tcx_file_path)
    root = tree.getroot()

    # Define the namespace
    namespaces = {'tcx': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}

    # Find all trackpoints
    trackpoints = root.findall('.//tcx:Trackpoint', namespaces)

    # Initialize counters
    total_trackpoints = 0
    relevant_trackpoints = 0

    # Loop through all trackpoints
    for trackpoint in trackpoints:
        total_trackpoints += 1
        latitude = trackpoint.find('.//tcx:LatitudeDegrees', namespaces)
        longitude = trackpoint.find('.//tcx:LongitudeDegrees', namespaces)
        
        if latitude is not None and longitude is not None:
            relevant_trackpoints += 1

    print(f"Total trackpoints: {total_trackpoints}")
    print(f"Trackpoints with both latitude and longitude: {relevant_trackpoints}")

    return relevant_trackpoints

# Example usage
relevant_trackpoints = count_relevant_trackpoints(file)

# Output the number of relevant trackpoints
print(f"Number of relevant trackpoints: {relevant_trackpoints}")