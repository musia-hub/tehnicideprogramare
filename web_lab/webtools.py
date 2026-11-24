import requests
import socket
import ssl
import re
import json
from datetime import datetime


# EX 47
DEFAULT_HEADERS = {"User-Agent": "WebLab-Marius"}


# EX 44
def fetch(url):
    return requests.get(url, headers=DEFAULT_HEADERS)


def get_status(url):
    return fetch(url).status_code


def get_title(html):
    return html[html.find("<title>") + 7:html.find("</title>")]


def security_headers(url):
    h = fetch(url).headers
    return {
        x: h.get(x) for x in [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
            "Referrer-Policy"
        ]
    }


# EX 50
def extract_links(html):
    return list(dict.fromkeys(re.findall(r'href="([^"]+)"', html)))
def resolve(hostname):
    return socket.gethostbyname(hostname)
def cert_days_left(hostname):
    with socket.create_connection((hostname, 443)) as s:
        with ssl.create_default_context().wrap_socket(
                s, server_hostname=hostname) as s:
            d = s.getpeercert()["notAfter"]
    return int(
        (ssl.cert_time_to_seconds(d) -
         datetime.now().timestamp()) / 86400
    )
def check_paths(url):
    return [
        (p, fetch(url.rstrip("/") + p).status_code)
        for p in ["/admin", "/private"]
    ]
def site_report(url):
    r = fetch(url)
    host = r.url.split("/")[2]
    links = extract_links(r.text)
    h = security_headers(url)
    report = {
        "status": r.status_code,
        "url": r.url,
        "title": get_title(r.text),
        "ip": resolve(host),
        "redirects": [x.status_code for x in r.history],
        "security": f"{sum(bool(x) for x in h.values())}/5",
        "certificate_days": cert_days_left(host),
        "links": len(links),
        "forbidden_paths": check_paths(url)
    }
    print(report)
    with open("report.json", "w") as f:
        json.dump(report, f, indent=2)
# EX 46
if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
