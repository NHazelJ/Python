#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = (1, "two", 3.0, [4,"four"], 5)
y = (1, "two", 3.0, [4,"four"], 5)
print('x is {}'.format(x))
print(type(x[1]))

if x[1] is y[1]:
    print("yep")
else:
    print("nope")