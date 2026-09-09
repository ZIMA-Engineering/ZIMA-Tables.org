> Historický stav před opravami; data odpovídají commitu 9ad27d1. Aktuální stav: [protokol oprav](../threads-2026-09-09.md).

# Kontrolní nálezy závitových tabulek

Automatický výstup čtecího auditu. Hodnoty nebyly změněny. Metodika a meze ověření: [protokol](threads-2026-09-09.md).

Čísla řádků HTML odkazují na zdroj; u CSV jde u některých exportů o pořadí datových řádků. Výpočetní shoda sama nepotvrzuje normovou přípustnost rozměrové řady.

## Potvrzené chyby a vnitřní rozpory

Počet nálezů: 83.

### [01-Zavity ISO](../../../data/mechanical-tables/03-ZAVITY/01-Zavity%20ISO/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0001 / 42 | Záhlaví / text | Jednotky vzorců s n | 0,866025404/n | — | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length). Pro n závitů na palec platí P[mm]=25,4/n. Výrazy s 1/n bez 25,4 dávají palce; doplnit jednotky všech pěti vzorců. |
| THR-0002 / 42 | Záhlaví / text | Vzorec výšky H | 0,5.n | 0,5 × P | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [01-rozmery pro M1 az M18](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0003 / 56 | M 1,1 | d3 [mm] | 0,739 | 0.793 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0004 / 149 | M 2,2 | P hrubé řady | 0,4 | 0.45 | [Gühring, Technical section, PDF s. 38](https://guehring.com/wp-content/downloads/EN/Catalogues-Special-Programmes/GUE_technical-section_EN.pdf).  |
| THR-0005 / 188 | M 3×0,24 | Rozteč v označení | M 3×0,24 | M 3 × 0.35 | Vnitřní konzistence uživatelských dat / struktura HTML. Rozteč v označení nesouhlasí se sloupcem P; všechny tři průměry odpovídají sloupci P. |
| THR-0006 / 311 | M 7×0,5 | D2 [mm] | 5,675 | 6.675 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0007 / 343 | M 8×0,5 | D2 [mm] | 6,675 | 7.675 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0008 / 632 | M 18×2 | d3 [mm] | 14,546 | 15.546 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [02-rozmery pro M20 az M48](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/02-rozmery%20pro%20M20%20az%20M48/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0014 / 41 | M 20 | d3 [mm] | 26,933 | 16.933 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0015 / 161 | M 24×1 | d3 [mm] | 22,733 | 22.773 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0016 / 217 | M 27×2 | d3 [mm] | 25,546 | 24.546 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0017 / 305 | M 30×1 | d3 [mm] | 27,773 | 28.773 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [03-rozmery pro M50 az M82](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/03-rozmery%20pro%20M50%20az%20M82/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0018 / 249 | M 60×2 | d3 [mm] | 57,54 | 57.546 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0019 / 513 | M 72×1 | d3 [mm] | 70,779 | 70.773 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0020 / 593 | M 76×1 | d3 [mm] | 73,773 | 74.773 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [04-rozmery pro M85 az M175](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/04-rozmery%20pro%20M85%20az%20M175/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0021 / 56 | M 85×3 | d3 [mm] | 71,319 | 81.319 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0022 / 64 | M 85×2 | d3 [mm] | 85,546 | 82.546 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0023 / 127 | M 95×4 | D2 [mm] | 82,402 | 92.402 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0024 / 312 | M 120×3 | d3 [mm] | 113,319 | 116.319 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0025 / 430 | M 135×2 | D1 [mm] | 132,735 | 132.835 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [05-rozmery pro M180 az M300](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/05-rozmery%20pro%20M180%20az%20M300/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0030 / 159 | M 200×6 | d3 [mm] | 196,639 | 192.639 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0031 / 175 | M 200×3 | d3 [mm] | 192,319 | 196.319 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0035 / 527 | M 270×6 | d3 [mm] | 252,639 | 262.639 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0037 / 615 | M 290×4 | d3 [mm] | 290,093 | 285.093 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [02-Metricke zavity ISO - pro jemnou mechaniku a optiku](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/02-Metricke%20zavity%20ISO%20-%20pro%20jemnou%20mechaniku%20a%20optiku/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0039 / 164 | M 7 × 035 | P [mm] | 035 | 0.35 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf). Ostatní průměry odpovídají P=0,35 mm. |
| THR-0040 / 854 | M 28,5 × 0,5 | d3 [mm] | 27,877 | 27.887 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0041 / 939 | M 32 × 1 | D2 [mm] | 32,350 | 31.35 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0042 / 963 | M 32,5 × 0,5 | d = jmenovitý průměr [mm] | 23,500 | 32.5 | Vnitřní konzistence uživatelských dat / struktura HTML.  |
| THR-0043 / 964 | M 32,5 × 0,5 | D2 [mm] | 23,175 | 32.175 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0044 / 1042 | M 35 × 0,75 | D1 [mm] | 34,1188 | 34.188 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0045 / 1153 | M 38,5 × 0,5 | D1 [mm] | 39,959 | 37.959 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0046 / 1161 | M 39 × 0,75 | D2 [mm] | 28,513 | 38.513 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0048 / 1392 | M 46 × 1 | D1 [mm] | 44917 | 44.917 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0049 / 1426 | M 47 × 1,5 | D1 [mm] | 45,959 | 45.376 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0050 / 1427 | M 47 × 1,5 | d3 [mm] | 45,887 | 45.16 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0051 / 1570 | M 51 × 1 | D1 [mm] | 49,717 | 49.917 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0052 / 1610 | M 52 × 0,75 | d = jmenovitý průměr [mm] | 42,000 | 52.0 | Vnitřní konzistence uživatelských dat / struktura HTML.  |
| THR-0053 / 1687 | M 54 × 0,75 | D2 [mm] | 53513 | 53.513 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0054 / 1780 | M 57 × 0,5 | D1 [mm] | 46,459 | 56.459 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0055 / 1781 | M 57 × 0,5 | d3 [mm] | 46,387 | 56.387 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0056 / 2333 | M 92 × 1 | d3 [mm] | 90,778 | 90.773 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0057 / 2442 | M 101 × 1 | D1 [mm] | 99,947 | 99.917 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0058 / 2527 | M 106 × 1 | D1 [mm] | 104,517 | 104.917 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0059 / 2700 | M 130 × 1 | d3 [mm] | 128,778 | 128.773 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [03-Palcove zavity ISO](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0065 / 50 | MINOR DIA | Popis průměru | Mezní rozměry středního průměru závitu | Mezní rozměry malého průměru závitu | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |

### [01-Palcove zavity ISO - prehled](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/01-Palcove%20zavity%20ISO%20-%20prehled/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0067 / 937 | 35/8 | d [in], podle smíšeného čísla | 3,3750 | 3.625 | Vnitřní konzistence uživatelských dat / struktura HTML.  |

### [02-Palcove zavity ISO - zakladni rozmery](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/02-Palcove%20zavity%20ISO%20-%20zakladni%20rozmery/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0068 / 39 | Záhlaví | Jednotka D2/D1 | [mm] | [in] | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf). Hodnoty jsou základní průměry v palcích. |
| THR-0069 / 40 | Záhlaví | Jednotka D2/D1 | [mm] | [in] | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf). Hodnoty jsou základní průměry v palcích. |
| THR-0071 / 212 | No.8-36 UNF | d [mm] | 4,1565 | 4.1656 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0073 / 517 | 1/2 - 28 UNEF | D2 [in] | 0.4784 | 0.4768 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0075 / 1099 | 1 1/16 - 8 UN 8 | D1 [in] | 1.9272 | 0.9272 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0076 / 1110 | 1 1/16 - 12 UN 12 | D1 [in] | 1.9723 | 0.9723 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0077 / 1121 | 1 1/16 - 16 UN 16 | D1 [in] | 1.9948 | 0.9948 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0078 / 1389 | 1 5/16 - 8 UN 8 | D1 [in] | 1.7772 | 1.1772 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0092 / 1967 | 1 13/16 - 8 UN 8 | d [mm] | 16,0380 | 46.0375 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0095 / 1999 | 1 13/16 - 20 UN 20 | d [in] | 1.8750 | 1.8125 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0097 / 2025 | 1 7/8 - 8 UN 8 | D1 [in] | 1.7379 | 1.7397 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0098 / 2170 | 2 1/8 - 20 UN 20 | D1 [in] | 0.0709 | 2.0709 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0099 / 2538 | 2 7/8 - 12 UN 12 | D2 [in] | 2.8109 | 2.8209 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0100 / 2560 | 2 7/8 - 20 UN 20 | D2 [in] | 8.8425 | 2.8425 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0101 / 2572 | 3 - 4 UNC | D2 [in] | 2.9376 | 2.8376 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0102 / 2696 | 3 1/4 - 4 UNC | D1 [in] | 3.9794 | 2.9794 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0103 / 2718 | 3 1/4 - 8 UN 8 | D1 [in] | 3.1174 | 3.1147 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0104 / 2931 | 3 7/8 - 6 UN 6 | D1 [in] | 3.9646 | 3.6946 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0105 / 3187 | 4 3/8 - 16 UN 16 | D2 [in] | 4.3349 | 4.3344 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0106 / 3603 | 5 3/8 - 6 UN 6 | D1 [in] | 5.1956 | 5.1946 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |

### [04-Whitworthovy zavity](../../../data/mechanical-tables/03-ZAVITY/04-Whitworthovy%20zavity/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0109 / 134 | W 9/16 | Počet závitů na palec | 11 | 12 | [VÖLKEL, řady BSW](https://voelkel.com/media/4e/69/b8/1709295983/VD%2023%20DE-EN.pdf).  |
| THR-0110 / 149 | W 5/8 | Počet závitů na palec | 10 | 11 | [VÖLKEL, řady BSW](https://voelkel.com/media/4e/69/b8/1709295983/VD%2023%20DE-EN.pdf).  |
| THR-0111 / 164 | W 3/4 | Počet závitů na palec | 9 | 10 | [VÖLKEL, řady BSW](https://voelkel.com/media/4e/69/b8/1709295983/VD%2023%20DE-EN.pdf).  |

### [02-Rozmery trubkovĂ˝ch zavitu podle ISO 228 pro spoje netesnici mezi boky](../../../data/mechanical-tables/03-ZAVITY/05-Trubkove%20zavity%20ISO/02-Rozmery%20trubkov%C4%82%CB%9Dch%20zavitu%20podle%20ISO%20228%20pro%20spoje%20netesnici%20mezi%20boky/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0115 / 25 | Záhlaví | rowspan záhlaví | Závit | 4 | Vnitřní konzistence uživatelských dat / struktura HTML. Záhlaví má čtyři řádky; přesah posouvá datové buňky. |
| THR-0116 / 113 | G5/8 | D1 [mm] | 20,581 | 20.587 | [ISO 228-1:2000, tab. 1](https://cdn.standards.iteh.ai/samples/33777/842b7c5409454ceba69c7dad9c308be1/ISO-228-1-2000.pdf).  |

### [01-Lichobeznikove zavity - zakladni rozmery](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/01-Lichobeznikove%20zavity%20-%20zakladni%20rozmery/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0117 / 42 | Záhlaví | Počet chodů n | 5 | 6 | [ISO 2901:2016, čl. 6 a tab. 2](https://cdn.standards.iteh.ai/samples/68337/c87112d8e3dc487c95fd964d13101ca4/ISO-2901-2016.pdf). Stoupání v těchto sloupcích odpovídají n=6 a n=8. |
| THR-0118 / 43 | Záhlaví | Počet chodů n | 6 | 8 | [ISO 2901:2016, čl. 6 a tab. 2](https://cdn.standards.iteh.ai/samples/68337/c87112d8e3dc487c95fd964d13101ca4/ISO-2901-2016.pdf). Stoupání v těchto sloupcích odpovídají n=6 a n=8. |
| THR-0119 / 573 | Tr 28 × 4 | Označení | Tr 28 × 4 | Tr 28 × 3 | Vnitřní konzistence uživatelských dat / struktura HTML. Rozteč a označení musejí popisovat stejný závit. |
| THR-0120 / 1053 | Tr 44 × 12 | Ph pro 3 chodů [mm] | 32 | 36.0 | [ISO 2901:2016, čl. 6 a tab. 2](https://cdn.standards.iteh.ai/samples/68337/c87112d8e3dc487c95fd964d13101ca4/ISO-2901-2016.pdf).  |
| THR-0121 / 1102 | Tr 48 × 12 | Ph pro 3 chodů [mm] | 32 | 36.0 | [ISO 2901:2016, čl. 6 a tab. 2](https://cdn.standards.iteh.ai/samples/68337/c87112d8e3dc487c95fd964d13101ca4/ISO-2901-2016.pdf).  |
| THR-0122 / 1864 | Tr 180 × 18 | Ph pro 1 chodů [mm] | 16 | 18.0 | [ISO 2901:2016, čl. 6 a tab. 2](https://cdn.standards.iteh.ai/samples/68337/c87112d8e3dc487c95fd964d13101ca4/ISO-2901-2016.pdf).  |

### [01-Lichobeznikove zavity - zakladni rozmery](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/01-Lichobeznikove%20zavity%20-%20zakladni%20rozmery/0000-index/tabulka.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0123 / 29 | (('number', 26.0), ('number', 5.0)) | CSV / HTML rozdíl | 5: 24,500 / 23,500; 6: 22,500 / 20,500; 7: 23,000 / 21,000 | — | [ISO 2901:2016, čl. 6 a tab. 2](https://cdn.standards.iteh.ai/samples/68337/c87112d8e3dc487c95fd964d13101ca4/ISO-2901-2016.pdf). HTML: 03-ZAVITY/06-Lichobeznikove zavity/01-Lichobeznikove zavity - zakladni rozmery/0000-index/index_cs.html:485. Řádek CSV zde znamená pořadí datového řádku. |

### [07-Zvlastni zavity uzivane na jizdnich kolech](../../../data/mechanical-tables/03-ZAVITY/07-Zvlastni%20zavity%20uzivane%20na%20jizdnich%20kolech/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0124 / 73 | 7,9 × 56 | Označení | 7,9 × 56 | 7,9 × 26 | [VÖLKEL, FG/BSC](https://voelkel.com/media/05/ac/15/1658319338/14_Information%20Technique_Diam%C3%A8tre%20axes.pdf).  |
| THR-0125 / 74 | 7,9 × 56 | Počet závitů na palec | 56 | 26 | [VÖLKEL, FG/BSC](https://voelkel.com/media/05/ac/15/1658319338/14_Information%20Technique_Diam%C3%A8tre%20axes.pdf).  |
| THR-0128 / 123 | Záhlaví / text | Jednotka úhlu | 55°C | 55° | Vnitřní konzistence uživatelských dat / struktura HTML.  |
| THR-0129 / 169 | Záhlaví / text | Číslo normy | ISO 6669 | ISO 6696 | [ISO 6696:1989](https://www.iso.org/standard/13131.html).  |

### [08-Vybehy a zkoseni zavitu](../../../data/mechanical-tables/03-ZAVITY/08-Vybehy%20a%20zkoseni%20zavitu/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0140 / 212 | P=1,0 | Délka výběhu musí být kladná | -1,5 | — | Vnitřní konzistence uživatelských dat / struktura HTML. Záporná délka je chybná. Správnou kladnou hodnotu určit podle původní normy; DIN 76-1:2016 uvádí 1,25 mm. |

## Odchylky v posledních místech

Počet nálezů: 31.

### [04-rozmery pro M85 az M175](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/04-rozmery%20pro%20M85%20az%20M175/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0026 / 518 | M 150×6 | D1 [mm] | 143,506 | 143.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0027 / 582 | M 160×6 | D1 [mm] | 153,506 | 153.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0028 / 638 | M 170×6 | D1 [mm] | 163,506 | 163.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [05-rozmery pro M180 az M300](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/05-rozmery%20pro%20M180%20az%20M300/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0029 / 45 | M 180×6 | D1 [mm] | 173,506 | 173.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0032 / 437 | M 250×6 | D1 [mm] | 243,506 | 243.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0033 / 485 | M 260×6 | D1 [mm] | 253,506 | 253.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0034 / 525 | M 270×6 | D1 [mm] | 263,506 | 263.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |
| THR-0036 / 565 | M 280×6 | D1 [mm] | 273,506 | 273.505 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [02-Metricke zavity ISO - pro jemnou mechaniku a optiku](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/02-Metricke%20zavity%20ISO%20-%20pro%20jemnou%20mechaniku%20a%20optiku/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0047 / 1222 | M 41 × 1,5 | D1 [mm] | 39,375 | 39.376 | [ISO 724:2023, čl. 5](https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf).  |

### [02-Palcove zavity ISO - zakladni rozmery](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/02-Palcove%20zavity%20ISO%20-%20zakladni%20rozmery/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0070 / 210 | No.8-36 UNF | P [mm] | 0,7055 | 0.7056 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0072 / 237 | No.10-32 UNF | D1 [in] | 0.1561 | 0.1562 | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf).  |
| THR-0074 / 615 | 5/8 - 11 UNC | P [mm] | 2,3090 | 2.3091 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0079 / 1688 | 1 9/16 - 6 UN 6 | d [mm] | 39,6880 | 39.6875 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0080 / 1699 | 1 9/16 - 8 UN 8 | d [mm] | 39,6880 | 39.6875 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0081 / 1710 | 1 9/16 - 12 UN 12 | d [mm] | 39,6880 | 39.6875 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0082 / 1721 | 1 9/16 - 16 UN 16 | d [mm] | 39,6880 | 39.6875 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0083 / 1732 | 1 9/16 - 18 UNEF | d [mm] | 39,6880 | 39.6875 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0084 / 1743 | 1 9/16 - 20 UN 20 | d [mm] | 39,6880 | 39.6875 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0085 / 1822 | 1 11/16 - 6 UN 6 | d [mm] | 42,8630 | 42.8625 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0086 / 1833 | 1 11/16 - 8 UN 8 | d [mm] | 42,8630 | 42.8625 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0087 / 1844 | 1 11/16 - 12 UN 12 | d [mm] | 42,8630 | 42.8625 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0088 / 1855 | 1 11/16 - 16 UN 16 | d [mm] | 42,8630 | 42.8625 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0089 / 1866 | 1 11/16 - 18 UNEF | d [mm] | 42,8630 | 42.8625 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0090 / 1877 | 1 11/16 - 20 UN 20 | d [mm] | 42,8630 | 42.8625 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0091 / 1956 | 1 13/16 - 6 UN 6 | d [mm] | 46,0380 | 46.0375 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0093 / 1978 | 1 13/16 - 12 UN 12 | d [mm] | 46,0380 | 46.0375 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0094 / 1989 | 1 13/16 - 16 UN 16 | d [mm] | 46,0380 | 46.0375 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0096 / 2000 | 1 13/16 - 20 UN 20 | d [mm] | 46,0380 | 46.0375 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |

### [04-Whitworthovy zavity](../../../data/mechanical-tables/03-ZAVITY/04-Whitworthovy%20zavity/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0113 / 435 | W 4 | P [mm] | 8,468 | 8.467 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |

### [07-Zvlastni zavity uzivane na jizdnich kolech](../../../data/mechanical-tables/03-ZAVITY/07-Zvlastni%20zavity%20uzivane%20na%20jizdnich%20kolech/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0126 / 105 | *25,4 × 24 | P [mm] | 1,0580 | 1.0583 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |
| THR-0127 / 115 | *34,7 × 24 | P [mm] | 1,0580 | 1.0583 | [NIST, převod palce](https://www.nist.gov/pml/owm/si-units-length).  |

## Rozdíly proti DIN 76-1:2016; původní norma neurčena

Počet nálezů: 79.

### [08-Vybehy a zkoseni zavitu](../../../data/mechanical-tables/03-ZAVITY/08-Vybehy%20a%20zkoseni%20zavitu/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0130 / 85 | P=0,3 | x1 DIN | 0,8 | 0.75 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0131 / 99 | P=0,35 | x1 DIN | 1 | 0.9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0132 / 100 | P=0,35 | x2 DIN | 0,5 | 0.45 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0133 / 127 | P=0,45 | x1 DIN | 1,2 | 1.1 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0134 / 141 | P=0,5 | x1 DIN | 1,2 | 1.25 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0135 / 142 | P=0,5 | x2 DIN | 0,8 | 0.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0136 / 156 | P=0,6 | x2 DIN | 0,8 | 0.75 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0137 / 169 | P=0,7 | x1 DIN | 1,7 | 1.75 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0138 / 170 | P=0,7 | x2 DIN | 1 | 0.9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0139 / 183 | P=0,75 | x1 DIN | 1,7 | 1.9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0141 / 212 | P=1,0 | x2 DIN | -1,5 | 1.25 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0142 / 225 | P=1,25 | x1 DIN | 2,5 | 3.2 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0143 / 226 | P=1,25 | x2 DIN | 1,5 | 1.6 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0144 / 239 | P=1,5 | x1 DIN | 4 | 3.8 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0145 / 240 | P=1,5 | x2 DIN | 2 | 1.9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0146 / 253 | P=1,75 | x1 DIN | 4 | 4.3 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0147 / 254 | P=1,75 | x2 DIN | 2 | 2.2 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0148 / 281 | P=2,5 | x1 DIN | 7 | 6.3 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0149 / 282 | P=2,5 | x2 DIN | 3 | 3.2 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0150 / 295 | P=3 | x1 DIN | 8 | 7.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0151 / 296 | P=3 | x2 DIN | 4 | 3.8 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0152 / 309 | P=3,5 | x1 DIN | 8 | 9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0153 / 310 | P=3,5 | x2 DIN | 4 | 4.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0154 / 337 | P=4,5 | x1 DIN | 12 | 11 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0155 / 338 | P=4,5 | x2 DIN | 6 | 5.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0156 / 351 | P=5 | x1 DIN | 12 | 12.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0157 / 352 | P=5 | x2 DIN | 6 | 6.3 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0158 / 365 | P=5,5 | x1 DIN | 15 | 14 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0159 / 366 | P=5,5 | x2 DIN | 8 | 7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0160 / 380 | P=6 | x2 DIN | 8 | 7.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |

### [09-Drazky za zavity](../../../data/mechanical-tables/03-ZAVITY/09-Drazky%20za%20zavity/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0161 / 56 | P=0,2 | a / g1 DIN | 0,32 | 0.45 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0162 / 57 | P=0,2 | b / g2 DIN | 0,6 | 0.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0163 / 70 | P=0,25 | a / g1 DIN | 0,4 | 0.55 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0164 / 71 | P=0,25 | b / g2 DIN | 0,8 | 0.9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0165 / 84 | P=0,3 | a / g1 DIN | 0,5 | 0.6 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0166 / 85 | P=0,3 | b / g2 DIN | 1 | 1.05 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0167 / 98 | P=0,35 | a / g1 DIN | 0,6 | 0.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0168 / 99 | P=0,35 | b / g2 DIN | 1 | 1.2 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0169 / 112 | P=0,4 | a / g1 DIN | 0,6 | 0.8 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0170 / 113 | P=0,4 | b / g2 DIN | 1,2 | 1.4 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0171 / 126 | P=0,45 | a / g1 DIN | 0,7 | 1 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0172 / 127 | P=0,45 | b / g2 DIN | 1,5 | 1.6 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0173 / 140 | P=0,5 | a / g1 DIN | 0,8 | 1.1 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0174 / 141 | P=0,5 | b / g2 DIN | 1,5 | 1.75 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0175 / 154 | P=0,6 | a / g1 DIN | 0,9 | 1.2 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0176 / 155 | P=0,6 | b / g2 DIN | 2 | 2.1 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0177 / 168 | P=0,7 | a / g1 DIN | 1,1 | 1.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0178 / 169 | P=0,7 | b / g2 DIN | 2 | 2.45 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0179 / 182 | P=0,75 | a / g1 DIN | 1,2 | 1.6 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0180 / 183 | P=0,75 | b / g2 DIN | 2,5 | 2.6 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0181 / 196 | P=0,8 | a / g1 DIN | 1,3 | 1.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0182 / 197 | P=0,8 | b / g2 DIN | 2,5 | 2.8 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0183 / 210 | P=1,0 | a / g1 DIN | 1,6 | 2.1 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0184 / 211 | P=1,0 | b / g2 DIN | 3 | 3.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0185 / 224 | P=1,25 | a / g1 DIN | 2,0 | 2.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0186 / 225 | P=1,25 | b / g2 DIN | 4 | 4.4 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0187 / 237 | P=1,5 | dd / dg DIN | d - 2,5 | d - 2.3 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0188 / 238 | P=1,5 | a / g1 DIN | 2,5 | 3.2 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0189 / 239 | P=1,5 | b / g2 DIN | 4,5 | 5.2 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0190 / 252 | P=1,75 | a / g1 DIN | 3,0 | 3.9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0191 / 253 | P=1,75 | b / g2 DIN | 6 | 6.1 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0192 / 266 | P=2 | a / g1 DIN | 3,4 | 4.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0193 / 267 | P=2 | b / g2 DIN | 6 | 7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0194 / 280 | P=2,5 | a / g1 DIN | 4,4 | 5.6 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0195 / 281 | P=2,5 | b / g2 DIN | 7,5 | 8.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0196 / 294 | P=3 | a / g1 DIN | 5,2 | 6.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0197 / 295 | P=3 | b / g2 DIN | 10 | 10.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0198 / 308 | P=3,5 | a / g1 DIN | 6,2 | 7.7 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0199 / 309 | P=3,5 | b / g2 DIN | 10 | 12 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0200 / 322 | P=4 | a / g1 DIN | 7 | 9 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0201 / 323 | P=4 | b / g2 DIN | 12,5 | 14 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0202 / 336 | P=4,5 | a / g1 DIN | 8 | 10.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0203 / 337 | P=4,5 | b / g2 DIN | 15 | 16 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0204 / 350 | P=5 | a / g1 DIN | 9 | 11.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0205 / 351 | P=5 | b / g2 DIN | 15 | 17.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0206 / 364 | P=5,5 | a / g1 DIN | 11 | 12.5 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0207 / 365 | P=5,5 | b / g2 DIN | 18 | 19 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0208 / 378 | P=6 | a / g1 DIN | 11 | 14 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |
| THR-0209 / 379 | P=6 | b / g2 DIN | 18 | 21 | [DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27](https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf).  |

## Nejasné údaje k dořešení

Počet nálezů: 8.

### [02-Metricke zavity ISO - pro jemnou mechaniku a optiku](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/02-Metricke%20zavity%20ISO%20-%20pro%20jemnou%20mechaniku%20a%20optiku/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0038 / 62 | M 4,5 × 0,35 | Rozpor jmenovitého a velkého průměru | 4,5 | — | Vnitřní konzistence uživatelských dat / struktura HTML. Označení uvádí 4,5 mm, všechny čtyři průměry odpovídají 5 mm. Nejprve určit správné označení. |

### [03-Metricke zavity ISO - tolerovani](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0060 / 447 | Záhlaví / text | Toleranční značka | 4j6k | — | Vnitřní konzistence uživatelských dat / struktura HTML. Podezřelý zápis; bez původní ČSN pro přechodná uložení nenavrhuji náhradu. |
| THR-0061 / 519 | Záhlaví / text | Toleranční značka | 4H6J | — | Vnitřní konzistence uživatelských dat / struktura HTML. Podezřelý zápis; bez původní ČSN pro přechodná uložení nenavrhuji náhradu. |

### [05-Tolerancni znacky pro ulozeni prechodna](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/05-Tolerancni%20znacky%20pro%20ulozeni%20prechodna/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0062 / 52 | Záhlaví / text | Toleranční značka | 4j6k | — | Vnitřní konzistence uživatelských dat / struktura HTML. Podezřelý zápis; bez původní ČSN pro přechodná uložení nenavrhuji náhradu. |

### [06-Kombinace tolerancnich poli pro ulozeni prechodna](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/06-Kombinace%20tolerancnich%20poli%20pro%20ulozeni%20prechodna/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0063 / 58 | Záhlaví / text | Toleranční značka | 4H6J | — | Vnitřní konzistence uživatelských dat / struktura HTML. Podezřelý zápis; bez původní ČSN pro přechodná uložení nenavrhuji náhradu. |

### [03-Palcove zavity ISO](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0064 / 36 | Záhlaví / text | Neslučitelný příklad PD | PD 0.4485 - 0.4422 | — | [ISO 725:2009, čl. 3](https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf). Obě meze jsou větší než velký průměr 1/4 in; nelze určit, zda je špatné označení závitu nebo jeho meze. |

### [01-Palcove zavity ISO - prehled](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/01-Palcove%20zavity%20ISO%20-%20prehled/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0066 / 936 | Záhlaví / text | Nejednoznačný zápis smíšených čísel | <th>35/8</th> | 3 5/8 | Vnitřní konzistence uživatelských dat / struktura HTML. Od 1 in jsou zápisy jako 11/16 a 35/8 bez mezery. V této části znamenají 1 1/16 a 3 5/8; upravit celou řadu. |

### [04-Whitworthovy zavity](../../../data/mechanical-tables/03-ZAVITY/04-Whitworthovy%20zavity/0000-index/index_cs.html)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0112 / 377 | W 3 | Dolní mezní úchylka d | -90 -100 | — | Vnitřní konzistence uživatelských dat / struktura HTML. -100 µm přerušuje řadu -950, -1050 µm; ověřit chybějící nulu podle původní normy. |

## Formát a strojová použitelnost

Počet nálezů: 8.

### [01-rozmery pro M1 az M18](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table1.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0009 / 1 | table1.csv | Soubor s příponou CSV obsahuje HTML | HTML | — | Vnitřní konzistence uživatelských dat / struktura HTML. Čísla byla porovnána s HTML. |

### [01-rozmery pro M1 az M18](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table2.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0010 / 1 | table2.csv | Soubor s příponou CSV obsahuje HTML | HTML | — | Vnitřní konzistence uživatelských dat / struktura HTML. Čísla byla porovnána s HTML. |

### [01-rozmery pro M1 az M18](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table3.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0011 / 1 | table3.csv | Soubor s příponou CSV obsahuje HTML | HTML | — | Vnitřní konzistence uživatelských dat / struktura HTML. Čísla byla porovnána s HTML. |

### [01-rozmery pro M1 az M18](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table4.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0012 / 1 | table4.csv | Nepravidelný formát exportu | Víceřádkové záhlaví, oddělovač \| | — | Vnitřní konzistence uživatelských dat / struktura HTML.  |

### [01-rozmery pro M1 az M18](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table5.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0013 / 1 | table5.csv | Soubor s příponou CSV obsahuje HTML | HTML | — | Vnitřní konzistence uživatelských dat / struktura HTML. Čísla byla porovnána s HTML. |

### [02-Palcove zavity ISO - zakladni rozmery](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/02-Palcove%20zavity%20ISO%20-%20zakladni%20rozmery/0000-index/tabulka.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0107 / 76 | CSV | Nečitelný řádek exportu | 7/8 \| UNC 9 \| 2,8222 \| 0.8750 \| 22,2250 \| 0.8028 \| 0.7547 \| 7/8 - 9 UNC | — | Vnitřní konzistence uživatelských dat / struktura HTML. Řádek má 8 polí; tato tabulka vyžaduje 9. Chybí oddělovač nebo je sloučen text sousedních buněk. |
| THR-0108 / 77 | CSV | Nečitelný řádek exportu | 7/8 \| UN 12 \| 12 \| 2,1167 \| 0.8750 \| 22,2250 \| 0.8209 \| 0.7848q7/8 - 12 UN 12 | — | Vnitřní konzistence uživatelských dat / struktura HTML. Řádek má 8 polí; tato tabulka vyžaduje 9. Chybí oddělovač nebo je sloučen text sousedních buněk. |

### [01-Rozmery trubkovych zavitu podle ISO 7 pro spoje tesnici mezi boky](../../../data/mechanical-tables/03-ZAVITY/05-Trubkove%20zavity%20ISO/01-Rozmery%20trubkovych%20zavitu%20podle%20ISO%207%20pro%20spoje%20tesnici%20mezi%20boky/0000-index/tabulka.csv)

| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |
|---|---|---|---|---|---|
| THR-0114 / 1 | tabulka.csv | Neúplné řádky CSV po sloučených buňkách | [4, 5, 6, 7, 8, 11] | — | Vnitřní konzistence uživatelských dat / struktura HTML. Nejde o plochou tabulku: bez HTML nelze bezpečně obnovit význam některých polí. |

## Pokrytí souborů

| Soubor | Formát | Řádky včetně záhlaví / data CSV | Výpočetní kontroly / spárované řádky CSV |
|---|---|---|---|
| [03-ZAVITY/01-Zavity ISO/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/01-Zavity%20ISO/0000-index/index_cs.html) | html | 0 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/0000-index/index_cs.html) | html | 0 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/0000-index/index_cs.html) | html | 8 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/alt_table.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/alt_table.html) | html | 0 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/index_cs.html) | html | 80 | 293 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/02-rozmery pro M20 az M48/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/02-rozmery%20pro%20M20%20az%20M48/0000-index/index_cs.html) | html | 77 | 292 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/03-rozmery pro M50 az M82/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/03-rozmery%20pro%20M50%20az%20M82/0000-index/index_cs.html) | html | 79 | 306 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/04-rozmery pro M85 az M175/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/04-rozmery%20pro%20M85%20az%20M175/0000-index/index_cs.html) | html | 82 | 324 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/05-rozmery pro M180 az M300/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/05-rozmery%20pro%20M180%20az%20M300/0000-index/index_cs.html) | html | 79 | 312 |
| [03-ZAVITY/02-Metricke zavity ISO/02-Metricke zavity ISO - pro jemnou mechaniku a optiku/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/02-Metricke%20zavity%20ISO%20-%20pro%20jemnou%20mechaniku%20a%20optiku/0000-index/index_cs.html) | html | 315 | 1252 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/0000-index/index_cs.html) | html | 63 | 48 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/01-Tolerancni pole pro ulozeni s vuli/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/01-Tolerancni%20pole%20pro%20ulozeni%20s%20vuli/0000-index/index_cs.html) | html | 13 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/02-Tolerancni znacky pro ulozeni s vuli/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/02-Tolerancni%20znacky%20pro%20ulozeni%20s%20vuli/0000-index/index_cs.html) | html | 7 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/03-Delky zasroubovani pro ulozeni s vuli/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/03-Delky%20zasroubovani%20pro%20ulozeni%20s%20vuli/0000-index/index_cs.html) | html | 15 | 48 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/04-Zakladni uchylky a stupne presnosti pro ulozeni prechodna/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/04-Zakladni%20uchylky%20a%20stupne%20presnosti%20pro%20ulozeni%20prechodna/0000-index/index_cs.html) | html | 7 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/05-Tolerancni znacky pro ulozeni prechodna/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/05-Tolerancni%20znacky%20pro%20ulozeni%20prechodna/0000-index/index_cs.html) | html | 5 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/06-Kombinace tolerancnich poli pro ulozeni prechodna/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/06-Kombinace%20tolerancnich%20poli%20pro%20ulozeni%20prechodna/0000-index/index_cs.html) | html | 11 | 0 |
| [03-ZAVITY/02-Metricke zavity ISO/03-Metricke zavity ISO - tolerovani/07-Tolerancni znacky pro ulozeni s presahem/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/03-Metricke%20zavity%20ISO%20-%20tolerovani/07-Tolerancni%20znacky%20pro%20ulozeni%20s%20presahem/0000-index/index_cs.html) | html | 5 | 0 |
| [03-ZAVITY/03-Palcove zavity ISO/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/0000-index/index_cs.html) | html | 5 | 0 |
| [03-ZAVITY/03-Palcove zavity ISO/01-Palcove zavity ISO - prehled/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/01-Palcove%20zavity%20ISO%20-%20prehled/0000-index/index_cs.html) | html | 75 | 71 |
| [03-ZAVITY/03-Palcove zavity ISO/02-Palcove zavity ISO - zakladni rozmery/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/02-Palcove%20zavity%20ISO%20-%20zakladni%20rozmery/0000-index/index_cs.html) | html | 348 | 1730 |
| [03-ZAVITY/03-Palcove zavity ISO/03-Palcove zavity ISO - delky zasroubovanych zavitu/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/03-Palcove%20zavity%20ISO%20-%20delky%20zasroubovanych%20zavitu/0000-index/index_cs.html) | html | 8 | 0 |
| [03-ZAVITY/03-Palcove zavity ISO/04-Palcove zavity ISO - trida presnosti zavitu/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/04-Palcove%20zavity%20ISO%20-%20trida%20presnosti%20zavitu/0000-index/index_cs.html) | html | 2 | 0 |
| [03-ZAVITY/04-Whitworthovy zavity/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/04-Whitworthovy%20zavity/0000-index/index_cs.html) | html | 33 | 213 |
| [03-ZAVITY/05-Trubkove zavity ISO/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/05-Trubkove%20zavity%20ISO/0000-index/index_cs.html) | html | 0 | 0 |
| [03-ZAVITY/05-Trubkove zavity ISO/01-Rozmery trubkovych zavitu podle ISO 7 pro spoje tesnici mezi boky/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/05-Trubkove%20zavity%20ISO/01-Rozmery%20trubkovych%20zavitu%20podle%20ISO%207%20pro%20spoje%20tesnici%20mezi%20boky/0000-index/index_cs.html) | html | 18 | 85 |
| [03-ZAVITY/05-Trubkove zavity ISO/02-Rozmery trubkovĂ˝ch zavitu podle ISO 228 pro spoje netesnici mezi boky/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/05-Trubkove%20zavity%20ISO/02-Rozmery%20trubkov%C4%82%CB%9Dch%20zavitu%20podle%20ISO%20228%20pro%20spoje%20netesnici%20mezi%20boky/0000-index/index_cs.html) | html | 28 | 240 |
| [03-ZAVITY/06-Lichobeznikove zavity/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/0000-index/index_cs.html) | html | 0 | 0 |
| [03-ZAVITY/06-Lichobeznikove zavity/01-Lichobeznikove zavity - zakladni rozmery/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/01-Lichobeznikove%20zavity%20-%20zakladni%20rozmery/0000-index/index_cs.html) | html | 146 | 974 |
| [03-ZAVITY/06-Lichobeznikove zavity/02-Lichobeznikove zavity - tolerancni pole/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/02-Lichobeznikove%20zavity%20-%20tolerancni%20pole/0000-index/index_cs.html) | html | 24 | 0 |
| [03-ZAVITY/06-Lichobeznikove zavity/03-Lichobeznikove zavity - delka zasroubovanych zavitÅ¯/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/03-Lichobeznikove%20zavity%20-%20delka%20zasroubovanych%20zavit%C3%85%C2%AF/0000-index/index_cs.html) | html | 19 | 0 |
| [03-ZAVITY/06-Lichobeznikove zavity/03-Lichobeznikove zavity - delka zasroubovanych zavitĹŻ/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/03-Lichobeznikove%20zavity%20-%20delka%20zasroubovanych%20zavit%C4%B9%C5%BB/0000-index/index_cs.html) | html | 19 | 0 |
| [03-ZAVITY/07-Zvlastni zavity uzivane na jizdnich kolech/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/07-Zvlastni%20zavity%20uzivane%20na%20jizdnich%20kolech/0000-index/index_cs.html) | html | 15 | 13 |
| [03-ZAVITY/08-Vybehy a zkoseni zavitu/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/08-Vybehy%20a%20zkoseni%20zavitu/0000-index/index_cs.html) | html | 27 | 260 |
| [03-ZAVITY/09-Drazky za zavity/0000-index/index_cs.html](../../../data/mechanical-tables/03-ZAVITY/09-Drazky%20za%20zavity/0000-index/index_cs.html) | html | 27 | 72 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/table1.csv](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table1.csv) | csv | 79 | 79 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/table2.csv](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table2.csv) | csv | 76 | 76 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/table3.csv](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table3.csv) | csv | 78 | 78 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/table4.csv](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table4.csv) | csv | 81 | 81 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/table5.csv](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/table5.csv) | csv | 78 | 78 |
| [03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/01-rozmery pro M1 az M18/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/01-Metricke%20zavity%20ISO%20-%20pro%20vseobecne%20pouziti/01-rozmery%20pro%20M1%20az%20M18/0000-index/tabulka.csv) | csv | 391 | 391 |
| [03-ZAVITY/02-Metricke zavity ISO/02-Metricke zavity ISO - pro jemnou mechaniku a optiku/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/02-Metricke%20zavity%20ISO/02-Metricke%20zavity%20ISO%20-%20pro%20jemnou%20mechaniku%20a%20optiku/0000-index/tabulka.csv) | csv | 71 | 71 |
| [03-ZAVITY/03-Palcove zavity ISO/02-Palcove zavity ISO - zakladni rozmery/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/03-Palcove%20zavity%20ISO/02-Palcove%20zavity%20ISO%20-%20zakladni%20rozmery/0000-index/tabulka.csv) | csv | 346 | 344 |
| [03-ZAVITY/04-Whitworthovy zavity/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/04-Whitworthovy%20zavity/0000-index/tabulka.csv) | csv | 28 | 28 |
| [03-ZAVITY/05-Trubkove zavity ISO/01-Rozmery trubkovych zavitu podle ISO 7 pro spoje tesnici mezi boky/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/05-Trubkove%20zavity%20ISO/01-Rozmery%20trubkovych%20zavitu%20podle%20ISO%207%20pro%20spoje%20tesnici%20mezi%20boky/0000-index/tabulka.csv) | csv | 15 | 0 |
| [03-ZAVITY/05-Trubkove zavity ISO/02-Rozmery trubkovĂ˝ch zavitu podle ISO 228 pro spoje netesnici mezi boky/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/05-Trubkove%20zavity%20ISO/02-Rozmery%20trubkov%C4%82%CB%9Dch%20zavitu%20podle%20ISO%20228%20pro%20spoje%20netesnici%20mezi%20boky/0000-index/tabulka.csv) | csv | 24 | 24 |
| [03-ZAVITY/06-Lichobeznikove zavity/01-Lichobeznikove zavity - zakladni rozmery/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/06-Lichobeznikove%20zavity/01-Lichobeznikove%20zavity%20-%20zakladni%20rozmery/0000-index/tabulka.csv) | csv | 143 | 143 |
| [03-ZAVITY/07-Zvlastni zavity uzivane na jizdnich kolech/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/07-Zvlastni%20zavity%20uzivane%20na%20jizdnich%20kolech/0000-index/tabulka.csv) | csv | 12 | 12 |
| [03-ZAVITY/08-Vybehy a zkoseni zavitu/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/08-Vybehy%20a%20zkoseni%20zavitu/0000-index/tabulka.csv) | csv | 24 | 24 |
| [03-ZAVITY/09-Drazky za zavity/0000-index/tabulka.csv](../../../data/mechanical-tables/03-ZAVITY/09-Drazky%20za%20zavity/0000-index/tabulka.csv) | csv | 24 | 24 |
