#coding=utf-8
import os, sys, platform
os.system('https://facebook.com/groups/347577560720737/')
os.system('rm -rf Project1.so Project2.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Project1.so Project2.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Project1.so'):
        os.system('curl -L https://github.com/Mradi007/Dump/blob/main/Project1.cpython-311.so.so?raw=true -o Project1.so') 
        import Project1
    else:
        import Project1

elif bit == '32bit':
    if not os.path.isfile('Project2.so'):
        os.system('curl -L https://github.com/Mradi007/Dump/blob/main/Project2.cpython-311.so.so?raw=true -o Project2.so') 
         
        import Project2
    else:
        import Project2
