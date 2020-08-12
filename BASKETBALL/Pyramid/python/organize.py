#import libraries
import pandas as pd
import os

# Every path to a file
# paths and names of files may need to be altered

PATH_TO_DATASET=r'C:\collegebb\College Analytics\Pyramid201920'
#Pyramid_data_path_201516 = 'PyramidB12Data_201516.csv'
#Pyramid_data_path_201617 = 'PyramidB12Data_201617.csv'
#Pyramid_data_path_201718 = 'PyramidB12Data_201718.csv'
Pyramid_data_path = 'PyramidB12Data_201920_Total.csv'

# convert to pd df
#df1 = pd.read_csv(os.path.join(PATH_TO_DATASET, Pyramid_data_path_201516))
#df2 = pd.read_csv(os.path.join(PATH_TO_DATASET, Pyramid_data_path_201617))
#df3 = pd.read_csv(os.path.join(PATH_TO_DATASET, Pyramid_data_path_201718))
df4 = pd.read_csv(os.path.join(PATH_TO_DATASET, Pyramid_data_path))

#df_list = [df1, df2, df3, df4]

# organize columns
organized_cols = ['Season', 'TeamName', 'O_eFGPct', 'O_RankeFGPct', 'O_B12RankeFGPct', 'O_TOPct', 'O_RankTOPct', 'O_B12RankTOPct', 'O_ORPct','O_RankORPct', 'O_B12RankORPct', 'O_FTRate','O_RankFTRate', 'O_B12RankFTRate', 'O_AdjOER', 'O_RankAdjOER', 'O_B12RankAdjOER', 'O_RawOER', 'O_RankRawOER', 'O_B12RankRawOER', 'D_eFGPct', 'D_RankeFGPct', 'D_B12RankeFGPct', 'D_TOPct', 'D_RankTOPct', 'D_B12RankTOPct', 'D_DRPct', 'D_RankDRPct', 'D_B12RankDRPct', 'D_FTRate', 'D_RankFTRate', 'D_B12RankFTRate', 'D_AdjDER', 'D_RankAdjDER', 'D_B12RankAdjDER', 'D_RawDER', 'D_RankRawDER', 'D_B12RankRawDER', 'AdjNetR', 'RankAdjNetR', 'B12RankAdjNetR', 'RawNetR', 'RankRawNetR', 'B12RankRawNetR']

#df1 = df1[organized_cols]
#df2 = df2[organized_cols]
#df3 = df3[organized_cols]
df4 = df4[organized_cols]

#print(df.head())
#print(list(df.columns.values))

# Convert Dataframe to to_csv
# paths and names of files may need to be altered

#export_csv = df1.to_csv (r'C:\College Analytics\Pyramid Data\Pyramid_Data_201516.csv', index = False)
#export_csv = df2.to_csv (r'C:\College Analytics\Pyramid Data\Pyramid_Data_201617.csv', index = False)
#export_csv = df3.to_csv (r'C:\College Analytics\Pyramid Data\Pyramid_Data_201718.csv', index = False)
export_csv = df4.to_csv (r'C:\collegebb\College Analytics\Pyramid201920\Pyramid_Data_201920_Total.csv', index = False)