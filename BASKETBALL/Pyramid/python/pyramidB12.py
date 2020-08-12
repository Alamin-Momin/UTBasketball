#import libraries
import pandas as pd
import os

# Every path to a file
# paths and names of files may need to be altered

PATH_TO_DATASET=r'C:\collegebb\College Analytics\Pyramid201920'
Pyramid_data_path = 'PyramidData_201920_Total.csv'

# convert to pd df
df = pd.read_csv(os.path.join(PATH_TO_DATASET, Pyramid_data_path))

# cut non b12 teams

# Define B12 list
B12_list = ["Iowa St.", "Baylor", "Texas Tech", "Kansas", "Texas", "Oklahoma", "TCU", "West Virginia", "Oklahoma St.", "Kansas St."]

results = []
for i in range(len(df)):
    if df["TeamName"].iloc[i] not in B12_list:
        results.append(i)
df = df.drop(results)

# add B12 rankings for every column
df["O_B12RankeFGPct"] = 0
df["O_B12RankTOPct"] = 0
df["O_B12RankORPct"] = 0
df["O_B12RankFTRate"] = 0
df["D_B12RankeFGPct"] = 0
df["D_B12RankTOPct"] = 0
df["D_B12RankORPct"] = 0
df["D_B12RankFTRate"] = 0
df["D_B12RankDRPct"] = 0
df["O_B12RankAdjOER"] = 0
df["D_B12RankAdjDER"] = 0
df["O_B12RankRawOER"] = 0
df["D_B12RankRawDER"] = 0
df["B12RankAdjNetR"] = 0
df["B12RankRawNetR"] = 0

rank_columns = ["O_RankeFGPct", "O_RankTOPct", "O_RankORPct", "O_RankFTRate", "D_RankeFGPct", "D_RankTOPct", "D_RankORPct", "D_RankFTRate", "D_RankDRPct", "O_RankAdjOER", "D_RankAdjDER", "O_RankRawOER", "D_RankRawDER", "RankAdjNetR", "RankRawNetR"]
new_rank_columns = ["O_B12RankeFGPct", "O_B12RankTOPct", "O_B12RankORPct", "O_B12RankFTRate", "D_B12RankeFGPct", "D_B12RankTOPct", "D_B12RankORPct", "D_B12RankFTRate", "D_B12RankDRPct", "O_B12RankAdjOER", "D_B12RankAdjDER", "O_B12RankRawOER", "D_B12RankRawDER", "B12RankAdjNetR", "B12RankRawNetR"]

# loop through newly created ranking lists and add them to the df accordingly
for i in range(len(rank_columns)):
    # get the current rank column that you want to transfer to just B12
    current_col = rank_columns[i]
    # sort the df by this column
    df = df.sort_values(by = current_col)
    # get the new ranking column
    new_col = new_rank_columns[i]
    # loop through df and add new B12 rankings to corresponding columns
    for j in range (len(df)):
        df[new_col].iloc[j] = j + 1


# Convert Dataframe to to_csv
# paths and names of files may need to be altered

export_csv = df.to_csv (r'C:\collegebb\College Analytics\Pyramid201920\PyramidB12Data_201920_Total.csv', index = False)