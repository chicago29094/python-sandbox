f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed
f.close()
f.read()

f.read()
f.read()

f.readline()
f.readline()
f.readline()

for line in f:
    print(line, end='')
    