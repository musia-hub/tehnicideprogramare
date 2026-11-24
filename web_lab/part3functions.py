# Laborator: Importuri
#
# # Student: Adam Marius
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10
import requests
#ex 21
def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response
response = fetch(BASE_URL)
print("ex 21",response.status_code)
#ex 22
def get_status(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
print("ex 22 ",get_status(BASE_URL + "/"))
print(get_status(BASE_URL + "/robots.txt"))
print(get_status(BASE_URL + "/sitemap.xml"))
#ex 23
def fetch(url, timeout=10):
    return requests.get(url, timeout=timeout)

print("ex 23",fetch(BASE_URL).status_code)
print(fetch(BASE_URL, timeout=3).status_code)
#ex 24
def get_title(html):
    start = html.find("<title>")
    end = html.find("</title>")
    return html[start + 7:end]

response = fetch(BASE_URL)
print("ex 24 ",get_title(response.text))
#ex 25
# ex 25
def get_title(html):
    """Titlul paginii."""
    start = html.find("<title>")
    end = html.find("</title>")
    return html[start+7:end]

print("ex 25")
help(get_title)
#ex 26
def get_status(url: str) -> int:
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
# ex 26
def get_status(url: str) -> int:
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

print("ex 26", get_status(BASE_URL))
#ex 27
print("ex 27")

def page_exists(url):
    try:
        requests.get(url, timeout=TIMEOUT)
        return True
    except requests.RequestException:
        return False
print(page_exists(BASE_URL))
# Ex 28
print("ex 28")
def check_paths(base, paths):
    return {p: get_status(base + p) for p in paths}
print(check_paths(BASE_URL, ["/", "/robots.txt", "/sitemap.xml"]))
# Ex 29
print("ex 29")
def get_header(url, name, default="lipsește"):
    return requests.get(url, timeout=TIMEOUT).headers.get(name, default)

print(get_header(BASE_URL, name="Server"))
# Ex 30
print("ex 30")
def security_headers(url):
    h = requests.get(url, timeout=TIMEOUT).headers
    return {x: x in h for x in [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]}
print(security_headers(BASE_URL))
#ex 31
print("ex 31")
def score_headers(results):
    total = len(results)
    score = sum(results.values())
    return f"{score}/{total}"
print(score_headers(security_headers(BASE_URL)))
#ex 32
print("ex 32")

def fetch_robots(base):
    r = requests.get(base + "/robots.txt", timeout=TIMEOUT)
    return None if r.status_code == 404 else r.text


def disallowed_paths(robots_text):
    if robots_text is None:
        return []
    return [line.split(":", 1)[1].strip()
            for line in robots_text.splitlines()
            if line.startswith("Disallow:")]


robots = fetch_robots(BASE_URL)
print(disallowed_paths(robots))

#ex 33
print("ex 33")

def response_times(*urls):
    result = {}

    for url in urls:
        r = requests.get(url, timeout=TIMEOUT)
        result[url] = r.elapsed.total_seconds()

    return result

print(response_times(BASE_URL, ECHO_URL))
# ex 34
print("ex 34")
def log(message, **details):
    print(message, end="")
    for key, value in details.items():
        print(f" | {key}={value}", end="")
    print()
log("verificat", url=BASE_URL, status=200)