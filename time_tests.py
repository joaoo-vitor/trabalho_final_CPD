import pandas as pd
from ternary_trie import *
from hashing import *
import datetime
import csv


before = datetime.datetime.now()
df_tags = pd.read_csv('tags.csv')
count1 = 0
count2=0
count3=0

for _, row in df_tags.iterrows():
    if(row['tag']):
        count1+=1
time1 =  datetime.datetime.now() - before

print('Pandas time: ', time1)


before = datetime.datetime.now()
with open('tags.csv', "r") as arquivo_tags:
        arquivo_csv = csv.reader(arquivo_tags, delimiter=",")
        next(arquivo_csv)
        for linha in arquivo_csv:
            if(linha[2]):
                count2+=1
              
time2 = datetime.datetime.now() - before
print('Csv time: ', time2)

before = datetime.datetime.now()
def process_chunk(chunk):
    count3=0
    # Perform operations on the chunk (e.g., filtering, aggregation)
    for _, row in chunk.iterrows():
        if(row['tag']):
            count3+=1
    return chunk, count3
for chunk in pd.read_csv('tags.csv', chunksize=10000):
    processed_chunk, count = process_chunk(chunk)
    count3 +=count

time3 = datetime.datetime.now() - before
print('Pandas with chunksize: ', time3)
print('Counts: ', count1, count2, count3)

