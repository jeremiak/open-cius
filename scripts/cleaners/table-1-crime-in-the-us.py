import glob
import textwrap

import pandas as pd

clean_path = '/data/clean'
raw_path = '/data/raw'
dest_filename = 'table-1-crime-in-the-us-1994-2013.csv'
dest_path = '%s/table-1-crime-in-the-us-1994-2013.csv' % clean_path
filename = 'Table_1_Crime_in_the_United_States_by_Volume_and_Rate_per_100000_Inhabitants_1994-2013.xls'
filepath = '%s/cius2013datatables/%s' % (raw_path, filename)

print('Cleaning table 1 (%s)' % dest_filename)

cius = pd.read_excel(filepath)
cius = cius.drop(['Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23'], axis=1)
cius.columns = ['Year', 'Population', 'Violent crime', 'Violent crime rate',
           'Murder and nonnegligent manslaughter', 'Murder and nonnegligent manslaughter rate',
           'Rape (legacy definition)', 'Rape (legacy definition) rate', 'Robbery', 'Robbery rate',
           'Aggrevated assault', 'Aggrevated assault rate', 'Property crime', 'Property crime rate', 'Burglary',
           'Burglary rate', 'Larceny-theft', 'Larceny-theft rate', 'Motor vehicle theft', 'Motor vehicle theft rate'
          ]
footnotes = cius.loc[23:27, 'Year']

cius = cius.loc[3:22]
cius.loc[10, 'Year'] = '2001'
cius.loc[21, 'Year'] = '2012'
cius.set_index('Year', inplace=True)

cius.to_csv(dest_path)
