# -*- coding: utf-8-*-

import random
import time
from arrayPack.stack import stack as st


baseStack = st.Stack("i")


for index in range(0, 10):

    baseStack.push(random.randint(0, 3))
    print "Primo elemento dello stack: ", baseStack.peek()
    length = baseStack.size()
    print "Lunghezza stack: %d" % length

    time.sleep(1)
