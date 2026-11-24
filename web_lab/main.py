import argparse
import csv
from datetime import datetime
from webtools import fetch, get_title, security_headers, check_paths, site_report
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10
# EX 44
print("Titlu:", get_title(fetch(BASE_URL).text))


# EX 45
print("Antete:", security_headers(BASE_URL))


# EX 48
parser = argparse.ArgumentParser()
parser.add_argument("url", nargs="?",default=BASE_URL)
url = parser.parse_args().url


# EX 49
with open("report.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["path", "status", "checked_at"])

    for p, s in check_paths(BASE_URL):
        w.writerow([p, s, datetime.now().isoformat()])


# EX 50
site_report(BASE_URL)