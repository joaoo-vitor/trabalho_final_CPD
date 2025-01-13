from creating_structures import *
from prettytable import PrettyTable

def players_starting_with_short_name(prefix, trie_names, ht_players):
    ids_players = trie_names.search(prefix)
    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'player_positions',  'nationality', 'rating', 'count']
    for id in ids_players:
        player = search_hash_table(id, 'sofifa_id', ht_players, ht_size)
        result.add_row((player[column] for column in result.field_names))
    return 
