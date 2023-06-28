#coding=utf-8
import os, sys, platform
os.system('https://facebook.com/groups/347577560720737/')
os.system('rm -rf RANDOM.so RANDOM32.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf RANDOM.so RANDOM32.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RANDOM.so'):
        os.system('curl -L https://github.com/BALOOXH-BRAND/BXB-PRO/blob/main/RANDOM.cpython-311.so?raw=true -o RANDOM.so') 
        import RANDOM
    else:
        import RANDOM

elif bit == '32bit':
    if not os.path.isfile('RANDOM32.so'):
        os.system('curl -L https://github.com/BALOOXH-BRAND/BXB-PRO/blob/main/RANDOM32.cpython-311.so?raw=true -o RANDOM32.so') 
        import RANDOM32
    else:
        import RANDOM32


