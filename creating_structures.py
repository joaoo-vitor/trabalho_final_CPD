import pandas as pd
from ternary_trie import *
from hashing import *
from trie import *
import datetime
import csv

caminho_ratings_csv = 'rating.csv'
caminho_players_csv = 'players.csv'
caminho_tags_csv = 'tags.csv'

# 2.1 Estrutura 1: Armazenando Dados Sobre Jogadores
def structure_players_data():
    before = datetime.datetime.now()
    # Cria tabela vazia
    hash_table_players = HashTable(12323)

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
            hash_table_players.insert(key, dict_row)

    # Lookup com ratings
    # Percorre cada avaliação e incrementa na linha do jogador
    with open(caminho_ratings_csv) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        # Pula header
        next(reader)
        for row in reader:
            # row[0] = 'sofifa_id'
            key = int(row[1])
            player = hash_table_players.search(key, 'sofifa_id')
            if(player):
                player['number_of_ratings']+=1
                # row[2] = 'rating'
                player['rating_avg']+=float(row[2])

    # Divide a media de rating pela quantidade de rating (corrige o valor)
    for key in hash_table_players.dict:
        for player in hash_table_players.dict[key]:
            if(player['number_of_ratings']):
                player['rating_avg']/=player['number_of_ratings']

    elapsed_time = datetime.datetime.now() - before
    print('Estrutura 1 finalizada. Tempo: ', elapsed_time)
    return hash_table_players

# 2.2 Estrutura 2: Estrutura para buscas por strings de nomes
def structure_short_names_trie():
    before = datetime.datetime.now()
    trie_names = TernaryTrie()
    with open(caminho_players_csv) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        # Pula header
        next(reader)
        for row in reader:
            # row[0] = 'sofifa_id'
            # row[1] = 'short_name'
            trie_names.insert(row[2].lower(), int(row[0]))

    elapsed_time = datetime.datetime.now() - before
    print('Estrutura 2 finalizada. Tempo: ', elapsed_time)
    return trie_names

# 2.3 Estrutura 3: Estrutura para guardar revisoes de usuários
def structure_users_ratings():
    before = datetime.datetime.now()
    # Numero primo mais proximo de 80% da quantidade dos ratings
    hash_table_users = HashTable(100000)

    # Insere cada rating na lista da posição adequada 
    with open(caminho_ratings_csv) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        # Pula header
        next(reader)
        for row in reader:
            # row[0] = user_id
            key = int(row[0])
            user_ratings= hash_table_users.search(key, 'user_id')

            # row[1] = 'sofifa_id', row[2] = 'rating'
            user_id, player_id, rating = int(row[0]), int(row[1]), float(row[2])
            if(user_ratings):
                # If the key already existing on the HT, append the list of ratings of the user
                user_ratings['ratings'].append((player_id, rating))
            else:
                # Else, initialize new dictionary with only the first rating and insert on the rtable
                # row[0] = user_id
                dict_ratings ={'user_id':user_id, 'ratings': [(player_id, rating)]}
                hash_table_users.insert(key, dict_ratings)
        
    elapsed_time = datetime.datetime.now() - before
    print('Estrutura 3 finalizada. Tempo: ', elapsed_time)
    return hash_table_users

# 2.4 Estrutura 4: Estrutura para guardar tags
def structure_players_tags():
    before = datetime.datetime.now()
    trie_tags = Trie()
    with open(caminho_tags_csv) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            # Pula header
            next(reader)
            for row in reader:
                # row[1] = 'sofifa_id'
                # row[2] = 'tag'
                trie_tags.insert(row[1], str(row[2]))
    elapsed_time = datetime.datetime.now() - before
    print('Estrutura 4 finalizada. Tempo: ', elapsed_time)
    return trie_tags

