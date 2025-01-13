import csv
from prettytable import PrettyTable

#2.2 Estrutura 2: Estrutura para buscas por strings de nomes
def criar_tabela_hash(tamanho):
    return [None] * tamanho

def inserir_na_tabela(tabela, chave, valor):
    indice = hash(chave) % len(tabela)

    if tabela[indice] is None:
        tabela[indice] = [(chave, valor)]
    else:
        for i, (chave_existente, _) in enumerate(tabela[indice]):
            if chave_existente == chave:
                tabela[indice][i] = (chave, valor)
                return
        tabela[indice].append((chave, valor))

def buscar_na_tabela(tabela, chave):
    indice = hash(chave) % len(tabela)
    lista_encadeada = tabela[indice]

    if lista_encadeada is not None:
        for chave_existente, valor in lista_encadeada:
            if chave_existente == chave:
                return valor

    print(f"Nenhuma avaliação encontrada para o usuário com ID {chave}.")
    return None

# Pesquisa 2

def buscar_sofifa_ids_por_usuario(tabela, user_id):
    avaliacao = buscar_na_tabela(tabela, user_id)

    if avaliacao is None:
        return None

    players, ratings = avaliacao["jogador_avaliado"], avaliacao["rating"]
    resultado = list(zip(players, ratings))
    resultado.sort(key=lambda x: x[1], reverse=True)

    tabela_resultados = PrettyTable()
    tabela_resultados.field_names = ["Sofifa ID", "Rating by User"]
    for jogador, rating in resultado[:20]:
        tabela_resultados.add_row([jogador, rating])

    print(tabela_resultados)

def carregar_jogadores(arquivo):
    tabela = criar_tabela_hash(100000)

    with open(arquivo, "r") as arquivo_jogadores:
        arquivo_csv = csv.reader(arquivo_jogadores, delimiter=",")
        next(arquivo_csv)

        for linha in arquivo_csv:
            sofifa_id, short_name, *_ = linha
            inserir_na_tabela(tabela, sofifa_id, {
                "short_name": short_name,
                "rating_soma": 0,
                "rating_contador": 0
            })

    return tabela

def carregar_ratings(arquivo, tabela_jogadores):
    tabela_ratings = criar_tabela_hash(100000)
    user_rating = set()

    with open(arquivo, "r") as arquivo_rating:
        arquivo_csv = csv.reader(arquivo_rating, delimiter=",")
        next(arquivo_csv)

        for linha in arquivo_csv:
            user_id, sofifa_id, rating = linha[0], linha[1], float(linha[2])
            jogador = buscar_na_tabela(tabela_jogadores, sofifa_id)

            if jogador is not None:
                jogador["rating_soma"] += rating
                jogador["rating_contador"] += 1

                if user_id not in user_rating:
                    user_rating.add(user_id)
                    inserir_na_tabela(tabela_ratings, user_id, {
                        "jogador_avaliado": [sofifa_id],
                        "rating": [rating]
                    })
                else:
                    avaliacao_usuario = buscar_na_tabela(tabela_ratings, user_id)
                    avaliacao_usuario["jogador_avaliado"].append(sofifa_id)
                    avaliacao_usuario["rating"].append(rating)

    return tabela_ratings

tabela_jogadores = carregar_jogadores("players.csv")
tabela_ratings = carregar_ratings("minirating.csv", tabela_jogadores)

buscar_sofifa_ids_por_usuario(tabela_ratings, "1018")
