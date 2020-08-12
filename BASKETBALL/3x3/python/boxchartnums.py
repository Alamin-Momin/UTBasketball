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

def get_total_eFG(df, FGA):
    three_list = []
    two_list = []
    
    for i in range (len(z_list)):
        if ('1' in z_list[i] or '2' in z_list[i] or '3' in z_list[i]) and ('Make' in z_list[i]):
            three_list.append(z_list[i])
    for i in range (len(z_list)):
        if ('1' not in z_list[i] and '2' not in z_list[i] and '3' not in z_list[i]) and ('Make' in z_list[i]):
            two_list.append(z_list[i])
    threes = 0
    twos = 0
    for i in range (len(three_list)):
        threes += sum(df[three_list[i]])
    for i in range (len(two_list)):
        twos += sum(df[two_list[i]])

    efg = (twos + (1.5 * threes) ) / FGA

    return efg * 100


def get_long_efg(df):
    three_list = []
    for i in range (len(z_list)):
        if ('1' in z_list[i] or '2' in z_list[i] or '3' in z_list[i]):
            three_list.append(z_list[i])
    three_att = 0
    for i in range(len(three_list)):
        three_att += sum(df[three_list[i]])
    three_make_list = []
    for i in range (len(three_list)):
        if 'Make' in three_list[i]:
            three_make_list.append(three_list[i])
    three_makes = 0 
    for i in range (len(three_make_list)):
        three_makes += sum(df[three_make_list[i]])
    if three_att == 0:
        return three_att, 0
    three_efg = (1.5 * three_makes) / three_att
    return three_att, three_efg * 100 

def get_mid_efg(df):
    three_list = []
    for i in range (len(z_list)):
        if ('4' in z_list[i] or '5' in z_list[i] or '6' in z_list[i]):
            three_list.append(z_list[i])
    three_att = 0
    for i in range(len(three_list)):
        three_att += sum(df[three_list[i]])
    three_make_list = []
    for i in range (len(three_list)):
        if 'Make' in three_list[i]:
            three_make_list.append(three_list[i])
    three_makes = 0 
    for i in range (len(three_make_list)):
        three_makes += sum(df[three_make_list[i]])
    if three_att == 0:
        return three_att, 0
    three_efg = (three_makes) / three_att
    return three_att, three_efg * 100

def get_short_efg(df):
    three_list = []
    for i in range (len(z_list)):
        if ('7' in z_list[i] or '8' in z_list[i] or '9' in z_list[i]):
            three_list.append(z_list[i])
    three_att = 0
    for i in range(len(three_list)):
        three_att += sum(df[three_list[i]])
    three_make_list = []
    for i in range (len(three_list)):
        if 'Make' in three_list[i]:
            three_make_list.append(three_list[i])
    three_makes = 0 
    for i in range (len(three_make_list)):
        three_makes += sum(df[three_make_list[i]])
    three_efg = (three_makes) / three_att
    return three_att, three_efg * 100  

def get_early_efg(df):
    three_list = []
    two_list = []
    for i in range (len(z_list)):
        if ('1' in z_list[i]):
            three_list.append(z_list[i])
    for i in range (len(z_list)):
        if ('4' in z_list[i] or '7' in z_list[i]):
            two_list.append(z_list[i])
    
    total_att = 0
    for i in range(len(three_list)):
        total_att += sum(df[three_list[i]])
    for i in range(len(two_list)):
        total_att += sum(df[two_list[i]])
    
    three_make_list = []
    for i in range (len(three_list)):
        if 'Make' in three_list[i]:
            three_make_list.append(three_list[i])
    two_make_list = []
    for i in range (len(two_list)):
        if 'Make' in two_list[i]:
            two_make_list.append(two_list[i])
    
    three_makes = 0 
    for i in range (len(three_make_list)):
        three_makes += sum(df[three_make_list[i]])
    two_makes = 0 
    for i in range (len(two_make_list)):
        two_makes += sum(df[two_make_list[i]])

    late_efg = (two_makes + (1.5 * three_makes)) / total_att
    return total_att, late_efg * 100 

def get_middle_efg(df):
    three_list = []
    two_list = []
    for i in range (len(z_list)):
        if ('2' in z_list[i]):
            three_list.append(z_list[i])
    for i in range (len(z_list)):
        if ('5' in z_list[i] or '8' in z_list[i]):
            two_list.append(z_list[i])
    
    total_att = 0
    for i in range(len(three_list)):
        total_att += sum(df[three_list[i]])
    for i in range(len(two_list)):
        total_att += sum(df[two_list[i]])
    
    three_make_list = []
    for i in range (len(three_list)):
        if 'Make' in three_list[i]:
            three_make_list.append(three_list[i])
    two_make_list = []
    for i in range (len(two_list)):
        if 'Make' in two_list[i]:
            two_make_list.append(two_list[i])
    
    three_makes = 0 
    for i in range (len(three_make_list)):
        three_makes += sum(df[three_make_list[i]])
    two_makes = 0 
    for i in range (len(two_make_list)):
        two_makes += sum(df[two_make_list[i]])

    late_efg = (two_makes + (1.5 * three_makes)) / total_att
    return total_att, late_efg * 100

def get_late_efg(df):
    three_list = []
    two_list = []
    for i in range (len(z_list)):
        if ('3' in z_list[i]):
            three_list.append(z_list[i])
    for i in range (len(z_list)):
        if ('6' in z_list[i] or '9' in z_list[i]):
            two_list.append(z_list[i])
    
    total_att = 0
    for i in range(len(three_list)):
        total_att += sum(df[three_list[i]])
    for i in range(len(two_list)):
        total_att += sum(df[two_list[i]])
    
    three_make_list = []
    for i in range (len(three_list)):
        if 'Make' in three_list[i]:
            three_make_list.append(three_list[i])
    two_make_list = []
    for i in range (len(two_list)):
        if 'Make' in two_list[i]:
            two_make_list.append(two_list[i])
    
    three_makes = 0 
    for i in range (len(three_make_list)):
        three_makes += sum(df[three_make_list[i]])
    two_makes = 0 
    for i in range (len(two_make_list)):
        two_makes += sum(df[two_make_list[i]])

    late_efg = (two_makes + (1.5 * three_makes)) / total_att
    return total_att, late_efg * 100

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

    z1_efg = (1.5 * makes) / att
    return att, z1_efg * 100

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
    return att, z1_efg * 100

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
    return att, z1_efg * 100

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
    return att, z1_efg * 100

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
    return att, z1_efg * 100

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
    return att, z1_efg * 100

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
    return att, z1_efg * 100

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
    return att, z1_efg * 100

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
    return att, z1_efg * 100


print('-------------------', df['name'].iloc[0], '----------------')
print()
print('TOTAL FGA:', get_total_FGA(df))
print()
print('TOTAL eFG%:', get_total_eFG(df, FGA))
print()
print('LONG:', get_long_efg(df))
print()
print('MID:', get_mid_efg(df))
print()
print('SHORT:', get_short_efg(df))
print()
print('EARLY:', get_early_efg(df))
print()
print('MIDDLE:', get_middle_efg(df))
print()
print('LATE:', get_late_efg(df))
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
