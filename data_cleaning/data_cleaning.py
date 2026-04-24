# AMA Museum data set - contains human-entered data with a lot of inconsistencies.

# Here is some sample code for how to read in csv to extract the text fields. "import re" gives you access to regex.

import  re
import csv
import pandas as pd 
import matplotlib.pyplot  as plt

# exit year functions
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
    if re.search(r'^[0-9]+',year) is None:
        #if value is false remove from df
        return False
    return True

def get_year(year:str) -> int|None:
    #get the first 1-4 digits from the string
    val = None
    if is_empty(year):
        return None
    if is_not_student(year):
        return None
    if has_year(year):
        val = re.findall('^[0-9]+',year)
    if val:
        return int(val[0])
    return None

def add_19(year:int) -> int:
    if(year>2000):
        return year - 100
    if(year>100):
        return year
    return 1900 + year

def clean_exit_year(row1: str) -> int|None:
    v = get_year(row1)
    if v is None:
        return None
    return add_19(v)

#birth year functions

def has_birthday_field(bd: str) -> bool:
    if len(bd) == 0:
        return False
    return True

def has_birth_year(bnd: str) -> bool:
    if len(bnd) == 0:
        return False
    if re.search(r'^Died',bnd) is not None:
        return False
    if re.search(r'^DOD',bnd) is not None:
        return False
    if re.search(r'DOB:\s\?', bnd) is not None:
        return False
    if re.search(r'DOB:\sUNK',bnd) is not None:
        return False
    return True

def get_birth_year(bnd: str) -> int|None:

    val1 = re.findall('\d+\/\d+\/(\d+)',bnd)
    val2 = re.findall('\d{4}', bnd)
    if len(val1) != 0:
        val = int(val1[0])
        return add_19(val)
    if len(val2) != 0:
        val = int(val2[0])
        return add_19(val)
    return None

def clean_birthday(row4:str) -> int|None:
    if has_birthday_field(row4):
        return get_birth_year(row4)
    return None

def clean_birth_year(row3:str) -> int|None:
    if has_birth_year(row3):
        return get_birth_year(row3)
    return None

def clean_entries(ent:list) -> pd.DataFrame:
    df = pd.DataFrame(entries)
    df['Age_at_Exit'] = df['Exit_Year'] - df['Birth_Year']
    df = df.loc[(df['Age_at_Exit'] > 7) & (df['Age_at_Exit'] < 23)]
    df = df.loc[(df['Birth_Year'] >= 1857) & (df['Birth_Year'] <= 1980)]
    df = df.loc[(df['Exit_Year'] >= 1880) & (df['Exit_Year'] <= 1984)]
    return df

with open('alumni_birthdays.csv') as records:
    reader = csv.reader(records)
    entries = [] #this will store the rows in dictionary form
    next(reader)  #skip header
    count = 0
    for row in reader:
        # print(row)
        # print(row[0])
        new_exit_year = clean_exit_year(row[1])
        new_birth_year = clean_birthday(row[5])
        if new_birth_year is None:
            new_birth_year = clean_birth_year(row[4])
        if new_exit_year is not None and new_birth_year is not None:
            new_row = dict()
            new_row['Id'] = row[3]
            new_row['Last_Name'] = row[0]
            new_row['Exit_Year'] = new_exit_year
            new_row['Birth_Year'] = new_birth_year
            # print(new_row)
            entries.append(new_row)
    df = clean_entries(entries)


# with open('alumni_clean.csv', 'w', newline='') as new_file: 
#     csv_writer = csv.DictWriter(new_file,fieldnames=['Last_Name','Exit_Year','Id','Birth_Year'])
#     csv_writer.writeheader()
#     csv_writer.writerows(entries)

df.to_csv('alumni_clean.csv', index=False)

total = df['Age_at_Exit'].value_counts().sort_index()
plt.bar(x=total.index,height=total.values,color='darkblue')
plt.xlabel('Age at Exit')
plt.ylabel('Count')
plt.title('Count of Ages at Exit')
plt.savefig('Age_Count',dpi=200)
plt.show()

av = df.groupby('Exit_Year')['Age_at_Exit'].mean()
plt.plot(av.index,av.values,color='darkblue')
plt.title('Average Age at Exit per Year')
plt.xlabel('Year')
plt.ylabel('Average Age at Exit')
plt.savefig('Year_Average',dpi=200)
plt.show()