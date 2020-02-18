import numpy as np
import drift_calculus as dc

lista_ss = []
lista_lung = []
lista_insiemi = []

for i in range(2):	
	model_name = '%s_hela_nf_0.species' %(i)
	file_out = '%s_hela_cl_0.species' %(i)

	set_ss = dc.leggi(model_name)
	lista_ss.append(set_ss)

	lista_nodb = dc.double(lista_ss[i])
	lista_noiso = dc.check_iso_text(lista_nodb)	

	dc.scrivi(file_out, lista_noiso)

	fi_set = dc.fare_insieme(file_out)
	lista_insiemi.append(fi_set)

drift = dc.normal_dist(lista_insiemi)
 
avg_std_drift = (np.mean(drift), np.std(drift))

intersezione = set.intersection(*lista_insiemi)
len_inter = len(intersezione)

unione = set.union(*lista_insiemi)
len_unione = len(unione)

metrica_inter = float(len(intersezione))/float(len(unione))

for i in lista_insiemi:
	lunghezza = len(i)
	lista_lung.append(lunghezza)

avg_std_lung = (np.mean(lista_lung), np.std(lista_lung))


print 'avg_std_drift'
print avg_std_drift
print 'avg_std_lung'
print avg_std_lung
print 'len_inter'
print len_inter
print 'len_unione'
print len_unione