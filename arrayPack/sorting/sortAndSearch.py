import time as time_


def selectionSort(myVector):
    for i in xrange(len(myVector) - 1):
        m = i

        for j in xrange(i + 1, len(myVector)):
            if myVector[j] < myVector[m]: m = j

            myVector[i], myVector[m] = myVector[m], myVector[i]

        return


def bubbleSort(myVector):

    length = len(myVector)
    cicle = True

    while cicle:
        cicle = False

        for i in range(0, length - 1):

            if myVector[i] > myVector[i + 1]:

                aux = myVector[i]
                myVector[i] = myVector[i + 1]
                myVector[i + 1] = aux

                cicle = True

    return


def shakerSort(myVector):

    length = len(myVector)
    cicle = True

    while cicle:

        lastElementSorted = length
        cicle = False

        for i in range(0, lastElementSorted - 1):

            if myVector[i] > myVector[i + 1]:

                aiuto = myVector[i]
                myVector[i] = myVector[i + 1]
                myVector[i + 1] = aiuto

                cicle = True
                lastElementSorted = i

        for i in range(lastElementSorted - 1, 0):

            if myVector[i] > myVector[i - 1]:

                aiuto = myVector[i]
                myVector[i] = myVector[i - 1]
                myVector[i - 1] = aiuto

                cicle = True
                lastElementSorted = i
    return


def gapInsertionSort(myVector, start, gap):

    for i in range(start + gap, len(myVector), gap):

        currentvalue = myVector[i]
        position = i

        while position >= gap and myVector[position - gap] > currentvalue:
            myVector[position] = myVector[position - gap]
            position = position - gap

        myVector[position] = currentvalue
    return


def insertionSort(myVector):
    for index in range(1, len(myVector)):

        currentvalue = myVector[index]
        position = index

        while position > 0 and myVector[position - 1] > currentvalue:

            myVector[position] = myVector[position - 1]
            position = position - 1

        myVector[position] = currentvalue
    return


def shellSort(myVector):

    sublistcount = len(myVector) // 2

    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(myVector, startposition, sublistcount)

        sublistcount = sublistcount // 2
    return


def seqSearch(myVector, elementToSearch):

    for i in range(len(myVector)):

        if myVector[i] == elementToSearch:
            return i

    return False


def binSearch(myVector, elementToSearch):
    length = len(myVector)
    first = 0
    last = length - 1
    isFound = False

    while (first <= last) and (not isFound):

        middle = (first + last) / 2

        if myVector[middle] == elementToSearch:

            index = middle
            return index

        elif myVector[middle] < elementToSearch:
            first = middle + 1

        else:
            last = middle - 1

    return isFound


def millis():
    return time_.time()


def sortExecutionTime(array, kindOfSort):

    tstart = millis()
    kindOfSort(array)
    tend = millis()

    ttot = tend - tstart

    return ttot
