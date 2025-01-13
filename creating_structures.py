import pandas as pd
from ternary_trie import *
from hashing import *

df_players = pd.read_csv('players.csv')
df_ratings = pd.read_csv('minirating.csv')


# 2.1 Estrutura 1: Armazenando Dados Sobre Jogadores

# Define colunas novas em df_players para os ratings
df_players['number_of_ratings']=0
df_players['rating_avg']=0

# Cria tabela vazia
ht_size=12323
hash_table_players = start_hash_table(ht_size)

# Insere cada jogador na lista da posição adequada 
for index, row in df_players.iterrows():
    key = int(row['sofifa_id'])
    insert_hash_table(key, row.to_dict(), hash_table_players, ht_size)

# Percorre cada avaliação e incrementa na linha do jogador
for index, row in df_ratings.iterrows():
    key = int(row['sofifa_id'])
    _, player = search_hash_table(key, 'sofifa_id', hash_table_players, ht_size)
    if(player):
        player['number_of_ratings']+=1
        player['rating_avg']+=float(row['rating'])

# Divide a media de rating pela quantidade de rating (corrige o valor)
for key in hash_table_players:
    for player in hash_table_players[key]:
      if(player['number_of_ratings']):
        player['rating_avg']/=player['number_of_ratings']

_, player = search_hash_table(158023, 'sofifa_id', hash_table_players, ht_size)
print(player['rating_avg'])

# 2.2 Estrutura 2: Estrutura para buscas por strings de nomes
trie_names = TernaryTrie()
for _, row in df_players.iterrows():
   trie_names.insert(row['long_name'].lower(), row['sofifa_id'])



