import pandas as pd
from ternary_trie import *
from hashing import *
from trie import *
from prettytable import PrettyTable
from quicksort import quick_sort_lomuto

# 3.1 Pesquisa 1: prefixos de nomes de jogadores
def prefixo(prefix, names_trie, ht_players):  
    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'player_positions',  'nationality', 'rating_avg', 'number_of_ratings']
    ids_players = names_trie.search(prefix)
    arr_rows = []
    if(ids_players):
        for id in ids_players:
            player = ht_players.search(id, 'sofifa_id')
            player['rating_avg'] = '%0.6f' % player['rating_avg']  
            arr_rows.append([player[column] for column in result.field_names])
            print('adding to the table: \n', [player[column] for column in result.field_names])
        # Ordena em ordem decrescente a partir do rating global (index 5)
        quick_sort_lomuto(arr_rows, 5, 0, len(arr_rows)-1, dec=True)
    # Adiciona da array para a tabela
    for row in arr_rows:
        result.add_row(row)
    return result

# 3.2 Pesquisa 2: jogadores revisados por usuários
def user(user_id, ht_users, ht_players):
    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'rating_avg', 'number_of_ratings', "user's rating"]
    ratings_user = ht_users.search(user_id, 'user_id')
    print(f'encontrei {len(ratings_user)} ratings desse usuario')
    arr_rows = []
    if(ratings_user):
        for rating in ratings_user['ratings']:
            player = ht_players.search(rating[0], 'sofifa_id')
            player['rating_avg'] = '%0.6f' % player['rating_avg']  
            arr_rows.append([player['sofifa_id'], player['short_name'], player['long_name'], player['rating_avg'], player['number_of_ratings'], rating[1]])
        # Ordena em ordem decrescente a partir da nota global do jogador (index 3) - sorting secundária
        quick_sort_lomuto(arr_rows, 3, 0, len(arr_rows)-1, dec=True)
        # Ordena em ordem decrescente a partir da nota atribuida pelo user (index 5) - sorting primária
        quick_sort_lomuto(arr_rows, 5, 0, len(arr_rows)-1, dec=True)
        # Remove o sobrejacente (apenas 30)
        count =0
        for row in arr_rows:
            result.add_row(row)
            count+=1
            if(count==30):
                break
    # Adiciona da array para a tabela
    for row in arr_rows:
        result.add_row(row)
    return result

# 3.3 Pesquisa 3: melhores jogadores de uma determinada posicão


# 3.4 Pesquisa 4: prefixos de nomes de jogadores
def tags(trie_tags_list, ht_players, tags_list):
    ids_players = trie_tags_list.search(tags_list[0])

    for trie_tags in tags_list[1:]:
        newTagResult = trie_tags_list.search(trie_tags)
        new_tag_ids_set = set(newTagResult)
        ids_players = list(set(ids_players).intersection(new_tag_ids_set))

    if not ids_players:
        print ("Nenhum jogador encontrado com essas tags")
        return

    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'player_positions',  'nationality', 'rating_avg', 'number_of_ratings']
    for id in ids_players:
        player = ht_players.search(int(id), 'sofifa_id')
        result.add_row([player[column] for column in result.field_names])

    return result


# 3.3 Pesquisa 3: melhores jogadores de uma determinada posicão


# 3.4 Pesquisa 4: prefixos de nomes de jogadores

def tags(trie_tags_list, ht_players, tags_list):
    ids_players = trie_tags_list.search(tags_list[0])

    for trie_tags in tags_list[1:]:
        newTagResult = trie_tags_list.search(trie_tags)
        new_tag_ids_set = set(newTagResult)
        ids_players = list(set(ids_players).intersection(new_tag_ids_set))

    if not ids_players:
        print ("Nenhum jogador encontrado com essas tags")
        return

    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'player_positions',  'nationality', 'rating_avg', 'number_of_ratings']
    for id in ids_players:
        player = ht_players.search(int(id), 'sofifa_id')
        result.add_row([player[column] for column in result.field_names])

    return result
