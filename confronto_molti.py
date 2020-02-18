import pylab as pl
import numpy as np
import sys

# https://xkcd.com/color/rgb/
colors = [	'xkcd:teal', 			#0
			'xkcd:salmon', 			#1
			'xkcd:silver',			#2
			'xkcd:magenta',			#3
			'xkcd:teal',			#4
			'xkcd:grey',			#5
			'xkcd:light blue',		#6
			'xkcd:orange',			#7
			'xkcd:lime green',		#8
			'xkcd:black']			#9

#file_name = 'analisi_%s.csv' %(sys.argv[1])
time = np.loadtxt('analisi_hela_nf.csv', delimiter=',')[:,0]


# NB: u2os rko k562 mcf7 e jurkat colore nero (9)
# 

file_name_0 = 'analisi_hela_nf.csv'
file_name_1 = 'analisi_generic_nf.csv'
#file_name_2 = 'analisi_a549_nf.csv'
# file_name_3 = 'analisi_u2os_nf.csv'
file_name_4 = 'analisi_mcf7_nf.csv'
file_name_5 = 'analisi_hepg2_nf.csv'
file_name_6 = 'analisi_rko_nf.csv'
file_name_7 = 'analisi_jurkat_nf.csv'
file_name_8 = 'analisi_lncap_nf.csv'
file_name_9 = 'analisi_hek293_nf.csv'
file_name_10 = 'analisi_k562_nf.csv'

file_name_no_0 = 'analisi_hela_nf_noegfr.csv'
file_name_no_1 = 'analisi_generic_nf_noegfr.csv'
#file_name_no_2 = 'analisi_a549_nf_noegfr.csv'
# file_name_no_3 = 'analisi_u2os_nf_noegfr.csv'
file_name_no_4 = 'analisi_mcf7_nf_noegfr.csv'
file_name_no_5 = 'analisi_hepg2_nf_noegfr.csv'
file_name_no_6 = 'analisi_rko_nf_noegfr.csv'
file_name_no_7 = 'analisi_jurkat_nf_noegfr.csv'
file_name_no_8 = 'analisi_lncap_nf_noegfr.csv'
file_name_no_9 = 'analisi_hek293_nf_noegfr.csv'
file_name_no_10 = 'analisi_k562_nf_noegfr.csv'

############## DEFINIZIONI 1  ################################################################################################################

drift_0 = np.loadtxt(file_name_0, delimiter=',')[:,1]
std_drift_0 = np.loadtxt(file_name_0, delimiter=',')[:,2]
inter_0 = np.loadtxt(file_name_0, delimiter=',')[:,3]
lenght_0 = np.loadtxt(file_name_0, delimiter=',')[:,4]
std_lenght_0 = np.loadtxt(file_name_0, delimiter=',')[:,5]
inter_len_0 = np.loadtxt(file_name_0, delimiter=',')[:,6]
unione_0 = np.loadtxt(file_name_0, delimiter=',')[:,7]
drinter_0 = np.loadtxt(file_name_0, delimiter=',')[:,8]

drift_1 = np.loadtxt(file_name_1, delimiter=',')[:,1]
std_drift_1 = np.loadtxt(file_name_1, delimiter=',')[:,2]
inter_1 = np.loadtxt(file_name_1, delimiter=',')[:,3]
lenght_1 = np.loadtxt(file_name_1, delimiter=',')[:,4]
std_lenght_1 = np.loadtxt(file_name_1, delimiter=',')[:,5]
inter_len_1 = np.loadtxt(file_name_1, delimiter=',')[:,6]
unione_1 = np.loadtxt(file_name_1, delimiter=',')[:,7]
drinter_1 = np.loadtxt(file_name_1, delimiter=',')[:,8]

# drift_2 = np.loadtxt(file_name_2, delimiter=',')[:,1]
# std_drift_2 = np.loadtxt(file_name_2, delimiter=',')[:,2]
# inter_2 = np.loadtxt(file_name_2, delimiter=',')[:,3]
# lenght_2 = np.loadtxt(file_name_2, delimiter=',')[:,4]
# std_lenght_2 = np.loadtxt(file_name_2, delimiter=',')[:,5]
# inter_len_2 = np.loadtxt(file_name_2, delimiter=',')[:,6]
# unione_2 = np.loadtxt(file_name_2, delimiter=',')[:,7]
# drinter_2 = np.loadtxt(file_name_2, delimiter=',')[:,8]

