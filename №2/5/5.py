import pandas as pd
import collections
import json
import msgpack
import pickle
import os


df = pd.read_csv("./5/Alzheimer_s_Disease_and_Healthy_Aging_Data.csv", low_memory=False)
df.head()
#df.info(memory_usage='deep')
data = df[['YearStart', 'LocationAbbr', 'LocationDesc', 'Class', 'Topic', 'Data_Value',  'LocationID']]
#print(data)
#data.describe() #нетсуммы

result = list()
#r = df[['YearStart', 'Data_Value',  'LocationID']].agg(["min","mean", "median", "max", "std", "sum"])
pd.set_option('display.float_format', '{:.2f}'.format)
result.append({
            "YearStart min": int(df['YearStart'].min()),
            "YearStart max": int(df['YearStart'].max()),
            "YearStart sum": int(df['YearStart'].sum()),
            "YearStart mean": int(df['YearStart'].mean()),
            "YearStart std": int(df['YearStart'].std()),
            "Data_Value min": int(df['Data_Value'].min()),
            "Data_Value max": int(df['Data_Value'].max()),
            "Data_Value sum": int(df['Data_Value'].sum()),
            "Data_Value mean": int(df['Data_Value'].mean()),
            "Data_Value std": int(df['Data_Value'].std()),
            "LocationID": int(df['LocationID'].min()),
            "LocationID": int(df['LocationID'].max()),
            "LocationID": int(df['LocationID'].sum()),
            "LocationID": int(df['LocationID'].mean()),
            "LocationIDd": int(df['LocationID'].std())
        })
#print(result)

data1 = df['LocationAbbr']
words1 = collections.Counter(data1)
result.append(words1)

data2 = df['LocationDesc']
words2 = collections.Counter(data2)
result.append(words2)

data3 = df['Class']
words3 = collections.Counter(data3)
result.append(words3)

data4 = df['Topic']
words4 = collections.Counter(data4)
result.append(words4)

print(result)


with open("result!.json", "w") as file:
    file.write(json.dumps(result))

with open("result!.msgpack", "wb") as file:
    file.write(msgpack.dumps(result))

with open("result!.pkl", "wb") as file:
    file.write(pickle.dumps(result))




print(f"json = {os.path.getsize('result!.json')}")
print(f"msgpack = {os.path.getsize('result!.msgpack')}")
print(f"pkl = {os.path.getsize('result!.msgpack')}")







