import json
from io import StringIO

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) )

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()

str=json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
print( str )

    