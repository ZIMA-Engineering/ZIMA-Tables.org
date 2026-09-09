#!/usr/bin/env python3
"""Read-only audit of the imported tables; Python 3.8+, standard library.
Exit 0: no confirmed defects, 1: confirmed defects, 2: invalid input.
A calculation does not certify a standard series or a tolerance class.
"""
import argparse, csv, hashlib, html, json, math, re, sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from urllib.parse import quote
from thread_html import Extractor, expand

SOURCES = {
    'ISO724': ('ISO 724:2023, čl. 5','https://cdn.standards.iteh.ai/samples/85104/9815392ad8904c9aa23cf7727e7b1dde/ISO-724-2023.pdf'),
    'ISO725': ('ISO 725:2009, čl. 3','https://cdn.standards.iteh.ai/samples/51386/8bc5f5f2a14341e989c242c0c817f335/ISO-725-2009.pdf'),
    'ISO228': ('ISO 228-1:2000, tab. 1','https://cdn.standards.iteh.ai/samples/33777/842b7c5409454ceba69c7dad9c308be1/ISO-228-1-2000.pdf'),
    'ISO2901': ('ISO 2901:2016, čl. 6 a tab. 2','https://cdn.standards.iteh.ai/samples/68337/c87112d8e3dc487c95fd964d13101ca4/ISO-2901-2016.pdf'),
    'NIST': ('NIST, převod palce','https://www.nist.gov/pml/owm/si-units-length'),
    'GUEHRING': ('Gühring, Technical section, PDF s. 38','https://guehring.com/wp-content/downloads/EN/Catalogues-Special-Programmes/GUE_technical-section_EN.pdf'),
    'VOLKEL': ('VÖLKEL, řady BSW','https://voelkel.com/media/4e/69/b8/1709295983/VD%2023%20DE-EN.pdf'),
    'CYCLE': ('VÖLKEL, FG/BSC','https://voelkel.com/media/05/ac/15/1658319338/14_Information%20Technique_Diam%C3%A8tre%20axes.pdf'),
    'ISO6696': ('ISO 6696:1989','https://www.iso.org/standard/13131.html'),
    'DIN76': ('DIN 76-1:2016-08, tab. 1–2; DIN Handbook 193, PDF s. 24 a 27','https://api.pageplace.de/preview/DT0400.9783410274964_A35868027/preview-9783410274964_A35868027.pdf'),
    'BOSSARD': ('Bossard, Metric ISO threads, 01/2025, s. 97','https://assets.eu.ctfassets.net/0vp0u5uh75zd/2tYqENAuufvdsudjM8Qbrc/b3461eaa59c2203d3a8b9509ac24dacf/096_098_Metric_ISOthreads_Fastening_EN_01_2025.pdf'),
    'FINELOK': ('FINELOK, Tube Fittings, PDF s. 4','https://www.rometec.it/gpEasy/data/_uploaded/file/Sito%20Rometec/finelok/Raccordi.pdf'),
    'LOCAL': ('Vnitřní konzistence uživatelských dat / struktura HTML',None),
}
H=math.sqrt(3)/2
def number(s):
    s=re.sub(r'[()*]','',s).strip().replace(',','.')
    if '/' in s: return sum(float(Fraction(part)) for part in s.split())
    return float(re.sub(r'\s','',s))
def inches(s):
    s=s.strip().replace('_',' ')
    m=re.fullmatch(r'No\.\s*(\d+)',s,re.I)
    if m: return .060+.013*int(m[1])
    s=re.sub(r'^(?:W|G|R)\s*','',s).replace('"','').strip()
    return sum(float(Fraction(p)) for p in s.split())
def norm(s):
    s=html.unescape(re.sub(r'<[^>]+>',' ',s))
    s=s.replace('_',' ').strip()
    try: return ('number',round(number(s),8))
    except ValueError: pass
    s=re.sub(r'(?<![0-9])(\d+)\s+(\d+/\d+)',r'\1+\2',s)
    s=re.sub(r'[\s*]','',s).replace('×','x').replace(',','.')
    try: return ('number',round(float(s),8))
    except ValueError: return ('text',s)
