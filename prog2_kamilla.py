#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import date
import struct

arquivo = open('func.dat', 'rb')
tamanho_leitura = len(struct.pack('i30sfi',0,''.encode('ascii'), 0.0, 0))

#desloca pro fim do arquivo
arquivo.seek(0,2)
#pega o tamanho do arquivo em bytes
tamanho_arquivo = arquivo.tell()
#desloca pro inicio do arquivo
arquivo.seek(0,0)

def naoTerminouArquivoBinario(arquivo, tamanho_arquivo, tamanho_leitura):
    tamanho_lido = arquivo.tell()
    if(tamanho_arquivo - tamanho_lido >= tamanho_leitura):
        return True
    return False

def calculaBonificacao(salario, dataAdmissao, dataLimite):
    dataAdmissao = int(dataAdmissao)
    anoAdm = dataAdmissao % 10000
    dataAdmissao = dataAdmissao // 10000
    mesAdm = dataAdmissao % 100
    dataAdmissao = dataAdmissao // 100
    diaAdm = dataAdmissao
    dataLimite = int(dataLimite)
    anoLim = dataLimite % 10000
    dataLimite = dataLimite // 10000
    mesLim = dataLimite % 100
    dataLimite = dataLimite // 100
    diaLim = dataLimite
    umPorcentoDoSalario = 0.01*salario
    d1=date(anoAdm,mesAdm,diaAdm)
    d2=date(anoLim,mesLim,diaLim)
    result = diff_dates(d2-d1)
    print result



def calculaNumeroDeDias(dataAdmissao, dataLimite):
    return 0
def calculaINSS(salario, bonificacao):
    desconto = 0.13*(salario+bonificacao)
    if(desconto >= 608.44):
        desconto = 608.44
    return desconto

def calculaIRFF(salario, bonificacao, inss):
    irff = (salario+bonificacao-inss)*0.27
    return irff

def calculaSalarioLiquido(salario, bonificacao, inss, irff):
    salarioLiquido = salario+bonificacao+inss+irff
    return salarioLiquido


while naoTerminouArquivoBinario(arquivo, tamanho_arquivo,tamanho_leitura):
    registro = arquivo.read(tamanho_leitura)
    if registro == "b":break
    (codigo,nome,salario, data)= struct.unpack('i30sfi',registro)
    print('%04d %-30s %8.2f %d' % (codigo, str(nome,'ascii').strip('\x00'), salario, data))
arquivo.close()
