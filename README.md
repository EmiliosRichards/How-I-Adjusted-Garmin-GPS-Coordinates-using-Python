# XML-Workout-Data-GPS-Interpolation

Welcome! The following document contains the details of a small issue I had and what I did to overcome it. Find out how I used Python to solve an real-world problem related to my Gamrin Multisport GPS Watch and how the implications of the Isreal-Palistine conflict incentivised some deeper learning of 3 Python Libraries. 

# Document Contents 

- [**Introduction**](#Introduction): Provides context to the problem. Reveals the requirement for a solution. 

# Introduction 

To provide some context, since a child I've relished in a variety of sports and as I've grown to become young adult I've maintained that same keen interest, with a my motivation broadening from something i enjoyed to a activity that bringme  shift from having fun to well being and fitness.


My most recent focus is an exercise that some may see as burdensome, albeit challenging at times I see it as an escape from the hustle and bustle of life, its a simple workout that I can only regard as a classic, that is, the art of running. It's a form birthed at childhood that we all know too well, its beauty lays in its simplicity and due to it being one of our most natural movements, it's needless to say running is one of the best investments for your mind and body. As with most of my hobbies, I found great joy in quantifying my progress and seeking ways to improve my ability level. Heartrate and Distance were metrics I soon began to observe. By utilising Garmin's Fenix Multisport GPS watch and their accompanying platform Garmin Connect, I have been able to . The Fenix encompasses a broad range of features and capabilities, including Heart-Rate Monitoring, GPS tracking, and . through Garmin connect, workout data - Mapping the rounts taken during a run.

It is a great watch, and I love the design and features it provides, it has accomplished everything 

with one major exception, the GPS produced perculiar results. It will come at no shock to those who have travelled through the Mediterranean, Baltic, and Middle-Eastern regions that it is no fault of brand or model. The problem I faced stems from a much deeper issue: electronic warfare and our spatial proximity to the Middle-Eastern region. The geopolitical conflict in this area has resulted in GPS and satellite signal disruptions. 


geopolitical conflicts, electronic warefare, satellite and gps interference

Due to the GPS interference, the incorrect coordinates it produced had serveral implications; First, an inaccuracy of distance, : Example meant that a 10k run may show up as 7k or at times even 0.7k. Second -- Gaining insights into the run, accumulated data, and progression of fitness metrics. third -- the maps look silly, and I cant visualise my runs in the inrtended manner. 

can i manually change the coords to fix all these issues? Adjusting this using the garmin or similar programs prooved exceedingly difficult if not impossible, with the knowledge that garmin stores their data in a tcx file (a type of xml) repairing this deta in the source file manually seemed to be the most viable option, but with 1000s of data points to adjust doing this line by line would be tedious and big word. Insert python. 

This is what the workout data looks like. 

As it turns out, the workout data could be remediated by accessing and adapting the corresponding TCX - Training Center XML - file. My goal was simple, download the xml file and find the affected tackpoints, create data that reflects true to facts coordinates, reupload, enjoy. Simple enough. 

The first step was to create correct route through an online map - this gave me details or all turning points. not a linear run, from one point to the next its straight. 

next interpolation - why i need it, to evenly distrubute along the route -- wont cover now but good to mention another step would be required to create a more correct synergy of metrics (will provide later, pace vs distance calc)-- leads to step 

The second step involves calculating the number of coordinates needed in order to manually replace coordinates 

code for interpolation 

calculating distance 

parse and replace file 

maintaining header and format


limitations + 

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

This project is licensed under the MIT License - see the [LICENSE]([https://github.com/EmiliosRichards/File-Management-System/blob/main/LICENSE) file for details.

### Contact Information

If you have any questions or comments about the project, or if you're interested in contributing, feel free to reach out:

- **Project Maintainer**: Emilios Richards
- **Email**: emiliosmrichards@gmail.com
- **GitHub Profile**: [EmiliosRichards](https://github.com/EmiliosRichards)

Gif bye