def read_html(path):
    raw=path.read_text(encoding='utf-8-sig');parser=Extractor()
    parser.feed('<table>'+raw+'</table>' if path.suffix=='.csv' and not re.search(r'<table\b',raw,re.I) else raw)
    return raw,parser,[expand(t) for t in parser.tables]

# Tabulated pipe values are used, rather than recomputing a rounded profile.
PIPE_MAJOR=dict(zip(
    ('1/16','1/8','1/4','3/8','1/2','5/8','3/4','7/8','1','1 1/8','1 1/4','1 1/2','1 3/4','2','2 1/4','2 1/2','2 3/4','3','3 1/2','4','4 1/2','5','5 1/2','6'),
    (7.723,9.728,13.157,16.662,20.955,22.911,26.441,30.201,33.249,37.897,41.910,47.803,53.746,59.614,65.710,75.184,81.534,87.884,100.330,113.030,125.730,138.430,151.130,163.830)))
PIPE_GROUP={28:(.907,.581,214,107,282),19:(1.337,.856,250,125,445),14:(1.814,1.162,284,142,541),11:(2.309,1.479,360,180,640)}
GAUGE=dict(zip(('1/16','1/8','1/4','3/8','1/2','3/4','1','1 1/4','1 1/2','2'),(4,4,6,6.4,8.2,9.5,10.4,12.7,12.7,15.9)))
AC={1.5:.15,**dict.fromkeys((2,3,4,5),.25),**dict.fromkeys((6,7,8,9,10,12),.5),**dict.fromkeys((14,16,18,20,22,24,28,32,36,40,44),1)}
ENGAGEMENT={
    (3,5.5,.5):(1.5,4.5),(3,5.5,.7):(2,6),(3,5.5,.8):(2.5,7.5),
    (6,11,1):(3,9),(6,11,1.25):(4,12),(6,11,1.5):(5,15),
    (12,22,1.75):(6,18),(12,22,2):(8,24),(12,22,2.5):(10,30),
    (24,45,3):(12,36),(24,45,3.5):(15,45),(24,45,4):(18,53)}
# Comparative DIN edition only; not a replacement for unidentified older CSN.
# x1, x2, dg offset, g1 type A, g2 type A.
DIN_EXT={
    .2:(.5,.25,.3,.45,.7),.25:(.6,.3,.4,.55,.9),.3:(.75,.4,.5,.6,1.05),
    .35:(.9,.45,.6,.7,1.2),.4:(1,.5,.7,.8,1.4),.45:(1.1,.6,.7,1,1.6),
    .5:(1.25,.7,.8,1.1,1.75),.6:(1.5,.75,1,1.2,2.1),.7:(1.75,.9,1.1,1.5,2.45),
    .75:(1.9,1,1.2,1.6,2.6),.8:(2,1,1.3,1.7,2.8),1:(2.5,1.25,1.6,2.1,3.5),
    1.25:(3.2,1.6,2,2.7,4.4),1.5:(3.8,1.9,2.3,3.2,5.2),1.75:(4.3,2.2,2.6,3.9,6.1),
    2:(5,2.5,3,4.5,7),2.5:(6.3,3.2,3.6,5.6,8.7),3:(7.5,3.8,4.4,6.7,10.5),
    3.5:(9,4.5,5,7.7,12),4:(10,5,5.7,9,14),4.5:(11,5.5,6.4,10.5,16),
    5:(12.5,6.3,7,11.5,17.5),5.5:(14,7,7.7,12.5,19),6:(15,7.5,8.3,14,21)}

