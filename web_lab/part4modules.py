# Laborator: Alte module din biblioteca standard
# Student: Adam Marius
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10
import requests
#ex 35
print("ex 35")
from urllib.parse import urlparse

url = urlparse("https://cybercor.org/path?x=1#top")

print(url.scheme)
print(url.netloc)
print(url.path)
print(url.query)
print(url.fragment)
#ex 36
print("ex 36")

from urllib.parse import urljoin

print(urljoin(BASE_URL, "/about"))
print(urljoin(BASE_URL, "contact.html"))
print(urljoin(BASE_URL, "../index.html"))
#ex 37
print("ex 37")
import re

def extract_links(html):
    links = re.findall(r'href="([^"]+)"', html)
    return list(set(links))

html = requests.get(BASE_URL, timeout=TIMEOUT).text
print(extract_links(html))


#ex 38
print("ex 38")
from urllib.parse import urljoin, urlparse

def split_links(links, domain):
    i, e = [], []
    d = urlparse(domain).netloc

    for x in links:
        x = urljoin(domain, x)
        (i if urlparse(x).netloc == d else e).append(x)

    return i, e

print(split_links(extract_links(html), BASE_URL))
# ex 39
print("ex 39")
from html.parser import HTMLParser

class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs).get("src"))
finder = ImageFinder()
finder.feed(html)
print(finder.images)
#ex 40
print("ex 40")
import hashlib
def page_fingerprint(url):
    response = requests.get(url, timeout=TIMEOUT)
    return hashlib.sha256(response.content).hexdigest()
a = page_fingerprint(BASE_URL)
b = page_fingerprint(BASE_URL)
print(a)
print(b)
print(a == b)
#ex 41
print("ex 41")
import json
response = requests.get(BASE_URL, timeout=TIMEOUT)
with open("headers.json", "w") as file:
    json.dump(dict(response.headers), file, indent=2)
with open("headers.json") as file:
    headers = json.load(file)
print(headers["Server"])
#Ex 42
import socket
def resolve(hostname):
    return socket.gethostbyname(hostname)
print("EX 42")
print(resolve("cybercor.org"))
#ex 43
import socket
import ssl
from datetime import datetime
def cert_days_left(hostname):
    with socket.create_connection((hostname, 443)) as s:
        with ssl.create_default_context().wrap_socket(s, server_hostname=hostname) as s:
            cert = s.getpeercert()
    return (datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z") - datetime.now()).days
print("ex 43 ")
print(cert_days_left("cybercor.org"))