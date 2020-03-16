# import os for file directory
import os
# import pandas to read excel file
import pandas as pd
# import distance calculator
import distance as dst

# directory of the folder with excel file
folder_dir = __file__[0:__file__.rfind("\\")]

# dataframe containing location file
df_locations = pd.read_excel(folder_dir + "\\Locations.xlsx")
# dataframe containing ride group file
df_ride_groups = pd.read_excel(folder_dir + "\\Ride Group Template.xlsx")

# list of drivers and passengers
drivers = []
passengers = []
for index in range(len(df_ride_groups['Rides'])):
    if df_ride_groups['Rides'][index] == 'Yes':
        drivers.append((df_ride_groups['Name'][index],df_ride_groups['Car Size (including driver)'][index]))
    else:
        passengers.append((df_ride_groups['Name'][index],df_ride_groups['Drop Off'][index]))

print(drivers)  
print(passengers)

# cluster people who live close to each other

    

dst.distance(1,2)