# Eye Tracking Sequences Data Extraction
**Kevin Xie, Dr. Jinjuan Heidi Feng**

**Affiliations**: Towson University: Department of Computer and Information Sciences

## Overview
When presented with any visual stimuli, individuals naturally focus on certain areas. Utilizing eye tracking software allows the collection of data concerning these **Areas of Interest (AOI)**, pinpointing where the eyes fixate and when these fixations occur.

By extracting and processing this data, further visualization and analysis can be conducted to **understand more about human cognitive processes**. Eye tracking data is crucial in various fields, including psychology, user experience research, and human-computer interaction. 

**This repository contains the code for extracting eye tracking data and processing the collected data sheets from Tobii Eye Tracker Software.**

It provides a streamlined process for extracting raw eye tracking data and generating processed data sheets for analysis, **significantly reducing the time and labor required to filter through millions of lines of data.**

## Installation
Ensure you have Python 3.9+ and Pandas installed:
- [Python](https://www.python.org/downloads/)
- [Pandas](https://pandas.pydata.org/)

Install the necessary dependencies using:
```
pip install pandas
```

## Research Overview
This section provides an overview of the research process.

### Tobii Software
All data was collected using the [Tobii Eye Tracking Software](https://www.tobii.com/).

Tobii classified eyegaze events to **3 categories**: fixation, saccades, and unclassified.
 
**Fixation**: The period when eyes essentially stop scanning a visual scene and remain relatively still. Fixations allow holding a stationary object of interest on the fovea for a detailed visual information intake.
- Composed of slower, smaller-scale eye movements (microsaccades, tremors, and drifts) that help the eye align with the target and avoid perceptual fading (fixational eye movements).
- The duration varies between 50-600 ms.
- The minimum duration required for information intake depends on the task and stimulus at hand (Land & Tatler, 2012; Rayner, 2009).
 
**Saccades**: Rapid, ballistic eye movements between fixations that bring an area of the visual scene onto the fovea (Hessels et al., 2018). The vision is highly suppressed during saccades, which allows for continuous and stable perception during saccadic reorientation. Human perception is guided by alternating sequences of fixations and saccades.
- Binocular and conjugate.
- The average duration of a saccade is 20-40 ms.
- The endpoint of a saccade cannot be changed when the eye is moving (Land & Tatler, 2012; Rayner, 2009).
 
**Unclassified**: Eyegaze events that were not classified as either ‘fixation’ or ‘saccades’.

*The time of ‘no hits’ in our extracted data files include the time of saccades and ‘no hits’.*

<p align = "center">
<img width="1292" alt="Eye Tracking Data Example" src="https://github.com/kevinxie06/Eye-Tracking-Project/assets/135569406/b438504c-517a-4c29-80c6-bc329dc6891d">
Raw Data

### Data Collection
**50 volunteers** participated in our study. They were each presented with **four different visual stimuli**:

<p align = "center">
<img width="600" height = "510" alt="AOI 1" src="https://github.com/kevinxie06/Eye-Tracking-Project/assets/135569406/ebbb363e-5d69-4e41-8b00-4b7e3b620479">
<img width="600" height = "510" alt="AOI 2" src="https://github.com/kevinxie06/Eye-Tracking-Project/assets/135569406/0a3c3599-b02f-42da-b882-3a2d62d3c30a">
<img width="600" height = "510" alt="AOI 3" src="https://github.com/kevinxie06/Eye-Tracking-Project/assets/135569406/9938de1c-41c3-4428-916f-995d67e1006c">
<img width="600" height = "510" alt="AOI 4" src="https://github.com/kevinxie06/Eye-Tracking-Project/assets/135569406/a4e5f8d0-a73a-458f-aa7e-370a7039edfd">

Each **colored section** of the chart represents an **Area of Interest (AOI)**. During the participants' analysis of the charts, Tobii Software tracked each instance of a participant fixating on an AOI. Both the **specific AOI** and the **corresponding timestamp** were recorded by the software.

Once the participant had finished examining the charts, they were given a series of questions to ensure they had analyzed the chart meaningfully rather than just glancing over it randomly.

## Program Features
- **Data Extraction**: The code includes scripts to extract eye tracking data from various eye tracking devices and formats. It supports common eye tracking file formats, ensuring compatibility with different systems.
- **Data Sheets**: The processed data sheets are generated in user-friendly formats (e.g., CSV, Excel) for easy integration into data analysis tools such as Python, R, or spreadsheet software.
- **Documentation**: Comprehensive documentation is provided to guide users through the extraction and processing steps.


Thank you for visiting my repository. Your suggestions and feedback are greatly appreciated! I hope this resource proves helpful to your research!

Kevin Xie
kevinxie2024@gmail.com

