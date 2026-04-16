# AMA Museum data set - contains human-entered data with a lot of inconsistencies.

# Here is some sample code for how to read in csv to extract the text fields. "import re" gives you access to regex.

import  re
import csv

#TODO: add to this program
    # clean the data using your functions 
    # write the cleaned data into a new csv file (optional but helpful for next step)
    # put the cleaned data into a dataframe
    #    - use your cereal_analysis python file as a template to read from csv

with open('ama.csv') as records:
    reader = csv.reader(records)
    entries = [] #this will store the rows in dictionary form
    next(reader)  #skip header
    count = 0
    for row in reader:
        new_row = dict()
        if count< 6:
            print(row)
            print(row[0])
            new_row['Exit_Year'] = row[1]
            new_row['Last_Name'] = row[0]
            entries.append(new_row)
        count+=1

with open('alumni_clean.csv', 'w', newline='') as new_file:
    csv_writer = csv.DictWriter(new_file,fieldnames=['Last_Name','Exit_Year'])
    csv_writer.writeheader()
    csv_writer.writerows(entries)

def is_empty(year:str) -> bool:
    if len(year) == 0:
        #if value is empty remove from df
        return True
    else:
        return False

def is_not_student(year:str) -> bool:
    if re.search(r'Faculty',year) is None:
        return False
    #if value is true remove from df
    return True

def has_year(year:str) -> bool:
    if re.search(r'^\d+',year) is None:
        #if value is false remove from df
        return False
    return True

def get_year(year:str) -> int|None:
    #get the first 1-4 digits from the string
    val = re.findall('^[0-9]+',year)
    if len(val) > 0:
        return int(val[0])
    return None

def add_19(year:int) -> int:
    if(year>100):
        return year
    return 1900 + year

