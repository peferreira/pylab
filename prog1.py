#!/usr/bin/python3
# -*- coding: utf-8 -*-
# código do Programa 1 - Dados dos funcionários

# Início do programa
# Criação do Arquivo Binário
import struct

i = 1

arquivo = open('func.dat', 'wb')
codigo = 0
while True:
	if codigo == 9999:
		break
	correto = 0
	correto2 = 0
	correto3 = 0
	correto4 = 0
	print('\n%do. funcionário: \n' % i)
	entra_while = 1
	while entra_while == 1 :
		codigo = int(input("Digite o código do funcionário: "))
		if codigo <= 0 :
			corrige = input("Código incorreto. Deseja corrigi-lo? S ou N: ")
			if corrige == "N" :
				entra_while = 0
				break
			if corrige == "S":
				entra_while = 1
		if codigo == 9999:
			entra_while = 0
			break
		else:
			correto = 1
			letra_ini = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
			entra_while2 = 1
			while entra_while2 == 1:
				nome = input("Digite o nome do funcionário: ")
				if nome[0] not in letra_ini:
					corrige = input("Nome fora do padrão - letra maiúscula inicial. Deseja corrigi-lo? S ou N: ")
					if corrige == "N" :
						entra_while2 = 0
						entra_while = 0
						break
					if corrige == "S":
						entra_while2 = 1
				else:
					correto2 = 1
					entra_while3 = 1
					while entra_while3 == 1:
						salario = float(input("Digite o salário do funcionário: "))
						if salario <= 0 :
							corrige = input("Salário incorreto. Deseja corrigi-lo? S ou N: ")
							if corrige == "N" :
								entra_while3 = 0
								entra_while2 = 0
								entra_while = 0
								break
							if corrige == "S":
								entra_while3 = 1
						else:
							validade = "true"
							entra_while4 = 0
							entra_while = 0
							entra_while2 = 0
							entra_while3 = 0
							correto4 = 1
							correto3 = 1
							correto = 1
							correto2 = 1

	if ((correto == 1) and (correto2 == 1) and (correto3 == 1) and (correto4 == 1)):
		i = i + 1
		print (nome)
		print (codigo)
		print (salario)
		registro = struct.pack('i30sf', codigo, nome.encode('ascii'), salario)
		arquivo.write(registro)
arquivo.close()
