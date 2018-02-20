# -*- coding: utf-8-*-

from arrayPack import generic as ar

myDynamicArray = ar.newDynamicArray('i')

ar.fillDynamicArray(myDynamicArray, 'i', 5)

ar.printArray(myDynamicArray)

new = ar.reverseInNewArray(myDynamicArray)

ar.printArray(new)