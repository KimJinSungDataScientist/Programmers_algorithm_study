import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)

temp = pd.read_csv('stylist_table.csv')
temp.drop('Unnamed: 0',axis=1,inplace=True)

temp_save = temp.copy()

color_table = pd.read_csv('color_table.csv')
color_table.drop('Unnamed: 0',axis=1,inplace=True)
lang = ['eng','kor']

for m in temp:
    chk ={0:False,1:False,2:False}
    for color_cnt in range(len(color_table)):
        for i in lang:
            for j in range(3):
                if color_table[i][color_cnt].lstrip() in str(temp[m][j * 2]).lower():
                    print(color_table['eng'][color_cnt].lstrip())
                    temp_save[m][j*2] = color_table['eng'][color_cnt].lstrip()
                    chk[j]=True

    for i,j in enumerate(chk.values()):
        if j==False:
            temp_save[m][i*2] = np.nan
            temp_save[m][i*2+1] = np.nan



temp_save.to_csv('stylist_table_clean.csv',encoding='utf-8-sig')











# print(temp['여자2번 model'][0])


# chk = False
#
# for n in range(3):
#     dirty_txt = temp['여자2번 model'][n*2].replace('_',' ').split(' ')
#     clean_txt = []
#
#     get_color = ''
#     for i in dirty_txt:
#         clean_txt.append((''.join(char for char in i if char.isalnum())).lower())
#
#
#     for i in color_table:
#         if chk==True:
#             break
#         for j in color_table[i].isin(clean_txt):
#             if j==True:
#                 get_color = color_table[i][color_table[i].isin(clean_txt)].index[0]
#                 print(color_table[i][color_table[i].isin(clean_txt)].index[0])
#                 chk = True
#                 break
#
#     if chk == True:
#         chk = False
#         temp_save['여자2번 model'][n*2] = color_table.iloc[get_color][2].replace(" ","")
#
# print(temp_save['여자2번 model'])

