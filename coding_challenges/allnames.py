# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import pandas as pd

def unisex(allnames):
    # Your code goes here.
    print(allnames)
    boys = allnames.loc[allnames['sex'] == 'M']
    girls = allnames.loc[allnames['sex'] == 'F']

    nboys = sum(boys['number'])
    ngirls = sum(girls['number'])

    ratio = nboys / ngirls
    unisex = (ratio > 0.5) and (ratio < 0.2)

    print(unisex)
    print(boys)
    print(girls)

