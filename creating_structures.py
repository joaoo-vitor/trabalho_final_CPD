import pandas as pd
from ternary_trie import *
from hashing import *
from trie import *
import datetime

df_players = pd.read_csv('players.csv')
df_ratings = pd.read_csv('minirating.csv')
df_tags = pd.read_csv('tags.csv')

print('Criando estruturas...')

# 2.1 Estrutura 1: Armazenando Dados Sobre Jogadores
before = datetime.datetime.now()
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

# Lookup com ratings
# Percorre cada avaliação e incrementa na linha do jogador
for index, row in df_ratings.iterrows():
    key = int(row['sofifa_id'])
    player = search_hash_table(key, 'sofifa_id', hash_table_players, ht_size)
    if(player):
        player['number_of_ratings']+=1
        player['rating_avg']+=float(row['rating'])

# Divide a media de rating pela quantidade de rating (corrige o valor)
for key in hash_table_players:
    for player in hash_table_players[key]:
      if(player['number_of_ratings']):
        player['rating_avg']/=player['number_of_ratings']

# player = search_hash_table(158023, 'sofifa_id', hash_table_players, ht_size)
# print(player['rating_avg'])
elapsed_time = datetime.datetime.now() - before
print('Estrutura 1 finalizada. Tempo: ', elapsed_time)

# 2.2 Estrutura 2: Estrutura para buscas por strings de nomes
before = datetime.datetime.now()
trie_names = TernaryTrie()
for _, row in df_players.iterrows():
   trie_names.insert(row['long_name'].lower(), row['sofifa_id'])
elapsed_time = datetime.datetime.now() - before
print('Estrutura 2 finalizada. Tempo: ', elapsed_time)

# 2.3 Estrutura 3: Estrutura para guardar revisoes de usuários
before = datetime.datetime.now()
hash_table_users = start_hash_table(ht_size)

# Insere cada rating na lista da posição adequada 
for index, row in df_ratings.iterrows():
    key = int(row['user_id'])
    user_ratings= search_hash_table(key, 'user_id', hash_table_users, ht_size)
    player_id, rating = int(row['sofifa_id']), int(row['rating'])
    if(user_ratings):
        # If the key already existing on the HT, append the list of ratings of the user
        user_ratings['ratings'].append((player_id, rating))
    else:
       # Else, initialize new dictionary with only the first rating and insert on the rtable
       dict_ratings ={}
       dict_ratings['user_id']=row['user_id']
       dict_ratings['ratings'] = [(player_id, rating)]
       insert_hash_table(key, dict_ratings, hash_table_users, ht_size)
       
elapsed_time = datetime.datetime.now() - before
print('Estrutura 3 finalizada. Tempo: ', elapsed_time)

# user_ratings = search_hash_table(12320, 'user_id', hash_table_users, ht_size)
# print(user_ratings['ratings'])

# # 2.4 Estrutura 4: Estrutura para guardar tags
# trie_tags = Trie()
# for _, row in df_tags.iterrows():
#    trie_tags.insert(row['sofifa_id'], str(row['tag']))

# print(trie_tags.search('B'))


