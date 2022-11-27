#!/usr/bin/python
import pandas as pd


def output():
# reading csv files
 data1 = pd.read_csv('./dest/csv_output.csv',sep=",")
 data2 = pd.read_csv('./Input/asset_data.csv',sep=",")
  
# using merge function by setting how='outer'
 output4 = pd.merge(data1, data2, 
                   on='assetId', 
                   how='outer') 
# displaying result
 print(output4)
 output4.to_csv("./dest/agent_output.csv", index=False, encoding='utf-8-sig')