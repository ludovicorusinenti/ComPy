import sys
import os
import subprocess
import compy as cp

##########################################################################################################################
####### python timec_official.py (1)model_name (2)n_step (3)time_nfsim (4)t_step_nfsim (5)gml (6)opt_flag (7)n_sim #######
##########################################################################################################################  

############################################  CREAZIONE VARIABILI 1 #####################################################

n = int(sys.argv[2])  # numero di time step per una simulazione
m = int(sys.argv[7])  # numero di simulazioni
model_name = '%s' %sys.argv[1] # nome modello

############################################# CREAZIONE VARIABILI 2 ####################################################


if __name__ == "__main__":

	for j in range(m):

		print '\n***************************\n'
		print 'Simulation %s' %j
		print '\n***************************\n'

		for i in range(n): #una sola simulazione che ha n time step
			
			print '\n***************************\n'
			print 'Step %s' %i
			print '\n***************************\n'

			file_species = "%s_%s_nf_%s.species" %(j, sys.argv[1], i)
			file_bngl = '%s.bngl' %(sys.argv[1])
			file_seed = "seed_%s.species" %(sys.argv[1])

			nf_command = ["C:"+os.sep+'Programmi'+os.sep+"BioNetGen-2.4"+os.sep+"bin"+os.sep+"NFsim", "-xml", "%s.xml" %sys.argv[1], "-sim", "%s" %sys.argv[3], "-oSteps", "%s" %sys.argv[4] ,"-gml" ,"%s" %sys.argv[5],"-ss", "C:"+os.sep+"Working"+os.sep+"Working"+os.sep+'sim_reali'+os.sep+'dolan'+os.sep+"%s_%s_nf_%s.species" %(j, sys.argv[1], i), "%s" %(sys.argv[6])]
			bng_command = ["C:"+os.sep+'Programmi'+os.sep+"BioNetGen-2.4"+os.sep+"BNG2.pl", "-xml", "C:"+os.sep+"Working"+os.sep+"Working"+os.sep+'sim_reali'+os.sep+'dolan'+os.sep+file_bngl]


############################################ CHIAMATA PROCESSI ############################################################

			if i == 0:
				lista_seed = cp.leggi(file_seed)
				cp.SeedBM(lista_seed, file_bngl)
				subprocess.call(bng_command, shell=True)
				subprocess.call(nf_command) 
				print '\n***********************\n'
				print 'SEED' 
				print '\n***********************\n'

			else:
				subprocess.call(nf_command)

			print '\n***********************\n'
			print 'DONE NFsim' 
			print '\n***********************\n'

			lista_ss = cp.leggi(file_species)  #leggo le specie e le metto in una lista
			lista_nodb = cp.CIsoS_1(lista_ss) #pulisco le specie da doppi 
			lista_noiso = cp.CIsoS(lista_nodb) #pulisco le specie da isomorfi
			

			cp.scrivi(file_species, lista_noiso) #scrivo la lista noiso in un file


			print '\n***********************\n'
			print 'DONE CLEANING'
			print '\n***********************\n'


			cp.SeedBM(lista_noiso, file_bngl) #metto nelle seed species la lista delle specie

			print '\n***********************\n'
			print 'CREATED BNGL'
			print '\n***********************\n'

			subprocess.call(bng_command, shell=True) #faccio generare l xml

			print '\n***********************\n'
			print 'DONE BNG2'
			print '\n***********************\n'


	print 'DONE SIMULATIONS'