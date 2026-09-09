"""Read the legacy HTML tables without rewriting their markup. Standard library only."""
from html.parser import HTMLParser
import re

class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self.table = None
        self.row = None
        self.cell = None
        self.text = []
        self.prose = []
        self.in_table = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'table':
            self.in_table += 1
            if self.in_table == 1:
                self.table = []
        elif tag == 'tr' and self.in_table == 1:
            if self.row is not None:
                self.close_row()
            self.row = []
        elif tag in ('th', 'td') and self.in_table == 1:
            self.close_cell()
            if self.row is None:
                self.row = []
            self.cell = dict(text='', tag=tag, rowspan=int(attrs.get('rowspan',1)), colspan=int(attrs.get('colspan',1)), line=self.getpos()[0])
        elif tag == 'br':
            self.handle_data(' ')
    def close_cell(self):
        if self.cell is not None:
            self.cell['text'] = re.sub(r'\s+', ' ', self.cell['text']).strip()
            self.row.append(self.cell)
            self.cell = None
    def close_row(self):
        self.close_cell()
        if self.row is not None:
            self.table.append(self.row)
            self.row = None
    def handle_endtag(self,tag):
        if tag in ('td','th') and self.in_table == 1:
            self.close_cell()
        elif tag == 'tr' and self.in_table == 1:
            self.close_row()
        elif tag == 'table':
            if self.in_table == 1:
                self.close_row()
                self.tables.append(self.table)
                self.table = None
            self.in_table = max(0,self.in_table-1)
        elif tag in ('p','h1','h2','h3','li'):
            self.prose.append('\n')
    def handle_data(self,data):
        self.text.append(data)
        if self.cell is not None:
            self.cell['text'] += data
        if not self.in_table:
            self.prose.append(data)

def expand(rows):
    grid = []
    occupied = {}
    for ri,row in enumerate(rows):
        cells = {}
        for (r,c),val in list(occupied.items()):
            if r == ri:
                cells[c] = val
        col = 0
        for cell in row:
            while col in cells:
                col += 1
            for dr in range(cell['rowspan']):
                for dc in range(cell['colspan']):
                    occupied[(ri+dr,col+dc)] = cell
                    if dr == 0:
                        cells[col+dc] = cell
            col += cell['colspan']
        grid.append([cells.get(c,dict(text='',line=0)) for c in range(max(cells,default=-1)+1)])
    return grid
