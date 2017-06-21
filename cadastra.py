#!/usr/bin/python3
# -*- coding: utf-8 -*-
# código do Programa 1 - Dados dos funcionários

import struct

i = 1
arquivo = open('func.dat','wb')

while True:
    print('\n%do.funcionario:\n' %i)
    codigo = int(input('Codigo..:'))
    if codigo == 9999: break
    nome = input('Nome....:')
    salario = float(input('Salario.:'))
    registro = struct.pack('i30sf', codigo, nome.encode('ascii'), salario)
    arquivo.write(registro)
    i+=1
arquivo.close()
