import pandas as pd
import numpy as np
from functools import reduce

df = pd.read_csv('../data/BL-Flickr-Images-Book.csv')
# df.head()
# to_drop = ['Publisher']
# df.drop(to_drop, inplace = True, axis =1)
# df.head()
# print('result2 = \n', df)
#
# df.set_index('Identifier', inplace = True)
# df.head()
# print('result3 = \n', df)
#
# df['Date of Publication'].head(25)
# print('result4 = \n', df)

unwanted_characters = ['[', ',', '-']
def clean_dates(item):
    dop = str(item.loc['Date of Publication'])

    if dop == 'nan' or dop[0] == '[':
        return np.NaN

    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]
    return dop

df['Date of Publication'] = df.apply(clean_dates, axis=1)

df.to_csv('c:/wuda/1.csv')
