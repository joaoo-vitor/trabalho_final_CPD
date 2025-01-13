import pandas as pd
from ternary_trie import *
from hashing import *
from trie import *
from prettytable import PrettyTable

def players_starting_with_short_name(prefix, names_trie, ht_players):
    ids_players = names_trie.search(prefix)
    result = PrettyTable()
    result.field_names = ['sofifa_id', 'short_name', 'long_name', 'player_positions',  'nationality', 'rating_avg', 'number_of_ratings']
    for id in ids_players:
        player = ht_players.search(id, 'sofifa_id')
        result.add_row(tuple(player[column] for column in result.field_names))
    # fazer o sort
    
    return result
