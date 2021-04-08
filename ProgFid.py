# -*- Coding: UTF-8 -*-
#coding: utf-8

print('Programa de fidelidade')

print(' ')

ask = int(input('O que você quer fazer? (1)Pesquisar (2)Adicionar pontuação (3)Criar usuário: '))
lask = 0

while ask < 4:

    if ask == 1:
        while ask == 1:
            nome = input("Nome: ")
            arq = nome + ".txt"
            f = open("clientes/" + arq,"r")
            valor = f.readline()
            print(valor)
            f.close()

            print(' ')
            lask = ask
            ask = int(input('Gostaria de (1)Pesquisar novamente (2)Adicionar pontuação (3)Criar novo usuário (4)Finalizar: '))
    if ask == 2:
        while ask == 2:
            if lask != 1:
                nome = input("Nome: ")
                arq = nome + ".txt"
            f = open("clientes/" + arq,"r")
            v1 = f.readline()
            print('Pontuação atual {}'.format(v1))
            f.close()
            w = open("clientes/" + arq,"w")
            ponto = float(input("Adicionar pontuação: "))
            novo = int(v1) + ponto
            print('Nova pontuação {}'.format(novo))
            w.write(str(novo))
            w.close()

            print(' ')
            lask = ask
            ask = int(input('Gostaria de (1)Pesquisar (2)Adicionar pontuação (3)Criar novo usuário (4)Finalizar: '))
    if ask == 3:
        while ask == 3:
            nome = input("Nome: ")
            arq = nome + ".txt"
            ponto = int(input("Primeira pontuação: "))
            f = open("clientes/" + arq,"w")
            f.write(str(ponto))
            f.close()

            print(' ')
            lask = ask
            ask = int(input('Gostaria de (1)Pesquisar novamente (2)Adicionar pontuação (3)Criar novo usuário (4)Finalizar: '))
    if ask == 0:
        conf = input('Gostaria de ZERAR um cliente? ')
        if conf == "sim":
            nome = input("Nome: ")
            arq = nome + ".txt"
            f = open("clientes/" + arq,"r")
            v1 = f.readline()
            print('Pontuação atual {}'.format(v1))
            f.close()
            conf2 = input("Gostaria mesmo de zerar o cliente? ")
            if conf2 == "sim":
                w = open("clientes/" + arq,"w")
                novo = 0
                print('Nova pontuação {}'.format(novo))
                w.write(str(novo))
                w.close()
        else:
            print(' ')
            lask = ask
            ask = int(input('Gostaria de (1)Pesquisar (2)Adicionar pontuação (3)Criar novo usuário (4)Finalizar: '))
    elif ask == 4:
        print(' ')
        print('Finalizado.')