#!/usr/bin/env python
# coding: utf-8
import pandas as pd

def main():
    airline_data = pd.read_csv('airport_data.csv', on_bad_lines='skip')
    print(airline_data.head())
    airline_data = airline_data.reset_index(drop=True)
    airline_data.to_csv('processed_data.csv', index=False)

if __name__ == "__main__":
    main()

