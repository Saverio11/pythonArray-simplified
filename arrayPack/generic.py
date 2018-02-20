# -*- coding: utf-8 -*-

# Modulo Array
import array as ar
import random


def newStaticArray(typeOfData, length):
    try:
        if typeOfData.lower() == "i" or typeOfData.lower() == "f":
            pass
    except ValueError:
        print("CRITICAL ERROR! Type of data not supported. Please enter i or f")
        return 1

    newArray = ar.array(str(typeOfData), [])

    if typeOfData.lower() == "i":
        for i in range(0, length):
            newArray.append(0)
    else:
        for i in range(0, length):
            newArray.append(0.0)

    return newArray


def newDynamicArray(typeOfData):
    try:
        if typeOfData.lower() == "i" or typeOfData.lower() == "f":
            pass
    except ValueError:
        print("CRITICAL ERROR! Type of data not supported. Please enter i or f")
        return 1

    newArray = ar.array(str(typeOfData), [])

    return newArray


def printArray(myVector):
    state = isDynamicEmpty(myVector)

    if state:
        print ("Empty array")

        return 0

    else:
        length = len(myVector)
        for i in range(0, length):
            print myVector[i]

        return 0


def fillStaticArray(myVector, typeOfData):
    state = isDynamicEmpty(myVector)

    if state:
        print ("Empty array!")

        return 1

    else:
        length = len(myVector)

        for i in range(0, length):

            try:
                if typeOfData.lower() == "i":
                    element = random.randint(0, length)
                elif typeOfData.lower() == "f":
                    element = random.uniform(0, length)

            except ValueError:

                print("CRITICAL ERROR! Type of data not supported. Please enter i or f")
                return 1

            myVector[i] = element

        return 0


def fillDynamicArray(myVector, typeOfData, numberOfElementsToInitialize):
    length = len(myVector)

    for i in range(0, numberOfElementsToInitialize):
        try:
            if typeOfData.lower() == "i":
                element = random.randint(0, numberOfElementsToInitialize)
            elif typeOfData.lower() == "f":
                element = random.uniform(0, numberOfElementsToInitialize)

        except ValueError:

            print("CRITICAL ERROR! Type of data not supported. Please enter i or f")
            return 1

        myVector.append(element)

    return 0


def emptyStaticArray(myVector):
    state = isStaticEmpty(myVector)

    if state:
        return True

    else:
        lenght = len(myVector)
        typeOfData = type(myVector[0])

        for i in range(0, lenght):
            if typeOfData is int:
                myVector[i] = 0
            else:
                myVector[i] = 0.0

    return True


def emptyDynamicArray(myVector):
    state = isDynamicEmpty(myVector)

    if state:
        return True

    else:
        while 1:
            for item in myVector:
                myVector.remove(item)

            currentNumberOfElements = len(myVector)
            if currentNumberOfElements == 0:
                break

    return True


def cloneArray(myVector):
    state = isDynamicEmpty(myVector)

    if state:
        return ar.array('i', [])

    else:
        typeOfData = type(myVector[0])

        if typeOfData is int:
            clone = ar.array('i', [])
        else:
            clone = ar.array('f', [])

    for item in myVector:
        clone.append(item)

    return clone


def deleteDuplicates(myVector):
    state = isDynamicEmpty(myVector)

    if not state:
        typeOfData = type(myVector[0])

        if typeOfData is int:
            newVector = ar.array('i', [])
        else:
            newVector = ar.array('f', [])

        for item in myVector:
            if item not in newVector:
                newVector.append(item)

    return newVector


def isStaticEmpty(myVector):
    for item in myVector:
        if item != 0:
            return False

    return True


def isDynamicEmpty(myVector):
    length = len(myVector)

    if length == 0:
        return True
    else:
        return False


def isFull(myVector):
    for index in range(0, len(myVector)):
        if myVector[index] != 0:
            continue
        else:
            return False

    return True


def reverseInNewArray(myVector):

    clone = cloneArray(myVector)
    clone.reverse()

    return clone
