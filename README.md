# XML-Workout-Data-GPS-Interpolation

Welcome! The following document contains the details a small project working with XML, Interpolation, and python scripts. Find out how I used Python to solve a real-world problem related to my Gamrin Multisport GPS Watch and how the implications of the Isreal-Palistine conflict incentivised some deeper learning of 3 Python Libraries. 

# Document Contents 

- [**Introduction**](#Introduction): Provides context to the problem. Reveals the requirements for a solution. 

# Introduction 

To provide some context, since a child I've relished in a variety of sports and as I've grown to become young adult I've maintained that same keen interest, over the years what started out as an enjoyable pass-time, expanded to become a core value contributing to my wellbeing and health. My most recent focus is an exercise that some may see as burdensome, albeit challenging at times I see it as an escape from the hustle and bustle of life, its a simple workout that I can only regard as a classic, that is, the art of running. It's a form birthed at childhood that we all know too well, its beauty lies in its simplicity and with it being one of our most natural movements, it's needless to say running is among the best investments one can make for their body and mind. As with most of my hobbies, I found great joy in quantifying my progress and seeking ways to improve my ability level. Heartrate and Distance were metrics I soon began to observe. This was made easy by utilizing Garmin's Fenix Multisport GPS watch and their accompanying platform Garmin Connect. The Fenix encompasses a broad range of features and capabilities for measuring essential workout metrics, including Heart-Rate Monitoring, GPS tracking, recovery insights and much more. Garmin connect on the other hand, is a platform that can hold your data, allowing a holistic overwiew of progress through an intuituve interface, its main usage include: visualising the geographical rounts taken, and valuable insights facilitated by readily available workout statistics.

It is a great watch and I love the ergonomical design, however there was a giant issue that I soon encountered. The GPS produced perculiar results, not only was the map visual misaligned, the distance metric was rendered useless. Was something wrong with the Garmin Watch? No. It will come at no shock to those who have travelled through the Mediterranean, Baltic, and Middle-Eastern regions that these results are no fault of brand or model. The problem I faced stems from a much deeper issue: electronic warfare and our spatial proximity to the Middle-Eastern region. The geopolitical conflict in this area has resulted in GPS and satellite signal disruptions. Many areas of life are being affected, to list a few: flight navigation and air traffic control, delays in emergency serives such as ambulances, police and fire-services, these are all underpinned by the finacial impact and psycological strain. I bring forward my experience not to diminish that of what is going on around us, but instead to bring light to a comparitively small, yet very real conscequence of the ongoing conflict. With that being said, I was all the more determined to reconcile the problem I was facing. 

geopolitical conflicts, electronic warefare, satellite and gps interference -- the interference in my GPS coord is one of the many (disruptions) being felt by people. Although this issue is a small compared to many people are currently facing, it still a ery real byproduct of the war. With that being said,

## Initial problem solving

Due to the GPS interference, the incorrect coordinates it produced had serveral implications; First, an inaccuracy of distance, Example: A 10k run may show up as 7k or at times even 0.7k. Second, skewed variables renders Garmin Connect and gaining insights through it, ineffective; accumulated data and fitness progression, non-existant. Lastly the maps look choatic, much like if you employed a toddler to draw their finest scribble on a map, therefore debilitating ones aptitude to visualise their run in the intended manner. The final issue may be the least impactful of the three, yet in my heart, solving it was of paramount importance.


Thought process No1

Can I manually change the adjust the map, in a drag and drop fashion - similiar to https://onthegomap.com/#/create 's 'how far did I run?' - to fix all these issues? Adjusting this using the garmin or similar programs prooved exceedingly difficult if not impossible. Searching  with the knowledge that garmin stores their data in a tcx file (a type of xml) repairing this deta in the source file manually seemed to be the most viable option, but with 1000s of data points to adjust doing this line by line would be tedious and big word. Insert python. 

This is what the workout data looks like. 

As it turns out, the workout data could be remediated by accessing and adapting the corresponding TCX - Training Center XML - file. My goal was simple, download the xml file and find the affected tackpoints, create data that reflects true to facts coordinates, reupload, enjoy. Simple enough. 





The first step was to create correct route through an online map - this gave me details or all turning points. not a linear run, from one point to the next its straight. 

reversing the data points, (go into what code means and what i used and what i learned)





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