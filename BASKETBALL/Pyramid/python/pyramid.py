#import libraries
import pandas as pd
import os

# Every path to a file
# paths and names of files may need to be altered

PATH_TO_DATASET=r'C:\collegebb\College Analytics\Pyramid201920'
FF_data_path1 = 'FF_201920_Total.csv'
Eff_data_path = 'Eff_201920_Total.csv'

# convert to pd df
FF1_df = pd.read_csv(os.path.join(PATH_TO_DATASET, FF_data_path1))
Eff_df = pd.read_csv(os.path.join(PATH_TO_DATASET, Eff_data_path))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# get rid of numbers at the end of team names
for i in range(len(Eff_df)):
    team = Eff_df["Team"].iloc[i]
    if team[-2:].isdigit():
        team = team[:-3]
        Eff_df["Team"].iloc[i] = team
    if team[-1:].isdigit():
        team = team[:-2]
        Eff_df["Team"].iloc[i] = team

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# add D_DRPct and D_RankDRPct to FF1_df
FF1_df["D_DRPct"] = 0
FF1_df["D_RankDRPct"] = 0

# add DRPct 
for i in range (len(FF1_df)):
    Opp_ORpct = FF1_df["D_ORPct"].iloc[i]
    DRPct = 100 - float(Opp_ORpct)
    FF1_df["D_DRPct"].iloc[i] = DRPct

# add the rankings 
FF1_df = FF1_df.sort_values(by = "D_DRPct", ascending = False)
for j in range(len(FF1_df)):
    FF1_df["D_RankDRPct"].iloc[j] = j + 1

#print(FF1_df.head())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# add Offensive, Defensive, Net ratings and their rankings for adj/raw
FF1_df["O_AdjOER"] = 0
FF1_df["O_RankAdjOER"] = 0
FF1_df["D_AdjDER"] = 0
FF1_df["D_RankAdjDER"] = 0
FF1_df["AdjNetR"] = 0
FF1_df["RankAdjNetR"] = 0
FF1_df["O_RawOER"] = 0
FF1_df["O_RankRawOER"] = 0
FF1_df["D_RawDER"] = 0
FF1_df["D_RankRawDER"] = 0
FF1_df["RawNetR"] = 0
FF1_df["RankRawNetR"] = 0

# add the O/D ratings
for i in range (len(FF1_df)):
    for j in range(len(Eff_df)):
        if FF1_df["TeamName"].iloc[i] == Eff_df["Team"].iloc[j]:
            FF1_df["O_AdjOER"].iloc[i] = Eff_df["Adj_OER"].iloc[j]
            FF1_df["O_RankAdjOER"].iloc[i] = Eff_df["Adj_OER_Rank"].iloc[j]
            FF1_df["D_AdjDER"].iloc[i] = Eff_df["Adj_DER"].iloc[j]
            FF1_df["D_RankAdjDER"].iloc[i] = Eff_df["Adj_DER_Rank"].iloc[j]
            FF1_df["O_RawOER"].iloc[i] = Eff_df["Raw_OER"].iloc[j]
            FF1_df["O_RankRawOER"].iloc[i] = Eff_df["Raw_OER_Rank"].iloc[j]
            FF1_df["D_RawDER"].iloc[i] = Eff_df["Raw_DER"].iloc[j]
            FF1_df["D_RankRawDER"].iloc[i] = Eff_df["Raw_DER_Rank"].iloc[j]

#print(FF1_df.head())

# add net ratings
for i in range(len(FF1_df)):
    adj_O = FF1_df["O_AdjOER"].iloc[i]
    adj_D = FF1_df["D_AdjDER"].iloc[i]
    raw_O = FF1_df["O_RawOER"].iloc[i]
    raw_D = FF1_df["D_RawDER"].iloc[i]
    FF1_df["AdjNetR"].iloc[i] = adj_O - adj_D
    FF1_df["RawNetR"].iloc[i] = raw_O - raw_D

net_rank_columns = ["RankAdjNetR", "RankRawNetR"]
net_columns = ["AdjNetR", "RawNetR"]

for i in range(len(net_columns)):
    current_col = net_columns[i]
    rank_col = net_rank_columns[i]
    FF1_df = FF1_df.sort_values(by = current_col, ascending = False)
    for j in range(len(FF1_df)):
        FF1_df[rank_col].iloc[j] = j + 1

#print(FF1_df.head())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# cut dataset to just B12 teams

# Define B12 list
B12_list = ["Iowa St.", "Baylor", "Texas Tech", "Kansas", "Texas", "Oklahoma", "TCU", "West Virginia", "Oklahoma St.", "Kansas St."]

results = []
for i in range(len(FF1_df)):
    if FF1_df["TeamName"].iloc[i] not in B12_list:
        results.append(i)
FF1_df = FF1_df.drop(results)
print(FF1_df.head())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# add B12 rankings for every column :/
rank_columns = ["O_RankeFGPct", "O_RankTOPct", "O_RankORPct", "O_RankFTRate", "D_RankeFGPct", "D_RankTOPct", "D_RankORPct", "D_RankFTRate", "D_RankDRPct", "O_RankAdjOER", "D_RankAdjDER", "O_RankRawOER", "D_RankRawDER", "RankAdjNetR", "RankRawNetR"]
new_rank_columns = ["O_B12RankeFGPct", "O_B12RankTOPct", "O_B12RankORPct", "O_B12RankFTRate", "D_B12RankeFGPct", "D_B12RankTOPct", "D_B12RankORPct", "D_B12RankFTRate", "D_B12RankDRPct", "O_B12RankAdjOER", "D_B12RankAdjDER", "O_B12RankRawOER", "D_B12RankRawDER", "B12RankAdjNetR", "B12RankRawNetR"]

# loop through newly created ranking lists and add them to the df accordingly
for i in range(len(rank_columns)):
    # get the current rank column that you want to transfer to just B12
    current_col = rank_columns[i]
    # sort the df by this column
    FF1_df = FF1_df.sort_values(by = current_col)
    # get the new ranking column
    new_col = new_rank_columns[i]
    # loop through df and add new B12 rankings to corresponding columns
    for j in range ():
        FF1_df[new_col].iloc[j] = j + 1

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# Convert Dataframe to to_csv
# paths and names of files may need to be altered

export_csv = FF1_df.to_csv (r'C:\collegebb\College Analytics\Pyramid201920\PyramidData_201920_Total.csv', index = False)