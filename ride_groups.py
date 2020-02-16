# import os for file directory
import os
# import pandas to read excel file
import pandas as pd

# directory of the folder with excel file
folder_dir = __file__[0:__file__.rfind("\\")];

# dataframe containing excel file
df = pd.read_excel(folder_dir + "\\Ride Group Template.xlsx");

print(df.columns);
print(df['Name']);