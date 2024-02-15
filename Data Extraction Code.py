import pandas as pd

# Kevin Xie

def function(file_path, column_names, output_columns, timestamp_columns, chart_column, list_number):
    
    df = pd.read_excel(file_path, usecols = column_names)

    # All timestamps from excel
    time_df = pd.read_excel(file_path, usecols= timestamp_columns)

    # Chart data
    chart_name_df = pd.read_excel(file_path, usecols = chart_column)

    # Create data frame with appropriate output columns
    output_file = pd.DataFrame()
    for i in range(0,3):
        output_file[output_columns[i]] = '' 

    # Tracks the indices of each UNIQUE hit
    hit_list = []   

    # Stores all appended times from conditions
    time_list = []

    # Stores corresponding hits
    chart_list = []
 
    # Index Lists
    index_list = []
    
    # Extracts every hit (unfiltered) in three lists (hit, time, chart)
    for row in range(0, len(df) - 1):
        hit_tracker = 0
        col_tracker = 0

        for column in range(len(column_names)):
                col_tracker += 1
        
                # Check for any rows that have NO HITS
                if col_tracker == len(column_names):
                    if (df.iloc[row, column] == 1):
                        hit_tracker = 1

                    if hit_tracker != 1:
                        hit_list.append('NO HITS')
                        time_list.append(time_df.iloc[row, 0])
                        chart_list.append(chart_name_df.iloc[row, 0])

                        index_list.append(row)
                            
                    col_tracker = 0
                    hit_tracker = 0

                else:
                    if (df.iloc[row, column] == 1):
                        hit_tracker = 1

                # Check for the hits in all of the columns in each row
                if (df.iloc[row, column]) == 1:
                    if column < (len(column_names) - 1):

                        # If there is more than 1 hit in a row, select only one of them to extract
                        # For P6 - P49, AOI[Rectangle 4]Hit was extracted when there were >1 hits
                        if (df.iloc[row, column] == 1) and (df.iloc[row,column + 1] == 1):
                            hit_list.append('AOI[Rectangle 4]Hit')
                            #hit_list.append('AOI[Key]Hit')

                            time_list.append(time_df.iloc[row, 0])
                            chart_list.append(chart_name_df.iloc[row, 0])

                            index_list.append(row)
                            
                        elif (df.iloc[row, column] == 1) and (df.iloc[row,column - 1] != 1):
                            hit_list.append(column_names[column])
                            time_list.append(time_df.iloc[row, 0])
                            chart_list.append(chart_name_df.iloc[row, 0])
                            
                            index_list.append(row)
                           
                    else:
                        if (df.iloc[row, column] == 1) and (df.iloc[row,column - 1] != 1):
                            hit_list.append(column_names[column])
                            time_list.append(time_df.iloc[row, 0])
                            chart_list.append(chart_name_df.iloc[row, 0])

                            index_list.append(row)

                    
    # Creating final output lists
    final_hit_list = []
    final_time_list = []
    final_chart_list = []
    final_index_list = []

    # Filtering each list (checking for consecutive hits)
    # Uses the consecutive hits to calculate time of fixation.
    for i in range(len(hit_list)):

        if i == 0:
            if hit_list[i] == hit_list[i + 1]:
                final_hit_list.append(hit_list[i])
                final_chart_list.append(chart_list[i])

                initial_time = time_list[i]
                initial_index = str(index_list[i] + 2)

            elif hit_list[i] != hit_list[i + 1]:
                final_hit_list.append(hit_list[i])
                final_chart_list.append(chart_list[i])

                initial_time = time_list[i]   
                final_time = time_list[i+1]

                # Calculates the final time
                final_time_list.append((final_time-initial_time)/1000)

                # Index of hit
                initial_index = str(index_list[i] + 2)
                final_index = str(index_list[i] + 1 + 2)
                final_index_list.append(initial_index + ', ' + final_index)

        if i >= 1 and i < len(hit_list) - 1:
            # Single, non-consecutive hit
            if (hit_list[i] != hit_list[i-1]) and (hit_list[i] != hit_list[i+1]):
                # Hit
                final_hit_list.append(hit_list[i])  
                final_chart_list.append(chart_list[i])

                # Time
                initial_time = time_list[i]    
                final_time = time_list[i+1]

                # Calculates final time
                final_time_list.append((final_time-initial_time)/1000)

                # Index of hit
                initial_index = str(index_list[i] + 2)
                final_index = str(index_list[i] + 1 + 2)
                final_index_list.append(initial_index + ', ' + final_index)

            else:    
                # Consecutive hit
                if (hit_list[i] != hit_list[i-1]) and (hit_list[i] == hit_list[i+1]):
                    # Hit
                    final_hit_list.append(hit_list[i])
                    final_chart_list.append(chart_list[i])

                    # Time
                    initial_time = time_list[i]

                    # Index of hit
                    initial_index = str(index_list[i] + 2)

                # Sandwiched hit
                elif (hit_list[i] == hit_list[i + 1]) and (hit_list[i] == hit_list[i-1]):
                    continue
                
                # End hit
                elif (hit_list[i] != hit_list[i + 1]) and (hit_list[i] == hit_list[i-1]):
                    final_time = time_list[i+1]

                    # Calculates final time
                    final_time_list.append((final_time-initial_time)/1000)

                    # INDEX
                    final_index = str(index_list[i] + 1 + 2)
                    final_index_list.append(initial_index + ', ' + final_index)

        # Check the final hit
        elif i == len(hit_list) - 1:
            if hit_list[i] == hit_list[i-1]:
                final_time = time_list[i]

                # Calculates final time
                final_time_list.append((final_time-initial_time)/1000)

                # Index of the final hit
                final_index = str(index_list[i] + 1 + 2)
                final_index_list.append(initial_index + ', ' + final_index)


    # Updating empty output df with extracted, filtered data
    output_file['Chart Name'] = final_chart_list
    output_file['Name of AOI Hit'] = final_hit_list
    output_file['Time Stayed (seconds)'] = final_time_list
    output_file['Row #'] = final_index_list

    # Outputs the extracted data to desired output path
    # Change the path, excel file name, and sheet name
    output_file.to_excel('/Users/kevinxie/Desktop/TU Intern Folder/Eye Tracking Project/Final Processed Data/P' + str(list_number) +'_Processed_Data.xlsx', sheet_name = 'P' + str(list_number) + 'Processed Data')