# drift_3 = np.loadtxt(file_name_3, delimiter=',')[:,1]
# std_drift_3 = np.loadtxt(file_name_3, delimiter=',')[:,2]
# inter_3 = np.loadtxt(file_name_3, delimiter=',')[:,3]
# lenght_3 = np.loadtxt(file_name_3, delimiter=',')[:,4]
# std_lenght_3 = np.loadtxt(file_name_3, delimiter=',')[:,5]
# inter_len_3 = np.loadtxt(file_name_3, delimiter=',')[:,6]
# unione_3 = np.loadtxt(file_name_3, delimiter=',')[:,7]
# drinter_3 = np.loadtxt(file_name_3, delimiter=',')[:,8]

drift_4 = np.loadtxt(file_name_4, delimiter=',')[:,1]
std_drift_4 = np.loadtxt(file_name_4, delimiter=',')[:,2]
inter_4 = np.loadtxt(file_name_4, delimiter=',')[:,3]
lenght_4 = np.loadtxt(file_name_4, delimiter=',')[:,4]
std_lenght_4 = np.loadtxt(file_name_4, delimiter=',')[:,5]
inter_len_4 = np.loadtxt(file_name_4, delimiter=',')[:,6]
unione_4 = np.loadtxt(file_name_4, delimiter=',')[:,7]
drinter_4 = np.loadtxt(file_name_4, delimiter=',')[:,8]

drift_5 = np.loadtxt(file_name_5, delimiter=',')[:,1]
std_drift_5 = np.loadtxt(file_name_5, delimiter=',')[:,2]
inter_5 = np.loadtxt(file_name_5, delimiter=',')[:,3]
lenght_5 = np.loadtxt(file_name_5, delimiter=',')[:,4]
std_lenght_5 = np.loadtxt(file_name_5, delimiter=',')[:,5]
inter_len_5 = np.loadtxt(file_name_5, delimiter=',')[:,6]
unione_5 = np.loadtxt(file_name_5, delimiter=',')[:,7]
drinter_5 = np.loadtxt(file_name_5, delimiter=',')[:,8]

drift_6 = np.loadtxt(file_name_6, delimiter=',')[:,1]
std_drift_6 = np.loadtxt(file_name_6, delimiter=',')[:,2]
inter_6 = np.loadtxt(file_name_6, delimiter=',')[:,3]
lenght_6 = np.loadtxt(file_name_6, delimiter=',')[:,4]
std_lenght_6 = np.loadtxt(file_name_6, delimiter=',')[:,5]
inter_len_6 = np.loadtxt(file_name_6, delimiter=',')[:,6]
unione_6 = np.loadtxt(file_name_6, delimiter=',')[:,7]
drinter_6 = np.loadtxt(file_name_6, delimiter=',')[:,8]

drift_7 = np.loadtxt(file_name_7, delimiter=',')[:,1]
std_drift_7 = np.loadtxt(file_name_7, delimiter=',')[:,2]
inter_7 = np.loadtxt(file_name_7, delimiter=',')[:,3]
lenght_7 = np.loadtxt(file_name_7, delimiter=',')[:,4]
std_lenght_7 = np.loadtxt(file_name_7, delimiter=',')[:,5]
inter_len_7 = np.loadtxt(file_name_7, delimiter=',')[:,6]
unione_7 = np.loadtxt(file_name_7, delimiter=',')[:,7]
drinter_7 = np.loadtxt(file_name_7, delimiter=',')[:,8]

