#!/usr/bin/env python3

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
print('tel: ', tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

list(tel)
list(tel)
print('list(tel): ', list(tel))

sorted(tel)
print('sorted(tel): ', sorted(tel) )

'guido' in tel
print('\'guido\' in tel: ', 'guido' in tel)

'jack' not in tel
print('\'jack\' not in tel: ', 'jack' not in tel)


