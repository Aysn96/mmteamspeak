# -*- coding: utf-8 -*-
"""MM Teamspeak v2 — 'KEK SELECT' Character-Select-Screen fuer mmteamspeak.de.
Parst Fotos (Base64) + Banner aus dem pristinen Original und injiziert sie
als JSON in template.html -> index.html. Fotos gehen nie verloren.

Aufruf:  python build_v2.py   (aus dem Ordner mmteamspeak.de heraus)
"""
import re, html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Quelle: die zuletzt gepflegte Live-Version (aktuellste Namen/Rollen/Fotos).
SRC = os.path.join(HERE, "..", "netlify-upload", "index.html")
SRC_FALLBACK = os.path.join(HERE, "..", "mmteamspeak_original_backup.html")
TPL = os.path.join(HERE, "template.html")
OUT = os.path.join(HERE, "index.html")

raw = open(SRC, encoding="utf-8").read()

# Neues Kartenformat (article + data-Attribute)
pat = re.compile(
    r'<article class="member[^"]*"[^>]*data-name="([^"]*)" data-role="([^"]*)" '
    r'data-rank="(\d+)">.*?<img class="photo" loading="lazy" alt="[^"]*" src="([^"]*)"', re.S)
members = [(name, role, src) for (name, role, rank, src) in pat.findall(raw)]

if not members:  # Fallback: altes Format aus dem Original-Backup
    raw = open(SRC_FALLBACK, encoding="utf-8").read()
    pat_old = re.compile(
        r'<div class="member">\s*<div class="photo-wrap"><img class="photo" loading="lazy" '
        r'alt="([^"]*)" src="([^"]*)"></div>\s*<div class="m-body"><div class="m-name">(.*?)</div>'
        r'<div class="m-role">(.*?)</div></div>\s*</div>', re.S)
    members = [(name, role, src) for (alt, src, name, role) in pat_old.findall(raw)]

bm = re.search(r'<img src="(https://[^"]+)" alt="MM Teamspeak"', raw)
BANNER = bm.group(1) if bm else ""

if len(members) != 11:
    print("WARN: nur %d Member gefunden (erwartet 11)!" % len(members))
if not BANNER:
    print("WARN: kein Banner gefunden!")

data = []
for i, (name, role, src) in enumerate(members):
    data.append({
        "rank": "%02d" % (i + 1),
        "name": html.unescape(name),
        "role": html.unescape(role),
        "src": src,
    })

tpl = open(TPL, encoding="utf-8").read()
out = tpl.replace("__BANNER__", BANNER)
out = out.replace("__MEMBER_JSON__", json.dumps(data, ensure_ascii=False))
open(OUT, "w", encoding="utf-8").write(out)
print("OK: %d Member, Banner=%s -> index.html (%d KB)" % (len(data), bool(BANNER), len(out) // 1024))
