# How I Adjusted Garmin GPS Coordinates using Python

Welcome! The following document contains the details a small project working with XML, Interpolation, and python scripts. Find out how I used Python to solve a real-world problem related to my Gamrin Multisport GPS Watch and how the implications of the Isreal-Palistine conflict incentivised some deeper learning of 3 Python Libraries. 

# Document Contents 

- [**Introduction**](#Introduction): Provides context to the problem. Reveals the requirements for a solution. 

# Introduction 

To provide some context, since a child I've relished in a variety of sports and as I've grown to become young adult I've maintained that same keen interest, over the years what started out as an enjoyable pass-time, expanded to become a core value contributing to my wellbeing and health. My most recent focus is an exercise that some may see as burdensome, albeit challenging at times I see it as an escape from the hustle and bustle of life, its a simple workout that I can only regard as a classic, that is, the art of running. It's a form birthed at childhood that we all know too well, its beauty lies in its simplicity and with it being one of our most natural movements, it's needless to say running is among the best investments one can make for their body and mind. As with most of my hobbies, I found great joy in quantifying my progress and seeking ways to improve my ability level. Heartrate and Distance were metrics I soon began to observe. This was made easy by utilizing Garmin's Fenix Multisport GPS watch and their accompanying platform Garmin Connect. The Fenix encompasses a broad range of features and capabilities for measuring essential workout metrics, including Heart-Rate Monitoring, GPS tracking, recovery insights and much more. Garmin connect on the other hand, is a platform that can hold your data, allowing a holistic overwiew of progress through an intuituve interface, its main usage include: visualising the geographical rounts taken, and valuable insights facilitated by readily available workout statistics.

It is a great watch and I love the ergonomical design, however there was a giant issue that I soon encountered. The GPS produced perculiar results, not only was the map visual misaligned, the distance metric was rendered useless. Was something wrong with the Garmin Watch? No. It will come at no shock to those who have travelled through the Mediterranean, Baltic, and Middle-Eastern regions that these results are no fault of brand or model. The problem I faced stems from a much deeper issue: electronic warfare and our spatial proximity to the Middle-Eastern region. The geopolitical conflict in this area has resulted in GPS and satellite signal disruptions. Many areas of life are being affected, to list a few: flight navigation and air traffic control, delays in emergency serives such as ambulances, police and fire-services, these are all underpinned by the finacial impact and psycological strain. I bring forward my experience not to diminish that of what is going on around us, but instead to bring light to a comparitively small, yet very real conscequence of the ongoing conflict. With that being said, I was all the more determined to reconcile the problem I was facing. 

geopolitical conflicts, electronic warefare, satellite and gps interference -- the interference in my GPS coord is one of the many (disruptions) being felt by people. Although this issue is a small compared to many people are currently facing, it still a ery real byproduct of the war. With that being said,

## Initial problem solving

Due to the GPS interference, the incorrect coordinates it produced had serveral implications; 

1) First, an inaccuracy of distance, Example: A 10k run may show up as 7k or at times even 0.7k. 

2) Second, skewed variables rendered Garmin Connect and gaining insights through it, ineffective; and the accumulated data that leads to fitness progression insight, virtually non-existant. 

3) Lastly the maps looked choatic, much like if you employed a toddler to draw their finest scribble on a map, this debilitates ones aptitude to visualise their run in the intended manner. 

Now being unable to view a map of the route taken in your run admittedly is annoying, but of the three issues, you might say it falls last in priority. If so you are probably right, however at the time of conducting this project I was still baring the afterglow of a beautiful morning run, edorphins and adreneline were running through my vains, logic had taken a backseat, the lack of a simple yet playful visual of my overhead route was not just an inconvenience, it was a cry for help! Determined to be deprived no longer, I fired up my laptop, opened my IDE, and got to work, Issue 3 was of paramount importance.


Thought process No1

Can I manually change the adjust the map, in a drag and drop fashion - similiar to https://onthegomap.com/#/create 's 'how far did I run?' - to fix all these issues? Adjusting the coordinates in this way is not supported by garmin directly, I even attempted to use Golden Cheetah with no success. Effort to resolve the issue in this way did not go to waste, as it was through the process of downloading the workout data from garmin - in order to upload it to the Golden Cheeter application - that I discovered Garmin's XML equivalent TCX (Training Center XML). 

Available File Formats: ![downloadtcx](Files/downloadtcx.png)

I knew I could easily enough go into the file, plug in the right coordinates, and re-upload the file to garmin, but there were 1000s of records to change. But, I had a great idea! A Python script could make short work of the repititious task. 