drift_8 = np.loadtxt(file_name_8, delimiter=',')[:,1]
std_drift_8 = np.loadtxt(file_name_8, delimiter=',')[:,2]
inter_8 = np.loadtxt(file_name_8, delimiter=',')[:,3]
lenght_8 = np.loadtxt(file_name_8, delimiter=',')[:,4]
std_lenght_8 = np.loadtxt(file_name_8, delimiter=',')[:,5]
inter_len_8 = np.loadtxt(file_name_8, delimiter=',')[:,6]
unione_8 = np.loadtxt(file_name_8, delimiter=',')[:,7]
drinter_8 = np.loadtxt(file_name_8, delimiter=',')[:,8]

drift_9 = np.loadtxt(file_name_9, delimiter=',')[:,1]
std_drift_9 = np.loadtxt(file_name_9, delimiter=',')[:,2]
inter_9 = np.loadtxt(file_name_9, delimiter=',')[:,3]
lenght_9 = np.loadtxt(file_name_9, delimiter=',')[:,4]
std_lenght_9 = np.loadtxt(file_name_9, delimiter=',')[:,5]
inter_len_9 = np.loadtxt(file_name_9, delimiter=',')[:,6]
unione_9 = np.loadtxt(file_name_9, delimiter=',')[:,7]
drinter_9 = np.loadtxt(file_name_9, delimiter=',')[:,8]

drift_10 = np.loadtxt(file_name_10, delimiter=',')[:,1]
std_drift_10 = np.loadtxt(file_name_10, delimiter=',')[:,2]
inter_10 = np.loadtxt(file_name_10, delimiter=',')[:,3]
lenght_10 = np.loadtxt(file_name_10, delimiter=',')[:,4]
std_lenght_10 = np.loadtxt(file_name_10, delimiter=',')[:,5]
inter_len_10 = np.loadtxt(file_name_10, delimiter=',')[:,6]
unione_10 = np.loadtxt(file_name_10, delimiter=',')[:,7]
drinter_10 = np.loadtxt(file_name_10, delimiter=',')[:,8]

############# DEFINIZIONI 2 ################################################################################################################

drift_no_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,1]
std_drift_no_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,2]
inter_no_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,3]
lenght_no_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,4]
std_lenght_no_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,5]
inter_no_len_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,6]
unione_no_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,7]
drinter_no_0 = np.loadtxt(file_name_no_0, delimiter=',')[:,8]

drift_no_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,1]
std_drift_no_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,2]
inter_no_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,3]
lenght_no_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,4]
std_lenght_no_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,5]
inter_no_len_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,6]
unione_no_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,7]
drinter_no_1 = np.loadtxt(file_name_no_1, delimiter=',')[:,8]

# drift_no_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,1]
# std_drift_no_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,2]
# inter_no_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,3]
# lenght_no_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,4]
# std_lenght_no_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,5]
# inter_no_len_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,6]
# unione_no_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,7]
# drinter_no_2 = np.loadtxt(file_name_no_2, delimiter=',')[:,8]

# drift_no_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,1]
# std_drift_no_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,2]
# inter_no_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,3]
# lenght_no_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,4]
# std_lenght_no_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,5]
# inter_no_len_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,6]
# unione_no_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,7]
# drinter_no_3 = np.loadtxt(file_name_no_3, delimiter=',')[:,8]

drift_no_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,1]
std_drift_no_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,2]
inter_no_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,3]
lenght_no_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,4]
std_lenght_no_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,5]
inter_no_len_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,6]
unione_no_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,7]
drinter_no_4 = np.loadtxt(file_name_no_4, delimiter=',')[:,8]

drift_no_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,1]
std_drift_no_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,2]
inter_no_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,3]
lenght_no_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,4]
std_lenght_no_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,5]
inter_no_len_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,6]
unione_no_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,7]
drinter_no_5 = np.loadtxt(file_name_no_5, delimiter=',')[:,8]

drift_no_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,1]
std_drift_no_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,2]
inter_no_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,3]
lenght_no_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,4]
std_lenght_no_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,5]
inter_no_len_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,6]
unione_no_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,7]
drinter_no_6 = np.loadtxt(file_name_no_6, delimiter=',')[:,8]

drift_no_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,1]
std_drift_no_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,2]
inter_no_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,3]
lenght_no_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,4]
std_lenght_no_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,5]
inter_no_len_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,6]
unione_no_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,7]
drinter_no_7 = np.loadtxt(file_name_no_7, delimiter=',')[:,8]

