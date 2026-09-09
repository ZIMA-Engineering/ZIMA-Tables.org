# Knihovna strojírenských tabulek

Repozitář obsahuje původní webovou aplikaci a celou datovou knihovnu v
[data/mechanical-tables](../data/mechanical-tables).

Import z 9. 9. 2026 pochází ze složky **04-MECHANICAL_TABLES**. Zahrnuje všech
2 806 původních souborů, včetně metadat, HTML, CSV, obrázků, PDF, CAD podkladů
a výpočtů. Hierarchie a názvy adresářů zůstávají zachovány. Nejde pouze o
adresář závitů.

## Stav validace

Doložené chyby závitových tabulek jsou opravené v aktivních HTML a ve všech
15 CSV. Aktuální audit má nulové nálezy v provedených kontrolách. Historické
tolerance a konstrukční varianty nejsou automaticky prohlášeny za shodné
s dnešními normami; přesné meze ověření stanoví protokol.

- [Výsledek kontroly závitů a rozsah ověření](validation/threads-2026-09-09.md)
- [Úplný seznam nálezů po souborech](validation/thread-findings.md)
- [Strojově čitelné nálezy](validation/thread-findings.json)
- [Původní inventář importu s SHA-256](data-import-2026-09-09.json)
- [Protokol oprav a jejich zdrojů](validation/thread-corrections.json)
- [Schémata CSV](validation/thread-export-schema.json)
- [Kontrolní součty opravených souborů](validation/thread-repair-manifest.json)

Ostatní kapitoly byly importovány beze změny; jejich technické hodnoty tento
audit neověřuje. Ani geometricky správný základní průměr není mezní výrobní
rozměr: ten závisí také na příslušné normě, tolerančním poli a dalších
předepsaných podmínkách.

## Použití dat

Kořenem knihovny pro ZIMA-CAD-Parts je **data/mechanical-tables**. U webové
aplikace tento adresář použijte jako datový zdroj v **ZWP_DATA_SOURCES** podle
konfiguračního rozhraní instalované verze
[ZIMA-WEB-Parts](https://github.com/ZIMA-Engineering/ZIMA-WEB-Parts).

Soubor **zima_tables/local_settings.py** zůstává lokální konfigurací. Import
dat sám neinstaluje ani nespouští Django a nezveřejňuje webovou službu.
Instalační požadavky původní aplikace v README jsou historické; tento import
není aktualizací jejího frameworku.

Všech 15 závitových CSV je nyní skutečná plochá tabulka v UTF-8, oddělená
tabulátory, bez záhlaví. Sloučené buňky HTML jsou v exportu zopakované.
Schéma uvádí jednotky i případné vícehodnotové buňky. Tabulka drážek má
nově 12 sloupců: vnější a vnitřní poloměr jsou oddělené. Ostatní CSV
v dalších kapitolách nebyla tímto auditem opravována.

## Opakování auditu

Kontrolní nástroj potřebuje pouze Python 3.8 nebo novější, bez instalace
knihoven a bez síťového připojení:

    python tools/thread_audit.py --json docs/validation/thread-findings.json --markdown docs/validation/thread-findings.md
    python -m unittest discover -s tools -p test_thread_audit.py -v

Audit lze spustit i na jiné kopii knihovny:

    python tools/thread_audit.py --root "/cesta/ke/knihovne" --json audit.json

Návratový kód auditu **1** znamená chyby, nejasnosti nebo vadný export; nejde o pád
programu. Kód **0** znamená nepřítomnost těchto nálezů v provedených kontrolách,
nikoli úplnou certifikaci. Kód **2** znamená chybný vstup.
Testy kontrolují správnost nástroje i opravená data a záměrně poškozené vstupy.

Původní soubory jsou v .gitattributes označeny -text, aby Git při přenosu
mezi Windows a Linuxem nezměnil jejich konce řádků. Prázdné složky jsou
uvedeny v inventáři; případné soubory .gitkeep slouží jen k jejich
zachování v Gitu.

## Další úpravy

Oprava hodnoty musí uvádět původní a novou hodnotu, její význam a zdroj.
Nejprve se ověřuje označení závitu, jednotka a rozteč; až potom odvozené
průměry. Oprava se musí promítnout také do odpovídajících exportů a případných
duplicitních HTML. Původní vydání norem u tolerancí, výběhů a drážek je nutné
doložit před hromadnou změnou těchto tabulek.
## Dlouhé cesty ve Windows

Knihovna zachovává dlouhé původní názvy. Při klonování použijte krátkou
cílovou cestu a zapnutou podporu dlouhých cest Gitu, například:

    git -c core.longpaths=true clone https://github.com/ZIMA-Engineering/ZIMA-Tables.org.git C:\ZIMA-Tables
    git -C C:\ZIMA-Tables config core.longpaths true

Jde o nastavení konkrétního klonu. Není potřeba měnit globální nastavení
ostatních repozitářů.
