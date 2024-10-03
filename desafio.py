# Primeira função adicionar contato!
def adicionar_contato(contatos, nome_contato, numero_telefone, endereço_email): # Aqui comecei a primeira função
    contato = {"Contato": nome_contato, "Adicionado": False}        # Aqui nessa parte de contato tentei ampliar também
    telefone = {"Telefone": numero_telefone, "Adicionado": False}  # para colocar o telefone e o email.
    email = {"Email": endereço_email, "Adicionado": False}
    contatos.append([contato, telefone, email])   # append faz adicionar os dados em contato
    # Quando adicionei "[]" dentro de append resolveu o erro, mas não sei porque.
    print(f"contato {nome_contato, telefone, email} foi adicionada com sucesso!")
    return         # return para retornar o resultado

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

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["Contato"] = novo_nome_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato}")
    else:
        print("indice de tarefa Inválido.")
    return

contatos = []  #Esse "contatos = []" é o que armazena os dados inseridos pelo input #Esse "[]" siginifica que é lista !
while True:    # comando while para rodar o software em loop
    print("1. Adicionar contato: ")
    print("2. Visualizar lista de contatos: ")
    print("3. Editar lista de contatos: ")           #Aqui os comandos do menu
    print("4. Marcar/Desmarcar favoritos: ")
    print("5. Ver lista favoritos: ")
    print("6. Apagar contato: ")
    print("7. Sair")
    
    escolha = input("Digite um número correspondente as opções: ")
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        print("Agora coloque o telefone: ")
        numero_telefone = input("Digite o número do telefone com DDD (xx)xxxxx-xxxx:")
        print("Agora coloque o email: ")
        endereço_email = input("Digite o endereço de email: ")
        adicionar_contato(contatos, nome_contato, numero_telefone, endereço_email)
    
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        indice_contato = input("Digite o número da contato que deseja atualizar: ")
        novo_nome_contato = input("Digite o novo nome do contato: ")
        atualizar_nome_contato(contatos, indice_contato, novo_nome_contato)
    elif escolha == "7":
        break

print("Programa finalizado")