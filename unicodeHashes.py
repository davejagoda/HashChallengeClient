#!/usr/bin/python
import hashlib, unicodedata

def get_unicode_using_unicode_escape(n):
    s = '%x' % n
    return ('\U' + s.zfill(8)).decode('unicode-escape')

def print_unicode_hash(n):
    u = get_unicode_using_unicode_escape(n)
    h = hashlib.sha512(u.encode('utf8'))
    print(u.encode('utf8') + ':' + h.hexdigest())

if __name__ == '__main__':
    for i in xrange(0x110000):
        print_unicode_hash(i)
