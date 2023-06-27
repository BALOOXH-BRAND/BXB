#coding=utf-8
import os, sys, platform
os.system('https://facebook.com/groups/347577560720737/')
os.system('rm -rf BXB.so BXB32.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf BXB.so BXB32.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('BXB.so'):
        os.system('curl -L https://github.com/BALOOXH-BRAND/BXB-PRO/blob/main/BXB.cpython-311.so?raw=true -o BXB.so') 
        import BXB
    else:
        import BXB

elif bit == '32bit':
    if not os.path.isfile('BXB32.so'):
        os.system('curl -L https://github.com/BALOOXH-BRAND/BXB-PRO/blob/main/BXB32.cpython-311.so?raw=true -o BXB32.so') 
        import BXB32
    else:
        import BXB32

