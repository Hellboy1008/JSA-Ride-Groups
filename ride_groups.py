# import os for file directory, sys for exiting program, math for nan values
import os
import sys
import math
# import pandas to read excel file
import pandas as pd
# import ride group maker
import make_groups

# directory of the folder with excel file
folder_dir = __file__[0:__file__.rfind('\\')]

# dataframe containing ride group file
df_ride_groups = pd.read_excel(folder_dir + '\\Ride Group Template.xlsx')

# prompt for Uber if needed
uber_to_size = []
num_uber_to = input(
    'How many Ubers do we need to call on the way there? Type 0 if it is not needed: ')
if int(num_uber_to) < 0:
    print('Invalid value for the number of Ubers.')
    sys.exit()
if int(num_uber_to) != 0:
    for index in range(int(num_uber_to)):
        uber_to_size.append(
            input('What is the size of Uber ' + str(index + 1) + ' (5,7,etc.): '))

uber_back_size = []
num_uber_back = input(
    'How many Ubers do we need to call on the way back? Type 0 if it is not needed: ')
if int(num_uber_back) < 0:
    print('Invalid value for number of Ubers.')
    sys.exit()
if int(num_uber_back) != 0:
    for index in range(int(num_uber_back)):
        uber_back_size.append(
            input('What is the size of Uber ' + str(index + 1) + ' (5,7,etc.): '))


# create list of drivers and passengers
drivers_to = []
drivers_back = []
passengers_to = []
passengers_back = []
max_people_to = 0
max_people_back = 0

# add Uber to drivers list if needed
if int(num_uber_to) != 0:
    for index in range(int(num_uber_to)):
        drivers_to.append(('Uber ' + str(index + 1), uber_to_size[index]))
        max_people_to += int(uber_to_size[index])

if int(num_uber_back) != 0:
    for index in range(int(num_uber_back)):
        drivers_back.append(('Uber ' + str(index + 1), uber_back_size[index]))
        max_people_back += int(uber_back_size[index])

# make different groups for to and back
for index in range(len(df_ride_groups['Rides'])):
    if df_ride_groups['Rides'][index] == 'Yes' and df_ride_groups['Only one way driver? (To or Back)'][index] != "Back":
        drivers_to.append(
            (df_ride_groups['Name'][index], int(df_ride_groups['Car Size (including driver)'][index])))
        max_people_to += df_ride_groups['Car Size (including driver)'][index]
    elif df_ride_groups['Rides'][index] == 'No' and df_ride_groups['Only need ride one way? (To or Back)'][index] != "Back":
        if math.isnan(df_ride_groups['Preset rides there? (driver name)'][index]):
            passengers_to.append(
                (df_ride_groups['Name'][index], df_ride_groups['Drop Off'][index], 'No'))
        else:
            passengers_to.append(
                (df_ride_groups['Name'][index], df_ride_groups['Drop Off'][index], df_ride_groups['Preset rides there? (driver name)'][index]))
    if df_ride_groups['Rides'][index] == 'Yes' and df_ride_groups['Only one way driver? (To or Back)'][index] != "To":
        drivers_back.append(
            (df_ride_groups['Name'][index], int(df_ride_groups['Car Size (including driver)'][index])))
        max_people_back += df_ride_groups['Car Size (including driver)'][index]
    elif df_ride_groups['Rides'][index] == 'No' and df_ride_groups['Only need ride one way? (To or Back)'][index] != "To":
        if math.isnan(df_ride_groups['Preset rides there? (driver name)'][index]):
            passengers_back.append(
                (df_ride_groups['Name'][index], df_ride_groups['Drop Off'][index], 'No'))
        else:
            passengers_back.append(
                (df_ride_groups['Name'][index], df_ride_groups['Drop Off'][index], df_ride_groups['Preset rides back? (driver name)'][index]))

num_drivers_to = len(drivers_to)
num_drivers_back = len(drivers_back)
num_passengers_to = len(passengers_to)
num_passengers_back = len(passengers_back)

# end program if we cannot accommodate
if (num_drivers_to + num_passengers_to > max_people_to or num_drivers_back + num_passengers_back > max_people_back):
    print('There are not enough spaces in the cars to accommodate these people')
    sys.exit()

# check if we need different ride groups for to and back
different_ride_groups = False
if drivers_to != drivers_back or passengers_to != passengers_back:
    different_ride_groups = True

print(passengers_to == passengers_back)

# create ride groups as needed
ride_group_to = []
ride_group_back = []
if different_ride_groups == True:
    ride_group_to = make_groups.makeGroups(drivers_to, passengers_to)
    ride_group_back = make_groups.makeGroups(drivers_back, passengers_back)
else:
    ride_group_to = make_groups.makeGroups(drivers_to, passengers_to)

print(drivers_to)
print(passengers_to)
print(max_people_to)
print(drivers_back)
print(passengers_back)
print(max_people_back)
print(num_drivers_to)
print(num_passengers_to)
print(num_drivers_back)
print(num_passengers_back)
print(different_ride_groups)
print(ride_group_to)
print(ride_group_back)
