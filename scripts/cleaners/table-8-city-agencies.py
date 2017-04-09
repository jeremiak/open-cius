import re

import numpy as np
import pandas as pd

def insert_rate(df, column):
    column_index = list(df.columns.values).index(column) + 1
    column_name = '%s rate' % column
    rates = (df[column] * 100000) / df['Population']

    df.insert(column_index, column_name, rates)

    return df

def process(year):
    last_state = None
    df = pd.read_excel('%s/%s' % (raw_path, table_files[year]))

    df.columns = df.loc[2]
    df = df.iloc[3:, :14]
    df = df[df['City'] != False] # drop things like footnotes
    df = df[df['Population'] > 0] # drop cities with no population
    df['State'] = df['State'].fillna(False)
    df.reset_index()

    if np.nan in df.columns:
        df = df.drop(np.nan, axis=1)

    for index, row in df.iterrows():
        # associate states with cities to account for FBI report formatting
        if row['State'] != False:
            last_state = row['State']
        else:
            df.loc[index, 'State'] = last_state

        # remove footnote references from city names
        if re.search(r'\d$', row['City']):
            row['City'] = remove_footnote(row['City'])

    df = df.replace(r'^\s+', np.nan, regex=True)
    df.insert(2, 'Year', year)

    return df

def remove_footnote(str):
    return re.sub(r'\d$', '', str)


clean_path = '/data/clean'
raw_path = '/data/raw'
table_files = {
    '2006': 'cius2006datatables/06tbl08.xls',
    '2007': 'cius2007datatables/documents/07tbl08.xls',
    '2008': 'cius2008datatables/CIUS2008datatables/08tbl08.xls',
    '2009': 'cius2009datatables/Data Tables/09tbl08.xls',
    '2010': 'CIUS2010downloadablefiles/Cius1/Excel/10tbl08.xls',
    '2011': 'CIUS2011datatables/CIUS2011datatables/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2011.xls',
    '2012': 'cius2012datatables/Tables/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2012.xls',
    '2013': 'cius2013datatables/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2013.xls'
}
# 2013 is not yet included because it has both definitions of rape
years = ['2008', '2009', '2010', '2011', '2012']
dest_filename = 'table-8-offenses-known-to-law-enforcement-by-state-by-city-%s-%s.csv' % (years[0], years[-1])

print('Cleaning table 8 (%s)' % dest_filename)
dataframes = [process(year) for year in years]
cols = ['State', 'City', 'Year', 'Population', 'Violent crime', 'Murder and nonnegligent manslaughter', 'Rape (legacy definition)', 'Robbery', 'Aggravated assault', 'Property crime', 'Burglary', 'Larceny-theft', 'Motor vehicle theft', 'Arson']
for df in dataframes:
    df.columns = cols

data = pd.concat(dataframes)

for col in cols[4:]:
    data = insert_rate(data, col)

data.to_csv('%s/%s' % (clean_path, dest_filename))
