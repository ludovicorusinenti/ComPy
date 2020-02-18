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
time = np.loadtxt('analisi_dolan_tutti_nf.csv', delimiter=',')[:,0]

file_name_0 = 'analisi_dolan_tutti_nf.csv'				#7 arancio
#file_name_1 = 'analisi_dolan_tutti_dna.csv'				#8 lime green
#file_name_4 = 'analisi_dolan_tutti_not_p53.csv'			
file_name_5 = 'analisi_dolan_tutti_nodna.csv'		#4 teal
#file_name_6 = 'analisi_dolan_tutti_cmplx.csv'			#5 grey
# file_name_7 = 'analisi_jurkat_nf_egfr.csv'
# file_name_8 = 'analisi_lncap_nf_egfr.csv'
# file_name_9 = 'analisi_hek293_nf_egfr.csv'
# file_name_10 = 'analisi_k562_nf_egfr.csv'

# osservazioni:
#	lenght:
# 		nf e not_p53 sono uguali (rispettivamente arancione e salmone)

drift_0 = np.loadtxt(file_name_0, delimiter=',')[:,1]
std_drift_0 = np.loadtxt(file_name_0, delimiter=',')[:,2]
inter_0 = np.loadtxt(file_name_0, delimiter=',')[:,3]
lenght_0 = np.loadtxt(file_name_0, delimiter=',')[:,4]
std_lenght_0 = np.loadtxt(file_name_0, delimiter=',')[:,5]
inter_len_0 = np.loadtxt(file_name_0, delimiter=',')[:,6]
unione_0 = np.loadtxt(file_name_0, delimiter=',')[:,7]
drinter_0 = np.loadtxt(file_name_0, delimiter=',')[:,8]

# drift_1 = np.loadtxt(file_name_1, delimiter=',')[:,1]
# std_drift_1 = np.loadtxt(file_name_1, delimiter=',')[:,2]
# inter_1 = np.loadtxt(file_name_1, delimiter=',')[:,3]
# lenght_1 = np.loadtxt(file_name_1, delimiter=',')[:,4]
# std_lenght_1 = np.loadtxt(file_name_1, delimiter=',')[:,5]
# inter_len_1 = np.loadtxt(file_name_1, delimiter=',')[:,6]
# unione_1 = np.loadtxt(file_name_1, delimiter=',')[:,7]
# drinter_1 = np.loadtxt(file_name_1, delimiter=',')[:,8]

# drift_4 = np.loadtxt(file_name_4, delimiter=',')[:,1]
# std_drift_4 = np.loadtxt(file_name_4, delimiter=',')[:,2]
# inter_4 = np.loadtxt(file_name_4, delimiter=',')[:,3]
# lenght_4 = np.loadtxt(file_name_4, delimiter=',')[:,4]
# std_lenght_4 = np.loadtxt(file_name_4, delimiter=',')[:,5]
# inter_len_4 = np.loadtxt(file_name_4, delimiter=',')[:,6]
# unione_4 = np.loadtxt(file_name_4, delimiter=',')[:,7]
# drinter_4 = np.loadtxt(file_name_4, delimiter=',')[:,8]

drift_5 = np.loadtxt(file_name_5, delimiter=',')[:,1]
std_drift_5 = np.loadtxt(file_name_5, delimiter=',')[:,2]
inter_5 = np.loadtxt(file_name_5, delimiter=',')[:,3]
lenght_5 = np.loadtxt(file_name_5, delimiter=',')[:,4]
std_lenght_5 = np.loadtxt(file_name_5, delimiter=',')[:,5]
inter_len_5 = np.loadtxt(file_name_5, delimiter=',')[:,6]
unione_5 = np.loadtxt(file_name_5, delimiter=',')[:,7]
drinter_5 = np.loadtxt(file_name_5, delimiter=',')[:,8]

# drift_6 = np.loadtxt(file_name_6, delimiter=',')[:,1]
# std_drift_6 = np.loadtxt(file_name_6, delimiter=',')[:,2]
# inter_6 = np.loadtxt(file_name_6, delimiter=',')[:,3]
# lenght_6 = np.loadtxt(file_name_6, delimiter=',')[:,4]
# std_lenght_6 = np.loadtxt(file_name_6, delimiter=',')[:,5]
# inter_len_6 = np.loadtxt(file_name_6, delimiter=',')[:,6]
# unione_6 = np.loadtxt(file_name_6, delimiter=',')[:,7]
# drinter_6 = np.loadtxt(file_name_6, delimiter=',')[:,8]

# drift_7 = np.loadtxt(file_name_7, delimiter=',')[:,1]
# std_drift_7 = np.loadtxt(file_name_7, delimiter=',')[:,2]
# inter_7 = np.loadtxt(file_name_7, delimiter=',')[:,3]
# lenght_7 = np.loadtxt(file_name_7, delimiter=',')[:,4]
# std_lenght_7 = np.loadtxt(file_name_7, delimiter=',')[:,5]
# inter_len_7 = np.loadtxt(file_name_7, delimiter=',')[:,6]
# unione_7 = np.loadtxt(file_name_7, delimiter=',')[:,7]
# drinter_7 = np.loadtxt(file_name_7, delimiter=',')[:,8]

