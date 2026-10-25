# AI lekce

Interaktivní výukové stránky o AI nástrojích pro kancelářskou praxi. Účastník si je proklikává vlastním tempem, lektor je může promítat nebo nahrát jako video.

Autorka: Eva Hermanová — školení Microsoft Office, Microsoft 365 a AI nástrojů.

## Lekce

Rozcestník se všemi lekcemi: **https://evcaher.github.io/ai-lekce/**

| Lekce | Co obsahuje |
|---|---|
| [1. Základy AI pro kancelář](https://evcaher.github.io/ai-lekce/ai-zaklady.html) | Jak model skládá odpověď, proč si vymýšlí, prompt po částech, kam ho pustit a kam ne |
| [2. AI Act bez paniky](https://evcaher.github.io/ai-lekce/ai-act.html) | Role podle nařízení, časová osa termínů, čtyři stupně rizika, zakázané praktiky, kdy se obsah musí označit |
| [3. Chat, asistent, agent](https://evcaher.github.io/ai-lekce/ai-nastroje.html) | Rozdíl mezi chatem, asistentem a agentem, čtyři velké nástroje, zdarma vs. placené vs. firemní, lokální AI |
| [4. Hlas, video, obrázek](https://evcaher.github.io/ai-lekce/ai-media.html) | Specializované aplikace na hlas, video a grafiku, profesionální portréty, prompty na obrázky, rozcestník nástrojů |

Druhá a třetí lekce obsahují údaje s trvanlivostí — termíny z AI Actu a tarify nástrojů. Obě uvádějí, ke kterému datu platí. Před dalším školením si ověřte, jestli pořád sedí.

Na konkrétní krok se dá odkázat kotvou — `#k1` až `#k6`. Hodí se, když chcete po školení poslat odkaz na jedno místo.

## Jak to je postavené

Jedna lekce = jeden soubor HTML. Žádný framework, žádný balíčkovací nástroj, žádné sledovací skripty. Jen fonty z Google Fonts.

```
src/            zdroj lekce (bez <html> a <head> — kvůli Claude Artifacts)
build.py        doplní hlavičku a vyrobí stránku pro web
index.html      vygenerovaná stránka, tu servíruje GitHub Pages
```

Dva soubory místo jednoho mají důvod: zdroj v `src/` jde beze změny publikovat jako Claude Artifact (privátní odkaz pro klienta), stejný zdroj se přes `build.py` vyrobí jako veřejná stránka. Nic se nepíše dvakrát.

## Úprava lekce

1. Upravit soubor v `src/`.
2. `py build.py`
3. `git commit` a `git push` — GitHub Pages se přegeneruje do minuty.

## Nová lekce

Přidat soubor do `src/` a zapsat ho do seznamu `LEKCE` v `build.py`. První položka v seznamu se stává `index.html`, ostatní dostanou vlastní adresu podle názvu souboru.

## Použití

Materiál je volně k nahlédnutí. Pro použití ve vlastním školení nebo jakoukoli úpravu a šíření se prosím ozvěte.
