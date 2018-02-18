def selectionSort(myVector):
	
	i=0
	j=0
	comodo=0
	
	
	n=len(myVector)
	for i in range(i, n-i):
		j=i+1
		
		for j in range(j, n):
			
			if(myVector[i]>myVector[j]):
				comodo=myVector[i]
				myVector[i]=myVector[j]
				myVector[j]=comodo
	
	
	return


def bubbleSort(myVector):
	
	N=len(myVector)
	Continua=True
	
	while(Continua):
	
		Continua=False
		for i in range(0, N-1):
			if(myVector[i]>myVector[i+1]):
				comodo=myVector[i]
				myVector[i]=myVector[i+1]
				myVector[i+1]=comodo
				Continua=True
				
	
	return

	
def shakerSort(myVector):
	
	numeroElementi= len(myVector)
	continua=True
	while continua==True:
		superiore=numeroElementi
		continua=False
		for i in range(0, superiore-1):
			if(myVector[i]>myVector[i+1]):
				aiuto=myVector[i]
				myVector[i]=myVector[i+1]
				myVector[i+1]=aiuto
				
				continua=True
				superiore=i
				
		for i in range(superiore-1, 0):
			if(myVector[i]>myVector[i-1]):
				aiuto=myVector[i]
				myVector[i]=myVector[i-1]
				myVector[i-1]=aiuto

				continua=True
				superiore=i
		print myVector
	return 


def RicercaBinaria(vettore, x):
	
	n=len(vettore)
	primo = 0
	ultimo = n-1
	trovato = False
	indice=0
	
	while (primo <= ultimo) and (not trovato):
		centro = (primo + ultimo) / 2
		
		if (vettore[centro] == x):
			trovato = True
			indice=centro
			
			print "L'elemento ricercato e' in posizione ", indice
			
		elif (vettore[centro] < x):
				primo = centro + 1
       
		else:
			ultimo = centro - 1
        
	return trovato
	
	

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue


def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


def RicercaSequenziale(vettore,x):
	for i in range(len(vettore)):
		if vettore[i] == x:
			return 1
	return False