drift_no_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,1]
std_drift_no_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,2]
inter_no_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,3]
lenght_no_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,4]
std_lenght_no_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,5]
inter_no_len_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,6]
unione_no_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,7]
drinter_no_8 = np.loadtxt(file_name_no_8, delimiter=',')[:,8]

drift_no_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,1]
std_drift_no_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,2]
inter_no_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,3]
lenght_no_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,4]
std_lenght_no_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,5]
inter_no_len_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,6]
unione_no_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,7]
drinter_no_9 = np.loadtxt(file_name_no_9, delimiter=',')[:,8]

drift_no_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,1]
std_drift_no_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,2]
inter_no_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,3]
lenght_no_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,4]
std_lenght_no_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,5]
inter_no_len_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,6]
unione_no_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,7]
drinter_no_10 = np.loadtxt(file_name_no_10, delimiter=',')[:,8]

##########################################################################################################################################################

f, axarr = pl.subplots(2, 6, sharex = True)

##########################################################################################################################################################

axarr[0][0].errorbar(time, lenght_0, yerr=std_lenght_0, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_1, yerr=std_lenght_1, ecolor=colors[4], elinewidth=.1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[0][0].errorbar(time, lenght_2, yerr=std_lenght_2, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[0][0].errorbar(time, lenght_3, yerr=std_lenght_3, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_4, yerr=std_lenght_4, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_5, yerr=std_lenght_5, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_6, yerr=std_lenght_6, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_7, yerr=std_lenght_7, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_8, yerr=std_lenght_8, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_9, yerr=std_lenght_9, ecolor=colors[8], elinewidth=.1, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[0][0].errorbar(time, lenght_10, yerr=std_lenght_10, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][0].set_ylabel('Medio')

axarr[0][1].plot(time, unione_0, color=colors[3], marker='o', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_1, color=colors[4], marker='^', markersize=0, linewidth=.7)
# axarr[0][1].plot(time, unione_2, color=colors[3], marker='^', markersize=0, linewidth=.7)
# axarr[0][1].plot(time, unione_3, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_4, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_5, color=colors[3], marker='^', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_6, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_7, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_8, color=colors[3], marker='^', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_9, color=colors[8], marker='^', markersize=0, linewidth=.7)
axarr[0][1].plot(time, unione_10, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[0][1].set_ylabel('Unione')

axarr[0][2].plot(time, inter_len_0, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[0][2].plot(time, inter_len_2, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[0][2].plot(time, inter_len_3, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_4, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_5, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_6, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_7, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_8, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_9, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[0][2].plot(time, inter_len_10, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][2].set_ylabel('Intersezione')
axarr[0][2].set_xlabel('Time [s]')

axarr[0][3].plot(time, inter_0, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[0][3].plot(time, inter_2, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[0][3].plot(time, inter_3, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_4, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_5, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_6, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_7, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_8, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_9, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[0][3].plot(time, inter_10, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][3].set_ylim(0,1)
axarr[0][3].set_ylabel('Inter')

axarr[0][4].errorbar(time, drift_0, yerr=std_drift_0, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_1, yerr=std_drift_1, ecolor=colors[4], elinewidth=.1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[0][4].errorbar(time, drift_2, yerr=std_drift_2, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[0][4].errorbar(time, drift_3, yerr=std_drift_3, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_4, yerr=std_drift_4, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_5, yerr=std_drift_5, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_6, yerr=std_drift_6, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_7, yerr=std_drift_7, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_8, yerr=std_drift_8, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_9, yerr=std_drift_9, ecolor=colors[8], elinewidth=.1, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[0][4].errorbar(time, drift_10, yerr=std_drift_10, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][4].set_ylim(0,1)
axarr[0][4].set_ylabel('Drift')

axarr[0][5].plot(time, drinter_0, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[0][5].plot(time, drinter_2, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[0][5].plot(time, drinter_3, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_4, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_5, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_6, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_7, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_8, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_9, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[0][5].plot(time, drinter_10, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[0][5].set_ylim(0,1)
axarr[0][5].set_xlabel('Time [s]')
axarr[0][5].set_ylabel('Drinter')

####################################################################################################################################################### 

axarr[1][0].errorbar(time, lenght_no_0, yerr=std_lenght_no_0, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_1, yerr=std_lenght_no_1, ecolor=colors[4], elinewidth=.1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[1][0].errorbar(time, lenght_no_2, yerr=std_lenght_no_2, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[1][0].errorbar(time, lenght_no_3, yerr=std_lenght_no_3, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_4, yerr=std_lenght_no_4, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_5, yerr=std_lenght_no_5, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_6, yerr=std_lenght_no_6, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_7, yerr=std_lenght_no_7, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_8, yerr=std_lenght_no_8, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_9, yerr=std_lenght_no_9, ecolor=colors[8], elinewidth=.1, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[1][0].errorbar(time, lenght_no_10, yerr=std_lenght_no_10, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][0].set_ylabel('Medio')

axarr[1][1].plot(time, unione_no_0, color=colors[3], marker='o', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_1, color=colors[4], marker='^', markersize=0, linewidth=.7)
# axarr[1][1].plot(time, unione_no_2, color=colors[3], marker='^', markersize=0, linewidth=.7)
# axarr[1][1].plot(time, unione_no_3, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_4, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_5, color=colors[3], marker='^', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_6, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_7, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_8, color=colors[3], marker='^', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_9, color=colors[8], marker='^', markersize=0, linewidth=.7)
axarr[1][1].plot(time, unione_no_10, color=colors[9], marker='^', markersize=0, linewidth=.7)
axarr[1][1].set_ylabel('Unione')

axarr[1][2].plot(time, inter_no_len_0, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[1][2].plot(time, inter_no_len_2, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[1][2].plot(time, inter_no_len_3, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_4, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_5, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_6, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_7, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_8, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_9, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[1][2].plot(time, inter_no_len_10, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][2].set_ylabel('intersezione')
axarr[1][2].set_xlabel('Time [s]')

axarr[1][3].plot(time, inter_no_0, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[1][3].plot(time, inter_no_2, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[1][3].plot(time, inter_no_3, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_4, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_5, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_6, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_7, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_8, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_9, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[1][3].plot(time, inter_no_10, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][3].set_ylim(0,1)
axarr[1][3].set_ylabel('Inter')

axarr[1][4].errorbar(time, drift_no_0, yerr=std_drift_no_0, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_1, yerr=std_drift_no_1, ecolor=colors[4], elinewidth=.1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[1][1].errorbar(time, drift_no_2, yerr=std_drift_no_2, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[1][1].errorbar(time, drift_no_3, yerr=std_drift_no_3, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_4, yerr=std_drift_no_4, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_5, yerr=std_drift_no_5, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_6, yerr=std_drift_no_6, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_7, yerr=std_drift_no_7, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_8, yerr=std_drift_no_8, ecolor=colors[3], elinewidth=.1, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_9, yerr=std_drift_no_9, ecolor=colors[8], elinewidth=.1, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[1][4].errorbar(time, drift_no_10, yerr=std_drift_no_10, ecolor=colors[9], elinewidth=.1, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][4].set_ylim(0,1)
axarr[1][4].set_ylabel('Drift')

axarr[1][5].plot(time, drinter_no_0, color=colors[3], marker='1', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_1, color=colors[4], marker='2', markersize=0, linewidth=.7)
# axarr[1][5].plot(time, drinter_no_2, color=colors[3], marker='2', markersize=0, linewidth=.7)
# axarr[1][5].plot(time, drinter_no_3, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_4, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_5, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_6, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_7, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_8, color=colors[3], marker='2', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_9, color=colors[8], marker='2', markersize=0, linewidth=.7)
axarr[1][5].plot(time, drinter_no_10, color=colors[9], marker='2', markersize=0, linewidth=.7)
axarr[1][5].set_ylim(0,1)
axarr[1][5].set_xlabel('Time [s]')
axarr[1][5].set_ylabel('Drinter')

pl.show()