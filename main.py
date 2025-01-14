from searches import *
from creating_structures import *

# Chama função pra construir cada estrutura
print('Criando estruturas...')
hash_table_players = structure_players_data()
names_ternary_trie = structure_short_names_trie()
hash_table_users = structure_users_ratings()
tags_trie = structure_players_tags()

# Menu de busca
print('\nESCOLHA UMA DAS OPCOES DE PESQUISAS ABAIXO:\n')
user_input = -1  
while user_input != 0:
    try:
        print("\n  1 - Buscar jogadores por prefixo\n  2 - Avaliacoes dos jogadores pelos usuarios")
        print("  3 - Top jogadores por posicao\n  4 - Busca por tags\n  0 - Sair \n")
        user_input = int(input('> '))  

        if user_input == 1:
            while True:
                nome = input("\nDIGITE O PREFIXO DO NOME DO JOGADOR (ou '9' para voltar): ")
                if nome == '9':
                    break
                print(prefixo(nome,names_ternary_trie,hash_table_players))
                
        elif user_input == 2:
            while True:
                id = input("\nDIGITE O ID DO USUARIO (ou '9' para voltar): ")
                if id == '9':
                    break
                print(user(int(id), hash_table_users, hash_table_players))
                
        elif user_input == 3:
            while True:
                top_input_str = input("\nDIGITE O TAMANHO E A POSICAO DO RANKING (ou '9' para voltar): ")
                if top_input_str == '9':
                    break
                top_input = top_input_str.split()
                n = top_input[0]
                position = top_input[1]
                print(top(n, position, hash_table_players))
                
        elif user_input == 4:
            while True:
                tags_input = input("\nDIGITE AS TAGS PARA BUSCAR OS JOGADORES (ou '9' para voltar): ")
                if tags_input == '9':
                    break
                tags_input = tags_input.split("'")[1::2]
                print(tags(tags_trie, hash_table_players, tags_input))
                
        elif user_input == 0:
            print("Saindo do programa...")
            break
        else:
            print("OPCAO INVALIDA TENTE NOVAMENTE\n")
    except ValueError:
        print("ENTRADA INVALIDA! APENAS NUMEROS SAO ACEITOS\n")
