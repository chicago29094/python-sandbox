#!/usr/bin/env python3
import re

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
        lambda mo: mo.group(0).capitalize(), s)

my_list = list(titlecase("they're bill's friends."))
old_list = my_list;
my_list.reverse()

print( old_list, my_list )

third_list = my_list[::-2]
print(third_list)

