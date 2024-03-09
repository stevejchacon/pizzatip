''' 
This script will take the raw CSV file exported from the HoursTracker app and 
perform both cleaning and modification. More cleaning and modification are done
in the pizzaCleaning.ipynb Jupyter notebook.
'''

import calendar
import pandas as pd

# function to determine the season that date falls in
def which_season(date):
  month = date.month

  if month in [12, 1, 2]: # winter
    return "Winter"
  
  elif month in [3, 4, 5]: # spring
    return "Spring"

  elif month in [6, 7, 8]: # summer
    return "Summer"

  else: # fall
    return "Fall" 

# function to find holidays that fall on the same day every year
def same_day_holiday(df):

    # loop through each row to locate potential holiday
    for i, row in df.iterrows():
        # Valentine's Day
        if(row['Month'] == 2 and row['Day'] == 14):
            df.loc[i, 'Holiday Name'] = "Valentine's Day"
            df.loc[i, 'Is Holiday']   = True
            
        # St Patrick's Day
        elif(row['Month'] == 3 and row['Day'] == 17):
            df.loc[i, 'Holiday Name'] = "St. Patrick's Day"
            df.loc[i, 'Is Holiday']   = True

        # Halloween
        elif(row['Month'] == 10 and row['Day'] == 31):
            df.loc[i, 'Holiday Name'] = "Halloween"
            df.loc[i, 'Is Holiday']   = True

        # Christmas Eve
        elif(row['Month'] == 12 and row['Day'] == 24):
            df.loc[i, 'Holiday Name'] = "Christmas Eve"
            df.loc[i, 'Is Holiday']   = True

        # New Year's Eve
        elif(row['Month'] == 12 and row['Day'] == 31):
            df.loc[i, 'Holiday Name'] = "New Year's Eve"
            df.loc[i, 'Is Holiday']   = True
    
    return df


#-------------------------------------------------------------------------

# function to find Mother's Day
def get_mothers_day(year):

    # May's first day of the week and number of days
    first_day_of_may, may_days = calendar.monthrange(year, 5)
    
    # Calculate the second Sunday
    if first_day_of_may == 6: # Sunday
        return pd.Timestamp(year, 5, 8)
    else:
        return pd.Timestamp(year, 5, 14 - first_day_of_may)

# function to find Father's Day
def get_fathers_day(year):
    # June's first day of the week and number of days
    first_day_of_june, june_days = calendar.monthrange(year, 6)
    
    # Calculate the third Sunday
    if first_day_of_june == 6: # Sunday
        return pd.Timestamp(year, 6, 15)
    else:
        return pd.Timestamp(year, 6, 21 - first_day_of_june)

# fucntion to find Thanksgiving
def get_thanksgiving_day(year):

    # find the first day of November and which day of the week it is
    first_day_of_november, _ = calendar.monthrange(year, 11)

    # calculate the day of the first Thursday in November
    # if the first day of November is a Thursday, then the first Thursday is on the 1st
    if first_day_of_november <= 3:
        first_thursday = 1 + (3 - first_day_of_november)
    # otherwise, calculate the first Thursday
    else:
        first_thursday = 8 - (first_day_of_november - 3)

    # Thanksgiving is the fourth Thursday, so add 21 days to the first Thursday
    thanksgiving_day = first_thursday + 21

    return pd.Timestamp(year, 11, thanksgiving_day)
