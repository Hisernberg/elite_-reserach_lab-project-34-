#!/usr/bin/env python3
"""
Verify DOI fields in factuality_clinical_ts_bangla_215refs.bib or a Zotero export.

Usage:
  python verify_dois_crossref.py factuality_clinical_ts_bangla_215refs.bib

Output:
  verify_dois_log.csv

Requires internet access.
"""
import csv, re, sys, time, urllib.request, urllib.parse, json

path = sys.argv[1] if len(sys.argv) > 1 else "factuality_clinical_ts_bangla_215refs.bib"
text = open(path, encoding="utf-8").read()
entries = re.split(r"\n(?=@)", text)
rows = []

def get_field(entry, field):
    m = re.search(field + r"\s*=\s*\{(.+?)\}\s*,?", entry, flags=re.I|re.S)
    if not m: return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()

for e in entries:
    key_match = re.match(r"@\w+\{([^,]+),", e.strip())
    if not key_match: 
        continue
    key = key_match.group(1)
    title = get_field(e, "title")
    doi = get_field(e, "doi")
    if not doi:
        rows.append([key, title, "", "NO_DOI", "", "No DOI field; verify stable URL/arXiv/ACL manually."])
        continue
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ReviewDOIVerifier/1.0 (mailto:your-email@example.com)"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.load(resp)
        cr_title = (data.get("message", {}).get("title") or [""])[0]
        rows.append([key, title, doi, "OK", cr_title, ""])
    except Exception as ex:
        rows.append([key, title, doi, "FAIL", "", repr(ex)])
    time.sleep(1.0)

with open("verify_dois_log.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["citekey","local_title","doi","status","crossref_title","error_or_note"])
    w.writerows(rows)

print(f"Wrote verify_dois_log.csv with {len(rows)} rows.")
