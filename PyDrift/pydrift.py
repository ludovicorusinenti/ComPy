import numpy as np
import sys
import collections
import csv
import compy as cp

#########################################################################################################################
############################# python pydrift.py model_name n_step n_sim t_sim ##################################
#########################################################################################################################

step = []
sims = []
sim_dict = collections.OrderedDict()
step_dict = collections.OrderedDict()

lista_auto_drift = []
lista_auto_lunghezza = []
lista_auto_inter_uni = []

timec_auto_drift = []
timec_auto_len = []
timec_auto_inter = []
lista_inter_len =[]
lista_intersezione = []

lista_drift = []
lista_lunghezza = []
lista_inter_uni = []
lista_auto_inter_len = []

timec_drift = []
timec_len = []
timec_inter = []
timec_drinter = [0] # inizializzato con 0 perche cosi lunghezza come le altre liste, in questo modo il drinter tra step 0 e precedente e 0

file_out_txt = 'analisi_%s.txt' %(sys.argv[1])
#file_out_txt = 'analisi_prova.txt'
file_out_csv = 'analisi_%s.csv' %(sys.argv[1])
#file_out_csv = 'analisi_prova.csv'
file_auto_out_csv = 'analisi_auto_%s.csv' %(sys.argv[1])
#file_auto_out_csv = 'analisi_auto_prova.csv'
file_inter = 'analisi_inter_set_%s.species' %(sys.argv[1])

n = int(sys.argv[2]) #n e numero step
m = int(sys.argv[3]) #m e numero simulazioni
#n = 3
#m = 3


################################## DIVERSE SIMULAZIONI DIVERSI TIME STEP #################################################

# apro il file species e metto le specie in un insieme (simulazione_1). appendo questo insieme in lista

for i in range(n):
	for j in range(m):
		file_species = '%s_%s_%s.species' %(j, sys.argv[1], i) #confronto tra diverse simulazioni stesso step

		simulazione_1 = cp.fare_insieme(file_species)
		step.append(simulazione_1)

		if len(step) == m:
			step_dict['step%s' %(i)] = step
			step = []

for k, v in step_dict.items():
	drift = cp.normal_dist(v)
	lista_drift.append(drift)

	lunghezza = cp.lunghezza_insiemi(v)
	lista_lunghezza.append(lunghezza)

	inter_uni = (set.intersection(*v), set.union(*v))
	lista_inter_uni.append(inter_uni)

	intersezione = set.intersection(*v)
	#if intersezione not in lista_intersezione and len(intersezione) != 0:
	lista_intersezione.append(intersezione)
	inter_len = len(intersezione)
	lista_inter_len.append(inter_len) #lunghezza media insieme intersezione

	##################################################################################################################
	# QUESTO LA RENDE SCRIVI INTERSEZIONE
	# ovvero scrive il set intersezione tra tutte le simulazioni ad ogni step dovrebbero essere 99 (il primo e il seed uguale)
cp.scrivi(file_inter, lista_intersezione)
# Inserire qui i comandi per le altre scritture desiderate

for i in lista_drift: #lista valori drift come tuple con media e std per ogni step tra diverse sim
	avg_std_drift = (np.mean(i), np.std(i))
	timec_drift.append(avg_std_drift)	

for i in lista_lunghezza:
	avg_std_len = (np.mean(i), np.std(i))
	timec_len.append(avg_std_len)

for i in lista_inter_uni: #lista valori metrica inter per ogni step tra diverse sim
	metrica_inter = float(len(i[0]))/float(len(i[1]))
	timec_inter.append(metrica_inter)
#aggiunto qui
for i in range(len(lista_intersezione)-1):
	num = lista_intersezione[i] ^ lista_intersezione[i+1]
	den = lista_intersezione[i] | lista_intersezione[i+1]
	drinter = float(len(num))/float(len(den))
	timec_drinter.append(drinter)
#aggiunto ultimo writerow
with open(file_out_csv, 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(len(timec_drift)):
		writer.writerow([float(i)*float(sys.argv[4]), timec_drift[i][0], timec_drift[i][1], timec_inter[i], timec_len[i][0], timec_len[i][1], lista_inter_len[i], len(lista_inter_uni[i][1]), timec_drinter[i]])

print 'step_dict'
print len(step_dict) # deve coincidere con il numero di step
print 'DONE OPERATIONS 1'

###################################### STESSA SIMULAZIONE DIVERSI TIME STEP #############################################

# for j in range(m):
# 	for i in range(n):
# 		file_species = '%s_%s_%s.species' %(j, sys.argv[1], i)
# 		#file_species = '%s_prova_nf_%s.species' %(j, i)

# 		simulazione = cp.fare_insieme(file_species)
# 		sims.append(simulazione)

# 		if len(sims) == n:
# 			sim_dict['sim%s' %(j)] = sims
# 			sims = []

# for k, v in sim_dict.items():
# 	auto_drift = cp.normal_dist(v)
# 	lista_auto_drift.append(auto_drift)

# 	auto_lunghezza = cp.lunghezza_insiemi(v)
# 	lista_auto_lunghezza.append(auto_lunghezza)

# 	auto_inter_uni = (set.intersection(*v), set.union(*v))
# 	lista_auto_inter_uni.append(auto_inter_uni)

# 	inter_auto_len = len(set.intersection(*v))
# 	lista_auto_inter_len.append(inter_auto_len) #lunghezza media insieme intersezione


# for i in lista_auto_drift:
# 	avg_std_auto_drift = (np.mean(i), np.std(i))
# 	timec_auto_drift.append(avg_std_auto_drift)	

# for i in lista_auto_lunghezza:
# 	avg_std_auto_len = (np.mean(i), np.std(i))
# 	timec_auto_len.append(avg_std_auto_len)

# for i in lista_auto_inter_uni:
# 	metrica_auto_inter = float(len(i[0]))/float(len(i[1]))
# 	timec_auto_inter.append(metrica_auto_inter)

# with open(file_auto_out_csv, 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	for i in range(len(timec_auto_drift)):
# 		writer.writerow([float(i)*float(sys.argv[4]), timec_auto_drift[i][0], timec_auto_drift[i][1], timec_auto_inter[i], timec_auto_len[i][0], timec_auto_len[i][1], lista_auto_inter_len[i], len(lista_auto_inter_uni[i][1])])

# print 'sim_dict'
# print len(sim_dict)
# print sim_dict.keys()
# print 'DONE OPERATIONS 2'

#############################################      VENN     ###############################################################

# plotVennSample(intersezione, insieme[0])

# print 'DONE VENN PLOT'