# Used for Participants 6 - 49
AOIcols = ['AOI[Title]Hit',
                'AOI[Main Data]Hit',
                'AOI[Rectangle 4]Hit',
                'AOI[Y axis]Hit',
                'AOI[X axis]Hit',
                'AOI[Help text]Hit',
                'AOI[Main chart]Hit',
                'AOI[Title]Hit_1',
                'AOI[Y axis (Solar)]Hit',
                'AOI[Y axis (Temp)]Hit',
                'AOI[X axis]Hit_2',
                'AOI[Title]Hit_3',
                'AOI[AI and AN Reading Data]Hit',
                'AOI[Asian Reading Data]Hit',
                'AOI[Black Reading Data]Hit',
                'AOI[Hispanic Reading Data]Hit',
                'AOI[White Reading Data]Hit',
                'AOI[AI and AN Math Data]Hit',
                'AOI[Asian Math Data]Hit',
                'AOI[Black Math Data]Hit',
                'AOI[Hispanic Math Data]Hit',
                'AOI[White Math Data]Hit',
                'AOI[Title]Hit_4',
                'AOI[Key]Hit',
                'AOI[Main Chart]Hit.1',
                'AOI[Y axis]Hit_5',
                'AOI[Chart Help Text]Hit']


# Used for Participants 2 - 5
# AOIcols = ['AOI[Title Bar]Hit',
#            'AOI[Y axis]Hit',
#            'AOI[X axis]Hit',
#            'AOI[Help Text]Hit',
#            'AOI[Key]Hit',
#            'AOI[Main]Hit',
#            'AOI[Y axis 2]Hit',
#            'AOI[Title Bar]Hit_1',
#            'AOI[Main]Hit_2',
#            'AOI[Y - Axis (Solar)]Hit',
#            'AOI[Y - Axis (Temp)]Hit',
#            'AOI[X - Axis]Hit',
#            'AOI[Key (Temp)]Hit',
#            'AOI[Help Text]Hit_3',
#            'AOI[Key (Solar)]Hit',
#            'AOI[Title Bar]Hit_4',
#            'AOI[Reading]Hit',
#            'AOI[Reading Y -Axis]Hit',
#            'AOI[Reading X - Axis]Hit',
#            'AOI[AI AN - R]Hit',
#            'AOI[Asian - R]Hit',
#            'AOI[Black - R]Hit',
#            'AOI[Hispanic - R]Hit',
#            'AOI[White - R]Hit',
#            'AOI[Math]Hit',
#            'AOI[Math Y - Axis]Hit',
#            'AOI[Math X - Axis]Hit',
#            'AOI[AI AN - M]Hit',
#            'AOI[Asian - M]Hit',
#            'AOI[Black - M]Hit',
#            'AOI[Hispanic - M]Hit',
#            'AOI[White - M]Hit',
#            'AOI[Title Bar]Hit_5',
#            'AOI[Help Text 1]Hit',
#            'AOI[Key]Hit_6',
#            'AOI[X - Axis]Hit_7',
#            'AOI[Y - Axis]Hit',
#            'AOI[Main]Hit_8',
#            'AOI[Help Text 2]Hit']


timestamp_columns = ['RecordingTimestamp']

output_columns = ['Chart Name', 'Name of AOI Hit', 'Time Stayed (seconds)', 'Row #']

chart_column = ['MediaName']


# Change the path to data file
for i in range(6, 50):
    function('/Users/kevinxie/Desktop/TU Intern Folder/Participant Excel Sheets/P' + str(i) + ".xlsx", AOIcols, output_columns, timestamp_columns, chart_column, i)

# function('/Users/kevinxie/Desktop/TU Intern Folder/Participant Excel Sheets/P21.xlsx', AOIcols, output_columns, timestamp_columns, chart_column, 21)
