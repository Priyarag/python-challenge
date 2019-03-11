import pandas as pd
import datetime as dt
import os
import re

employee_csv = os.path.join("..","PyBoss", "employee_data.csv")
employee_data = pd.read_csv(employee_csv)
# new data frame with split value columns 
new_cols_name = employee_data["Name"].str.split(" ", n = 1, expand = True) 
# making seperate first name column from new data frame 
employee_data["First Name"]= new_cols_name[0] 
  
# making seperate last name column from new data frame 
employee_data["Last Name"]= new_cols_name[1] 
  
# Dropping old Name columns 
employee_data.drop(columns =["Name"], inplace = True) 
  
# df display 
#print(employee_data )
employee_data['DOB'] = pd.to_datetime(employee_data['DOB'])
employee_data['DOB'] = employee_data['DOB'].dt.strftime('%m/%d/%Y')
employee_data['SSN'] =  employee_data['SSN'].replace(r'\d\d\d-\d\d-', value='***-**-',regex=True) 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
employee_data['State'].replace(us_state_abbrev, inplace=True)
organized_data = employee_data[["Emp ID","First Name","Last Name","DOB","SSN","State"]]
organized_data.to_csv("OrganizedEmpData.csv", index=False, header=True)