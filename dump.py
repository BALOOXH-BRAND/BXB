import os, platform, time, sys
 
try:
 
    import requests
 
except:
 
    os.system('pip install requests')
 
os.system('git pull --quiet 2>/dev/null')
 
bit = platform.architecture()[0]
 
if bit == '64bit':
 
    print('\033[0;97m[•] \033[1;32mCONGRATULATIONS 64BIT SUCCESS')
 
    from Project1 import Menu
 
    Menu()
 
elif bit == '32bit':
 
    print('\033[0;97m[•] \033[1;32mCONGRATULATIONS 32BIT SUCCESS')
 
    from Project2 import Menu
 
    Menu()