// Searching  with the knowledge that garmin stores their data in a tcx file (a type of xml) repairing this deta in the source file manually seemed to be the most viable option, but with 1000s of data points to adjust doing this line by line would be tedious and big word. Insert python. 

// As it turns out, the workout data could be remediated by accessing and adapting the corresponding TCX - Training Center XML - file. My goal was simple, download the xml file and find the affected tackpoints, create data that reflects true to facts coordinates, reupload, enjoy. Simple enough. 




To give you an idea of what the file looks like, here is as snippet: 

![TCX Example](Files/tcxexample.png)


Before moving onto the main script, I needed to prepare the replacement data. This meant finding the coordinates of my run. For this I used https://www.gpsvisualizer.com/draw/

![gpsvisualiser](Files/gpsvisualiser.png)

This is an example of what some of the downloaded cordinates look like:

![Coordinates](Files/Coordinates.png)

As distinct from a circular route, the run followed what you wouuld call an out-and-back route, starting from a desired location, travelling to a midway checkpoint, followed by retracing your steps and eventually finishing where you started. Therefore my data points only represented half of the route and I had to add a reversed set of the coordinates to the end. To save time I used this:                  (go into what code means and what i used and what i learned)

![Out and Back Data Reversing py File](src/outandback-reverse.py)

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


With my Out and Back Coordinates saved in a handy Tab-Separated-Value file I was almost ready to start replacing my TCX File coordinates. 

However there was one small discrepency. When plannning my route and extracting the corrected cordinates, I simply droped markers at every turning point and took little notice to the distances between each marker, additionally the total number of paired Latitude and Longitude coordinates - including the reversed set - amounted to 87. The discrepency appears once you consider that during a workout a Garmin watch records data every second, with each second represented as a single Trackpoint within a TCX file. In consequence a thirty minute workout produces 1800 Trackpoints. Since each trackpoint contains metrics like Distance, Latitude, and Longitude; and every Trackpoint needed modification, I had to interpolate my 87 coordinates. 

///Could explain the interpolation and spreading between equal distances +  wont cover now but good to mention another step would be required to create a more correct synergy of metrics (will provide later, pace vs distance calc)-- 

To view the Python script I used to calculate the number of Trackpoints within a TCX (right click to open in new tab): [Count Trackpoints Code](src/count-trackpoints.py)

This is the python script I used to interpolate the newly generated precise coordinates - to a equal the sum total trackpoints measured in the previous step - and to ensure they are equally spaced. ![Data-Interpolation](src/data-interpolation.py)

During this step the geodesic module from the library geopy.distance was used to calculate distances. Here is a higher-level overview of the script:

```python 
import pandas as pd
import numpy as np
from geopy.distance import geodesic
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

# Format the resampled coordinates to 7 decimal places
formatted_coords = format_coordinates(resampled_coords, 15, 14)

# Save the resampled coordinates to a new file
resampled_data = pd.DataFrame(formatted_coords, columns=['latitude', 'longitude', 'distance_meters'])
resampled_data.to_csv(folder / 'resampled_coordinates.txt', index=False, sep='\t')
```

At this point, I have my /Data/resampled_coordinates.txt file - a TSV file containing 1800 equally distanced coordinates - accurately representing my morning-run. 

All I had to do, was parse the original TCX file and replace each Latitude, Longitude, and DistanceMeters variable. 

To acheive this, I used the following Python code: ![Parse and Replace](src/parse-and-replace.py)

To provide a short summary what takes place during the script, here is a higher-level overview:

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

With that, our newly created TCX file - /tcx/modified_file.tcx - is ready to be uploaded to Garmin Connect!

The Result:

![Final Run](Files/FinalRun.png)


## Limitations

manuual workaround 

using pace, + non gps run + 



Implementation Details

Provide a high-level overview of your final solution.
Focus on key parts of the code and their functions.
Explain any important decisions or trade-offs you made.

Maybe a tree or graph showing overall process






i hope this shows the usefulness of python and libraries 


Outcome and Reflection

Summarize the outcome of your project.
Reflect on what you learned and how you grew from the experience.
Mention how this experience has prepared you for future projects.

Conclusion
Wrap up with a final thought or takeaway message.
End on a positive note, reinforcing the value of the experience.

## Future Work
Enhancements
New Project Ideas
### Research Opportunities

### Licence

This project is licensed under the MIT License - see the ![LICENSE](/LICENSE) file for details.

### Contact Information

If you have any questions or comments about the project, or if you're interested in contributing, feel free to reach out:

- **Project Maintainer**: Emilios Richards
- **Email**: emiliosmrichards@gmail.com
- **GitHub Profile**: [EmiliosRichards](https://github.com/EmiliosRichards)

Gif bye