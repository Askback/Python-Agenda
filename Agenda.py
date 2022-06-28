import os

AGENDA =\
    {
        "Exemplo1":{
            "tel":"1111",
            "email":"exemplo1@gmail.com",
            "endereco":"Rua x, 11"
        },
        "Exemplo2":{
            "tel":"2222",
            "email":"exemplo2@live.com",
            "endereco":"Rua y, 22"
        },
        "Exemplo3": {
            "tel": "3333",
            "email": "exemplo3@hotmail.com",
            "endereco": "Rua z, 33"
        }
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


def incluir_editar_contatos(contato):
    endereco = input("Digite o endereco: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    AGENDA [contato] = {
        "tel": telefone,
        "email": email,
        "endereco": endereco
    }
    print("\nO contado {} foi adicionado com sucesso".format(contato))
    print("####-####-####-####-####-####-####-####\n")


def excluir_contatos(contato):
    try:
        AGENDA.pop(contato)
        print("\n>>>O contato {} foi excluido com sucesso\n".format(contato))
    except KeyError:
        print("\n>>>O contato {} não existe \n".format(contato))
    except Exception as e:
        print(">>>Um erro inesperado aconteceu {}".format(e))


def exportar_contatos():
    try:
        with open('agenda.csv','w') as arquivo:
            for contatos in AGENDA:
                telefone = AGENDA[contatos]["tel"]
                email = AGENDA[contatos]["email"]
                endereco = AGENDA[contatos]["endereco"]
                arquivo.write("{},{},{},{}\n".format(contatos,telefone,email,endereco))
    except Exception as e:
        print(">>> Ocorreu algum erro durante a exportação ", e)


def menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('0 - Sair da agenda')
    print("\n")


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
                incluir_editar_contatos(contato)
                buscar_contatos(contato)
            except Exception as e:
                print(">>>Um erro inesperado aconteceu {}".format(e))
        case '4':
            os.system('clear')
            contato = input("Digite o nome do contato a ser editado: ")

            try:
                AGENDA[contato]
                incluir_editar_contatos(contato)
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
            exportar_contatos()
        case _:
            os.system('clear')
            print("\nOpcao inválida ( ˘︹˘ )\n")


while True:
    menu()
    escolha(input("Escolha uma opção \n"))