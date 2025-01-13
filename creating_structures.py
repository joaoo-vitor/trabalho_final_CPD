import pandas as pd
from ternary_trie import *
from hashing import *
from trie import *
import datetime
import csv

ht_size=12323
print('Criando estruturas...')
caminho_ratings_csv = 'rating.csv'
caminho_players_csv = 'players.csv'
caminho_tags_csv = 'tags.csv'

# 2.1 Estrutura 1: Armazenando Dados Sobre Jogadores
before = datetime.datetime.now()
# Cria tabela vazia
hash_table_players = start_hash_table(ht_size)

# Insere cada jogador na lista da posição adequada 
with open(caminho_players_csv) as csvfile:
   reader = csv.reader(csvfile, delimiter=",")
   # Pula header
   next(reader)
   for row in reader:
    # row[0] = 'sofifa_id'
    key = int(row[0])
    dict_row = {'sofifa_id':int(row[0]), 'short_name':row[1], 'long_name':row[2], 'player_positions':row[3], 'nationality':row[4],
                'number_of_ratings':0, 'rating_avg':0}
    insert_hash_table(key, dict_row, hash_table_players, ht_size)

# Lookup com ratings
# Percorre cada avaliação e incrementa na linha do jogador
with open(caminho_ratings_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    # Pula header
    next(reader)
    for row in reader:
        # row[0] = 'sofifa_id'
        key = int(row[1])
        player = search_hash_table(key, 'sofifa_id', hash_table_players, ht_size)
        if(player):
            player['number_of_ratings']+=1
            # row[2] = 'rating'
            player['rating_avg']+=float(row[2])

# Divide a media de rating pela quantidade de rating (corrige o valor)
for key in hash_table_players:
    for player in hash_table_players[key]:
      if(player['number_of_ratings']):
        player['rating_avg']/=player['number_of_ratings']

elapsed_time = datetime.datetime.now() - before
print('Estrutura 1 finalizada. Tempo: ', elapsed_time)

# 2.2 Estrutura 2: Estrutura para buscas por strings de nomes
before = datetime.datetime.now()
trie_names = TernaryTrie()
with open(caminho_players_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    # Pula header
    next(reader)
    for row in reader:
        # row[0] = 'sofifa_id'
        # row[1] = 'short_name'
        trie_names.insert(row[2].lower(), row[0])

elapsed_time = datetime.datetime.now() - before
print('Estrutura 2 finalizada. Tempo: ', elapsed_time)

# 2.3 Estrutura 3: Estrutura para guardar revisoes de usuários
before = datetime.datetime.now()
hash_table_users = start_hash_table(ht_size)

# Insere cada rating na lista da posição adequada 
with open(caminho_ratings_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    # Pula header
    next(reader)
    for row in reader:
        # row[0] = user_id
        key = int(row[0])
        user_ratings= search_hash_table(key, 'user_id', hash_table_users, ht_size)
        # row[1] = 'sofifa_id', row[2] = 'rating'
        
        player_id, rating = int(row[1]), float(row[2])
        if(user_ratings):
            # If the key already existing on the HT, append the list of ratings of the user
            user_ratings['ratings'].append((player_id, rating))
        else:
            # Else, initialize new dictionary with only the first rating and insert on the rtable
            # row[0] = user_id
            dict_ratings ={'user_id':row[0], 'ratings': (player_id, rating)}
            insert_hash_table(key, dict_ratings, hash_table_users, ht_size)
       
elapsed_time = datetime.datetime.now() - before
print('Estrutura 3 finalizada. Tempo: ', elapsed_time)

user_ratings = search_hash_table(12320, 'user_id', hash_table_users, ht_size)
print(user_ratings['ratings'])

# # # 2.4 Estrutura 4: Estrutura para guardar tags
# # trie_tags = Trie()
# # for _, row in df_tags.iterrows():
# #    trie_tags.insert(row['sofifa_id'], str(row['tag']))

# # print(trie_tags.search('B'))


