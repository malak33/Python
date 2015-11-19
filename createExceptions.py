#! /usr/bin/python3
# createExceptions.py - an example of how to create an exception
try:
    a = input('Number 1: ')
    b = input('Number 2: ')
    result = float(a) / float(b)
    print('Division result is: {0}'.format(result))

except Exception as e:
    print(e, type(e))
