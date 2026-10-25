"""Zabalí rozcestník a lekce ze src/ do samostatných HTML stránek pro GitHub Pages.

Soubory v src/ jsou psané pro Claude Artifacts — bez <!doctype>, <html>, <head>
a <body>, protože ty si Claude doplňuje sám při publikování. Tenhle skript
doplní to samé, aby stránka fungovala i jako obyčejný soubor na webu.

Použití:   py build.py
Výstup:    index.html (rozcestník) + jedna stránka na lekci
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"

# rozcestník — vždy se publikuje jako index.html
HUB = ("rozcestnik.html", "Tři interaktivní lekce o AI pro kancelářskou praxi. "
                          "Klikáním, vlastním tempem, bez instalace.")

# lekce v pořadí, v jakém jsou na rozcestníku; každá dostane adresu podle názvu souboru
LEKCE = [
    ("ai-zaklady.html", "Interaktivní průvodce základy jazykových modelů pro kancelářskou praxi. "
                        "Šest kroků, v každém něco ke zkoušení."),
    ("ai-act.html", "Co z evropského nařízení o umělé inteligenci dopadá na běžnou kancelář. "
                    "Časová osa, kvízy a praktická pravidla pro označování AI obsahu."),
    ("ai-nastroje.html", "Rozdíl mezi chatem, asistentem a agentem, čtyři velké nástroje vedle sebe "
                         "a kdy má smysl provozovat AI lokálně."),
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


def zabal(zdroj: Path, cil: Path, popis: str) -> None:
    syrove = zdroj.read_text(encoding="utf-8")
    nadpis = titulek(syrove)

    obsah = syrove
    # metatag jen pro Artifacts, na webu nemá co dělat
    obsah = re.sub(r'<meta name="claude:[^>]*>\s*', "", obsah)
    # <title> patří do <head>, ne doprostřed stránky
    obsah = re.sub(r"<title>.*?</title>\s*", "", obsah, count=1, flags=re.S)
    # fonty z hlavičky zdroje zůstanou v <head>, tělo začíná za stylopisem
    obsah = obsah.replace("</style>", "</style>\n</head>\n<body>", 1)

    cil.write_text(SKELET.format(titulek=nadpis, popis=popis, obsah=obsah), encoding="utf-8")
    print(f"OK     {cil.name:22} {nadpis}")


def build() -> None:
    for jmeno, popis, cil in [(HUB[0], HUB[1], "index.html")] + [(j, p, j) for j, p in LEKCE]:
        zdroj = SRC / jmeno
        if not zdroj.exists():
            print(f"CHYBI  {zdroj}")
            continue
        zabal(zdroj, ROOT / cil, popis)


if __name__ == "__main__":
    build()
