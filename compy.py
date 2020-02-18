import re
import numpy as np
#from matplotlib_venn import venn2, venn3

# con questa fz tolgo i commenti da output di nfsim e genero testo pulito
def leggi(file):
	lista = []
	with open(str(file)) as fil:
		for linea in fil:
			A = linea
			if '#' not in A:
				lista.append(A)
	return lista # contiene le righe dell'output di -ss cosi come sono: ex A().B().C()  1\n

def leggi_togli_scrivi(leggi, scrivi):
	lista = []
	with open(str(leggi), 'r+') as fil:
		for linea in fil:
			linea = linea.replace('[', '')
			linea = linea.replace('])', '')
			linea = linea.replace("'", '')
			linea = linea.replace('set(', '')
			lista.append(linea)
	print len(lista)		
	
	with open(str(scrivi), 'w') as scr:
		for linea in lista:
			scr.write(str(linea)) # legge da un file di set[()] da una print di python e restituisce lo stesso pulito

# legge da una lista e scrive un file txt con un elemento per riga
def scrivi(file, lista):
	with open(str(file), 'w') as fl:
		for i in lista:
			fl.write(str(i))
			fl.write('\n')	

# questa fz serve per fare lista con complessi unici usata dentro a double
def unique_list(l):
  x = []
  for a in l:
	if a not in x:
	  x.append(a)
  return x

################################################## SIMULAZIONE ##########################################################################################

# controllo text-based di due specie isomorfiche
def CIsoS(lista_complessi):

	precount = -1
	count = len(lista_complessi)

	while count != precount:
		for c in lista_complessi:
			for d in lista_complessi: 
				i = c.split(' ')
				j = d.split(' ')
				differenza = set(i[0])^set(j[0])
				if i[0] != j[0]:
					if len(differenza) == 0 and (re.findall('!'+'[1-9]', i[0]) != re.findall('!'+'[1-9]', j[0]) or re.findall('!'+'[1-9]'+'[1-9]', i[0]) != re.findall('!'+'[1-9]'+'[1-9]', j[0]) or re.findall('~'+'[0-P]', i[0]) != re.findall('~'+'[0-P]', j[0]) or re.findall('~'+'[a-z]', i[0]) != re.findall('~'+'[a-z]', j[0]) or re.findall('~'+'[0-P]'+'!'+'[1-9]', i[0]) != re.findall('~'+'[0-P]'+'!'+'[1-9]', j[0]) or re.findall('~'+'[0-P]'+'!'+'[1-9]'+'[1-9]', i[0]) != re.findall('~'+'[0-P]'+'!'+'[1-9]'+'[1-9]', j[0])): #se fatti dello stesso materiale e se il !num cade in indici diversi				

						lista_complessi.remove(c)
						lista_complessi.remove(d)

						f = c.split(' ')
						numero_1 = f[-1]
						f.remove(f[-1])

						g = d.split(' ')
						numero_2 = g[-1]

						numero = int(numero_1) + int(numero_2)
						f.append(str(numero))
						c = ' '.join(f)
						lista_complessi.append(c)

		precount = count
		count = len(lista_complessi)
			

	return lista_complessi

# questa funzione unisce i complessi uguali e somma il numero di molecole, output contiene counter di quante volte ha trovato quel complessi
def CIsoS_1(lista):
	sort_num_cmplx = []
	sorted_cmplx = []

	for i in range(len(lista)):
		riga = lista[i] # lista con complessi come letti in ogni riga
		lista_complesso_numero = riga.split(' ')
		complesso = lista_complesso_numero[0] # ovvero nome complesso
		# da qui nuove per parentesi
		lista_monomeri = complesso.split('.')	
		for i in range(len(lista_monomeri)):	
			monomero = lista_monomeri[0]
			D = monomero.split('(')
			E = D[-1].split(')')
			F = E[0].split(',')
			componenti = sorted(F)
			H = ','.join(componenti)
			D.remove(D[-1])
			D.append(H)
			I = ('(').join(D)
			L = I+')'
			lista_monomeri.remove(lista_monomeri[0])
			lista_monomeri.append(L)	
			check = '.'.join(sorted(lista_monomeri))

		# sorted_cmplx e' lista con nomi dei complessi riordinati sia per punti che per parentesi
		sorted_cmplx.append(check)
		# appendo a sort_num_cmplx il nome del complesso e il numero di molecole
		sort_num_cmplx.append(check+' '+lista_complesso_numero[-1].replace('\n', '')) # contiene nome e numero complesso senza \n
	sorted_cmplx = unique_list(sorted_cmplx) # contiene solo nome del complesso
	sorted_list = []

	for i in sorted_cmplx:
		n_mol = []
		for j in range(len(sort_num_cmplx)):
			if i == sort_num_cmplx[j].split(' ')[0]:
				n_mol.append(int(sort_num_cmplx[j].split(' ')[1]))
		sorted_list.append(i + ' ' + str(sum(n_mol))) # contiene nome_complesso ordinato sia punti che parentesi e numero_mol

	return sorted_list

