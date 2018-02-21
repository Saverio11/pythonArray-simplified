# -*- coding: utf-8-*-

import arrayPack as ar

array1 = ar.newDynamicArray('f')

ar.fillDynamicArray(array1, 'f', 150)

array2 = ar.cloneArray(array1)
array3 = ar.cloneArray(array1)
array4 = ar.cloneArray(array1)
array5 = ar.cloneArray(array1)
array6 = ar.cloneArray(array1)

print str(ar.sortExecutionTime(array2, ar.selectionSort))
print str(ar.sortExecutionTime(array3, ar.bubbleSort))
print str(ar.sortExecutionTime(array4, ar.shakerSort))
print str(ar.sortExecutionTime(array5, ar.insertionSort))
print str(ar.sortExecutionTime(array6, ar.shellSort))

