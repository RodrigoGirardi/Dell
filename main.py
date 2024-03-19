import re
import csv
import pandas
import random

RED = "\033[31m"  
GREEN = "\033[32m" 
YELLOW = "\033[33m" 
RESET = "\033[0m"  

supriseList = []
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

def randomizer():
    for i in range(5):
        r = random.randrange(1,50)
        supriseList.append(r)
    print(supriseList)

def escrita(data):
    with open("apostas.csv", mode='a', newline='', encoding='utf-8') as arq:
        writer = csv.writer(arq)
        if arq.tell() == 0:
            writer.writerow({'nome', 'cpf','aposta'})   # 'registro',     
        writer.writerow(data)

def atualizaRegistro():#esta função tem o objetivo de ao inicializar o programa, percorrer apenas 1 vez o arquivo para verificar o número do último registro
    with open("apostas.csv", mode='r', newline='', encoding='utf-8') as arq2:
        registro = 1000
        reader = csv.reader(arq2)
        next(reader)#começar na linha 1 / pula cabecalho
        primLineValid = next(reader,None)
        if primLineValid is None:
            return registro
        for i in reader:
            registro = i[0]#coluna 'registro' / armazenei o ultimo valor da coluna registro
            #print(registro)
        #print(registro)
        registro = str(int(registro) + 1)
        return registro


#################################################
###############   INICIO
#################################################
        

print(GREEN + "Olá, seja bem-vindo a MegaSena DELL" + RESET)


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
            if a1 > 1 and a1 <= 50:
                print(a1)
                a2 = int(input("Digite o segundo valor da sua aposta!(entre 1 e 50))"))
                if a2 > 1 and a2 <= 50:
                    print(a1 , "/" , a2)
                    a3 = int(input("Digite o terceiro valor da sua aposta!(entre 1 e 50))"))
                    if a3 > 1 and a3 <= 50:
                        print(a1 , "/" , a2, "/" , a3)
                        a4 = int(input("Digite o quarto valor da sua aposta!(entre 1 e 50))"))
                        if a4 > 1 and a4 <= 50:
                            print(a1 , "/" , a2, "/" , a3 , "/" , a4)
                            a5 = int(input("Digite o quinto valor da sua aposta!(entre 1 e 50))"))
                            if a5 > 1 and a5 <= 50:
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
    if aposta == 2:
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
        break
    else:
        print("Opcao invalida!")