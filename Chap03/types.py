#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import * #The decimal module was used here. so you can get 0.00 decimal places
                    #so you can get 0.00 decimal places.

a = Decimal(".10")
b = Decimal(".30")
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))

