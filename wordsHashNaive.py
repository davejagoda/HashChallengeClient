#!/usr/bin/python

import hashlib

f = open('/usr/share/dict/words')
for line in f.readlines():
    line = line.rstrip()
    h = hashlib.sha512(line)
    print(line + ':' + h.hexdigest() + '  -')
f.close()