class Audit:
    def __init__(self,root):
        self.root=root;self.findings=[];self.files=[];self.checks=Counter();self.row_counts=Counter()
        self.records={};self.location=None;self.seen=set()
    def issue(self,cell,label,field,expected,status='confirmed',source='LOCAL',note=''):
        key=(self.location,cell.get('line',0),field,status)
        if key in self.seen: return
        self.seen.add(key)
        self.findings.append(dict(path=self.location,line=cell.get('line',0),label=label,field=field,
            actual=cell['text'],expected=expected,status=status,source=source,note=note))
    def check(self,row,col,expected,family,label,field,source,places=3,status=None,tolerance=None):
        self.checks[family]+=1
        try: value=number(row[col]['text'])
        except ValueError:
            self.issue(row[col],label,field,expected,'review',source,'Nečitelná číselná hodnota.');return
        delta=abs(value-expected)
        if delta <= (tolerance if tolerance is not None else .5*10**(-places)+1e-8): return
        kind=status or ('precision' if abs(value-round(expected,places))<=1.001*10**(-places) else 'confirmed')
        self.issue(row[col],label,field,round(expected,places),kind,source)
    def record(self,family,row,keycols,cols=None):
        texts=[c['text'] for c in row];key=tuple(norm(texts[c]) for c in keycols)
        data=[texts[c] for c in cols] if cols else texts
        self.records.setdefault(family,{}).setdefault(key,[]).append((self.location,row[0].get('line',0),data))
    def inspect(self,path,grids,raw):
        self.location=path.relative_to(self.root).as_posix();p=self.location
        for grid in grids:
            for row in grid:
                t=[c['text'] for c in row]
                try:
                    if '/01-Metricke zavity ISO - pro vseobecne pouziti/' in p and len(t)==5 and re.match(r'^M\s*\d',t[0]):
                        family='metric_basic';d=number(re.match(r'^M\s*([\d.,]+)',t[0])[1]);pitch=number(t[1])
                        explicit=re.search(r'[x×]\s*([\d.,]+)',t[0])
                        if explicit:
                            self.checks[family]+=1
                            if number(explicit[1])!=pitch:
                                self.issue(row[0],t[0],'Rozteč v označení',f'M {d:g} × {pitch:g}','confirmed','LOCAL',
                                    'Rozteč v označení nesouhlasí se sloupcem P; všechny tři průměry odpovídají sloupci P.')
                        if d==2.2 and not explicit:
                            self.check(row,1,.45,family,t[0],'P hrubé řady','GUEHRING',status='confirmed');pitch=.45
                        for c,e,name in ((2,d-1.25*H*pitch,'D1 [mm]'),(3,d-.75*H*pitch,'D2 [mm]'),(4,d-17*H*pitch/12,'d3 [mm]')):
                            self.check(row,c,e,family,t[0],name,'ISO724')
                        self.record(family,row,(0,1))
                    elif '/02-Metricke zavity ISO - pro jemnou mechaniku' in p and len(t)==6 and re.fullmatch(r'[\d,.]+',t[0]):
                        family='metric_optics';d=number(t[0]);pitch=number(t[1]);label='M '+t[0]+' × '+t[1]
                        if t[1]=='035':
                            self.issue(row[1],label,'P [mm]',.35,'confirmed','ISO724','Ostatní průměry odpovídají P=0,35 mm.');pitch=.35
                        if d==4.5 and pitch==.35 and number(t[2])==5:
                            self.issue(row[0],label,'Rozpor jmenovitého a velkého průměru',None,'review','LOCAL',
                                'Označení uvádí 4,5 mm, všechny čtyři průměry odpovídají 5 mm. Nejprve určit správné označení.')
                        else:
                            self.check(row,2,d,family,label,'d = jmenovitý průměr [mm]','LOCAL',status='confirmed')
                            for c,e,name in ((3,d-.75*H*pitch,'D2 [mm]'),(4,d-1.25*H*pitch,'D1 [mm]'),(5,d-17*H*pitch/12,'d3 [mm]')):
                                self.check(row,c,e,family,label,name,'ISO724')
                        self.record(family,row,(0,1))
                    elif '/02-Palcove zavity ISO - zakladni rozmery/' in p and len(t)==9 and re.fullmatch(r'[\d,./\s]+',t[2]):
                        family='unified';n=number(t[2]);d=inches(t[0]);label=t[8]
                        for c,e,name in ((3,25.4/n,'P [mm]'),(4,d,'d [in]'),(5,d*25.4,'d [mm]'),(6,d-.75*H/n,'D2 [in]'),(7,d-1.25*H/n,'D1 [in]')):
                            self.check(row,c,e,family,label,name,'ISO725' if c in (6,7) else 'NIST',places=4,
                                status='precision' if c==5 and abs(number(t[5])-d*25.4)<.00051 else None)
                        self.record(family,row,(8,))
                    elif '/04-Whitworthovy' in p and len(t)==13 and t[0].startswith('W '):
                        family='whitworth';d=inches(t[0])*25.4;n=number(t[1])
                        corrected={'W 9/16':12,'W 5/8':11,'W 3/4':10}.get(t[0])
                        if corrected:
                            self.check(row,1,corrected,family,t[0],'Počet závitů na palec','VOLKEL',status='confirmed');n=corrected
                        self.check(row,2,25.4/n,family,t[0],'P [mm]','NIST')
                        # Historical rounded profile heights: 0.002 mm is a sanity bound only.
                        h=.640327*25.4/n
                        for c,e,name in ((3,d,'d'),(5,d-h,'d2'),(7,d-2*h,'d1'),(8,d,'D'),(9,d-h,'D2'),(11,d-2*h,'D1')):
                            self.check(row,c,e,family,t[0],name+' [mm]','ISO228',tolerance=.002)
                        if t[0]=='W 3' and '-100' in t[4] and '-1000' not in t[4]:
                            self.issue(row[4],t[0],'Dolní mezní úchylka d',None,'review','LOCAL','-100 µm přerušuje řadu -950, -1050 µm; ověřit chybějící nulu podle původní normy.')
                        self.record(family,row,(0,))
                    elif '/01-Lichobeznikove zavity - zakladni rozmery/' in p and len(t)==14 and re.fullmatch(r'[\d,.()\s]+',t[0]):
                        family='trapezoidal';d=number(t[0]);pitch=number(t[1]);label=t[7]
                        dm=re.fullmatch(r'Tr\s*([\d,.]+)\s*[×x]\s*([\d,.]+)',label)
                        if dm and (number(dm[1])!=d or number(dm[2])!=pitch):
                            self.issue(row[7],label,'Označení',f'Tr {d:g} × {pitch:g}','confirmed','LOCAL','Rozteč a označení musejí popisovat stejný závit.')
                        ac=AC.get(pitch)
                        for c in range(2,7):
                            if ac is not None and re.fullmatch(r'[\d,.]+',t[c]):
                                e={2:d,3:d+2*ac,4:d-pitch/2,5:d-pitch-2*ac,6:d-pitch}[c]
                                self.check(row,c,e,family,label,{2:'d',3:'D4',4:'D2',5:'d3',6:'D1'}[c]+' [mm]','ISO2901')
                        for c,n in zip(range(8,14),(1,2,3,4,6,8)):
                            if re.fullmatch(r'[\d,.]+',t[c]): self.check(row,c,n*pitch,family,label,f'Ph pro {n} chodů [mm]','ISO2901',status='confirmed')
                        self.record(family,row,(0,1))
                    elif '/05-Trubkove' in p:
                        start=next((i for i,x in enumerate(t) if re.fullmatch(r'G?\s*\d+(?:[\s_]+\d+/\d+|/\d+)?',x) and i+5<len(t) and t[i+1] in ('28','19','14','11')),None)
                        if start is None: continue
                        row=row[start:];t=[c['text'] for c in row];family='pipe228' if 'ISO 228' in p else 'pipe7'
                        name=re.sub(r'^G\s*','',t[0]).replace('_',' ')
                        expected_n=28 if inches(name)<=.125 else 19 if inches(name)<=.375 else 14 if inches(name)<1 else 11
                        self.check(row,1,expected_n,family,t[0],'Počet závitů na palec','ISO228',status='confirmed')
                        pitch,h,td,td2,td1=PIPE_GROUP[expected_n];d=PIPE_MAJOR[name]
                        for c,e,field in ((2,pitch,'P'),(3,d,'d'),(4,d-h,'D2'),(5,d-2*h,'D1')):
                            self.check(row,c,e,family,t[0],field+' [mm]','ISO228',status='confirmed')
                        if family=='pipe228':
                            if inches(name)>2: td,td2=434,217
                            for c,expected,field in ((6,[0,-td],'d'),(7,[0,-td2],'d2 A'),(8,[0,-2*td2],'d2 B'),(9,[td2,0],'D2'),(10,[td1,0],'D1')):
                                self.checks[family]+=1
                                if [number(v) for v in t[c].split()]!=expected:
                                    self.issue(row[c],t[0],'Úchylky '+field+' [µm]',str(expected),'confirmed','ISO228')
                        elif name in GAUGE:
                            bounds=[number(v) for v in t[6].split()];self.checks[family]+=1
                            if len(bounds)!=2 or abs(sum(bounds)/2-GAUGE[name])>.051:
                                self.issue(row[6],t[0],'Střed mezí základní délky',GAUGE[name],'review','FINELOK')
                        self.record(family,row,(0,))
                    elif '/07-Zvlastni zavity' in p and len(t)==7 and re.search(r'[×x]',t[0]):
                        family='cycle';n=number(t[1]);label=t[0]
                        if label=='7,9 × 56':
                            self.issue(row[0],label,'Označení','7,9 × 26','confirmed','CYCLE')
                            self.check(row,1,26,family,label,'Počet závitů na palec','CYCLE',status='confirmed');n=26
                        self.check(row,2,25.4/n,family,label,'P [mm]','NIST',places=4,status='precision' if abs(number(t[2])-25.4/n)<.00051 else None)
                        self.record(family,row,(0,),list(range(6)))
                    elif '/08-Vybehy' in p and len(t)==11 and re.fullmatch(r'[\d,.]+',t[0]):
                        family='runouts';pitch=number(t[0]);label='P='+t[0]
                        for c in range(2,11):
                            if re.fullmatch(r'-?[\d,.]+',t[c]):
                                self.checks[family]+=1
                                if number(t[c])<0:
                                    self.issue(row[c],label,'Délka výběhu musí být kladná',None,'confirmed','LOCAL',
                                        'Záporná délka je chybná. Správnou kladnou hodnotu určit podle původní normy; DIN 76-1:2016 uvádí 1,25 mm.')
                        for c,e in ((2,DIN_EXT[pitch][0]),(3,DIN_EXT[pitch][1])):
                            if t[c]!='-': self.check(row,c,e,family,label,'x1 DIN' if c==2 else 'x2 DIN','DIN76',status='standard_difference')
                        self.record(family,row,(0,))
                    elif '/09-Drazky' in p and len(t)==11 and re.fullmatch(r'[\d,.]+',t[0]):
                        family='undercuts';pitch=number(t[0]);label='P='+t[0];ref=DIN_EXT[pitch]
                        for c,e in ((3,ref[3]),(4,ref[4])):
                            self.check(row,c,e,family,label,'a / g1 DIN' if c==3 else 'b / g2 DIN','DIN76',status='standard_difference')
                        off=re.search(r'd\s*-\s*([\d,.]+)',t[2]);self.checks[family]+=1
                        if off and abs(number(off[1])-ref[2])>.0001:
                            self.issue(row[2],label,'dd / dg DIN',f'd - {ref[2]:g}','standard_difference','DIN76')
                        self.record(family,row,(0,))
                    elif '/03-Metricke zavity ISO - tolerovani/' in p and len(t)==7 and re.fullmatch(r'[\d,.]+',t[0]) and re.fullmatch(r'[\d,.]+',t[2]):
                        family='metric_engagement';key=tuple(number(v) for v in t[:3])
                        if key in ENGAGEMENT:
                            low,high=ENGAGEMENT[key]
                            for c,e in ((3,low),(4,low),(5,high),(6,high)):
                                self.check(row,c,e,family,str(key),'Délka zašroubování [mm]','BOSSARD',status='confirmed')
                    else: continue
                    self.row_counts[family]+=1
                except (ValueError,KeyError,IndexError,ZeroDivisionError) as error:
                    self.issue(row[0],t[0],'Kontrola řádku',None,'review','LOCAL',str(error))
        self.headers_and_prose(p,grids,raw)

    def headers_and_prose(self,p,grids,raw):
        def match_issue(text,expected,field,status='confirmed',source='LOCAL',note=''):
            at=raw.find(text)
            if at>=0: self.issue(dict(text=text,line=raw[:at].count('\n')+1),'Záhlaví / text',field,expected,status,source,note)
        if '/02-Palcove zavity ISO - zakladni rozmery/' in p:
            for row in grids[0][:4]:
                if len(row)==9:
                    for c in (6,7):
                        if row[c]['text']=='[mm]':
                            self.issue(row[c],'Záhlaví','Jednotka D2/D1','[in]','confirmed','ISO725','Hodnoty jsou základní průměry v palcích.')
        if '/01-Lichobeznikove zavity - zakladni rozmery/' in p:
            for row in grids[0][:3]:
                if len(row)==14 and [c['text'] for c in row[8:]]==['1','2','3','4','5','6']:
                    for c,e in ((12,'6'),(13,'8')):
                        self.issue(row[c],'Záhlaví','Počet chodů n',e,'confirmed','ISO2901','Stoupání v těchto sloupcích odpovídají n=6 a n=8.')
        if 'ISO 228' in p:
            for grid in grids:
                for row in grid[:4]:
                    for c in row:
                        if c['text']=='Závit' and c.get('rowspan',1)>4:
                            self.issue(c,'Záhlaví','rowspan záhlaví','4','confirmed','LOCAL','Záhlaví má čtyři řádky; přesah posouvá datové buňky.')
        if '/01-Zavity ISO/' in p:
            match_issue('0,5.n','0,5 × P','Vzorec výšky H','confirmed','ISO724')
            match_issue('0,866025404/n',None,'Jednotky vzorců s n','confirmed','NIST',
                'Pro n závitů na palec platí P[mm]=25,4/n. Výrazy s 1/n bez 25,4 dávají palce; doplnit jednotky všech pěti vzorců.')
        if '/07-Zvlastni' in p:
            match_issue('55°C','55°','Jednotka úhlu')
            match_issue('ISO 6669','ISO 6696','Číslo normy','confirmed','ISO6696')
        if p=='03-ZAVITY/03-Palcove zavity ISO/0000-index/index_cs.html':
            match_issue('PD 0.4485 - 0.4422',None,'Neslučitelný příklad PD','review','ISO725',
                'Obě meze jsou větší než velký průměr 1/4 in; nelze určit, zda je špatné označení závitu nebo jeho meze.')
            for grid in grids:
                for row in grid:
                    if len(row)==2 and 'MINOR DIA' in row[1]['text'] and 'středního' in row[0]['text']:
                        self.issue(row[0],'MINOR DIA','Popis průměru','Mezní rozměry malého průměru závitu','confirmed','ISO725')
        if '/03-Metricke zavity ISO - tolerovani/' in p:
            for suspect in ('4j6k','4H6J'):
                match_issue(suspect,None,'Toleranční značka','review','LOCAL','Podezřelý zápis; bez původní ČSN pro přechodná uložení nenavrhuji náhradu.')
        if '/01-Palcove zavity ISO - prehled/' in p:
            ambiguous=[]
            for grid in grids:
                for row in grid[4:]:
                    if len(row)!=14: continue
                    label=row[0]['text'] or row[1]['text']
                    if not label: continue
                    # Overview alone uses ambiguous merged mixed numerals after 1 inch.
                    if number(row[2]['text'])>=1 and re.fullmatch(r'[1-5]\d+/\d+',label):
                        value=inches(label[0]+' '+label[1:]);ambiguous.append(label)
                        self.check(row,2,value,'unified_overview',label,'d [in], podle smíšeného čísla','LOCAL',places=4,status='confirmed')
                    else: self.check(row,2,inches(label),'unified_overview',label,'d [in]','NIST',places=4,status='confirmed')
                    self.row_counts['unified_overview']+=1
            if ambiguous:
                match_issue('<th>35/8</th>','3 5/8','Nejednoznačný zápis smíšených čísel','review','LOCAL',
                    'Od 1 in jsou zápisy jako 11/16 a 35/8 bez mezery. V této části znamenají 1 1/16 a 3 5/8; upravit celou řadu.')

    def exports(self,paths):
        for path in paths:
            self.location=path.relative_to(self.root).as_posix();raw=path.read_text(encoding='utf-8-sig')
            if re.search(r'<(?:table|thead|tr|td|th)\b',raw[:1000],re.I):
                _,parser,grids=read_html(path)
                rows=[[c['text'] for c in r] for g in grids for r in g if len(r)==5 and re.match(r'^M\s*\d',r[0]['text'])]
                self.issue(dict(text='HTML',line=1),path.name,'Soubor s příponou CSV obsahuje HTML',None,'format','LOCAL','Čísla byla porovnána s HTML.')
                family='metric_basic';keys=(0,1)
            else:
                delim='\t' if '\t' in raw else '|' if '|' in raw else ';'
                rows=[r for r in csv.reader(raw.splitlines(),delimiter=delim) if any(v.strip() for v in r)]
                if path.name=='table4.csv':
                    rows=[r for r in rows if len(r)==5 and re.match(r'^M\s*\d',r[0])]
                    family='metric_basic';keys=(0,1)
                    self.issue(dict(text='Víceřádkové záhlaví, oddělovač |',line=1),path.name,'Nepravidelný formát exportu',None,'format')
                elif 'pro vseobecne pouziti' in str(path):
                    rows=[[r[5],r[1],r[3],r[2],r[4]] for r in rows if len(r)>=6];family='metric_basic';keys=(0,1)
                elif 'pro jemnou mechaniku' in str(path):
                    rows=[r[:6] for r in rows];family='metric_optics';keys=(0,1)
                elif '02-Palcove zavity ISO - zakladni rozmery' in str(path):
                    family='unified';keys=(8,);previous=''
                    for r in rows:
                        if r[0]: previous=r[0]
                        else: r[0]=previous
                elif '04-Whitworthovy' in str(path): family='whitworth';keys=(0,)
                elif 'ISO 228' in str(path): family='pipe228';keys=(0,)
                elif 'ISO 7 pro' in str(path):
                    self.issue(dict(text=str(sorted(set(map(len,rows)))),line=1),path.name,'Neúplné řádky CSV po sloučených buňkách',None,'format','LOCAL',
                        'Nejde o plochou tabulku: bez HTML nelze bezpečně obnovit význam některých polí.')
                    self.files.append(dict(path=self.location,kind='csv',rows=len(rows),compared_rows=0,note='Ragged ISO 7 export; comparison unavailable'));continue
                elif '01-Lichobeznikove zavity' in str(path): family='trapezoidal';keys=(0,1)
                elif '07-Zvlastni' in str(path): family='cycle';keys=(0,)
                elif '08-Vybehy' in str(path): family='runouts';keys=(0,)
                elif '09-Drazky' in str(path): family='undercuts';keys=(0,)
                else: continue
            matched=0;available=self.records.get(family,{})
            for i,r in enumerate(rows):
                try:
                    key=tuple(norm(r[c]) for c in keys);candidates=available.get(key)
                    if not candidates:
                        self.issue(dict(text=' | '.join(r),line=i+1),str(key),'Řádek exportu bez protějšku HTML',None,'review');continue
                    original_path,original_line,target=candidates[0];compared=r
                    if family=='pipe228': target=[target[c] for c in (0,3,4,5)]
                    if family=='trapezoidal':
                        compared=r[:14]
                        target=[v if j<3 or j>6 or re.fullmatch(r'[\d,.]+',v) else '' for j,v in enumerate(target)]
                    if family=='cycle': compared=r[:6]
                    if len(compared)>len(target) and all(not v.strip() for v in compared[len(target):]): compared=compared[:len(target)]
                    matched+=1;self.checks['export_cells']+=min(len(compared),len(target))
                    if [norm(v) for v in compared]!=[norm(v) for v in target]:
                        diff=[f'{c+1}: {a} / {b}' for c,(a,b) in enumerate(zip(compared,target)) if norm(a)!=norm(b)]
                        self.issue(dict(text='; '.join(diff) or str(len(compared)),line=i+1),str(key),'CSV / HTML rozdíl',None,'confirmed' if family=='trapezoidal' else 'review','ISO2901' if family=='trapezoidal' else 'LOCAL',
                            'HTML: '+original_path+':'+str(original_line)+'. Řádek CSV zde znamená pořadí datového řádku.')
                except (ValueError,IndexError) as error:
                    self.issue(dict(text=' | '.join(r),line=i+1),'CSV','Nečitelný řádek exportu',None,'format','LOCAL',f'Řádek má {len(r)} polí; tato tabulka vyžaduje 9. Chybí oddělovač nebo je sloučen text sousedních buněk.')
            self.files.append(dict(path=self.location,kind='csv',rows=len(rows),compared_rows=matched,
                html_reference_rows=len(available),note='Partial export' if matched<len(available) else ''))
    def run(self):
        base=self.root/'03-ZAVITY'
        if not base.is_dir(): raise ValueError('Missing 03-ZAVITY directory')
        for path in sorted(base.rglob('*.html')):
            raw,parser,grids=read_html(path);before=sum(self.checks.values())
            self.inspect(path,grids,raw)
            self.files.append(dict(path=path.relative_to(self.root).as_posix(),kind='html',tables=len(grids),
                rows=sum(map(len,grids)),checks=sum(self.checks.values())-before,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        self.exports(sorted(base.rglob('*.csv')))
        self.findings.sort(key=lambda f:(f['path'],f['line'],f['field']))
        for i,f in enumerate(self.findings,1): f['id']=f'THR-{i:04}'
        return dict(schema_version=1,mode='read-only',sources={k:dict(title=v[0],url=v[1]) for k,v in SOURCES.items()},
            checks=dict(self.checks),rows=dict(self.row_counts),counts=dict(Counter(f['status'] for f in self.findings)),files=self.files,findings=self.findings)

def render(result,prefix='../../data/mechanical-tables'):
    esc=lambda x:str(x if x is not None else '—').replace('|',r'\|').replace('\n',' ')
    out=['# Kontrolní nálezy závitových tabulek','',
        'Automatický výstup čtecího auditu. Hodnoty nebyly změněny. Metodika a meze ověření: [protokol](threads-2026-09-09.md).','',
        'Čísla řádků HTML odkazují na zdroj; u CSV jde u některých exportů o pořadí datových řádků. Výpočetní shoda sama nepotvrzuje normovou přípustnost rozměrové řady.','']
    titles={'confirmed':'Potvrzené chyby a vnitřní rozpory','precision':'Odchylky v posledních místech',
        'standard_difference':'Rozdíly proti DIN 76-1:2016; původní norma neurčena','review':'Nejasné údaje k dořešení','format':'Formát a strojová použitelnost'}
    for status,title in titles.items():
        entries=[f for f in result['findings'] if f['status']==status]
        out+=['## '+title,'',f'Počet nálezů: {len(entries)}.','']
        for path in sorted(set(f['path'] for f in entries)):
            out+=[f'### [{Path(path).parent.parent.name}]({quote(prefix+"/"+path)})','',
                '| ID / řádek | Závit / položka | Pole | V tabulce | Reference / návrh | Zdroj / vysvětlení |','|---|---|---|---|---|---|']
            for f in (f for f in entries if f['path']==path):
                title,url=SOURCES[f['source']];source=f'[{title}]({url})' if url else title
                out.append('| '+' | '.join(map(esc,[f['id']+' / '+str(f['line']),f['label'],f['field'],f['actual'],f['expected'],source+'. '+f['note']]))+' |')
            out.append('')
    out+=['## Pokrytí souborů','','| Soubor | Formát | Řádky včetně záhlaví / data CSV | Výpočetní kontroly / spárované řádky CSV |','|---|---|---|---|']
    for f in result['files']:
        out.append(f'| [{esc(f["path"])}]({quote(prefix+"/"+f["path"])}) | {f["kind"]} | {f["rows"]} | {f.get("checks",f.get("compared_rows",0))} |')
    return '\n'.join(out)+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]/'data/mechanical-tables')
    parser.add_argument('--json',type=Path);parser.add_argument('--markdown',type=Path)
    args=parser.parse_args()
    try: result=Audit(args.root).run()
    except (ValueError,OSError) as error: parser.error(str(error))
    for path,content in ((args.json,json.dumps(result,ensure_ascii=False,indent=2)+'\n'),(args.markdown,render(result))):
        if path:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    print(json.dumps(dict(counts=result['counts'],rows=result['rows'],checks=result['checks']),ensure_ascii=False))
    return 1 if result['counts'].get('confirmed') else 0
if __name__=='__main__': sys.exit(main())
