#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

def main():
    airline_data = pd.read_csv('processed_data.csv', on_bad_lines='skip')
    lax_dept = airline_data[airline_data['ORIGIN'] == 'LAX']
    columns_to_keep = ['YEAR', 'MONTH', 'DAY_OF_MONTH', 'DAY_OF_WEEK','ORIGIN','DEST',
    'CRS_DEP_TIME', 'DEP_TIME', 'DEP_DELAY', 'CRS_ARR_TIME', 'ARR_TIME', 'ARR_DELAY']
    lax_dept = lax_dept[columns_to_keep]
    
    print(lax_dept.columns)

    lax_dept = lax_dept.dropna()
    lax_dept['DEP_TIME'] = lax_dept['DEP_TIME'].astype('int')
    lax_dept['DEP_DELAY'] = lax_dept['DEP_DELAY'].astype('int')

    lax_dept.rename(columns={'DAY_OF_MONTH': 'DAY', 'ORIGIN': 'ORG_AIRPORT', 'DEST': 'DEST_AIRPORT', 'CRS_DEP_TIME': 'SCHEDULED_DEPARTURE','DEP_TIME': 'DEPARTURE_TIME', 'DEP_DELAY': 'DEPARTURE_DELAY','CRS_ARR_TIME' : 'SCHEDULED_ARRIVAL','ARR_TIME': 'ARRIVAL_TIME', 'ARR_DELAY': 'ARRIVAL_DELAY'}, inplace=True)

    lax_dept['DEPARTURE_DELAY'] = lax_dept['DEPARTURE_DELAY'].clip(lower=0)
    lax_dept = lax_dept.reset_index(drop=True)
    lax_dept['DEPARTURE_DELAY'].dtype
    print(lax_dept.columns)

    lax_dept.to_csv('cleaned_data.csv', index=False)

if __name__ == "__main__":
    main()
