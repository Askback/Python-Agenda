import os

AGENDA =\
    {

    }


def mostrar_contatos():
    if len(AGENDA):
        for contato in AGENDA:
            buscar_contatos(contato)
    else:
        print(">>> A Agenda está vazia")


def buscar_contatos(contato):
    try:
        print("Nome:", contato)
        print("Email:", AGENDA[contato]["email"])
        print("Telefone:", AGENDA[contato]["tel"])
        print("Endereço:", AGENDA[contato]["endereco"])
        print("\n**************************************\n")
    except KeyError:
        print("\n>>>O contato {} não existe \n".format(contato))
    except Exception as e:
        print(">>>Um erro inesperado aconteceu {}".format(e))


def incluir_editar_contatos(contato,telefone,email,endereco):
    AGENDA [contato] = {
        "tel": telefone,
        "email": email,
        "endereco": endereco
    }
    salvar()
    print("\nO contado {} foi adicionado com sucesso".format(contato))
    print("####-####-####-####-####-####-####-####\n")


def excluir_contatos(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print("\n>>>O contato {} foi excluido com sucesso\n".format(contato))
    except KeyError:
        print("\n>>>O contato {} não existe \n".format(contato))
    except Exception as e:
        print(">>>Um erro inesperado aconteceu {}".format(e))


def ler_detalhes_contato():
    endereco = input("Digite o endereco: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    return telefone, email, endereco

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo,'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]["tel"]
                email = AGENDA[contato]["email"]
                endereco = AGENDA[contato]["endereco"]
                arquivo.write("{},{},{},{}\n".format(contato,telefone,email,endereco))
    except Exception as e:
        print(">>> Ocorreu algum erro durante a exportação ", e)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contatos(contato,telefone,email,endereco)
    except FileNotFoundError:
        print(">>> Arquivo não encontrado")
    except Exception as e:
        print(">>> Um erro inesperado ocorreu",e)


def menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos CSV')
    print('0 - Sair da agenda')
    print("\n")


def salvar():
    exportar_contatos("database.csv")


def carregar():
    try:
        with open("database.csv", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA [contato] = {
                    "tel": telefone,
                    "email": email,
                    "endereco": endereco
                }
            print(">>>Agenda carregada com sucesso")
            print(">>>{} contatos carregados com sucesso".format(len(AGENDA)))
    except FileNotFoundError:
        print(">>> Arquivo não encontrado")
    except Exception as e:
        print(">>> Um erro inesperado ocorreu",e)


def escolha(opcao):
    match opcao:
        case '1':
            os.system('clear')
            mostrar_contatos()
        case '2':
            os.system('clear')
            buscar_contatos(input("Digite o nome do contato desejado "))
        case '3':
            os.system('clear')
            contato = input("Digite o nome do contato a ser inserido: ")

            try:
                AGENDA[contato]
                print(">>> Contato já existente:", contato)
            except KeyError:
                telefone, email, endereco = ler_detalhes_contato()
                incluir_editar_contatos(contato,telefone,email,endereco)
                buscar_contatos(contato)
            except Exception as e:
                print(">>>Um erro inesperado aconteceu {}".format(e))
        case '4':
            os.system('clear')
            contato = input("Digite o nome do contato a ser editado: ")

            try:
                AGENDA[contato]
                telefone, email, endereco = ler_detalhes_contato()
                incluir_editar_contatos(contato,telefone,email,endereco)
                buscar_contatos(contato)
            except KeyError:
                print(">>> Contato inexistente")
            except Exception as e:
                print(">>>Um erro inesperado aconteceu {}".format(e))

        case '5':
            os.system('clear')
            excluir_contatos(input("Digite o nome do contato a ser excluido: "))
        case '0':
            os.system('clear')
            print("Fechando programa: (╥︣﹏᷅╥)")
            exit()
        case '6':
            os.system('clear')
            exportar_contatos(input("Digite o nome do arquivo: "))
        case '7':
            os.system('clear')
            importar_contatos(input("Digite o nome do arquivo a ser importado: "))
        case _:
            os.system('clear')
            print("\nOpcao inválida ( ˘︹˘ )\n")


carregar()


while True:
    menu()
    escolha(input("Escolha uma opção \n"))