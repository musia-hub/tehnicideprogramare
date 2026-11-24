# Laborator: funcții, metode și importuri pe web
# Student: Adam Marius

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10
import requests
#EX9 Elementele de bază ale răspunsului
response=requests.get(BASE_URL)
print("ex 9:",response.status_code)  # atribut
print(response.ok)           # atribut
print(response.url)          # atribut
print(response.encoding)     # atribut
#Ex 10 Tratarea erorilor cu o metodă
response = requests.get(BASE_URL)
print("ex 10:")
try:
    response.raise_for_status()
    print("pagina funcționeaza")
except requests.HTTPError:
    print("a aparut o eroare")

response = requests.get(BASE_URL + "/this-page-does-not-exist")
#EX 11 . Toate antetele

print(response.headers.items() )

for nume, valoare in response.headers.items():
    print(nume  + ":" +valoare)

# EX 12. Metode de dicționar

print(response.headers.get("Server", "lipsește"))
print(response.headers.get("Content-Type", "lipsește"))

print(response.headers.get("content-type", "lipsește"))
# EX 13 . Înlănțuirea metodelor de șir

print("ex13:",response.text.lower().count("cyber"))

#EX 14. Găsirea titlului
start=response.text.find("<title>") + len("<title>")
stop=response.text.find("</html>")
titlu = response.text[start:stop].strip()
print("ex 14",titlu)

#EX 15Numărarea liniilor
html = response.text
print("ex15:")
lines = html.splitlines()
print(lines)
print(len(lines))
print(len(max(lines, key=len)))
#ex 16 verificarea HTTPS
print("ex 16:",response.url.startswith(BASE_URL))
if response.url.startswith(BASE_URL)=="https://":
    print("conexiune securizata  ")
else:
    print("conexiune securizata ")
#ex 17 urmarirea redirectionarilor
response = requests.get(BASE_URL)
for r in response.history:
    print(r.status_code, r.url)
print("ex17","URL final:", response.url)
#EX 18 HEAD vs GET
import requests
response_head = requests.head(BASE_URL)
response_get = requests.get(BASE_URL)
print("ex 18 ","HEAD:", len(response_head.content))
print("GET:", len(response_get.content))
# HEAD primește informațiile despre pagină
# GET primește și conținutul paginii
# EX 19
if response.cookies:
    for cookie in response.cookies:
        print(cookie.name, cookie.secure)
else:
    print("ex 19 :","Niciun cookie setat")
## EX 20

session = requests.Session()

session.headers.update({
    "User-Agent": "WebLab-Marius"
})

response = session.get(ECHO_URL + "/headers")
print(response.text)