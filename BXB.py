#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf BXB.so BXB32.so')
except:
    pass
os.system('rm -rf BXB.so BXB32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('BXB.so'):
        os.system('curl -L https://github.com/BALOOXH-BRAND/Javed-xd/blob/main/BXB.cpython-311.so?raw=true -o BXB.so') 
        import BXB
    else:
        import BXB

