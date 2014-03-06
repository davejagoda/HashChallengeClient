#!/usr/bin/python

import hashlib

def sha512(arg):
    print(hashlib.sha512(arg).hexdigest())

if '__main__' == __name__:
    print('sha512("#Wednesday")')
    sha512("#Wednesday")
    print("sha512('#Wednesday')")
    sha512('#Wednesday')
    print('reference')
    print('2666e2c90134aa332918b02f68e137830cdd45e4d33c3c54735297eb107e509938d5c2a0f7838c20617a0370db3a0c13454bfc35ef04b3d4d708ee70caa95b5d')
