#!/usr/bin/env python

def mapper(c):
    if c in (' ', '.', "'", '(', ')'):
        return c
    a = ord('a')
    z = ord('z')
    x = ord(c) + 2
    if x > z:
        x = a + x-z - 1
    return chr(x)

print ''.join(map(mapper, "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))

print ''.join(map(mapper, "map"))
