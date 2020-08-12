#import libraries
import pandas as pd
import os
import numpy as np
# Every path to a file
# paths and names of files may need to be altered

PATH_TO_DATASET=r'C:\collegebb\Line Range\sets'

DF_PATH = '31Games.csv'

df = pd.read_csv(os.path.join(PATH_TO_DATASET, DF_PATH))
#drop_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#df = df.drop(df.index[drop_list])
x = list(df.columns)
z_list = []

for i in range (len(x)):
    if 'Z' in x[i] and ('Miss' in x[i] or 'Make' in x[i]):
        z_list.append(x[i])

def get_total_FGA(df):
    total_FGA = 0
    for i in range (len(z_list)):
       total_FGA += sum(df[z_list[i]])
    return total_FGA

FGA = get_total_FGA(df)

def get_z1(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '1' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make == '':
        z_make = 0
    if z_miss == '':
        z_miss == 0
    if z_make != 0 and z_miss != 0:
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == 0 and z_miss != 0:
        att = sum(df[z_miss])
    elif z_make != 0 and z_miss == 0:
        att = sum(df[z_miss])
    elif z_make == 0 and z_miss == 0:
        att = 0
    if att == 0:
        return 0, 0
    if z_make == 0:
        makes = 0
    else:
        makes = sum(df[z_make])

    return att, makes

def get_z2(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '2' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make == '':
        z_make = 0
    if z_miss == '':
        z_miss == 0
    if z_make != 0 and z_miss != 0:
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == 0 and z_miss != 0:
        att = sum(df[z_miss])
    elif z_make != 0 and z_miss == 0:
        att = sum(df[z_miss])
    elif z_make == 0 and z_miss == 0:
        att = 0
    if att == 0:
        return 0, 0
    if z_make == 0:
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (1.5 * makes) / att
    return att, makes

def get_z3(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '3' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    
    if z_make != '' and z_miss != '':
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == '' and z_miss != '':
        att = sum(df[z_miss])
    elif z_make != '' and z_miss == '':
        att = sum(df[z_make])
    elif z_make == '' and z_miss == '':
        att = 0
    if att == 0:
        return 0, 0
    if z_make == '':
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (1.5 * makes) / att
    return att, makes

def get_z4(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '4' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make != '' and z_miss != '':
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == '' and z_miss != '':
        att = sum(df[z_miss])
    elif z_make != '' and z_miss == '':
        att = sum(df[z_make])
    elif z_make == '' and z_miss == '':
        att = 0
    if att == 0:
        return 0, 0
    if z_make == '':
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (makes) / att
    return att, makes

def get_z5(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '5' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make != '' and z_miss != '':
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == '' and z_miss != '':
        att = sum(df[z_miss])
    elif z_make != '' and z_miss == '':
        att = sum(df[z_make])
    elif z_make == '' and z_miss == '':
        att = 0
    if att == 0:
        return 0, 0
    if z_make == '':
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (makes) / att
    return att, makes

def get_z6(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '6' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make != '' and z_miss != '':
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == '' and z_miss != '':
        att = sum(df[z_miss])
    elif z_make != '' and z_miss == '':
        att = sum(df[z_make])
    elif z_make == '' and z_miss == '':
        att = 0
    if att == 0:
        return 0, 0
    if z_make == '':
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (makes) / att
    return att, makes

def get_z7(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '7' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make != '' and z_miss != '':
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == '' and z_miss != '':
        att = sum(df[z_miss])
    elif z_make != '' and z_miss == '':
        att = sum(df[z_make])
    elif z_make == '' and z_miss == '':
        att = 0
    if att == 0:
        return 0, 0
    if z_make == '':
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (makes) / att
    return att, makes

def get_z8(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '8' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make != '' and z_miss != '':
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == '' and z_miss != '':
        att = sum(df[z_miss])
    elif z_make != '' and z_miss == '':
        att = sum(df[z_make])
    elif z_make == '' and z_miss == '':
        att = 0
    if att == 0:
        return 0, 0
    if z_make == '':
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (makes) / att
    return att, makes

def get_z9(df):
    z_make = ''
    z_miss = ''
    for i in range (len(z_list)):
        if '9' in z_list[i]:
            if 'Make' in z_list[i]:
                z_make = z_list[i]
            elif 'Miss' in z_list[i]:
                z_miss = z_list[i]
    if z_make != '' and z_miss != '':
        att = sum(df[z_make]) + sum(df[z_miss])
    elif z_make == '' and z_miss != '':
        att = sum(df[z_miss])
    elif z_make != '' and z_miss == '':
        att = sum(df[z_make])
    elif z_make == '' and z_miss == '':
        att = 0
    if att == 0:
        return 0, 0
    if z_make == '':
        makes = 0
    else:
        makes = sum(df[z_make])

    z1_efg = (makes) / att
    return att, makes


print('-----------------', df['name'].iloc[0] ,'------------------')
print()
print('TOTAL FGA:', get_total_FGA(df))
print()
print('Z1:', get_z1(df))
print()
print('Z2:', get_z2(df))
print()
print('Z3:', get_z3(df))
print()
print('Z4:', get_z4(df))
print()
print('Z5:', get_z5(df))
print()
print('Z6:', get_z6(df))
print()
print('Z7:', get_z7(df))
print()
print('Z8:', get_z8(df))
print()
print('Z9:', get_z9(df))
