# How I Adjusted Garmin GPS Coordinates Using Python

Welcome! The following document details of a small project working with XML, Interpolation, and Python scripts. Find out how I used Python to solve a real-world problem related to my Gamrin Multisport GPS Watch and how the implications of the Isreal-Palistine conflict incentivised some deeper learning of 3 Python Libraries. 

# Document Contents 

- [**Introduction**](#Introduction): Provides context to the problem. Reveals the requirements for a solution. 
- [**Initial Problem Solving**](#initial-problem-solving): Describes the GPS interference issues and their implications on running metrics.
- [**Thought Process No1**](#thought-process-no1): Explores the initial idea of manually adjusting maps and introduces Garmin's TCX file format.
- [**Thought Process No2**](#thought-process-no2): Shifts focus to automating the correction process using a Python script.
- [**Creating Replacement Data**](#creating-replacement-data): Details the process of preparing new coordinates using GPS Visualizer.
- [**Automated Coordinate Generator**](#automated-coordinate-generator): Discusses generating and combining coordinates using Python.
- [**A Mismatch in Data Points**](#a-mismatch-in-data-points): Explains the discrepancy between generated and recorded data points and the need for interpolation.
- [**Interpolation**](#interpolation): Outlines the process of interpolating the new coordinates to match the recorded trackpoints.
- [**Parse and Replace**](#parse-and-replace): Covers parsing the TCX file and replacing coordinates using Python.
- [**Final Product**](#final-product): Shows the successful upload and visualization of the corrected TCX file.
- [**Limitations**](#limitations): Discusses the limitations of the current solution and potential improvements.
- [**Summary**](#summary): Summarizes the project, its outcomes, and personal learnings.
- [**Future Work**](#future-work): Proposes future enhancements and new project ideas.
- [**Conclusion**](#conclusion): Concludes the document and invites feedback and contact.

# Introduction 

To provide some context, from childhood I've relished participating in a variety of sports and I've maintained that same keen interest throughout my life. Over the years, what began as an enjoyable hobby, developed into one of my core values. My most recent focus is running. Some may see running as burdensome, and albeit challenging for me at times, I see it as an healthy escape from the hustle and bustle of life. The art of running is a classic. As a child, running comes naturally, its beauty lies in its simplicity. By putting one foot in front of the other, we experience one our most natural movements. Running is among the best investments one can make for their body and mind. As with most of my hobbies, I found great satisfaction in quantifying my progress and seeking ways to improve my ability level. Heartrate and Distance were metrics I soon began to observe. This was made easy by utilizing Garmin's Fenix Multisport GPS watch and their accompanying platform Garmin Connect. The Fenix encompasses a broad range of features and capabilities, all aimed at measuring essential workout metrics, including Heart-Rate Monitoring, GPS tracking, recovery insights and much more. Garmin Connect on the other hand, is a platform capable for holding data and providing a holistic overview of progress through an intuituve interface. Its main uses include visualising the geographical routes taken and gaining valuable insight through workout monitoring.

The Garmin Fenix is a great watch and I love the ergonomical design, however there was a giant issue that I soon encountered. The GPS feature produced perculiar results. Not only was the map visual misaligned, the distance metric was incorrect. Was there something wrong with the Garmin Watch? No, but I wasn't suprised. If you live Cyprus, as I do, or have travelled through the Mediterranean, Baltic, and Middle-Eastern regions recently, you may have experienced something similar. It will come at no shock that the GPS discrepencies are no fault of brand or model. The problem stems from a much deeper issue: electronic warfare and our spatial proximity to the Middle-Eastern region. The geopolitical conflict in this area has resulted in GPS and satellite signal disruptions and many areas of life are being affected. To outline a few: flight navigation and air traffic control have reverted to traditional navigation methods. This costs them time and money. Delays are also being experienced by emergency serives such as Ambulances, Police and Fire-Services. For the general public, popular navigation methods such as Google Maps are suffering. This causes finacial implication to relevent industries and psycological strain to the general public. I bring forward my experience within this document not to diminish what is going on around us, but instead to bring light to a comparitively small, yet very real conscequence of the ongoing conflict. With that being said, I was determined to reconcile the problem I was facing. 

## Initial Problem Solving

Due to the GPS interference, the incorrect coordinates it produced had serveral implications; 

1) An inaccuracy of distance; for example - A 10k run may show up as 7k or at times even 0.7k. 

2) The skewed variables rendered the insights gained through Garmin Connect ineffective and therefore the accumulated data, which aids in ones progress, non-existant. 

3) The maps looked choatic, much like if you employed a toddler to draw their finest scribble on a map.

Here's an example of my first run with the Garmin Fenix: 

![Map-Example](/Files/stravaexample.png)

Being unable to view the route you ran is admittedly annoying. But, of the three problems at hand, it is probably last in priority. However this project was prompted by a beautiful morning run that I could not see on Garmin Connect. Edorphins and adreneline were pumping through my vains, logic had taken the backseat and the lack of a simple yet playful map displaying my route was not just an inconvenience, it was a cry for help! In need of a satisfying visual I fired up my laptop, opened my IDE, and got to work. To me, issue 3 was of paramount importance.


## Thought process No.1

Can I manually adjust the map, in a drag and drop fashion - similiar to https://onthegomap.com/#/create "How far did I run?" - to fix all these issues? Unfortunately adjusting the coordinates in this way is not supported by Garmin directly, I also attempted to use Golden Cheetah but with no success. Yet effort to resolve my issue in this way did not go to waste, as it was through the process of downloading workout data from Garmin - in order to upload it to the Golden Cheetah application - that I discovered Garmin's XML equivalent file type, TCX (Training Center XML). 

Garmin's Available File Formats for Download: 

![downloadtcx](Files/downloadtcx.png)

## Thought Process No.2

My new goal was simple: 1) Download the XML file and locate the affected data points, 2) create data that reflects the corrected coordinates, 3) re-upload. It sounded simple enough. Then it dawned on me, with 1000's of data points to modify, doing this line by line would be tedious and not worth the effort. But, I had a great idea! A Python script could make short work of this repetitive task. 

To give you an idea of what the file looks like, here is as snippet: 

![TCX Example](Files/tcxexample.png)

## Creating Replacement Data

Before moving onto the main script, I needed to prepare the replacement data. This meant finding the coordinates of my run. For this I used https://www.gpsvisualizer.com/draw/. Dropping pins at the desired location was quick and easy. The corresponding coordinates could be saved to a TXT file.

Here is an example of me dropping some pins:
![gpsvisualiser](Files/gpsvisualiser.png)

This is an example of what some of the downloaded cordinates look like:
![Coordinates](Files/Coordinates.png)

## Automated Coordinate Generator

As I didn't run in a loop, the run followed what you would call an 'out-and-back' route. Simply put, I ran to a midway point and then ran back, retracing my steps. Therefore my new coordinate data points only represented half of the route and I had to append a reversed set of the coordinates to the end of the original set, hense simulating the out-and-back path I had taken. To save time I used python. To view the code in its entirety click - or right click to open tab - the following link: [Out and Back Data Reversing Python File](src/outandback-reverse.py)

The following is a portion of the file with narrative comments:

```python
# Define input and output file names
input_file = 'input.txt'
output_file = 'output_combined.txt'

# Read the input file with tabs as delimiter
with open(input_file, 'r', newline='') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    rows = list(reader)  # Convert to a list to enable processing

# Reverse the order of the rows and combine with the original list
reversed_rows = rows[::-1]
combined_rows = rows + reversed_rows

# Write the combined rows to the output file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter='\t')
    writer.writeheader()  
    writer.writerows(combined_rows) 

print(f"Combined original and reversed records written to {output_file}")
```

## A Mismatch in Data Points

With my out-and-back Coordinates saved in a handy TSV (Tab-Separated-Value) file, I was almost ready to start replacing my TCX File coordinates. However, there was one small discrepency. When plannning my route and extracting the corrected cordinates, I simply droped markers at every turning point and took little notice to the distances between each marker. Additionally, the total number of paired latitude and longitude coordinates - including the reversed set - amounted to 87. The discrepency appears once you consider that during a workout a Garmin watch is recording data every second. Each second is represented as a single trackpoint within a TCX file. In consequence a thirty minute workout produces 1800 trackpoints (60 x 30). Since each trackpoint contains metrics like distance, latitude, and longitude; and every trackpoint needed modification, I had to interpolate my 87 coordinates. 

I will not cover the code I used to calculate the number of trackpoints within a TCX in this document, however if you would like to view the Python script click - right click to open in new tab - this link: [Count Trackpoints Code](src/count-trackpoints.py)


## Interpolation

In order to interpolate the newly generated precise coordinates - so they amount to the sum total trackpoints (measured in the previous script) - and to ensure they are equally spaced, I used the following Python script. To view the code in its entirety click the link: [Data-Interpolation](src/data-interpolation.py)

Here is a higher-level overview with narrative comments:

```python 
import pandas as pd
import numpy as np
from geopy.distance import geodesic # Note the geodesic module import from library geopy.distance, for the purpose of calculating distances. 
from pathlib import Path

# Below are the functions that were defined. 

# Calculate the total distance traveled.
def calculate_total_distance(coords):

# Resample the data to total trackpoints, equally spaced apart.
def resample_coordinates(coords, num_points):

# Format the coordinates to the specified number of decimal places. Important for reliability.
def format_coordinates(coords, decimal_places, for_dist):


# Below we run the functions with our desired inputs.

# Resample coordinates to total trackpoints
resampled_coords = resample_coordinates(coords, 1800)

# Format the resampled coordinates to 7 decimal places. This maintains Garmins Standard.
formatted_coords = format_coordinates(resampled_coords, 15, 14)

# Save the resampled coordinates to a new file
resampled_data = pd.DataFrame(formatted_coords, columns=['latitude', 'longitude', 'distance_meters'])
resampled_data.to_csv(folder / 'resampled_coordinates.txt', index=False, sep='\t')
```

## Parse and Replace

At this point, I have my /Data/resampled_coordinates.txt file - a TSV file containing 1800 equally distanced coordinates - accurately representing my morning run. Next I needed to parse the original TCX file and replace each Latitude, Longitude, and DistanceMeters variable. To acheive this, I used the following Python code. Click the link to view it in its entirety: [Parse and Replace](src/parse-and-replace.py)

Here is a higher-level overview with narrative comments:

```python
# Import Libaries***

# Load the resampled coordinates***

# Parse the TCX file
tcx_file_path = Path('tcx') / 'activity_16486638003.tcx'
tree = ET.parse(tcx_file_path)
root = tree.getroot()

# Define namespaces
namespaces = {
    'tcx': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'
}
# Find all Trackpoints
trackpoints = root.findall('.//tcx:Trackpoint', namespaces)

# Replace latitude, longitude, and distance values
for i, trackpoint in enumerate(trackpoints):
    # code continues

# Save the modified TCX file
modified_tcx_file_path = tcx_file_path = Path('tcx') / 'modified_file.tcx'

# Maintain TCX format identical to original. Ensures the file is supported by Garmin Connect
tree.write(modified_tcx_file_path, xml_declaration=True, encoding='UTF-8', pretty_print=True)
```


## Final Product

With the implementation of the previous step, my newly created TCX file - /tcx/modified_file.tcx - was ready to be uploaded to Garmin Connect!

Here is the Result:
![Final Run](Files/FinalRun.png)


## Limitations

Although this is a successful solution for GPS disruptions affecting Garmin measurements, I thought it was best to mention that this is by no means a perfect solution. When interpolating the new coordinates I was aware that this system equally spaces the distance of each data point. This assumes that the runner is running at a constant pace. Since this is unlikely, the various metrics will not perfectly align with their corresponding location. However ways of eliminating inconsitences, such as using checkpoints to segment the followed course or using Garmin's non-GPS distance and pace measurements to provide a far more realistic distrubution, will be discussed further in the future work section.


## Summary 

From what started out as an attack unjustly made against Garmin products (I still love their watches), to a conflict driven ripple-affect felt globaly, this small project provided an opportunity for deeper learning. By utilising libraries: geopy, pandas, and lxml; this system provides a viable solution to a real-life problem. I created new data, resampling it to the desired sum total and appropriate formatting; next we modified an existing TCX file, adapting several data points using our new data. The end result was an accurate rendering of the workout activity, hosted on Garmin Connect. The process of creating such a system also demonstrates the versitility of Python and its supporting libraries, which are viable for numerous tasks and processes. My personal growth manifests itself in a deeper understanding of XLM files, GPS coodinates and geopy, and resampling methods. Going forward, whether facing industry specific or personal obstacles, I hope this project serves as a reminder to myself and others that Python has great potential for improving everyday life. 


## Future Work

To enhance the accuracy of the system and address the limitations mentioned, future work will focus on implementing several key improvements. One such enhancement is the incorporation of checkpoints to segment the course, which will help mitigate inconsistencies by providing more precise reference points. Additionally, leveraging Garmin's non-GPS built-in distance and pace measurements will allow for a more realistic distribution of data points, aligning better with the actual run dynamics.

**New Project Ideas:**
1) Adaptive Interpolation Algorithm:
Develop an adaptive algorithm that dynamically adjusts interpolation based on pace variability detected from non-GPS sensors.

2) Machine Learning for GPS Anomaly Correction:
Integrate machine learning techniques to predict and correct GPS anomalies, offering a more robust solution for accurate race tracking.


## Conclusion

Thank you for reading this document! It was an enjoyable experience creating this system, I hope you can take away some value from it. I learnt a lot from the process, so I at least hope it encourages you to try coding something new. If you do, share it with me! Lastly, any feedback is welcome, my contact information is below. Thank you again and I will see you guys in the next one! Have a great weekend!

### Licence

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

### Contact Information

If you have any questions or comments about the project, or if you're interested in contributing, feel free to reach out:

- **Project Maintainer**: Emilios Richards
- **Email**: emiliosmrichards@gmail.com
- **GitHub Profile**: [EmiliosRichards](https://github.com/EmiliosRichards)

![Bye!](/Files/wavebye.png)