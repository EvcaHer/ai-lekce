"""Zabalí lekce ze src/ do samostatných HTML stránek pro GitHub Pages.

Soubory v src/ jsou psané pro Claude Artifacts — bez <!doctype>, <html>, <head>
a <body>, protože ty si Claude doplňuje sám při publikování. Tenhle skript
doplní to samé, aby stránka fungovala i jako obyčejný soubor na webu.

Použití:   py build.py
Výstup:    index.html (první lekce ze seznamu LEKCE) + <jmeno>.html pro ostatní
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"

# (soubor v src/, popis pro vyhledávače a náhled odkazu)
LEKCE = [
    ("ai-zaklady.html", "Interaktivní průvodce základy jazykových modelů pro kancelářskou praxi. "
                        "Šest kroků, v každém něco ke zkoušení."),
]

SKELET = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulek}</title>
<meta name="description" content="{popis}">
<meta name="author" content="Eva Hermanová">
<meta property="og:type" content="website">
<meta property="og:title" content="{titulek}">
<meta property="og:description" content="{popis}">
<meta property="og:locale" content="cs_CZ">
<style>
:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
body{{margin:0;font:14px system-ui,sans-serif}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>
{obsah}
</body>
</html>
"""


def titulek(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    return m.group(1).strip() if m else "Lekce"


def build() -> None:
    for i, (jmeno, popis) in enumerate(LEKCE):
        zdroj = SRC / jmeno
        if not zdroj.exists():
            print(f"CHYBI  {zdroj}")
            continue

        obsah = zdroj.read_text(encoding="utf-8")
        # metatag jen pro Artifacts, na webu nemá co dělat
        obsah = re.sub(r'<meta name="claude:[^>]*>\s*', "", obsah)
        # <title> patří do <head>, ne doprostřed stránky
        obsah = re.sub(r"<title>.*?</title>\s*", "", obsah, count=1, flags=re.S)
        # fonty z hlavičky zdroje zůstanou v <head>, tělo začíná za stylopisem
        obsah = obsah.replace("</style>", "</style>\n</head>\n<body>", 1)

        cil = ROOT / ("index.html" if i == 0 else jmeno)
        cil.write_text(
            SKELET.format(titulek=titulek(zdroj.read_text(encoding="utf-8")),
                          popis=popis, obsah=obsah),
            encoding="utf-8",
        )
        print(f"OK     {cil.name}  ({cil.stat().st_size // 1024} kB)")


if __name__ == "__main__":
    build()
