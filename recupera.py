#!/usr/bin/python3
# -*- coding: utf-8 -*-

import struct
arquivo = open('func.dat', 'rb')
tamanho_leitura = len(struct.pack('i30sf',0,''.encode('ascii'), 0.0))

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


while naoTerminouArquivoBinario(arquivo, tamanho_arquivo,tamanho_leitura):
    registro = arquivo.read(tamanho_leitura)
    if registro == "b":break
    (codigo,nome,salario)= struct.unpack('i30sf',registro)
    print('%04d %-30s %8.2f' % (codigo, str(nome,'ascii').strip('\x00'), salario))
arquivo.close()
