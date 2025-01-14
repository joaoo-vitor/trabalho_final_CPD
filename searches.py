import pandas as pd
from ternary_trie import *
from hashing import *
from trie import *
from prettytable import PrettyTable

# 3.1 Pesquisa 1: prefixos de nomes de jogadores
def prefixo(prefix, names_trie, ht_players):  
    ids_players = names_trie.search(prefix)
    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'player_positions',  'nationality', 'rating_avg', 'number_of_ratings']
    
    players_data = []

    for id in ids_players:
        player = ht_players.search(id, 'sofifa_id')
        player['rating_avg'] = '%0.6f' % player['rating_avg']  
        players_data.append(player)

    players_data.sort(key=lambda x: float(x['rating_avg']), reverse=True)
    for player in players_data:
        result.add_row([player[column] for column in result.field_names])

    return result

# 3.2 Pesquisa 2: jogadores revisados por usuários
def user(user_id, ht_users, ht_players):
    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'rating_avg', 'number_of_ratings', "user's rating"]
    ratings_user = ht_users.search(user_id, 'user_id')
    players_data = []
    for rating in ratings_user['ratings']:
        player = ht_players.search(rating[0], 'sofifa_id')
        player['rating_avg'] = '%0.6f' % player['rating_avg']  
        players_data.append({
            'sofifa_id': player['sofifa_id'],
            'short_name': player['short_name'],
            'long_name': player['long_name'],
            'rating_avg': float(player['rating_avg']),  
            'number_of_ratings': player['number_of_ratings'],
            "user_rating": rating[1]
        })
    players_data.sort(key=lambda x: (x['user_rating'], x['rating_avg']), reverse=True)
    
    players_data = players_data[:30]
    
    for player in players_data:
        result.add_row([
            player['sofifa_id'], 
            player['short_name'], 
            player['long_name'], 
            '%0.6f' % player['rating_avg'],  
            player['number_of_ratings'], 
            player['user_rating']
        ])
    return result


# 3.3 Pesquisa 3: melhores jogadores de uma determinada posicão


# 3.4 Pesquisa 4: prefixos de nomes de jogadores

def tags(trie_tags_list, ht_players, tags_list):
    # Busca inicial com a primeira tag
    ids_players = trie_tags_list.search(tags_list[0])

    # Filtra jogadores que possuem todas as tags
    for trie_tag in tags_list[1:]:
        new_tag_result = trie_tags_list.search(trie_tag)
        new_tag_ids_set = set(new_tag_result)
        ids_players = list(set(ids_players).intersection(new_tag_ids_set))

    if not ids_players:
        print("Nenhum jogador encontrado com essas tags")
        return

    # Cria tabela de resultados
    result = PrettyTable()
    result.field_names = [
        'sofifa_id', 'short_name', 'long_name', 
        'player_positions', 'nationality', 
        'rating_avg', 'number_of_ratings'
    ]

    # Obter dados e adicionar na tabela
    players_data = []
    for id in ids_players:
        player = ht_players.search(int(id), 'sofifa_id')
        if player:
            # Formata a nota global com 6 casas decimais
            player['rating_avg'] = "{:.6f}".format(float(player['rating_avg']))
            players_data.append(player)

    # Ordena os jogadores por nota global (decrescente)
    players_data.sort(key=lambda x: float(x['rating_avg']), reverse=True)

    # Adiciona jogadores à tabela
    for player in players_data:
        result.add_row([player[column] for column in result.field_names])

    return result
