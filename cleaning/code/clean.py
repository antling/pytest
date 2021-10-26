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

# unwanted_characters = [',', '[', '-']
# def clean_dates(item):
#     dop = str(item.loc['Date of Publication'])
#     if dop == 'nan' or dop[0] == '[':
#         return np.NaN
#
#     for character in unwanted_characters:
#         if character in dop:
#             character_index = dop.find(character)
#             print('index = ', character_index, " dop = ", dop, " after = ", dop[:character_index])
#             dop = dop[:character_index]
#     return dop
#
# df['Date of Publication'] = df.apply(clean_dates, axis=1)

# def clean_author_names(author):
#     author = str(author)
#
#     print("author = ", author)
#
#     if author == 'nan':
#         return 'NaN'
#
#     author = author.split(',')
#
#     if len(author) == 1:
#         name = filter(lambda x: x.isalpha(), author[0])
#         return reduce(lambda x, y: x + y, name)
#
#     last_name, first_name = author[0], author[1]
#     first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name
#
#     if first_name.endswith(('.', '.|')):
#         parts = first_name.split('.')
#         if len(parts) > 1:
#             first_occurence = first_name.find('.')
#             final_occurence = first_name.find('.', first_occurence + 1)
#             first_name = first_name[:final_occurence]
#         else:
#             first_name = first_name[:first_name.find('.')]
#     print("before last name = ", last_name)
#     last_name = last_name.capitalize()
#     print("after last name = ", last_name)
#     return f'{first_name} {last_name}'
#
#
# df['Author'] = df['Author'].apply(clean_author_names)

# def clean_title(title):
#     if title == 'nan':
#         return 'NaN'
#
#     if title[0] == '[':
#         print("title1 = " , title)
#         title = title[1: title.find(']')]
#         print("title2 = ", title)
#     if 'by' in title:
#         print("title3 = ", title)
#         title = title[:title.find('by')]
#         print("title4 = ", title)
#     elif 'By' in title:
#         title = title[:title.find('By')]
#
#     if '[' in title:
#         title = title[:title.find('[')]
#
#     print("title5 = ", title)
#     title = title[:-2]
#     print("title6 = ", title)
#
#     ad = title.split()
#     print("at = ", ad)
#
#     title = list(map(str.capitalize, title.split()))
#     print("title7 = ", title)
#     return ' '.join(title)
#
# df['Title'] = df['Title'].apply(clean_title)
# df.head()
#df.to_csv('c:/wuda/1.csv')

# pub = df['Place of Publication']
# df['Place of Publication'] = np.where(pub.str.contains('London'), 'London',
#                                       np.where(pub.str.contains('Oxford'), 'Oxford',
#                                                np.where(pub.eq('Newcastle upon Tyne'),
#                                                         'Newcastle-upon-Tyne', df['Place of Publication'])))
# df.to_csv('c:/wuda/1.csv')

# university_towns = []
#
# with open('../data/university_towns.txt', 'r') as file:
#     items = file.readlines()
#
#     print("items = ", items)
#     states = list(filter(lambda x: '[edit]' in x, items))
#
#     print("states = ", states)
#
#     for index, state in enumerate(states):
#         print("index = ", index, " state = ", state)
#         start = items.index(state) + 1
#         print("start = ", start)
#         if index == 49:  # since 50 states
#             end = len(items)
#             print("end = ", end)
#         else:
#             end = items.index(states[index + 1])
#
#         pairs = map(lambda x: [state, x], items[start:end])
#         university_towns.extend(pairs)
#
# towns_df = pd.DataFrame(university_towns, columns=['State', 'RegionName'])
# print(towns_df.head())
#
# def clean_up(item):
#     if '(' in item:
#         return item[:item.find('(') - 1]
#
#     if '[' in item:
#         return item[:item.find('[')]
#
# towns_df = towns_df.applymap(clean_up)
# print(towns_df.head(20))

# olympics_df = pd.read_csv('../data/olympics.csv', skiprows = 1, header= 0)
# new_names =  {'Unnamed: 0': 'Country',
#               '? Summer': 'Summer Olympics',
#               '01 !': 'Gold',
#               '02 !': 'Silver',
#               '03 !': 'Bronze',
#               '? Winter': 'Winter Olympics',
#               '01 !.1': 'Gold.1',
#               '02 !.1': 'Silver.1',
#               '03 !.1': 'Bronze.1',
#               '? Games': '# Games',
#               '01 !.2': 'Gold.2',
#               '02 !.2': 'Silver.2',
#               '03 !.2': 'Bronze.2'}
#
# olympics_df.rename(columns = new_names, inplace = True)
# print(olympics_df.head())
