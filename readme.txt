@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
																		
																		_____	_____		
																		|		|____|	
																		|____OM | Y


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Il modulo compy contiene tutte le funzioni utilizzate in simulazione ed analisi.


---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------- Simulazione ----------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------

	1. Aggiornare in time_course il percorso per trovare BioNetGen, NFsim, il modello e dove scrivere i file generati.
	2. Copiare il modelname.bngl 
	3. Copiare un seed_modelname.species con le specie iniziali.
		NB: l'estensione .species è un file di testo contenente la lista dele specie e il loro numero come segue:
			A() 6
			B() 7
			...
	4. Dalla linea di comando lanciare lo script con Python 2.7 inserendo gli argomenti come scritto nel commento iniziale su time_course.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------- Analisi --------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------

	1. I file di PyDrift sono tutti da lanciare tramite linea di comando con gli argomenti specificati al loro interno nel commento
	2. Verificare che la lunghezza di step_dict sia uguale al numero di step
	3. Per le analisi sono necessari tutti i file %s_modelname_nf_%s.species (%sim,step)
	4. L'output sarà un csv: ogni riga contiene i valori delle misure per uno step nell'ordine:
		0 time 
		1 drift medio
		2 deviazione standard drift
		3 inter
		4 numerosità media
		5 deviazione standard numerosità media
		6 intersezione
		7 unione
		8 drinter
	5. Così come sono le analisi scrivono un file.species con l'elenco delle specie presenti nei diversi set di intersezione. Cambiando l'apposito comando si possono scrivere tutti i set desiderati
	6. Per limitare le analisi a complessi o specie o per escludere specie dalle analisi usare le funzioni presenti in compy all'interno di pydrift nella sezione apposita segnalata con un commento

---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------- Visualizzazione ------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------

	Vengono forniti due script basati su matplotlib per la visualizzazione.
	confronto_molti è per molti diversi modelli o varianti da confrontare, confronto_due solo per due