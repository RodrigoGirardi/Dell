import re
import csv
from collections import Counter
import sys
import time
import pandas as pd
import os
from pathlib import Path
import random

RED = "\033[31m"  
GREEN = "\033[32m" 
YELLOW = "\033[33m" 
RESET = "\033[0m"  

supriseList = []
apostaGanhadora = []
bet = []
data = []

def verifyNome(data):
    if re.search(r'[#@\$%&*()/+*]', data):
        return False
    return True

def verifyCpf(data):
    if re.search(r'[#@\$%&*()/+*-]', data):
        return False
    return True

def randomizer():#gera a surprise list
    for i in range(5):
        r = random.randrange(1,50)
        supriseList.append(r)
    print(supriseList)

def apuração():#gera os valores ganhadores
    for i in range(5):
        w = random.randrange(1,50)
        apostaGanhadora.append(w)


def escrita(data):#escreve a aposta no arquivo
    with open("apostas.csv", mode='a', newline='', encoding='utf-8') as arq:
        fieldnames = ['registro','nome', 'cpf','aposta']
        writer = csv.DictWriter(arq, fieldnames=fieldnames)
        if arq.tell() == 0:
            writer.writeheader()
        #colocaCabecalho(arq)
        writer.writerow({'registro': data[0],'nome': data[1], 'cpf': data[2],'aposta':data[3]})
        arq.close()

'''def colocaCabecalho(arquivo):
    if os.path.getsize('apostas.csv') == 0:
        cabecalho = csv.DictWriter(arquivo, fieldnames={'registro','nome', 'cpf','aposta'})
        cabecalho.writeheader()'''


def leitura():
    with open('apostas.csv',mode = 'r', newline='', encoding='utf-8') as arq3:
        leitor = csv.reader(arq3)
        if os.path.getsize('apostas.csv') == 0:
            print("Nao ha apostas registradas")
            arq3.close()
        for i in leitor:
            print(i)
    arq3.close()

def atualizaRegistro():#esta função tem o objetivo de ao inicializar o programa, percorrer apenas 1 vez o arquivo para verificar o número do último registro
    with open("apostas.csv", mode='r', newline='', encoding='utf-8') as arq2:
        registro = 1000
        reader = csv.reader(arq2)
        if os.path.getsize('apostas.csv') == 0:
            return registro
        #colocaCabecalho(arq2)
        next(reader)#começar na linha 1 / pula cabecalho
        primLineValid = next(reader,None)
        if primLineValid is None:
            arq2.close()
            return registro
        for i in reader:
            registro = i[0]#coluna 'registro' / armazenei o ultimo valor da coluna registro
            #print(registro)
        #print(registro)
        registro = str(int(registro) + 1)
        arq2.close()
        return registro
        
def procuraGanhador(dadosPremiados):
    with open('apostas.csv', mode = 'r', newline='', encoding='utf-8') as win:
        #coluna = 'aposta'
        dadosPvalidar = []
        reader = csv.DictReader(win)
        for linha in reader:#percorrer as linhas
            print(linha['aposta'])
            dadosPvalidar.append(linha['aposta'])
            print(dadosPvalidar[0])
            conta_vencedor1 = Counter(dadosPvalidar)
            conta_vencedor2 = Counter(dadosPremiados)

            ganhador = conta_vencedor1 == conta_vencedor2

            if ganhador:
                print("Sim")
            else:
                print("Não")
            dadosPvalidar.clear()
            '''for x in range(5):
                if dadosPremiados[i] == dadosPvalidar[x]:
                    print("achei")'''

'''dadosPvalidar.append(linha['aposta'])
print(f"{dadosPvalidar}")'''



#################################################
###############   INICIO
#################################################
        

print(GREEN + "Olá, seja bem-vindo a MegaSena DELL" + RESET)
#################################################
###############   FASE DE APOSTAS
#################################################

