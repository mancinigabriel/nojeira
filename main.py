from win32com.client import Dispatch
import time

ie = Dispatch('InternetExplorer.Application.1')
ie.Visible = 1
ie.Navigate('http://www.haskell.org/arrows')

while ie.ReadyState != 4:
    time.sleep(1)

print('a')
document = ie.document
ie.Navigate('https://www.laranjalimashoes.com.br/')

while ie.ReadyState != 4:
    time.sleep(1)

li = document.getElementsByTagName("li")

for i in li:
    print (i.innerHTML)

span = document.getElementsByTagName("span")

for i in span:
    print (i.innerText)

texto = document.getElementById('header-search')

teste = document.getElementById('_003-magnifying-glass')