# Chamar função que construa estruturas


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
                
        elif user_input == 2:
            while True:
                nome = input("\nDIGITE O ID DO USUARIO (ou '9' para voltar): ")
                if nome == '9':
                    break
                
        elif user_input == 3:
            while True:
                nome = input("\nDIGITE O TAMANHO E A POSICAO DO RANKING (ou '9' para voltar): ")
                if nome == '9':
                    break
    
                
        elif user_input == 4:
            while True:
                tags = input("\nDIGITE AS TAGS PARA BUSCAR OS JOGADORES (ou '9' para voltar): ")
                if tags == '9':
                    break
                
        elif user_input == 0:
            print("Saindo do programa...")
            break
        else:
            print("OPCAO INVALIDA TENTE NOVAMENTE\n")
    except ValueError:
        print("ENTRADA INVALIDA! APENAS NUMEROS SAO ACEITOS\n")
