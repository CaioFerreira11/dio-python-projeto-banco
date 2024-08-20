from datetime import date 


depositos = []
saques = []
num_saques = 3
saldo = 0
LIMITE_SAQUE = 1500
while True:

    opc = int(input("""
    SELECIONE A OPERAÇÃO DESEJADA:
    ------------------------------
        [1] - EXTRATO   
        [2] - DEPOSITO    
        [3] - SAQUE
        [4] - SAIR
    ------------------------------
"""))


    if opc == 1:
        print(f""" 
                Depositos:
                    {depositos}

                Saques:
                    {saques}

                Saldo Atual:
                    R$ {saldo:.2f}
              """)
        

    elif opc == 2:
        quantia_dep = int(input('Quantia a ser depositada: \n'))
        saldo += quantia_dep

        reg_deposito = f"Deposito feito no horario de: {date.today()} na quantia de R$ {quantia_dep:.2f}"

        depositos.append(reg_deposito)

    elif opc == 3:
        quantia_saq = int(input('Quantia a ser sacada: \n'))
        
        if quantia_saq > saldo or quantia_saq <= 0:
            print("Impossível sacar, saldo insuficiente ou quantia solicitada para saque menor ou igual a zero.")
        
        elif quantia_saq> LIMITE_SAQUE or num_saques == 0:
            print('Limite de quantia de saque excedida.') 

        elif quantia_saq <= LIMITE_SAQUE and num_saques > 0 and quantia_saq<= saldo:

            saldo -= quantia_saq
            reg_saque = f"Saque feito no horario de {date.today()} na quantia de R$ {quantia_saq:.2f}"
            saques.append(reg_saque)
            LIMITE_SAQUE -= quantia_saq
            num_saques-= 1

    elif opc == 4:
        break