# drift_8 = np.loadtxt(file_name_8, delimiter=',')[:,1]
# std_drift_8 = np.loadtxt(file_name_8, delimiter=',')[:,2]
# inter_8 = np.loadtxt(file_name_8, delimiter=',')[:,3]
# lenght_8 = np.loadtxt(file_name_8, delimiter=',')[:,4]
# std_lenght_8 = np.loadtxt(file_name_8, delimiter=',')[:,5]
# inter_len_8 = np.loadtxt(file_name_8, delimiter=',')[:,6]
# unione_8 = np.loadtxt(file_name_8, delimiter=',')[:,7]
# drinter_8 = np.loadtxt(file_name_8, delimiter=',')[:,8]

# drift_9 = np.loadtxt(file_name_9, delimiter=',')[:,1]
# std_drift_9 = np.loadtxt(file_name_9, delimiter=',')[:,2]
# inter_9 = np.loadtxt(file_name_9, delimiter=',')[:,3]
# lenght_9 = np.loadtxt(file_name_9, delimiter=',')[:,4]
# std_lenght_9 = np.loadtxt(file_name_9, delimiter=',')[:,5]
# inter_len_9 = np.loadtxt(file_name_9, delimiter=',')[:,6]
# unione_9 = np.loadtxt(file_name_9, delimiter=',')[:,7]
# drinter_9 = np.loadtxt(file_name_9, delimiter=',')[:,8]

# drift_10 = np.loadtxt(file_name_10, delimiter=',')[:,1]
# std_drift_10 = np.loadtxt(file_name_10, delimiter=',')[:,2]
# inter_10 = np.loadtxt(file_name_10, delimiter=',')[:,3]
# lenght_10 = np.loadtxt(file_name_10, delimiter=',')[:,4]
# std_lenght_10 = np.loadtxt(file_name_10, delimiter=',')[:,5]
# inter_len_10 = np.loadtxt(file_name_10, delimiter=',')[:,6]
# unione_10 = np.loadtxt(file_name_10, delimiter=',')[:,7]
# drinter_10 = np.loadtxt(file_name_10, delimiter=',')[:,8]

f, axarr = pl.subplots(3, 2, sharex = True)

#f.suptitle('Dolan - 20sim')

axarr[0][0].errorbar(time, lenght_0, yerr=std_lenght_0, ecolor=colors[7], elinewidth=.3, color=colors[7], marker='o', markersize=1, linewidth=.5)
#axarr[0][0].errorbar(time, lenght_1, yerr=std_lenght_1, ecolor=colors[8], elinewidth=.3, color=colors[8], marker='^', markersize=1, linewidth=.5)
# axarr[0][0].errorbar(time, lenght_4, yerr=std_lenght_4, ecolor=colors[1], elinewidth=.3, color=colors[1], marker='^', markersize=1, linewidth=.5)
axarr[0][0].errorbar(time, lenght_5, yerr=std_lenght_5, ecolor=colors[4], elinewidth=.3, color=colors[4], marker='^', markersize=1, linewidth=.5)
#axarr[0][0].errorbar(time, lenght_6, yerr=std_lenght_6, ecolor=colors[5], elinewidth=.3, color=colors[5], marker='^', markersize=1, linewidth=.5)
# axarr[0][0].errorbar(time, lenght_7, yerr=std_lenght_7, ecolor=colors[3], elinewidth=.3, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[0][0].errorbar(time, lenght_8, yerr=std_lenght_8, ecolor=colors[3], elinewidth=.3, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[0][0].errorbar(time, lenght_9, yerr=std_lenght_9, ecolor=colors[9], elinewidth=.3, color=colors[9], marker='^', markersize=1, linewidth=.5)
# axarr[0][0].errorbar(time, lenght_10, yerr=std_lenght_10, ecolor=colors[3], elinewidth=.3, color=colors[3], marker='^', markersize=1, linewidth=.5)
axarr[0][0].set_ylabel('Numerosità media')

#######################################################################################################################

axarr[1][0].plot(time, unione_0, color=colors[7], marker='o', markersize=1, linewidth=.5)
#axarr[1][0].plot(time, unione_1, color=colors[8], marker='^', markersize=1, linewidth=.5)
#axarr[1][0].plot(time, unione_4, color=colors[1], marker='^', markersize=1, linewidth=.5)
axarr[1][0].plot(time, unione_5, color=colors[4], marker='^', markersize=1, linewidth=.5)
#axarr[1][0].plot(time, unione_6, color=colors[5], marker='^', markersize=1, linewidth=.5)
# axarr[1][0].plot(time, unione_7, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[1][0].plot(time, unione_8, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[1][0].plot(time, unione_9, color=colors[9], marker='^', markersize=1, linewidth=.5)
# axarr[1][0].plot(time, unione_10, color=colors[3], marker='^', markersize=1, linewidth=.5)
axarr[1][0].set_ylabel('Unione')

