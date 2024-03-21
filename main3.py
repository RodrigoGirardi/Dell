import re
import csv
import pandas as pd
import os
import numpy as np
import random
 
supriseList = []
apostaGanhadora = []
bet = []
data = []
pathCsv = "C:\\Users\\r.juvencio\\Documents\\Trabalhos\\Dell\\Dell-main\\apostas.csv"
def verifyNome(data):
    if re.search(r'[#@\$%&*()/+*]', data):
        return False
    return True

def verifyCpf(data):
    if re.search(r'[#@\$%&*()/+*-]', data):
        return False
    return True

def verifyVet(data):
    if re.search(r'[,]', data):
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
    with open(pathCsv, mode='a', newline='', encoding='utf-8') as arq:
        fieldnames = ['registro','nome', 'cpf','aposta']
        writer = csv.DictWriter(arq, fieldnames=fieldnames)
        if arq.tell() == 0:
            writer.writeheader()
        #colocaCabecalho(arq)
        writer.writerow({'registro': data[0],'nome': data[1], 'cpf': data[2],'aposta':data[3]})

        arq.close()

def leitura():
    with open(pathCsv,mode = 'r', newline='', encoding='utf-8') as arq3:
        leitor = csv.reader(arq3)
        if os.path.getsize(pathCsv) == 0:
            print("Nao ha apostas registradas")
            arq3.close()
        for i in leitor:
            print(i)
    arq3.close()

def atualizaRegistro():#esta função tem o objetivo de ao inicializar o programa, percorrer apenas 1 vez o arquivo para verificar o número do último registro
    with open(pathCsv, mode='r', newline='', encoding='utf-8') as arq2:
        registro = 1000
        reader = csv.reader(arq2)
        if os.path.getsize(pathCsv) == 0:
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
    with open(pathCsv, mode = 'r', newline='', encoding='utf-8') as win:
        #coluna = 'aposta'
        aux = []
        count = 0
        aux2 = []
        dadosPvalidar = []
        reader = csv.DictReader(win)
        for linha in reader:#percorrer as linhas
            linhaPValidar = []
            print(linha['aposta'])
            linhaPValidar.append(linha['registro'])
            linhaPValidar.append(linha['nome'])
            linhaPValidar.append(linha['cpf'])
            dadosPvalidar.append(linha['aposta'])# este loop termina com a lista com todo o conteudoda coluna 'apostas'
            #print(dadosPvalidar[0])
            aux = dadosPvalidar[0]
            print(aux[0])#[
            print(int(aux[1]))#2
            aux2.append(int(aux[1]))
            #print(aux[2])#,
            #print(aux[3])#' '
            print(int(aux[4]))#3
            aux2.append(int(aux[4]))
            #print(aux[5])#,
            #print(aux[6])#''
            print(int(aux[7]))#4
            aux2.append(int(aux[7]))
            #print(aux[8])#,
            #print(aux[9])#' '
            print(int(aux[10]))#5
            aux2.append(int(aux[10]))
            print(aux[11])#,
            #print(aux[12])#' '
            #print(int(aux[13]))#6
            aux2.append(int(aux[13]))
            #print(aux[14])#]
            print(aux2)
            for i in dadosPremiados:
                for j in aux2:
                    if i == j:
                        print (i ," - " , j )
                        print("Achei")
                        count += 1
                    else:
                        print (i , " - " , j )
                        print(":(")
                
            print(count)
            if count == 5:
                print("O Ganhador desta rodada é:")
                print(linhaPValidar)
                print("O ganhador: ", linhaPValidar[1]," receberá seu premio:")
                print("                 ____________________                    ")
                print("                /                    \                   ")
                print("               /0101010000010101001101\                  ")
                print("              /010101000010111101010100\                 ")
                print("             |10101010001010101010010101|                ")
                print("             |1111                  0101|                ")
                print("             |0000   ALAN TURING    0000|                ")
                print("             |1010                  0010|                ")
                print("             |01010101010101010001001010|                ")
                print("              \\000010001010101010101010/                 ")
                print("               \\1111110000101010000000/                  ")
                print("                \____________________/                   ")
                print("                                                         ")
                print("                                                         ")
                print("         O ganhador recebe a medalha Alan Turing         ")
                print("                                                         ")
                print("                                                         ")
            aux2.clear()
            dadosPvalidar.clear()




#################################################
###############   INICIO
#################################################
        

print("Olá, seja bem-vindo a MegaSena DELL")
#################################################
###############   FASE DE APOSTAS
#################################################

while True:
    print("Digite 1 para cadastrar nova aposta.")
    print("Digite 2 para listar as apostas registradas.")
    print("Digite 3 para iniciar apuração de vencedor/es.")
    print("Digite 4 para finalizar o programa.")
    opcao = int(input(""))
    if opcao == 1:
        #################################################
        ###############   VERIFICACAO DE NOME
        #################################################
        while True:
            name = input("Escreva seu nome(digite sem símbolos): ")
            if verifyNome(name):
                print("Nome valido")
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
                    print("Cpf valido")
                    break
                else:
                    print( "Cpf invalido- Quantidade incorreta de carateres")
            else:
                print( "Cpf Invalido - Contem caracteres especiais")
        #################################################
        ###############   VERIFICACAO DE APOSTA
        #################################################
        while True:
            print("Deseja fazer manualmente sua aposta? ")
            aposta = int(input("Digite 1 para SIM e digite 2 para NAO :" ))
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
                                        print("Nome: " + name +", Cpf: " + str(cpf) + ", Aposta: " + str(bet))
                                        data.append(atualizaRegistro())
                                        data.append(name)
                                        data.append(cpf)
                                        data.append(bet)
                                        #print("Aposta: " + str(data))
                                        #print(f"{data}")
                                        #atualizaRegistro()
                                        escrita(data)
                                        data.clear()
                                        bet.clear()
                                
                                        break
                                    else:
                                        print( "Valor Invalido")
                                else:
                                    print( "Valor Invalido")
                            else:
                                print( "Valor Invalido")
                        else:
                            print( "Valor Invalido")
                    else:
                        print( "Valor Invalido")  
                break
            elif aposta == 2:
                data.clear()
                supriseList.clear()
                randomizer()
                print("Seus números foram gerado! ")
                print(f"Sua aposta é:{supriseList}")
                print("Nome: " + name +", Cpf: " + str(cpf) + ", Aposta: " + str(supriseList))
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
                print("Aposta cadastrada! :)")
                break
            else:
                print("Opcao invalida!")
    elif opcao == 2:
        leitura()
        
    elif opcao == 3:#apuração
        print("Vamos iniciar a fase de apuração de ganhadores.")
        winner = input("Voce realmente deseja iniciar o sorteio?: y/n  ")
        if winner == 'y':
            #apuração()#populada a lista apostaGanhadora 33, 46, 10, 35, 35
            apostaGanhadora.append(2)
            apostaGanhadora.append(3)
            apostaGanhadora.append(4)
            apostaGanhadora.append(5)
            apostaGanhadora.append(6)

            print(f"Os números sorteados foram: "+ str(apostaGanhadora))

            procuraGanhador(apostaGanhadora)

        elif winner == 'n':
            break
        else:
            print( "Opcao invalida.")
    elif opcao == 4:#exit
        exit = input( "Voce realmente deseja sair? y/n  ")
        if exit == 'y':
            break
        if exit == 'n':
            continue
        else:
            print( "Opcao invalida.")
    else:
        print( "Opcao invalida. Digite novamente.")
