def adicionar_contato(contatos, nome_contato, numero_telefone, endereco_email): 
    contato = {
        "Contato": nome_contato, 
        "Telefone": numero_telefone, 
        "Email": endereco_email, 
        "Favoritos": False,  # Adicionando a chave Favoritos com valor padrão False
        "Adicionado": True
    }
    contatos.append(contato)
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
        print(f"{indice}. [{fav}] {nome_contato}")

contatos = []
while True:    # comando while para rodar o software em loop
    print("\nMenu:")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar lista de contatos")           # Aqui os comandos do menu
    print("4. Marcar/Desmarcar favoritos")
    print("5. Ver lista favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite um número correspondente às opções: ")
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        numero_telefone = input("Digite o número do telefone com DDD (xx)xxxxx-xxxx: ")
        endereco_email = input("Digite o endereço de email: ")
        adicionar_contato(contatos, nome_contato, numero_telefone, endereco_email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "7":
        break

print("Programa finalizado")