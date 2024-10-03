def ver_contatos(contatos):
    print("\nLista de Contatos:")
    if not contatos:
        print("A lista de contatos está vazia.")
        return
    
    # Exibe a lista de nomes dos contatos
    for indice, contato in enumerate(contatos, start=1):
        fav = "★" if contato["Favoritos"] else " "
        nome_contato = contato["Contato"]
        print(f"{indice}. [{fav}] Nome: {nome_contato}")
    
    # Pergunta se o usuário quer ver detalhes de um contato específico
    escolha_contato = input("\nDigite o número do contato para ver detalhes ou pressione Enter para voltar: ")

    # Verifica se a escolha é válida
    if escolha_contato.isdigit():
        indice = int(escolha_contato) - 1  # Converte a escolha para o índice da lista
        if 0 <= indice < len(contatos):
            contato = contatos[indice]
            nome_contato = contato["Contato"]
            telefone = contato["Telefone"]
            email = contato["Email"]
            print(f"\nDetalhes do contato {nome_contato}:")
            print(f"Telefone: {telefone}")
            print(f"Email: {email}")
        else:
            print("Número inválido! Por favor, tente novamente.")
    else:
        print("Voltando ao menu principal.")

contatos = []