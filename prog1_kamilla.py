#!/usr/bin/python3
# -*- coding: utf-8 -*-
# código do Programa 1 - Dados dos funcionários

import struct

def recebeNomeFuncionario():
    nome = input('Nome....:')
    return nome

def ehUmNomeDeFuncionarioValido(nome):
    #Uppercase letters A-Z ASCII 65-90
    if ( 65 <=ord(nome[0]) <= 90):
        return True
    return False

def recebeSalarioFuncionario():
    salario = float(input('Salario.:'))
    return salario

def ehUmSalarioDeFuncionarioValido(salario):
    if salario <= 0:
        return False
    return True

def recebeCodigoFuncionario():
    codigo = int(input('Codigo..:'))
    return codigo

def ehUmCodigoDeFuncionarioValido(codigo):
    if codigo <= 0:
        return False
    return True

def tentarNovamente(inputValido):
    if inputValido:
        tentar_novamente = False
    else:
        corrige = input("Dado fornecido inválido. Deseja ridigitar o campo? (S/N) ")
        if corrige == "S":
            return True
        else:
            return False
    return False

def recebeDataAdmissao():
    dataAdmissao = input('Data....:')
    return dataAdmissao



def ehAnoBissexto(ano):
    if ( ano % 4 == 0 and ano % 100 != 0):
        return True
    if(ano % 400 == 0):
        return True
    else:
        return False
def ehMesValido(mes):
    if 1<= mes <= 12:
        return True
    return False

def ehDiaValido(dia):
    if 1<=dia<=31:
        return True
    return False

def ehUmDiaValidoDoMesNoAno(dia,mes,ano):
    anoBissexto = ehAnoBissexto(ano)
    if(mes == 2):
        if(anoBissexto):
            if(dia > 28):
                return False
        else:
            if(dia > 29):
                return False
    elif (mes in (4,6,9,11)):
        if(dia > 30):
            return False
    return True

def ehUmaDataAdmissaoValida(dataAdmissao):
    if len(dataAdmissao) != 8:
        return False
    dataAdmissao = int(dataAdmissao)
    ano = dataAdmissao % 10000
    dataAdmissao = dataAdmissao // 10000
    mes = dataAdmissao % 100
    dataAdmissao = dataAdmissao // 100
    dia = dataAdmissao
    if(not ehMesValido(mes)):
        return False
    if(not ehDiaValido(dia)):
        return False
    if ehUmDiaValidoDoMesNoAno(dia, mes, ano):
        return True
    return False





i = 1
arquivo = open('func.dat','wb')

while True:
    codigoValido = False
    nomeValido = False
    salarioValido = False
    print('\n%do.funcionario:\n' %i)
    tentar_novamente = True
    while tentar_novamente:
        codigo = recebeCodigoFuncionario()
        codigoValido = ehUmCodigoDeFuncionarioValido(codigo)
        tentar_novamente = tentarNovamente(codigoValido)
    if codigo == 9999: break

    if codigoValido :
        tentar_novamente = True
        while tentar_novamente:
            nome = recebeNomeFuncionario()
            nomeValido = ehUmNomeDeFuncionarioValido(nome)
            tentar_novamente = tentarNovamente(nomeValido)

    if nomeValido :
        tentar_novamente = True
        while tentar_novamente:
            salario = recebeSalarioFuncionario()
            salarioValido = ehUmSalarioDeFuncionarioValido(salario)
            tentar_novamente = tentarNovamente(salarioValido)

    if salarioValido :
        tentar_novamente = True
        while tentar_novamente:
            data = recebeDataAdmissao()
            dataValida = ehUmaDataAdmissaoValida(data)
            tentar_novamente = tentarNovamente(dataValida)

    if (salarioValido and nomeValido and codigoValido and dataValida):
        data = int(data)
        registro = struct.pack('i30sfi', codigo, nome.encode('ascii'), salario, data)
        arquivo.write(registro)
        i+=1
arquivo.close()