#######################################################################################################################

axarr[2][0].plot(time, inter_len_0, color=colors[7], marker='o', markersize=1, linewidth=.5)
#axarr[2][0].plot(time, inter_len_1, color=colors[8], marker='^', markersize=1, linewidth=.5)
#axarr[2][0].plot(time, inter_len_4, color=colors[1], marker='^', markersize=1, linewidth=.5)
axarr[2][0].plot(time, inter_len_5, color=colors[4], marker='^', markersize=1, linewidth=.5) 
#axarr[2][0].plot(time, inter_len_6, color=colors[5], marker='^', markersize=1, linewidth=.5)
# axarr[2][0].plot(time, inter_len_7, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[2][0].plot(time, inter_len_8, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[2][0].plot(time, inter_len_9, color=colors[9], marker='^', markersize=1, linewidth=.5)
# axarr[2][0].plot(time, inter_len_10, color=colors[3], marker='^', markersize=1, linewidth=.5)
axarr[2][0].set_ylabel('Intersezione')
axarr[2][0].set_xlabel('Time [s]')

#######################################################################################################################

axarr[0][1].plot(time, inter_0, color=colors[7], marker='o', markersize=1, linewidth=.5)
#axarr[0][1].plot(time, inter_1, color=colors[8], marker='^', markersize=1, linewidth=.5)
#axarr[0][1].plot(time, inter_4, color=colors[1], marker='^', markersize=1, linewidth=.5)
axarr[0][1].plot(time, inter_5, color=colors[4], marker='^', markersize=1, linewidth=.5)
#axarr[0][1].plot(time, inter_6, color=colors[5], marker='^', markersize=1, linewidth=.5)
# axarr[0][1].plot(time, inter_7, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[0][1].plot(time, inter_8, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[0][1].plot(time, inter_9, color=colors[9], marker='^', markersize=1, linewidth=.5)
# axarr[0][1].plot(time, inter_10, color=colors[3], marker='^', markersize=1, linewidth=.5)
axarr[0][1].set_ylim(0,1)
axarr[0][1].set_ylabel('Inter')

#######################################################################################################################

axarr[1][1].errorbar(time, drift_0, yerr=std_drift_0, ecolor=colors[7], elinewidth=.3, color=colors[7], marker='o', markersize=1, linewidth=.5)
#axarr[1][1].errorbar(time, drift_1, yerr=std_drift_1, ecolor=colors[8], elinewidth=.3, color=colors[8], marker='^', markersize=1, linewidth=.5)
#axarr[1][1].errorbar(time, drift_4, yerr=std_drift_4, ecolor=colors[1], elinewidth=.3, color=colors[1], marker='^', markersize=1, linewidth=.5)
axarr[1][1].errorbar(time, drift_5, yerr=std_drift_5, ecolor=colors[4], elinewidth=.3, color=colors[4], marker='^', markersize=1, linewidth=.5)
#axarr[1][1].errorbar(time, drift_6, yerr=std_drift_6, ecolor=colors[5], elinewidth=.3, color=colors[5], marker='^', markersize=1, linewidth=.5)
# axarr[1][1].errorbar(time, drift_7, yerr=std_drift_7, ecolor=colors[3], elinewidth=.3, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[1][1].errorbar(time, drift_8, yerr=std_drift_8, ecolor=colors[3], elinewidth=.3, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[1][1].errorbar(time, drift_9, yerr=std_drift_9, ecolor=colors[9], elinewidth=.3, color=colors[9], marker='^', markersize=1, linewidth=.5)
# axarr[1][1].errorbar(time, drift_10, yerr=std_drift_10, ecolor=colors[3], elinewidth=.3, color=colors[3], marker='^', markersize=1, linewidth=.5)
axarr[1][1].set_ylim(0,1)
axarr[1][1].set_ylabel('Drift')

#######################################################################################################################

axarr[2][1].plot(time, drinter_0, color=colors[7], marker='o', markersize=1, linewidth=.5)
#axarr[2][1].plot(time, drinter_1, color=colors[8], marker='^', markersize=1, linewidth=.5)
#axarr[2][1].plot(time, drinter_4, color=colors[1], marker='^', markersize=1, linewidth=.5)
axarr[2][1].plot(time, drinter_5, color=colors[4], marker='^', markersize=1, linewidth=.5)
#axarr[2][1].plot(time, drinter_6, color=colors[5], marker='^', markersize=1, linewidth=.5)
# axarr[2][1].plot(time, drinter_7, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[2][1].plot(time, drinter_8, color=colors[3], marker='^', markersize=1, linewidth=.5)
# axarr[2][1].plot(time, drinter_9, color=colors[9], marker='^', markersize=1, linewidth=.5)
# axarr[2][1].plot(time, drinter_10, color=colors[3], marker='^', markersize=1, linewidth=.5)
axarr[2][1].set_ylim(0,1)
axarr[2][1].set_xlabel('Time [s]')
axarr[2][1].set_ylabel('Drinter')

pl.show()