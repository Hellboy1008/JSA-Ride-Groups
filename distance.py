# Created by: 龍ONE
# Date Created: February 7, 2020
# Date Edited: October 5, 2020
# Purpose: Calculate the distance between two points given longitude and latitude.

# import sys for exiting program
import sys

# import pandas to read excel file
import pandas as pd

# import libraries from math for distance calculation
from math import sin, cos, sqrt, asin, radians

# directory of the folder with excel file
folder_dir = __file__[0:__file__.rfind('\\')]

# dataframe containing location file
df_locations = pd.read_excel(folder_dir + '\\Locations.xlsx')

# calculate distances


def distance(pointA, pointB):
    # remove capitalization from locations
    pointA = pointA.lower()
    pointB = pointB.lower()

    pointA_location = None
    pointB_location = None

    # find longitude and latitude of the place
    for index in range(len(df_locations['Place'])):
        if df_locations['Place'][index].lower() == pointA:
            pointA_location = (
                radians(df_locations['Longitude'][index]), radians(df_locations['Latitude'][index]))
        if df_locations['Place'][index].lower() == pointB:
            pointB_location = (
                radians(df_locations['Longitude'][index]), radians(df_locations['Latitude'][index]))

    # if the points are not one of the preset locations, return error
    if pointA_location == None:
        print('The location \"' + pointA + '\" is not a valid location')
        sys.exit()
    if pointB_location == None:
        print('The location \"' + pointB + '\" is not a valid location')
        sys.exit()

    # calculate distance using Haversine formula
    longitude_diff = pointA_location[0] - pointB_location[0]
    latitude_diff = pointA_location[1] - pointB_location[1]

    a = sin(latitude_diff / 2) ** 2 + \
        cos(pointA_location[1]) * cos(pointB_location[1]) * \
        sin(longitude_diff / 2) ** 2

    r = 6371
    c = 2 * asin(sqrt(a))

    return r * c
