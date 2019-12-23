banco = 'BANCO SAFRA S/A'
nome = 'Ruan de Oliveira Camargo'
saldo = float(500.10)
conta = "AG 6789 C/C 65489-0"
senha = int(10)
mensagem = 'MENU'
inform = []
extrato = []


print('{0:^100}'.format(banco))
print()
print()
print('Nome: {}'.format(nome))
print('Conta: {}'.format(conta))
print('Saldo R$: {0:.2f}'.format(saldo))
print()
print('{0:^100}'.format(mensagem))
print()
print()
print('1-Saque\n2-transferência\n0-Sair')
print()

class bank:

    def saque(self,saldo):
        valor_saque = float(input('Valor a ser sacado:'))
        while (valor_saque > saldo):
            print('Você não possui saldo suficiente, seu saldo é de: R${0:.2f}'.format(saldo))
            valor_saque = float(input('Valor a ser sacado:'))
        verificacao = int(input('Informe a senha: '))
        while (verificacao != senha):
            print('Senha incorreta')
            verificacao = int(input('Informe a senha: '))
        confirmacao = str(input('Confirmar saque? 1-(S) 2-(N)'))
        if (confirmacao == 'S' or confirmacao == 's'):
            print('Saque realizado com sucesso')
            print('Saque R$:{}'.format(valor_saque))
            saldo -= valor_saque
            return saldo
        else:
            saldo = saldo
            return saldo

    def transferencia(self,saldo):
        beneficiario = input('Beneficiário: ')
        ag = int(input('Digite a Agência: '))
        conta = int(input('Digite a Conta: '))
        valor_transferencia = float(input('Valor para depósito: '))
        while(valor_transferencia > saldo):
            print('Você não possui saldo suficiente, seu saldo é de: R${0:.2f}'.format(saldo))
            valor_transferencia = float(input('Valor para depósito: '))
        verificacao = int(input('Informe a senha: '))
        while (verificacao != senha):
            print('Senha incorreta')
            verificacao = int(input('Informe a senha: '))
        confirmacao = str(input('Confirmar saque? 1-(S) 2-(N)'))
        if(confirmacao =='s' or confirmacao=='S'):
            print('Depósito realizado com sucesso')
            print('Beneficiário: {}'.format(beneficiario))
            print('Agência: {}'.format(ag))
            print('Conta: {}'.format(conta))
            print('Valor de transferência R${}'.format(valor_transferencia))
            saldo -= valor_transferencia
            return saldo
        else:
            saldo = saldo
            return saldo




menu = int(input('Informe a operação desejada: '))

while(menu !=0):
    if(menu ==1):
        operacao = bank()
        saldo = operacao.saque(saldo)
        print('Saldo R$: {0:.2f}'.format(saldo))
    elif(menu ==2):
        operacao = bank()
        saldo = operacao.transferencia(saldo)
        print('Saldo R$: {0:.2f}'.format(saldo))
    elif(menu >2):
        print("Você não digitou uma operação válida")


    print()
    print('1-Saque 2-Transferência 0-Sair')
    print()
    print()
    menu = int(input('Informe a operação desejada: '))
