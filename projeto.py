def adicionar_contato(contatos, nome_contato, numero_telefone, endereco_email): 
    contato = {
        "Contato": nome_contato, 
        "Telefone": numero_telefone, 
        "Email": endereco_email, 
        "Favoritos": False,  # Adicionando a chave Favoritos com valor padrão False
        "Adicionado": True
    }
    contatos.append(contato)  # Adiciona um dicionário diretamente à lista
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return 

def ver_contatos(contatos):
    print("\nLista de Contatos:")
    if not contatos:
        print("A lista de contatos está vazia.")
        return
    for indice, contato in enumerate(contatos, start=1):
        fav = "★" if contato["Favoritos"] else " "
        nome_contato = contato["Contato"]
        telefone = contato["Telefone"]
        email = contato["Email"]
        print(f"{indice}. [{fav}] Nome: {nome_contato}")
        print(f"   Telefone: {telefone}")
        print(f"   Email: {email}")

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["Contato"] = novo_nome_contato
        contatos[indice_contato_ajustado]["Telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["Email"] = novo_email
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato}, {novo_telefone}, {novo_email}")
    else:
        print("Índice de contato inválido.")
    return

def marcar_fav(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["Favoritos"] = True  # Corrigido para "Favoritos"
        print(f"Contato {indice_contato} marcado como favorito!")
    else:
        print("Índice de contato inválido.")
    return

def ver_favoritos(contatos):
    print("\nLista de Favoritos:")
    favoritos = [contato for contato in contatos if contato["Favoritos"]]
    if not favoritos:
        print("A lista de favoritos está vazia.")
        return
    for indice, contato in enumerate(favoritos, start=1):
        nome_contato = contato["Contato"]
        telefone = contato["Telefone"]
        email = contato["Email"]
        print(f"{indice}. Nome: {nome_contato}")
        print(f"   Telefone: {telefone}")
        print(f"   Email: {email}")

contatos = []

# Loop para o menu principal
while True:    
    print("\nMenu:")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar lista de contatos")
    print("4. Marcar favoritos")
    print("5. Ver lista de favoritos")
    print("6. Sair")

    escolha = input("Digite um número correspondente às opções: ")
    
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        numero_telefone = input("Digite o número do telefone com DDD (xx)xxxxx-xxxx: ")
        endereco_email = input("Digite o endereço de email: ")
        adicionar_contato(contatos, nome_contato, numero_telefone, endereco_email)

    elif escolha == "2":
        ver_contatos(contatos)
    
    elif escolha == "3":
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome_contato = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_email = input("Digite o novo email: ")
        atualizar_nome_contato(contatos, indice_contato, novo_nome_contato, novo_telefone, novo_email)
    
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        marcar_fav(contatos, indice_contato)
    elif escolha == "5":
        ver_favoritos(contatos)
    elif escolha == "6":
        break

print("Programa finalizado")
