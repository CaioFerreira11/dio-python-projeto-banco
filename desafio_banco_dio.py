from datetime import datetime 


def despositar(saldo,valor,extrato):
    if valor >0:
        saldo+= valor
        extrato+= f"Depósito feito de: {valor:.2f} no horário de {datetime.now()}\n"
        print("Depósito realizado com sucesso!!!")
    else:
        print("Depósito falhou!! Valor menor ou igual a 0!!")
    return saldo,extrato

def sacar(f_saldo,f_valor,f_extrato,f_limite,f_num_saques):
    excedeu_saldo = f_valor>f_saldo
    excedeu_limite = f_valor>f_limite
    excedeu_saqs = f_num_saques == 0

    if excedeu_saldo:
        print("Valor para saque maior do que valor disponível em saldo na conta!!!")

    elif excedeu_limite:
        print("Valor para saque maior que o valor limite de saque diário!!!")

    elif excedeu_saqs:
        print("Número de saques disponível no dia zerado.")

    elif f_valor>0: 
        f_saldo-= f_valor
        f_extrato+= f"Saque feito de: {f_valor:.2f} no horário de {datetime.now()}\n"
        f_num_saques-=1
        print(f"Saque realizado com sucesso no horário de {datetime.now()}!!!")
    return f_saldo,f_extrato,f_num_saques       

def exibir_extrato(f_saldo, /, *, f_extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações!!" if not f_extrato else f_extrato)
    print(f"Saldo atual é: {f_saldo:.2f}")
    print("==========================================")

def novo_usuario(f_nome,f_nasc,f_cpf,f_ende,f_list_us):
        if f_cpf in f_list_us:
            print("Usuário já existente!!")
        else:   
            no_lista = {f_cpf:{"nome":f_nome,"nascimento":f_nasc,"endereco":f_ende}}
            print("Usuário adicionado com sucesso!!")
            f_list_us.update(no_lista)
        return f_list_us

def listar_contas(f_list_contas):
    print("\n========================USUÁRIO================================")
    print("Não foram encontrados contas registradas!!" if not f_list_contas else f_list_contas)
    print("=================================================================")

def nova_conta(f_cpf,f_lista_contas,f_agencia,f_conta,f_lista_user):
    if f_cpf in f_lista_user:
        f_lista_contas.update({f_cpf:{"Agência":f_agencia,"Conta":f_conta}})
        f_conta+=1
    else:
        print("Usuário não encontrado!!")
    return f_lista_contas,f_conta

AGENCIA = "0001"
conta = 1
contas = {}
lista_user = {}
extrato = ""
depositos = []
saques = []
num_saques = 3
saldo = 0
LIMITE_SAQUE = 500
LIMITE_TRA = 10

while True:

    menu = input("""


        ================ MENU ================
                    [d]\tDepositar
                    [s]\tSacar
                    [e]\tExtrato
                    [nc]\tNova conta
                    [lc]\tListar contas
                    [nu]\tNovo usuário
                    [q]\tSair
                 """)

    if menu == "d":

        valor = float(input('Valor para depositar: '))
        saldo,extrato = despositar(saldo,valor,extrato)

    elif menu == "s":
        valor = float(input("Digite o valor para saque: "))
        saldo, extrato,num_saques = sacar(
                                f_extrato=extrato,
                                f_saldo=saldo,
                                f_valor=valor,
                                f_limite=LIMITE_SAQUE,
                                f_num_saques=num_saques
                                )
    elif menu == "e":
        exibir_extrato(saldo,f_extrato=extrato)
    
    elif menu == "nu":
        nome = input("Digite o Nome do usuário a ser adicionado: \n")
        nasc = input("Digite a Data de Nascimento do usuário a ser adicionado: \n")
        cpf = input("Digite o CPF do usuário a ser adicionado: \n")
        ende = input("Digite o Endereço do usuário a ser adicionado: \n")

        lista_user = novo_usuario(f_nome=nome,f_nasc=nasc,f_cpf=cpf,f_ende=ende,f_list_us=lista_user)
    
    elif menu == "lc":
        listar_contas(f_list_contas=contas)

    elif menu == "nc":
        cpf = input("Digite o CPF desejado para criar uma conta: ")
        contas, conta = nova_conta(f_cpf=cpf,f_lista_contas=contas,f_agencia=AGENCIA,f_conta=conta,f_lista_user=lista_user)

    elif menu == "q":
        break

    


