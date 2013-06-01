#!/usr/bin/env python

import csv
import json

def try_int(s):
	try:
		return int(s)
	except ValueError:
		return s

years = {}

reader = csv.reader(open("Council_population.csv", "rU"))
header = reader.next()
for row in reader:
	assert len(row) == len(header)
	vals = dict(zip(header, [try_int(val) for val in row]))
	year = vals.pop('Year')
	years[year] = vals

print json.dumps(years, sort_keys=True, indent=4)
