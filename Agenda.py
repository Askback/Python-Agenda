import os
import sys

AGENDA =\
    {
        "Marcos":{
            "tel":"945202128",
            "email":"askback@hotmail.com",
            "endereco":"Rua das ferreiras, 75"
        },
        "Jose":{
            "tel":"965403237",
            "email":"england-s2@live.com",
            "endereco":"Rua pindamoian, 67"
        },
        "Rugu": {
            "tel": "969343227",
            "email": "seven7@live.com",
            "endereco": "Rua balaomen, 77"
        }
    }


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contatos(contato)



def buscar_contatos(contato):
    print("Nome:", contato)
    print("Email:", AGENDA[contato]["email"])
    print("Telefone:", AGENDA[contato]["tel"])
    print("Endereço:", AGENDA[contato]["endereco"])
    print("\n**************************************\n")




def incluir_editar_contatos(contato, email, telefone, endereco):
    AGENDA [contato] = {
        "tel": telefone,
        "email": email,
        "endereco": endereco
    }
    print("\nO contado {} foi adicionado com sucesso".format(contato))
    print("####-####-####-####-####-####-####-####\n")


def excluir_contatos(contato):
    AGENDA.pop(contato)
    print("\nO contado {} foi excluido com sucesso".format(contato))


def menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Sair da agenda')
    print("\n")


def escolha(opcao):
    match opcao:
        case '1':
            mostrar_contatos()
        case '2':
            buscar_contatos(input("Digite o nome do contato desejado "))
        case '3'|'4':
            contato = input("Digite o nome do contato a ser inserido ou editado: ")
            endereco = input("Digite o endereco: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            incluir_editar_contatos(contato, telefone, endereco, email)
            buscar_contatos(contato)
        case '5':
            excluir_contatos(input("Digite o nome do contato a ser excluido"))
        case '0':
            print("Fechando programa (╥︣﹏᷅╥)")
            sys.exit()
        case _:
            os.system('clear')
            print("Opcao inválida")

while True:
    menu()
    escolha(input("Escolha uma opção \n"))