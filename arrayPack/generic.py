# -*- coding: utf-8 -*-

#Modulo Array
from array import *
import os
import random
import time as time_


def millis():
    return time_.time()

def creaArrayIntStatico(n_Elementi):
	newArray=array("i", [])

	for i in range(0, n_Elementi):
		newArray.append(-1)

	return newArray


def creaArrayIntDinamico():
	return array("i", [])


def creaArrayFloatStatico(n_Elementi):
	newArray=array("f", [])

	for i in range(0, n_Elementi):
		newArray.append(-1.0)

	return newArray


def creaArrayFloatDinamico():
	return array("f", [])


def stampaArray(myVector):

	state = isEmpty_v2_0(myVector)

	if (state == True):
		print ("L'array e' vuoto!")

		return
	else:
		lenght = len (myVector)
		for i in range (0, lenght):
			print myVector[i]

		
		return


def riempiArrayDinamico(n_Elementi, myVector):

	for i in range(0, n_Elementi):
		nuovoElemento=random.randint(0,n_Elementi)
		myVector.append(nuovoElemento)

	return 


def riempiArrayStatico(rangeElementi, myVector):
	state = isEmpty_v2_0(myVector)
	
	
	if (state == True):
		print ("L'array e' vuoto!")

		return False
	else:
		lenght = len (myVector)
		for i in range (0, lenght):
			nuovoElemento=random.randint(0, rangeElementi)
			myVector[i]=nuovoElemento

		
		return		

#Genera un IndexError: array index out of range
def svuotaArray_conErrore(n_Elementi, myVector):
	
	for i in range(0, n_Elementi):
		elementToRemove=myVector[i]
		myVector.remove(elementToRemove)

	return 


def svuotaArrayDinamico_con_errore(n_Elementi, myVector):
	
	nElementiDecrementata = n_Elementi

	while(nElementiDecrementata>0):
		headElement=myVector[0]
		myVector.remove(headElement)
		nElementiDecrementata = nElementiDecrementata -1

	return True


def svuotaArrayDinamico(myVector):
	
	state=isEmpty_v2_0(myVector)
	
	if (state==True):
		return True
	else:		
		nElementiDecrementata = len(myVector)

		while(nElementiDecrementata>0):
			headElement=myVector[0]
			myVector.remove(headElement)
			nElementiDecrementata = nElementiDecrementata -1

	return True


def svuotaArrayStatico(myVector):
	state = isEmpty_v2_0(myVector)

	if (state == True):
		return True
	else:
		lenght = len (myVector)
		for i in range (0, lenght):
			myVector[i]=-1
			
	return True


def clonaArray_conIterator(myVector):
	clonato=array('i',[])

	for elemento in myVector:
		clonato.append(elemento)
	
	return clonato


def clonaArray_conIndice(myVector):
	clonato=array('i',[])
	
	lunghezza=len(myVector)
	for i in range (0, lunghezza-1):
		elemento=myVector[i]
		clonato.append(elemento)
	
	return clonato


def eliminaUguali(myVector):
	newVector=array('i',[])

	for elemento in myVector:
		if elemento not in newVector:
			newVector.append(elemento)
	
	return newVector


def isEmpty_v1_0(myVector):
	lunghezza=len(myVector)
	
	if (lunghezza==0) :
		return 1
	else:
		return 0


def isEmpty_v1_1(myVector):
	lunghezza=myVector.count
	
	if (lunghezza==0) :
		return 1
	else:
		return 0


def isEmpty_v2_0(myVector):
	trueOrFalse = ( len(myVector) == 0 )
	
	return trueOrFalse


def isEmpty_v2_1(myVector):
	trueOrFalse = ( myVector.count == 0 )
	
	return trueOrFalse


def isEmpty_v3_0(myVector):
	return ( len(myVector) == 0 )

	
def isEmpty_v3_1(myVector):
	return ( myVector.count == 0 )


def isFull(myVector):
	for index in range (0,len(myVector)):
		if (myVector[index]!= -1):
			continue
		else:
			return 0


def separaElementi(myVector):

	arrayPari=array("i",[])
	arrayDispari=array("i",[])


	contaElementiPari=0
	contaElementiDispari=0

	for element in myVector:

		if((element%2) == 0):
			arrayPari.append(element)

		else:
			arrayDispari.append(element)
		
	return
	
	
def scambiaOrdine(myVector):
	
	lunghezza=len(myVector)
	
	halfLenght=lunghezza/2
	
	for i in range (0, halfLenght-1):
		
		aux=myVector[i]
		myVector[i]=myVector[(lunghezza-1)-i]
		myVector[(lunghezza-1)-i]=aux
	
	return


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
		
	return 

def shellSort(myVector):
    sublistcount = len(myVector)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(myVector,startposition,sublistcount)

      

      sublistcount = sublistcount // 2

def gapInsertionSort(myVector,start,gap):
    for i in range(start+gap,len(myVector),gap):

        currentvalue = myVector[i]
        position = i

        while position>=gap and myVector[position-gap]>currentvalue:
            myVector[position]=myVector[position-gap]
            position = position-gap

        myVector[position]=currentvalue

def insertionSort(myVector):
	for index in range(1,len(myVector)):

		currentvalue = myVector[index]
		position = index

	while position>0 and myVector[position-1]>currentvalue:
		myVector[position]=myVector[position-1]
		position = position-1

	myVector[position]=currentvalue

def ricercaBinaria(myVector, x):
	
	n=len(myVector)
	primo = 0
	ultimo = n-1
	trovato = False
	indice=0
	
	while (primo <= ultimo) and (not trovato):
		centro = (primo + ultimo) / 2
		
		if (myVector[centro] == x):
			trovato = True
			indice=centro
			
			return indice
			
		elif (myVector[centro] < x):
				primo = centro + 1
       
		else:
			ultimo = centro - 1
	
	if(trovato == False):
		return False


def ricercaSequenziale(myVector, x):
	
	for i in range(0, len(myVector)):
		if myVector[i] == x:
			print "L' elemento " + str(x) + " è in posizione : " +str(i)
			return i
			
	print "L' elemento " + str(x) + " non è stato trovato"
	return -1

def calcolaMedia(myVector):
	
	tot = 0
	
	length = len(myVector)
	
	for element in myVector:
		tot = tot + element
	
	media = tot / length
	
	return media

def calcolaTempoSort(kindOfSort, array):
	
	tstart = millis()
	kindOfSort(array)
	tend = millis()
	
	ttot = tend - tstart
	
	return ttot


