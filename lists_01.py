#!/usr/bin/env python3

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
a = fruits.count('apple') 
print( a )

a = fruits.count('tangerine') 
print( a )

a = fruits.index('banana')
print( a )

a=fruits.index('banana', 4)  # Find next banana starting a position 4
print( a )

fruits.reverse()
print( fruits )

fruits.append('grape')
print( fruits )

fruits.sort()
print( fruits )

fruits.pop()
print( fruits )
print( fruits[0] )
print( fruits[0:3] )
