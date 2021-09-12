#!/usr/bin/env python3
import re

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
        lambda mo: mo.group(0).capitalize(), s)

print( titlecase("tyEy're bill's friends.").split().reverse() )

