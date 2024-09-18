import json
import sys

data={}

def JsonSerialize(data, sfile):
    with open(sfile, 'w') as write_file:
        json.dump(data, write_file)
    
def JsonDeSerialize(sFile):
    with open(sFile, 'r') as read_file:
        return json.load(read_file)
    
def print_dictionary(dData):
    for key, value in dData.items():
        print(f'Trovata chiave {key}')
        print(value)
        print(type(dData[key]))

sFilePath='JSON/example.json'
data=JsonDeSerialize(sFilePath)

print(type(data['quiz']))
if type(data['quiz']) is dict:
    print_dictionary(data['quiz'])