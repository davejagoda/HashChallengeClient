#!/usr/bin/python
import hashlib
f=open('/usr/share/dict/words')
print('\n'.join([i+':'+hashlib.sha512(i).hexdigest()+'  -' for i in [l.rstrip() for l in f.readlines()]]))
