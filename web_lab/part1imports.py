# Laborator: Importuri

# Student: Adam Marius

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10
import requests
print("ex1:" ,requests.__version__)
import urllib.request
# requests este o bibliotecă externa si trebuie instalata cu pip install
# urllib.request face parte deja din biblioteca standard python
#EX 2
raspuns =requests.get(BASE_URL)
print("ex2",raspuns.status_code)
#codul este mai clar si se intelege din ce biblioteca provine functia
#codul este mai scurt
#EX 3
import requests as rq
raspuns =rq.get(BASE_URL)
print("ex3",raspuns.status_code)
# aliasul ajută la scrierea unui cod mai scurt,
# dar poate fi greu de înțeles dacă nu este clar
# EX 4

cerere = urllib.request.Request(
    BASE_URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

raspuns = urllib.request.urlopen(cerere)

print("ex4:", raspuns.status)

corp = raspuns.read().decode("utf-8")
print(corp[:200])
#EX 5
print(dir(requests)[:3])
print("ex 5",type(requests.get))#class function
print(type(requests.HTTPError))#lass type
print(type(requests.exceptions))#class module
# EX 6
import time
help(requests.get)
raspuns = requests.get(BASE_URL,timeout=TIMEOUT)
print("ex 6:",raspuns.status_code)
#EX 7
start = time.perf_counter()
raspuns=requests.get(BASE_URL)
stop=time.perf_counter()
durata=stop-start
print("ex 7:",durata )
#EX 8
try:
    import bs4
    print("ex 8:",bs4.__version__)
except ImportError:
    print(": Instalați modulul cu: pip install beautifulsoup4")









