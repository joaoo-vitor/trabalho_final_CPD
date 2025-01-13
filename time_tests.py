import pandas as pd
from ternary_trie import *
from hashing import *

df_ratings = pd.read_csv('rating.csv')

# # 2.3 Estrutura 1: Armazenando Dados Sobre Jogadores
ht_size=12323
hash_table_ratings = start_hash_table(ht_size)

# Insere cada rating na lista da posição adequada 
for index, row in df_ratings.iterrows():
    _, user_ratings= search_hash_table(row['user_id'], 'user_id', hash_table_ratings, ht_size)
