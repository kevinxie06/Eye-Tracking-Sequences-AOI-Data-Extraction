# Documentation
This documentation provides a detailed overview of the data extracted. 

## Rows and Columns

The rows in the dataset follow a *chronological order*, where each consecutive row represents the sequence in which the individual looked at and fixated on different items of interest. For instance, the first row indicates the first **Area of Interest (AOI)** that the individual focused on, while the very last row indicates the last AOI that the individual focused on during the study.


**Each output file contains four output columns:**
- *Chart Name*
- *Name of AOI Hit*
- *Time Stayed (seconds)*
- *Row Numbers*

The **"Chart Name"** indicates the chart number that the individual was looking at.

The **"Name of AOI Hit"** refers to the specific area within the chart that the individual fixated on.

The **"Time Stayed"** describes the time that the individual fixated on the specific AOI. 

The **"Row Numbers"** simply describes the rows in the excel file used to extract the data. This column mainly serves to help the validation of the extracted AOI data and to track any potential outliers. 


## No Hits
Within the output files, you may observe instances where the "Name of AOI Hit" field displays **"NO HIT"** instead of a specific AOI name. This occurrence signifies that the eye tracking software did not register any fixations on any of the Areas of Interest (AOIs) during that particular period.

The absence of hits could suggest that the individual may have looked away from the screen at that time, but the exact reason remains unknown. The corresponding duration when the software did not detect hits is also provided in the **"Time Stayed (seconds)"** column.

