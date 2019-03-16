#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

import csv
from collections import namedtuple

# reader csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print(row.Symbol, row.Date)

print('**********************************')
# reader data to dict
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Price'], row['Change'])


# writer csv
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '2008/11/6', '14:36', -0.18, 181800),
        ('AIG', 71.38, '2008/11/6', '14:36', -0.15, 195500),
        ('AXP', 62.58, '2008/11/6', '14:36', -0.46, 93500)
       ]

with open('stocks_new.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'2008/11/6',
         'Time':'14:36', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price':71.38, 'Date':'2008/11/6',
         'Time':'14:36', 'Change':-0.15, 'Volume':195500},
        {'Symbol':'AXP', 'Price':62.58, 'Date':'2008/11/6',
         'Time':'14:36', 'Change':-0.46, 'Volume':93500}
       ]

with open('stocks_new.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)