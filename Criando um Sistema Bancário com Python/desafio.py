from datetime import datetime
import sys
import os

class ContaBanco:
    def __init__(self):
        self.saldo = 0
        self.extratos = {}
        self.limiteSaques = 3
        pass

    def saque(self, valor):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if self.limiteSaques > 0:
            if valor > 500:
                print("[SISTEMA] Saque de valor muito alto!")
                return
            if self.saldo >= valor:
                self.extratos[dt_string] = f"{valor:.2f}"
                self.saldo = self.saldo - valor
                self.limiteSaques = self.limiteSaques - 1
                print(f"[SISTEMA] Saque no valor de R${valor:.2f} confirmado, ({self.limiteSaques} saques restantes)")
                pass
            else:
                print("[SISTEMA] Saldo insuficiente")
                self.extratos[dt_string] = "Saque mal-sucedido (Saldo Insuficiente)"
                pass
        else:
            print("[SISTEMA] Você não pode mais fazer saques hoje!")

    def deposito(self, valor):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.extratos[dt_string] = f"{valor:.2f}"
        self.saldo = self.saldo + valor
        print(f"[SISTEMA] Deposito no valor de R${valor:.2f} confirmado")
        pass

    def verExtrato(self):
        return self.extratos

if sys.platform.startswith('linux'):
    os.system('clear')
if sys.platform.startswith('win32'):
    os.system('cls')
conta = ContaBanco()
print("[SISTEMA] Digite o nome, o atalho, ou o número do comando (1~4):")
def update():
    print("\n[D] Depositar\n[S] Sacar\n[E] Extrato\n[Q] Sair")
    userinput = input().lower()
    if userinput == "d" or userinput == "depositar" or userinput == "1":
        try:
            valor = float(input("[SISTEMA] Digite o valor (R$): "))
            conta.deposito(valor)
        except:
            print("[SISTEMA] Ocorreu um erro! Tente novamente")
        pass
    if userinput == "s" or userinput == "sacar" or userinput == "2":
        try:
            valor = float(input("[SISTEMA] Digite o valor (R$): "))
            conta.saque(valor)
        except:
            print("[SISTEMA] Ocorreu um erro! Tente novamente")
        pass
    if userinput == "e" or userinput == "extrato" or userinput == "3":
        extratos = conta.verExtrato()
        s = ""
        for extrato in extratos:
            s = s + f"{extrato} : {extratos[extrato]}\n"
        s = s.strip("\n")
        print("[SISTEMA] Lista de Extratos\n" + s)
        print(f"Disponivel de Saldo: R${conta.saldo:.2f}")
        print(f"Saques Disponiveis de hoje: {conta.limiteSaques}")
        pass
    if userinput == "q" or userinput == "sair" or userinput == "4":
        sys.exit(0)
        pass
    pass

while True:
    update()