# scrive nella sezione seed species di .bngl il contenuto di una lista
def SeedBM(lista, file_bngl):
	lista_ss2 = []
	for elem in lista:
		elem = elem+'\n'
		lista_ss2.append(elem)

	with open(str(file_bngl), 'r') as bngl: #aprire il bngl e mettere le specie nella seed section	

		linee = bngl.readlines()
		for i in range(len(linee)):
			if linee[i] == 'begin seed species\n':
				linea_inizio = i
			if linee[i] == 'end seed species\n':
				linea_fine = i
		linee[linea_inizio+1:linea_fine] = lista_ss2


	with open(str(file_bngl), 'w') as bngl:
		for i in linee:
		 	bngl.write(i)

########################################################################################################################################################

################################################# PyDrift - ANALISI ####################################################################################

# questa funzione legge da un file di testo e mette i complessi senza n_mol in set 
def fare_insieme(leggi):
	# apro file e metto dentro a un set tutti i nomi dei complessi
	with open(str(leggi)) as fil:
		insieme = set()
		for linea in fil:
			A = linea
			B = A.split(' ')
			C = B[0] # ovvero nome complesso
			if '\n' not in C:
				if len(C) != 0:
					insieme.add(C)
	return insieme

def fare_insieme_complessi(leggi):
	# apro file e metto dentro a un set tutti i nomi dei complessi
	with open(str(leggi)) as fil:
		insieme = set()
		for linea in fil:
			A = linea
			B = A.split(' ')
			C = B[0] # ovvero nome complesso
			if '.' in C:	
				if '\n' not in C:
					if len(C) != 0:
						insieme.add(C)
	return insieme

def fare_insieme_specie(leggi, specie):
	# apro file e metto dentro a un set tutti i nomi dei complessi
	with open(str(leggi)) as fil:
		insieme = set()
		for linea in fil:
			A = linea
			B = A.split(' ')
			C = B[0] # ovvero nome complesso
			if str(specie) in C:	
				if '\n' not in C:
					if len(C) != 0:
						insieme.add(C)
	return insieme

def fare_insieme_not_specie(leggi, specie):
	# apro file e metto dentro a un set tutti i nomi dei complessi
	with open(str(leggi)) as fil:
		insieme = set()
		for linea in fil:
			A = linea
			B = A.split(' ')
			C = B[0] # ovvero nome complesso
			if str(specie) not in C:	
				if '\n' not in C:
					if len(C) != 0:
						insieme.add(C)
	return insieme

def fare_insieme_senza_siti(leggi, specie):
	# apro file e metto dentro a un set tutti i nomi dei complessi
	with open(str(leggi)) as fil:
		insieme = set()
		for linea in fil:
			A = linea
			B = A.split(' ')
			C = B[0] # ovvero nome complesso
			if str(specie) not in C:	
				if '\n' not in C:
					if len(C) != 0:
						insieme.add(C)
	return insieme

def fare_insieme_inter(leggi):
	# apro file e metto dentro a un set tutti i nomi dei complessi
	with open(str(leggi)) as fil:
		lista_insiemi = []		
		for linea in fil:
			insieme = set()
			A = linea
			B = A.split(', ')
			for i in B:
				insieme.add(i)
			lista_insiemi.append(insieme)
	print len(lista_insiemi)
	return lista_insiemi

# questa funzione calcola i valori della distanza normalizzata tra due insiemi (differenza simmetrica/unione)
def normal_dist(lista):
	n = len(lista)
	matrice = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			numeratore = lista[i] ^ lista[j]
			unione = set.union(*lista)
			drift = float(len(numeratore))/float(len(unione))
			matrice[i][j] = drift
	
	m3 = matrice[np.triu_indices(n, k = 1)]
	return m3

# questa fz restituisce la lunghezza dei set nella lista di set in input in una lista output
def lunghezza_insiemi(insieme):
	b = []
	for i in range(len(insieme)):
		b.append(float(len(insieme[i])))
	return b