while True:
    print(GREEN + "Digite 1 para cadastrar nova aposta." + RESET)
    print(GREEN + "Digite 2 para listar as apostas registradas." + RESET)
    print(GREEN + "Digite 3 para iniciar apuração de vencedor/es." + RESET)
    print(GREEN + "Digite 4 para finalizar o programa." + RESET)
    opcao = int(input(""))
    if opcao == 1:
        #################################################
        ###############   VERIFICACAO DE NOME
        #################################################
        while True:
            name = input("Escreva seu nome(digite sem símbolos): ")
            if verifyNome(name):
                print(GREEN + "Nome valido" + RESET)
                break
            else:
                print("Nome Invalido - Contem caracteres especiais")
        #################################################
        ###############   VERIFICACAO DE CPF
        #################################################
        while True:
            cpf = input("Escreva seu cpf(sem pontos ou tracos): ")#remover pontos ou tracos 
            if verifyCpf(cpf):
                if len(cpf) == 11:
                    print(GREEN + "Cpf valido" + RESET)
                    break
                else:
                    print(RED + "Cpf invalido- Quantidade incorreta de carateres" + RESET)
            else:
                print(RED + "Cpf Invalido - Contem caracteres especiais"+ RESET)
        #################################################
        ###############   VERIFICACAO DE APOSTA
        #################################################
        while True:
            print("Deseja fazer manualmente sua aposta? ")
            aposta = int(input("Digite 1 para"+ GREEN +" SIM "+ RESET+"e digite 2 para"+ RED +" NAO "+ RESET + ":" ))
            if aposta == 1:
                while True:
                    a1 = int(input("Digite o primeiro valor da sua aposta!(entre 1 e 50))"))
                    if a1 >0 and a1 <= 50:
                        print(a1)
                        a2 = int(input("Digite o segundo valor da sua aposta!(entre 1 e 50))"))
                        if a2 >0 and a2 <= 50:
                            print(a1 , "/" , a2)
                            a3 = int(input("Digite o terceiro valor da sua aposta!(entre 1 e 50))"))
                            if a3 >0 and a3 <= 50:
                                print(a1 , "/" , a2, "/" , a3)
                                a4 = int(input("Digite o quarto valor da sua aposta!(entre 1 e 50))"))
                                if a4 >0 and a4 <= 50:
                                    print(a1 , "/" , a2, "/" , a3 , "/" , a4)
                                    a5 = int(input("Digite o quinto valor da sua aposta!(entre 1 e 50))"))
                                    if a5 >0 and a5 <= 50:
                                        print(a1 , "/" , a2, "/" , a3 , "/" , a4, "/" , a5)
                                        bet.append(a1)
                                        bet.append(a2)
                                        bet.append(a3)
                                        bet.append(a4)
                                        bet.append(a5)
                                        print("Aposta: " + str(bet))
                                        print("Nome: " + GREEN + name + RESET +", Cpf: " + GREEN + str(cpf) + RESET + ", Aposta: " + GREEN + str(bet) + RESET)
                                        data.append(atualizaRegistro())
                                        data.append(name)
                                        data.append(cpf)
                                        data.append(bet)
                                        print("Aposta: " + str(data))
                                        print(f"{data}")
                                        #atualizaRegistro()
                                        escrita(data)
                                        data.clear()
                                        bet.clear()
                                        print(f"{data}")
                                        print(f"{bet}")
                                
                                        break
                                    else:
                                        print(RED + "Valor Invalido"+ RESET)
                                else:
                                    print(RED + "Valor Invalido"+ RESET)
                            else:
                                print(RED + "Valor Invalido"+ RESET)
                        else:
                            print(RED + "Valor Invalido"+ RESET)
                    else:
                        print(RED + "Valor Invalido"+ RESET)  
                break
            elif aposta == 2:
                data.clear()
                supriseList.clear()
                randomizer()
                print("Seus números foram gerado! ")
                print(f"Sua aposta é:{supriseList}")
                print("Nome: " + GREEN + name + RESET +", Cpf: " + GREEN + str(cpf) + RESET + ", Aposta: " + GREEN + str(supriseList) + RESET)
                data.append(atualizaRegistro())
                data.append(name)
                data.append(cpf)
                data.append(supriseList)
                print("Aposta: " + str(supriseList))
                print(f"{data}")
                #atualizaRegistro()
                escrita(data)
                supriseList.clear()
                data.clear()
                print(GREEN + "Aposta cadastrada! :)" + RESET)
                break
            else:
                print("Opcao invalida!")
    elif opcao == 2:
        leitura()
        
    elif opcao == 3:#apuração
        print("Vamos iniciar a fase de apuração de ganhadores.")
        winner = input(GREEN + "Voce realmente deseja iniciar o sorteio?: y/n  " + RESET)
        if winner == 'y':
            #apuração()#populada a lista apostaGanhadora 33, 46, 10, 35, 35
            apostaGanhadora.append(33)
            apostaGanhadora.append(46)
            apostaGanhadora.append(10)
            apostaGanhadora.append(35)
            apostaGanhadora.append(35)

            print(f"A aposta ganhadora foi: "+ str(apostaGanhadora))

            procuraGanhador(apostaGanhadora)

        elif winner == 'n':
            break
        else:
            print(RED + "Opcao invalida."+ RESET)
    elif opcao == 4:#exit
        exit = input(RED + "Voce realmente deseja sair? y/n  " + RESET)
        if exit == 'y':
            break
        if exit == 'n':
            continue
        else:
            print(RED + "Opcao invalida."+ RESET)
    else:
        print(RED + "Opcao invalida. Digite novamente."+ RESET)
